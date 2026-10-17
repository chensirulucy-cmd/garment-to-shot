# 成品提示词：合成 → 自然化 → 质感统一 → 只修脸

每条都标了**验证状态**。未实测的只作备用，不要当成已验证配方讲给用户。

## 1. 合成正向（基础版 · 已跑通，场景与服装正确）

```
Place the woman from <image1> into the office in <image3>, seated in the mesh task chair at the desk, dressed in the outfit from <image2>, and change nothing else in <image3>. <image1> is the only identity reference: take her face, hair, skin tone and body build exactly as that image shows them, add nothing to her features and carry over no clothing from it. <image2> is the only wardrobe reference: dress her in the garments it shows, keeping their garment count, design, cut, silhouette, colour, fabric, weave, sheen, print, seams, stitching, buttons, zips, fastenings, collars, cuffs, hems and footwear exactly as that image has them, and do not redesign, recolour, simplify, replace, add or divide any garment or accessory. <image3> is the canvas: keep its room exactly as it is, with the desk and its dark metal frame, the closed laptop, the white mug, the notebook and pen, the chair, the glass curtain wall with its mullions, the skyline and the river beyond, the off-white wall, the sideboard with its vase and the tall plant all in their own places, at their own scale and in their own light. Seat her in the chair that already stands at the desk: her back against the chair back, her body angled a few degrees to her left, her head and shoulders at the scale the chair, the desk and the room set, her hands resting on the desktop beside the closed laptop, and her lap and thighs hidden by the desktop where it crosses in front of her. Add a soft contact shadow under the chair base and a natural shadow under her body on the seat and on the floor, and let the same daylight from the glass wall and the same room light fall on her from the same direction and at the same colour temperature as the rest of the room, so she reads as a person who was sitting there when the photograph was taken. Her face is turned squarely to the camera, her eyes level on the lens, her expression calm and closed-mouthed, and her hair falls naturally on both sides. Do not move, remove, restyle, recolour, brighten or re-light anything that was already in <image3>, do not add any other person, furniture, prop or object, and keep the frame the same size and the same viewpoint as <image3>.
```

## 2. 自然化正向（中近景 · 已跑，比基础版好，但仍有合成感）

与基础版的差异：取景收成腰以上（脸占比 30–40%）、只由场景窗光照亮并禁止影棚感、显式要接触阴影与体重感、发丝融合、与场景同一层景深、皮肤不磨皮、双手在桌上且不被裁。

```
Place the woman from <image1> into the office in <image3>, seen from the waist up, seated in the mesh task chair at the desk, dressed in the outfit from <image2>, and change nothing else in <image3>. Keep the camera exactly where it is in <image3>: the same viewpoint, the same height, the same angle and the same lens, so the room keeps the perspective it already has. Frame her as a medium close-up that fills the picture from the top of her head down to just below the waist, with the lower edge of the frame cutting across her skirt above the hip so that neither her hands nor her elbows are cut, her head and shoulders large in the frame and her face clearly readable at full detail, and the glass curtain wall and the skyline filling the space above her shoulder. <image1> is the only identity reference: take her face, hair, skin tone and body build exactly as that image shows them, reproducing her facial structure, eye shape and spacing, nose, lips and jawline at full fidelity, add nothing to her features and carry over no clothing from it. <image2> is the only wardrobe reference: dress her in the garments it shows, keeping their garment count, design, cut, silhouette, colour, fabric, weave, sheen, print, seams, stitching, buttons, zips, fastenings, collars, cuffs, hems and footwear exactly as that image has them, and do not redesign, recolour, simplify, replace, add or divide any garment or accessory. Seat her so that she carries her own weight: her back and hips press into the chair seat with a soft shadow where her body meets the cushion, her forearms rest on the desktop with a faint contact shadow under each forearm, both hands lie open on the desk beside the closed laptop with the fingers clearly separated and correctly counted, and the near end of the table crosses in front of her below the waist. Light her only from the window that already lights <image3>: the daylight comes from the same side, at the same angle and at the same cool colour temperature as it falls on the desk and the chair, it leaves the same soft highlight on the side of her face that it leaves on the table edge, it carries a little cool spill onto the edge of her hair and shoulder, and it leaves the shaded side of her face lit only by the warm bounce of the room, so no studio key, no softbox, no frontal fill and no rim light touches her anywhere. Keep her skin natural and unretouched, with visible pores, fine texture and its own small variations, her hair blending into the background strand by strand with a few loose hairs crossing its edge and no cut-out line and no halo anywhere along her outline, and keep her clothing real: the weave and the folds of her knit, the thickness of the fabric at the seams and hems, the grain of the leather and a small honest highlight on the metal of her belt. Hold one single depth of field across the whole picture, the same one <image3> has, so the desk, the chair, the plant and the skyline fall away exactly as softly as they do in that image while she and the desk share one level of sharpness. Do not move, remove, restyle, recolour or re-light anything that was already in <image3>, including the small reflections on the glass and the contact shadows under the cup, the pen, the laptop and the plant, do not add any other person, furniture, prop or object, and keep the room, its proportions and its viewpoint exactly as they are.
```

### 负向（基础负向之后追加）

```
a different face, altered facial features, changed hairstyle, different hair colour, changed skin tone, changed body build, clothing from <image1>, bare shoulders where the outfit covers them, mixed outfits, extra garments, added accessories, added jewellery, added bag, added belt, missing garment pieces, redesigned clothing, simplified design, recoloured garment, added pattern, floating figure, no contact shadow, cut at the waist, cropped legs, feet not on the floor, wrong scale against the desk, a second person, extra limbs, extra fingers, deformed hands, deformed feet, mannequin, ghost mannequin, empty clothes with no body, text, watermark, logo, low resolution, blurry, plastic skin, waxy skin, illustration, painting, anime, cartoon, CGI, obvious 3D render
```

自然化时再追加：

```
wide shot, distant framing, small face, tiny face, full-body framing, studio lighting, softbox, frontal key light, rim light, beauty lighting, cut-out edge, halo, pasted-on appearance, sticker edge, weightless, missing shadows under objects, uniform depth of field, everything in focus, beauty filter, airbrushed skin, plastic skin, over-smoothed fabric, material without texture, hidden hands, cropped hands, missing fingers, merged fingers, glass without reflection, photo-composite look
```

## 3. 质感统一刀（备用 · 未实测）

`<image1>` = 上一刀成品图。保留结构，只改光与质感——专削合成感。

```
Keep everything in <image1> exactly where it is — her pose, her face, her hair, her clothing, the desk, the chair, the room, the objects and the framing — and make the picture look like one real photograph taken in that room instead of a composite: give her skin its natural texture and pores, give the knit its weave and folds, set every object down on the surface it stands on with its own soft contact shadow, let the window light fall on her from the same direction and colour temperature as it falls on the desk, soften the background exactly as much as the room itself is soft, and remove every cut-out line, halo and pasted-on edge. Change no content, no colour design, no pose and no framing, and add or remove nothing.
```

## 4. 只修脸刀（备用 · 未实测）

`<image1>` = 成品图，`<image2>` = 身份图。

```
Keep everything in <image1> exactly as it is — her pose, her hair, her body, her clothing, the desk, the chair, the room, the background, the lighting, the colours and the framing — and replace only her face with the face of the woman in <image2>: the same facial structure and face shape, the same eye shape and eye spacing, the same eyebrows, the same nose, the same lips and the same jawline as <image2>, with the same skin tone, the same apparent age and the same natural skin texture, blended cleanly into her head at the hairline, the temples, the ears, the jaw and the neck so that no seam and no halo is visible and her hairline and hairstyle stay unchanged. Keep her head the same size, at the same angle and in the same position in the frame, keep her expression calm and closed-mouthed and her gaze on the camera, and do not change anything else in the picture.
```

负向：

```
different pose, moved head, changed hairstyle, changed hairline, changed body, changed clothing, changed background, changed lighting, altered framing, zoomed, cropped differently, a different person, a second face, deformed face, distorted facial features, facial asymmetry, mismatched skin tone, visible seam, halo around the face, pasted-on face, mask edge, blurry face, plastic skin, waxy skin, cartoon, illustration, CGI, text, watermark, low resolution
```

## 5. 实测数字（用来判断「要不要改取景」）

| | 身份图 | 合成图（坐姿全身） | 合成图（中近景） |
|---|---|---|---|
| 画幅 | 832×1216 | 832×1216 | 832×1216 |
| 脸占画面高 | 55–60% | 9–15% | 30–40% |
| 脸高（px） | ≈700 | ≈120–180 | ≈370–490 |

- 线性比 ≥1/2 才谈得上「像」；<1/4 必然只剩「同类面孔」。
- 输出提到 1216×1824（2.2 MP）可在同取景下再把脸高抬约 1.5 倍，且 8 GB 卡仍安全。

## 6. 性能对照（8 GB 卡实测）

| 情形 | 数字 |
|---|---|
| 正常 | 25 步 @ 1 MP → **2.6 s/it**（≈92 秒） |
| 输出被顶到 9.11 MP | 每步数十秒–百秒，像卡死；重启进程无用 |
| 视频模型 staged 40 GB | 每步 80–166 s |

跑的时候看 GPU 利用率：长期 <20% 且显存钉在 7.9 GB = 在换页，不是「在算」。提速顺序：压像素 → 挂 8 步 Lightning LoRA（cfg 1.0）→ 再谈步数。
