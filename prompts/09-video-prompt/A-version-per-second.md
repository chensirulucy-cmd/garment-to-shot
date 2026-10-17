# A 版 · 官方骨架写法（逐秒编排）

**实测结果**：文件 `MiniMax_H3_00060_.mp4`（832×1440 · 24fps · 8.000s · 单镜）
**结构来源**：官方 `3d-animation-short-generator` 的六列分镜表 + 每秒五要素（`sources/minimax-official/shot-table-spec.md`）
**语法来源**：官方 Ref2VA 六段（`sources/minimax-official/ref-en.txt`）

## 六列分镜表（编译前）
| Shot ID & Duration | Continuity Handoff | Reference Anchors | Hook Type | Shot Description + 每秒指令 | Audio |
|---|---|---|---|---|---|
| S01 / 8s | 开场；结尾锁"手机光下的微笑脸"供下一镜接 | Landmarks：沙发=左半中景／茶几=底部前景／右窗纱帘+街灯／左墙绿植；Position：她=中央偏左、坐姿蜷腿、朝右前；Light：电视冷白主光（前偏左）+ 街灯暖轮廓（右）；Identity：`<Subject 1>`+`<Subject 2>` | tender | 中景→近景，唯一运镜=小幅慢推；逐秒 0–8s 五要素齐 | 电视环境声／两段震动／陶瓷杯触桌／缎面摩擦／一次轻呼吸；无台词 |

## 提示词（H3 Ref2VA 六段）
见 `A-version-ref2va.txt`（与本文件同目录）。

## 实测指标（客观）
平均运动 16.99 · 峰值 35.09（4.5–5.0s）· **前 2 秒 0.35–4.56（有静场）** · 亮度 97.9→112.8
→ 特征：**先静 → 爆发 → 收住**；能指定"哪一秒不动"。
