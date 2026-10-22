# 全量 PNG 元数据与提示词回放核对

日期：2026-10-22（Asia/Shanghai）。分支：`docs/replay-all-png`。基线提交：`0401244b14d5de09d042f9dab20d41db5984fca2`。

## 范围和判定方法

- 递归读取 `F:\ComfyUI-Data\output` 下的 PNG；只读原图，不调用生成模型。完整本地报告目录：`C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\outputs\replay-all-png`。
- 逐字比较保留首尾空白、换行、标点；SHA256 文本编码为 UTF-8。原图 SHA256 按完整文件字节计算。
- 输出阶段沿 SaveImage 的图像输入连接判断，并结合 filename_prefix 排除无关保存节点。多个输出节点均可能对应同一文件名时标为“无法确定”。未使用尺寸或图谱中出现某阶段来冒充实际保存节点证据。
- 151 张 PNG 的图谱同时包含 478 与 515 保存候选；仅凭这些 PNG 的元数据无法锁定本文件的实际保存阶段。因此下表统计的是“含该阶段文本的文件”，不是 151 张实际 515 成图。对这些文件的两阶段文本全部检查，避免漏检。
- 515 从原始文本中以固定模板分隔段提取现有 family/subject/role 槽，调用未修改的 render.py::render_config。历史负向的服装段只能在 fused garments 与 text, captions 等明确边界间原样提取；不复制整段原文充当模板回放，不改 family 的固定词句。
- “无法确定”表示无法从该历史文本可靠还原为当前完整配置，未生成候选文本，故第一差异位置不可给出；不是回放通过，也不判定图片失败。部分文件另记录了固定正文前缀的明确差异。
- 478 用 wardrobe_478.txt 的固定正文和槽边界提取五槽，再用原有 expand 组装。当前结构无法匹配时按请求标记“手写，不可回放”；该标签只表示当前模板不适配，不证明作者的实际编辑方式。没有把历史原文归档当作模板生成。
- 本报告核对文本、节点与文件来源，不重新判断图像质量、无头成功率或服装保真。扫描是运行期间的文件清单，不冻结正在产生的新图。

## 汇总

```json
{
  "inventory": {
    "png_files_scanned": 3359,
    "with_valid_prompt": 3358,
    "without_prompt": 1,
    "errors": 0,
    "walk_errors": [],
    "output_stage_counts": {
      "其他": 2866,
      "459": 341,
      "无法确定": 151
    },
    "files_with_478_text": 151,
    "files_with_515_text": 151
  },
  "replay515": {
    "无法确定": 136,
    "不一致": 6,
    "一致": 9
  },
  "replay478": {
    "手写，不可回放": 143,
    "一致": 8
  },
  "evidence": {
    "一致": 28
  },
  "missing_pngs": [],
  "coverage": "All files containing 478/515 text were checked, including ambiguous saving-stage files; graph-text presence is not proof of actual saved stage."
}
```

## 每文件回放结果

515 正/负两段可组装时，分别比较；不可组装时保留“无法确定”。所有行实际输出阶段均无法由保存节点元数据唯一确定。

| 本地 PNG 完整路径 | 515 总体 | 515 正向 | 515 负向 | 478 总体 |
|---|---|---|---|---|
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00092.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00093.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00094.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00095.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00096.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00097.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00098.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00099.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00100.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00101.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00103.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00104.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00105.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00106.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00107.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00109.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00110.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00111.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00112.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00114.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00115.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00116.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00185.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00186.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00187.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00190.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00191.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00192.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00194.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00195.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00196.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00197.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00198.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00200.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00201.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00202.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00203.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00206.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00207.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00208.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00210.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00211.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00212.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00213.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00214.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00215.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00216.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00222.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00223.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00224.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00225.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00226.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00227.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00228.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00229.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00230.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00231.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00232.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00233.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00258.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00259.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00260.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00261.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00262.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00263.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00264.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00307.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00308.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00320.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00321.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00324.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00325.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00368.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00369.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00371.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00372.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00382.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00383.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00402.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00403.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00404.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00405.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00406.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00407.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00408.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00409.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00410.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00411.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00415.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00416.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00417.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00418.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00421.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00422.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00423.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00424.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00425.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00426.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00427.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00428.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00429.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00430.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00431.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00432.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00436.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00437.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00438.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00439.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00440.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00441.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00442.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00443.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00475.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00476.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00477.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00478.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00479.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00480.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00481.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00482.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00483.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00484.png` | 不一致 | 不一致 | 不一致 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00485.png` | 不一致 | 不一致 | 不一致 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00486.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00487.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00488.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00489.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00490.png` | 不一致 | 一致 | 不一致 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00491.png` | 不一致 | 一致 | 不一致 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00493.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00494.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00495.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00496.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00497.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00498.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00499.png` | 不一致 | 不一致 | 一致 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00500.png` | 不一致 | 不一致 | 一致 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00501.png` | 一致 | 一致 | 一致 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00506.png` | 一致 | 一致 | 一致 | 一致 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00507.png` | 一致 | 一致 | 一致 | 一致 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00508.png` | 一致 | 一致 | 一致 | 一致 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00509.png` | 一致 | 一致 | 一致 | 一致 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00510.png` | 一致 | 一致 | 一致 | 一致 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00511.png` | 一致 | 一致 | 一致 | 一致 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00512.png` | 一致 | 一致 | 一致 | 一致 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00513.png` | 一致 | 一致 | 一致 | 一致 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00554.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00555.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00560.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00561.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |
| `F:\ComfyUI-Data\output\Qwen_image_2.1_00562.png` | 无法确定 | 无法确定 | 无法确定 | 手写，不可回放 |

## 已组装但不一致：全部首差异

索引从 0 开始；每个文本各列差异字符、前 60 字符和后 60 字符。到达文件边界时不足 60 字符，EOF 显示为 `<EOF>`。

### Qwen_image_2.1_00484.png / 515:513 / positive

```json
{
  "index_0based": 2792,
  "position_1based": 2793,
  "png": {
    "before_60": "r brown. Nothing else is added, removed, restyled or re-lit.",
    "at": "\n",
    "after_60": ""
  },
  "replay": {
    "before_60": "r brown. Nothing else is added, removed, restyled or re-lit.",
    "at": "<EOF>",
    "after_60": ""
  }
}
```

### Qwen_image_2.1_00484.png / 515:513 / negative

```json
{
  "index_0based": 201,
  "position_1based": 202,
  "png": {
    "before_60": "n the first three panels, a face in the first three panels, ",
    "at": "a",
    "after_60": " neck in the first three panels, skin rising above the colla"
  },
  "replay": {
    "before_60": "n the first three panels, a face in the first three panels, ",
    "at": "h",
    "after_60": "air falling over the shoulders in the first three panels, he"
  }
}
```

### Qwen_image_2.1_00485.png / 515:513 / positive

```json
{
  "index_0based": 2792,
  "position_1based": 2793,
  "png": {
    "before_60": "r brown. Nothing else is added, removed, restyled or re-lit.",
    "at": "\n",
    "after_60": ""
  },
  "replay": {
    "before_60": "r brown. Nothing else is added, removed, restyled or re-lit.",
    "at": "<EOF>",
    "after_60": ""
  }
}
```

### Qwen_image_2.1_00485.png / 515:513 / negative

```json
{
  "index_0based": 201,
  "position_1based": 202,
  "png": {
    "before_60": "n the first three panels, a face in the first three panels, ",
    "at": "a",
    "after_60": " neck in the first three panels, skin rising above the colla"
  },
  "replay": {
    "before_60": "n the first three panels, a face in the first three panels, ",
    "at": "h",
    "after_60": "air falling over the shoulders in the first three panels, he"
  }
}
```

### Qwen_image_2.1_00490.png / 515:513 / negative

```json
{
  "index_0based": 356,
  "position_1based": 357,
  "png": {
    "before_60": "ired crop, figure rescaled to fit the whole body, different ",
    "at": "p",
    "after_60": "erson between panels, different face between panels, differe"
  },
  "replay": {
    "before_60": "ired crop, figure rescaled to fit the whole body, different ",
    "at": "w",
    "after_60": "oman between panels, different face between panels, differen"
  }
}
```

### Qwen_image_2.1_00491.png / 515:513 / negative

```json
{
  "index_0based": 356,
  "position_1based": 357,
  "png": {
    "before_60": "ired crop, figure rescaled to fit the whole body, different ",
    "at": "p",
    "after_60": "erson between panels, different face between panels, differe"
  },
  "replay": {
    "before_60": "ired crop, figure rescaled to fit the whole body, different ",
    "at": "w",
    "after_60": "oman between panels, different face between panels, differen"
  }
}
```

### Qwen_image_2.1_00499.png / 515:513 / positive

```json
{
  "index_0based": 1228,
  "position_1based": 1229,
  "png": {
    "before_60": "figure in panels 1-3 ends cleanly at the sweater's own high ",
    "at": "m",
    "after_60": "ock collar, which closes around the base of the neck, no bar"
  },
  "replay": {
    "before_60": "figure in panels 1-3 ends cleanly at the sweater's own high ",
    "at": "c",
    "after_60": "ollar, which closes around the base of the neck, no bare ski"
  }
}
```

### Qwen_image_2.1_00500.png / 515:513 / positive

```json
{
  "index_0based": 1228,
  "position_1based": 1229,
  "png": {
    "before_60": "figure in panels 1-3 ends cleanly at the sweater's own high ",
    "at": "m",
    "after_60": "ock collar, which closes around the base of the neck, no bar"
  },
  "replay": {
    "before_60": "figure in panels 1-3 ends cleanly at the sweater's own high ",
    "at": "c",
    "after_60": "ollar, which closes around the base of the neck, no bare ski"
  }
}
```

## 历史 evidence.json 原图哈希

28 个样本在仓库中均无同名 PNG；本地均找到，完整 SHA256 均一致。缺失文件：无。完整本地路径和逐文件实际哈希另见 evidence-hashes.json。

| 文件名 | evidence.json SHA256 | 本地比较 |
|---|---|---|
| Qwen_image_2.1_00436.png | `4058103a22bda83feaeefca881014aeb07c154d9aaf10c1d8e23fcdeeb5ee674` | 一致 |
| Qwen_image_2.1_00440.png | `70fbc434eb8ac61aee77bf3ab4565334d296eefba19060348fd0f8b554345b67` | 一致 |
| Qwen_image_2.1_00441.png | `d4394efab04867e02bc57c4bd2962bf08c20b75cfba7503f38a3c98c8e8d8179` | 一致 |
| Qwen_image_2.1_00443.png | `3e02ae4f54e30fae5aad95339f79b597bd17f1d569fd84c289fe255cf35f38c6` | 一致 |
| Qwen_image_2.1_00476.png | `a1a7fd6abc6c05a1765593316b32cc3478a97905ddb78641a715a81212096d30` | 一致 |
| Qwen_image_2.1_00478.png | `516452706b15f4ab1523584e53b9072d5c4c296c0b320b5093e40e657a41990b` | 一致 |
| Qwen_image_2.1_00480.png | `f2375e8c248b9c07620eb4b3a6e48910fbafd927ee32a69763ab758b92d444ff` | 一致 |
| Qwen_image_2.1_00481.png | `efa7324d1eb652da6bd5a8fcefe22c82f93fe6738782a80f384a3a6694aaf17b` | 一致 |
| Qwen_image_2.1_00485.png | `61a9a70f29e813a86d447b7d63cf46193e4eaf918334646fbfc893da6a684fbb` | 一致 |
| Qwen_image_2.1_00487.png | `70f9cc829bdfdff6a5c80543010409dcf5e7b0a3a7ed1b1cf5b0d79faa76eed3` | 一致 |
| Qwen_image_2.1_00489.png | `da2ceb68f4d26bcb5ac04bd4f5440a82716b1d32674c4b15056646f408165605` | 一致 |
| Qwen_image_2.1_00491.png | `2c14ae1d6dbbb255d5b0dd3c3ccbc4093539b056debf6091bab14ea4f848d13b` | 一致 |
| Qwen_image_2.1_00492.png | `ca7f6048b8200af074efaed1f0891589003a022e5848650725a58d94b86153ae` | 一致 |
| Qwen_image_2.1_00494.png | `16ae10fbfee471764dae273aaae364c194a3152748bd37833e45aa02e75e7ff6` | 一致 |
| Qwen_image_2.1_00496.png | `5fbf9550ea917bebbb0c0b18f3f519e0ca480138ec07869a4718a4dd0164f7a5` | 一致 |
| Qwen_image_2.1_00498.png | `9447315fb13129ed1c1592c86a4c8bc631ac073fd9a81a1f4bd56c7f42464aaf` | 一致 |
| Qwen_image_2.1_00499.png | `e2fba6fbfdd679b11c9f0ec19296b118353647b97031a500d987a42db1576de0` | 一致 |
| Qwen_image_2.1_00500.png | `174c69e92793356cfb067d8baf673cc137114b1c22027c4ccad7325d766f08c3` | 一致 |
| Qwen_image_2.1_00501.png | `b61ecff857500f4c6266c5ffb4e6eb56830929da82bbacc04124ea96a13058aa` | 一致 |
| Qwen_image_2.1_00503.png | `13058f6a2e9e3a778af03b4ce0bf757dc31d2505f7bb0b9747c6e4219397a7f6` | 一致 |
| Qwen_image_2.1_00506.png | `65ab04000a8a0e6994cc59479f6ee2009bf57b8622123979ab932ea9856eb69a` | 一致 |
| Qwen_image_2.1_00507.png | `bf10bab0c038b64807e7dda76de9913eeb3e897741e698112a7d95bb144f9f13` | 一致 |
| Qwen_image_2.1_00508.png | `24f9946d0b747ed73e0082ceffadbb4bf22d47c71a00f2b7d1700ef0866fc693` | 一致 |
| Qwen_image_2.1_00509.png | `2de2386c2fa67b00540776631ef2e7170786e9289b788e1857bb5f62bb0b4a39` | 一致 |
| Qwen_image_2.1_00510.png | `42077960ee9a3c26d469eed8e8f397d58471941d261e63d9384f2ba512b9b51a` | 一致 |
| Qwen_image_2.1_00511.png | `7e33702104e4d06251c272cd6afefb2bcf098816f60dabd4e8508d149318e615` | 一致 |
| Qwen_image_2.1_00512.png | `5d5f2bddb966a538552c34e8d5e963af98fff2101c401e25044aa0c60b0e3d93` | 一致 |
| Qwen_image_2.1_00513.png | `e09eb0091783771904904145536fb8a5a50a490ace7bcf13c8a64e4d8f46d126` | 一致 |

## 命令和检查结果

```powershell
$out = 'C:\\Users\\xiaoj\\Documents\\Codex\\2026-10-19\\nin\\outputs\\replay-all-png'
python -X utf8 "$out\scan_inventory.py"
python -X utf8 "$out\audit_replays.py"
python -X utf8 "$out\run_checks.py"
```

上述三个报告脚本均在仓库外，最终运行退出码均为 0；审计退出码只表示审计程序完成，逐文件结果以状态字段为准。

### verify

工作目录：`C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\work\garment-to-shot\skills\fourview-headless`。退出码：`0`。

```text
C:\Users\xiaoj\AppData\Local\Programs\Python\Python311\python.exe scripts/verify.py
```

stdout：
```text
{
  "template_fingerprints": "2/2",
  "exact_prompt_replays": "18/18",
  "invalid_slots_and_subject_linkage": "PASS",
  "cli_four_files_and_overwrite_protection": "PASS",
  "original_pngs_verified": 0,
  "scope": "text/source validation; existing visual findings documented separately"
}
```

stderr：
```text
(empty)
```

### test_skill_references

工作目录：`C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\work\garment-to-shot`。退出码：`0`。

```text
C:\Users\xiaoj\AppData\Local\Programs\Python\Python311\python.exe tests/test_skill_references.py -v
```

stdout：
```text
(empty)
```

stderr：
```text
test_missing_external_is_not_silently_passed (__main__.SkillReferenceTests.test_missing_external_is_not_silently_passed) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.010s

OK
```

### test_prompt_validator

工作目录：`C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\work\garment-to-shot`。退出码：`0`。

```text
C:\Users\xiaoj\AppData\Local\Programs\Python\Python311\python.exe tests/test_prompt_validator.py -v
```

stdout：
```text
(empty)
```

stderr：
```text
test_baseline_with_newlines_and_4k_is_preserved (__main__.PromptEnvelopeTests.test_baseline_with_newlines_and_4k_is_preserved) ... ok
test_cli_exit_status_and_explicit_style_lint (__main__.PromptEnvelopeTests.test_cli_exit_status_and_explicit_style_lint) ... ok
test_malformed_fields_rejected_without_crashing (__main__.PromptEnvelopeTests.test_malformed_fields_rejected_without_crashing) ... ok
test_one_size_source_only (__main__.PromptEnvelopeTests.test_one_size_source_only) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.270s

OK
```

### test_four_view_evidence

工作目录：`C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\work\garment-to-shot`。退出码：`0`。

```text
C:\Users\xiaoj\AppData\Local\Programs\Python\Python311\python.exe tests/test_four_view_evidence.py -v
```

stdout：
```text
(empty)
```

stderr：
```text
test_backticks_warn_without_claiming_broken_wiring (__main__.EvidenceTools.test_backticks_warn_without_claiming_broken_wiring) ... ok
test_explicit_restriction_is_still_enforced (__main__.EvidenceTools.test_explicit_restriction_is_still_enforced) ... ok
test_face_words_are_not_an_automatic_failure (__main__.EvidenceTools.test_face_words_are_not_an_automatic_failure) ... ok
test_full_graph_changes_are_not_lost (__main__.EvidenceTools.test_full_graph_changes_are_not_lost) ... ok
test_same_graph_is_not_reported_as_same_output (__main__.EvidenceTools.test_same_graph_is_not_reported_as_same_output) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.010s

OK
```

## 本地交付文件及 SHA256

这些详细报告位于本地 outputs，未作为新案例或模板提交。以下指纹用于核对本次报告所依赖的实际文件。

| 完整路径 | 字节 | SHA256 |
|---|---:|---|
| `C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\outputs\replay-all-png\inventory.json` | 6601447 | `d43de1c7c2d62a14998311722f54210ea3c1a4c0cd05e606994e82892b4deb40` |
| `C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\outputs\replay-all-png\replay-515.json` | 152775 | `ef0db67690bf556e798d2a5d44b38be6164aec0d76e896f3c5e1fe8800326737` |
| `C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\outputs\replay-all-png\replay-478.json` | 87227 | `97e899d07243bed1b2ad6735c1784039450d50ee0cc8cd33e133d2e0ad4940cc` |
| `C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\outputs\replay-all-png\evidence-hashes.json` | 13025 | `307066d2bae8d9c0843e4b43b472d9706744a57a8d6043ffaf87eb88ad3dc489` |
| `C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\outputs\replay-all-png\summary.json` | 723 | `ab5da678c61b4733c2723505ccea4db270ab0ae21c5499da272af782031eb2ba` |
| `C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\outputs\replay-all-png\test-results.json` | 3293 | `299aac1d331921927a4a0c7bffb1fcec777a24eacb3fbcc8b26b438d1599d95d` |
| `C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\outputs\replay-all-png\scan_inventory.py` | 5792 | `2c29a41133293eabec5cef31f6683269cc0b20029af412757f7289c762663a14` |
| `C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\outputs\replay-all-png\audit_replays.py` | 11207 | `8a4057a4fe110701ee1ebbe252ee16dd9099c8fec7c293b701bec4a33f4faa42` |
| `C:\Users\xiaoj\Documents\Codex\2026-10-19\nin\outputs\replay-all-png\run_checks.py` | 1125 | `bfc4f59e8044a5ad9ca763196d75041af16b426218fb2dedfeea82fc9b095ff6` |

## 本次修改边界

仓库仅新增本报告：`skills/fourview-headless/references/replay-report.md`。main、render.py、verify.py、所有固定模板和已有案例均不修改。未合并，不强推。
