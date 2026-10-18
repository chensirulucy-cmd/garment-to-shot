# 用文字复刻一件服装（而不是用服装图）

服装有两条路线：**文生图 + 文字清单** 与 **编辑 + 服装图**。路线选错的代价是「货不对版」，所以先按下表定级，再决定用哪条线。

## 一、文字能复刻到什么程度

| 服装类型 | 文字复刻能力 | 用哪条线 |
|---|---|---|
| **AI 生成的服装**（原型本来就是文字：自家工作流出的产品图 / 幽灵服装台） | **高保真，可长期逐字复用** | 文生图即可 |
| 真实拍摄 · 纯色 + 结构清晰 | 同款级（材质与标志性结构件对得上） | 文生图（展示镜）/ 编辑（细节镜） |
| 真实拍摄 · **印花 / 条纹 / 渐变 / 特殊纹理 / logo** | **必漂**（图案走向、密度、位置全不受控） | 必须走编辑 + 服装图 |
| 真实拍摄 · 非对称剪裁 / 复杂褶皱 / 特殊工艺 | 半可控 | 结构件逐个写死，或走编辑 |

**机制**：文字是结构性描述，能锁的是**件数、结构件、颜色、材质**；锁不住的是**高频随机信息**（印花走向、织纹随机性）。AI 生成的服装本身没有真实高频信息，所以文字能原样再来一遍 —— 不要把这条归功于措辞。

## 二、「神似但不件件对齐」是文字线的常态

即使整体很像，仍会有 2–3 处结构漂移，典型三种：**领型被简化**（V 领 → 圆领/系带领）、**装饰位置被合并**（门襟两侧对称荷叶边 → 只留中部）、**可见细节数量变少**（两粒扣 → 只见一粒）。
→ 因此：**展示镜、氛围镜、多场景镜**用文字线没问题；**「货对版」的商品特写**必须用编辑 + 服装图。

## 三、结构清单四块（照填，跨镜逐字复用）

1. **结构件**：件数 · 领型 · 标志性结构（蝴蝶结 / 荷叶边 / 门襟 / 腰带）· 钮扣数量与位置 · 袖型与袖口（如收束后外扩的喇叭口）· 下装版型（高腰 / 铅笔 / A 字 / 百褶 + 缝线省道一类位置细节）· 鞋型
2. **材质**：纤维与织法（fine-rib knit / sheer chiffon / silk satin）+ 透度（semi-sheer）+ 垂坠与厚度（fluid drape, the weight of the folds）
3. **颜色**：每个颜色都带修饰词（dusty rose、charcoal、off-white），不用裸色名
4. **鞋与配件**：鞋型 + 跟高 + 颜色；包的形状与背法

**跨镜一致的关键是这段清单一个字都不改地复用**；每镜重新措辞 = 每镜都在微调这件衣服。清单本身存成模板（`F:\Sakura_Project\` 现成的三模块提示词文件可当样板），换衣服时只换这四块。

## 四、幽灵服装台（纯文生图）七段骨架

跑「服装照没有、只要一张挂拍/幽灵人台图」时用这个骨架，七段顺序固定：

1. **定调句**：`Photorealistic costume-department garment reference photograph of an invisible-mannequin display, presented in a warm, soft commercial studio light:`
2. **括号清单**：`[TOP: …], [BOTTOM: …], [SHOES: …]`——每件只写结构件（领型 / 袖长与袖口 / 下摆 / 腰头 / 五袋 / 裤型收口 / 鞋型与鞋底），不写风格词。
3. **隐形身体**：`appears worn by an invisible body with natural hollow volume` + 逐处点名空腔（空领口 / 两只空袖口 / 空腰头 / 两条空裤管 / 鞋里空着），并以一句 `No person, no mannequin, no dress form, no body, no arms, no hands, no legs, no feet, no skin anywhere in the frame` 收口。
4. **视角与可见细节**：`Front view, the complete outfit from … down to … filling most of the frame`，再列举要看见的缝线与部件（肩缝 / 罗纹领 / 袖口 / 腰头 / 铜扣 / 门襟 / 裤脚 / 鞋带与鞋底围条）。
5. **廓形段**：用两句写「贴而不紧」与「从哪收到哪」（`sits close without pulling` / `tapers to a narrow ankle opening` / `reads as … rather than anything oversized, baggy or flared`）。
6. **光与背景**：浅暖灰无缝底 + 前上左柔光 + 鞋下一道接触影 + 三色分离句。
7. **排除与保真**：`The outfit consists of … only: no bag, no belt, no jewellery` + 每个主色一条「保持 X、不许变 Y」（白棉不许变米/灰/蓝，浅蓝牛仔不许变藏青/黑/灰，白帆布鞋不许变米/灰）+ `No text, no labels, no watermark`。

**两条硬规则**：① 这条线通常是 `cfg 1` —— **负向完全不生效**，「不许出现人」只能靠第 3 段正压；② 版式跟服装一起变，换一件只换第 2 段清单与第 5 段廓形，其余五段逐字复用。

## 五、与身份提示词的关系（LoRA 生效时的写法）

- **LoRA 接走了「身份」那部分权重**，服装描述不必再和「这是谁」抢注意力，细节更容易被完整执行 —— 这是「加了 LoRA 之后衣服反而更像」的机制，不是措辞变好了。
- LoRA 生效时的正向默认写法：`触发词 + 年龄段 + identical face from the character master portrait`，**不再写五官清单**（五官描写会与 LoRA 抢身份，把脸往「通用好看脸」拉）。要写五官清单就先做 A/B：同一套服装清单、同一 seed 区间，带清单 vs 不带，各抽 N 张，选更像 LoRA 脸的那版再定稿。
