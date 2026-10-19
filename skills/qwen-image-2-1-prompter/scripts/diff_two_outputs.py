#!/usr/bin/env python3
"""diff_two_outputs.py - 两张 ComfyUI 出图的逐节点 / 逐句取证 diff。

用法:
  python diff_two_outputs.py A.png B.png
  python diff_two_outputs.py <输出目录>        # 取目录内最新两张

打出:
  1) 尺寸 / 节点数
  2) 完整图 diff: 节点、类型、连接、图像哈希与所有字段
  3) 文本入参: 词数、<imageN> token 计数、归一化相似度
  4) 句子级 diff (只列差异句)
  5) LoadImage 槽位各接了哪个文件

只用标准库解析 PNG 的 tEXt/iTXt chunk，不依赖 PIL。
判读规则: 完整 prompt 图相同也不证明同一输出节点或同一执行。
先确认保存阶段、实际输入内容和运行记录，不能自动推断随机性。
"""
import sys, os, re, json, zlib, struct, difflib, glob

TOKEN = re.compile(r'<image\s*\d+>', re.I)


def png_text_chunks(path):
    out = {}
    with open(path, 'rb') as f:
        if f.read(8) != b'\x89PNG\r\n\x1a\n':
            raise SystemExit('not a PNG: ' + path)
        while True:
            head = f.read(8)
            if len(head) < 8:
                break
            length, ctype = struct.unpack('>I4s', head)
            data = f.read(length)
            f.read(4)
            if ctype in (b'tEXt', b'iTXt'):
                try:
                    if ctype == b'tEXt':
                        k, v = data.split(b'\x00', 1)
                        out[k.decode('latin-1')] = v.decode('utf-8', 'replace')
                    else:
                        k, rest = data.split(b'\x00', 1)
                        comp = rest[0]
                        rest = rest[2:]
                        _lang, rest = rest.split(b'\x00', 1)
                        _trans, text = rest.split(b'\x00', 1)
                        if comp == 1:
                            text = zlib.decompress(text)
                        out[k.decode('latin-1')] = text.decode('utf-8', 'replace')
                except Exception:
                    pass
            if ctype == b'IEND':
                break
    return out


def load_api(path):
    t = png_text_chunks(path)
    if 'prompt' not in t:
        raise SystemExit(path + ': 没有 prompt chunk（不是 ComfyUI 出图？）')
    return json.loads(t['prompt'])


def scalars(d):
    rows = {}
    for nid, n in d.items():
        for k, v in (n.get('inputs') or {}).items():
            if isinstance(v, (str, int, float, bool)) or v is None:
                rows[(nid, k)] = v
    return rows


def graph_diff(a, b, path=''):
    """Compare every JSON field; preserve missing-vs-null and list wiring."""
    missing = object()
    if isinstance(a, dict) and isinstance(b, dict):
        result = []
        for key in sorted(a.keys() | b.keys()):
            va, vb = a.get(key, missing), b.get(key, missing)
            child = path + '/' + key
            if va is missing or vb is missing:
                result.append((child, '<MISSING>' if va is missing else va,
                               '<MISSING>' if vb is missing else vb))
            else:
                result.extend(graph_diff(va, vb, child))
        return result
    return [] if type(a) is type(b) and a == b else [(path, a, b)]


def texts(d):
    out = {}
    for nid, n in d.items():
        for k, v in (n.get('inputs') or {}).items():
            if isinstance(v, str) and len(v) >= 80:
                out[(nid, k)] = v
    return out


def norm(s):
    return re.sub(r'\s+', ' ', s).strip().lower()


def sents(s):
    return [x.strip() for x in re.split(r'(?<=[.!?])\s+', s.strip()) if x.strip()]


def size(path):
    with open(path, 'rb') as f:
        f.read(16)
        w, h = struct.unpack('>II', f.read(8))
    return w, h


def nkey(x):
    try:
        return (0, int(x), '')
    except Exception:
        return (1, 0, str(x))


def report(pa, pb):
    print('A = ' + os.path.basename(pa))
    print('B = ' + os.path.basename(pb))
    print('  size A = %dx%d   B = %dx%d' % (size(pa) + size(pb)))
    a, b = load_api(pa), load_api(pb)
    print('  nodes A = %d   B = %d' % (len(a), len(b)))

    print('\n== 节点级 diff ==')
    onlya = sorted(set(a) - set(b), key=nkey)
    onlyb = sorted(set(b) - set(a), key=nkey)
    if onlya:
        print('  只在 A: ' + ', '.join(onlya))
    if onlyb:
        print('  只在 B: ' + ', '.join(onlyb))
    for nid in sorted(set(a) & set(b), key=nkey):
        ca, cb = a[nid].get('class_type'), b[nid].get('class_type')
        if ca != cb:
            print('  node %s class: %s -> %s' % (nid, ca, cb))
    diffs = graph_diff(a, b)
    if not diffs:
        print('  完整 prompt 图: 逐字段相同')
    for path, va, vb in diffs:
        print('  %s: %s -> %s' % (path, str(va)[:70], str(vb)[:70]))

    print('\n== 文本入参 ==')
    ta, tb = texts(a), texts(b)
    ids = sorted(set(ta) & set(tb), key=lambda x: (nkey(x[0]), x[1]))
    if not ids:
        ids = []
        if ta:
            ids.append(max(ta, key=lambda k: len(ta[k])))
        if tb:
            ids.append(max(tb, key=lambda k: len(tb[k])))
    for i, k in enumerate(ids):
        ka, kb = k if k in ta else (list(ta)[0] if ta else k), k if k in tb else (list(tb)[0] if tb else k)
        va, vb = ta.get(ka, ''), tb.get(kb, '')
        if not va or not vb:
            continue
        ratio = difflib.SequenceMatcher(None, norm(va), norm(vb)).ratio()
        print('  node %s.%s' % (ka[0], ka[1]))
        print('    chars  A=%d B=%d | words A=%d B=%d' % (
            len(va), len(vb), len(va.split()), len(vb.split())))
        print('    tokens A=%d B=%d' % (len(TOKEN.findall(va)), len(TOKEN.findall(vb))))
        print('    normalized similarity = %.4f; raw text equal = %s' % (ratio, va == vb))
        d = [ln for ln in difflib.ndiff(sents(va), sents(vb)) if ln[:1] in '+-?']
        if d:
            print('    句级 diff:')
            for ln in d[:40]:
                print('      ' + ln)
        else:
            print('    句级 diff: 无差异')

    print('\n== LoadImage 槽位 ==')
    for tag, dd in (('A', a), ('B', b)):
        for nid in sorted(dd, key=nkey):
            n = dd[nid]
            img = (n.get('inputs') or {}).get('image')
            if img:
                print('  %s node %s %s -> %s' % (tag, nid, n.get('class_type'), img))

    same = not diffs
    print('\n== 判读 ==')
    if same:
        print('  完整 prompt 图相同，但不证明同一输出节点或同一次执行。')
        print('  先核对保存阶段与实际输入文件；禁止据此自动宣称随机性或要求复跑。')
    else:
        print('  完整图有 %d 个差异项（见上）；多变量结果只能作观察，不能作单因素归因。' % len(diffs))
    for tag, dd in (('A', a), ('B', b)):
        sinks = {nid: n.get('inputs', {}).get('images') for nid, n in dd.items()
                 if 'SaveImage' in n.get('class_type', '')}
        print('  %s 保存节点候选（不是此 PNG 的输出节点证明）: %s' % (tag, sinks))


def main():
    args = sys.argv[1:]
    if len(args) == 1 and os.path.isdir(args[0]):
        files = sorted(glob.glob(os.path.join(args[0], '*.png')), key=os.path.getmtime)
        if len(files) < 2:
            raise SystemExit('目录里不足两张 png')
        args = files[-2:]
    if len(args) != 2:
        raise SystemExit(__doc__ or 'usage: diff_two_outputs.py A.png B.png')
    report(args[0], args[1])


if __name__ == '__main__':
    main()
