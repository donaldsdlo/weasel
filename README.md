# Rime 输入法配置仓库

本仓库是一套精心调校的 Rime 输入法配置集合，涵盖自然码双拼（含辅助码）、五笔86、小鹤音形、雾凇拼音、以及多种不带辅助码的双拼方案，适用于 Windows 小狼毫（Weasel）平台。

---

## 目录

- [为什么选择 Rime 而不是商业输入法](#为什么选择-rime-而不是商业输入法)
- [Windows 安装与配置](#windows-安装与配置)
- [自然码双拼输入法教程](#自然码双拼输入法教程)
- [五笔86输入法教程](#五笔86输入法教程)
- [小鹤音形输入法教程](#小鹤音形输入法教程)
- [各种不带辅助码的双拼方案](#各种不带辅助码的双拼方案)
- [雾凇拼音（rime_ice）](#雾凇拼音rime_ice)

---

## 为什么选择 Rime 而不是商业输入法

### 隐私与数据安全

商业输入法（搜狗、百度、讯飞等）的核心商业模式是数据采集。你的每一次按键、每一条输入内容都可能被上传到服务器，用于用户画像、广告推送甚至更广泛的商业目的。Rime 是完全开源的自由软件（GPLv3），**所有计算在本地完成，不联网、不上传任何数据**，你的输入内容永远只属于你自己。

### 可控性与可定制性

商业输入法的功能和行为由厂商决定——你不能修改词库排序逻辑，不能自定义候选窗样式，不能调整按键映射。Rime 的每一个配置项都是透明的 YAML 文件，你可以：

- 自由组合输入方案（全拼、双拼、五笔、形码……）
- 定制按键行为、候选排序、标点映射
- 编写 Lua 脚本扩展功能
- 完全掌控自己的词库和用户数据

### 长期稳定性

商业输入法随时可能改版、加入广告、调整策略，甚至停止维护。Rime 由开源社区维护，配置文件是纯文本，**一次配置、终身可用**，不会因版本更新丢失你的定制。

### 跨平台一致性

Rime 支持 Windows（小狼毫）、macOS（鼠须管）、Linux（fcitx5-rime / ibus-rime），同一套配置可在所有平台上使用，体验一致。

### 对专业输入方案的支持

商业输入法通常只支持主流的全拼和少数双拼，对五笔、自然码、小鹤音形等专业方案支持有限或根本不支持。Rime 社区有大量高质量的专业方案词库和配置，本仓库正是其中之一。

---

## Windows 安装与配置

### 安装步骤

1. **下载小狼毫（Weasel）**：访问 [Rime 发布页](https://github.com/rime/weasel/releases) 下载最新版安装包
2. **安装**：运行安装程序，默认安装路径为 `C:\Program Files (x86)\Rime\weasel-<版本号>`
3. **部署配置**：安装完成后，右键系统托盘的小狼毫图标 →「部署」，等待编译完成

### 配置文件目录

|路径                                              |说明                                  |
|------------------------------------------------|------------------------------------|
|`%APPDATA%\Rime`                                |用户配置目录（所有 .yaml 配置文件、词库、Lua 脚本均在此目录）|
|`%APPDATA%\Rime\build\`                         |编译输出目录（部署后自动生成，勿手动编辑）               |
|`C:\Program Files (x86)\Rime\weasel-<版本号>\data\`|程序内置默认配置（勿修改）                       |

> 本仓库的文件应全部复制到 `%APPDATA%\Rime` 目录中，覆盖同名文件后重新部署即可。

### 核心配置文件说明

|文件                    |作用                            |
|----------------------|------------------------------|
|`default.custom.yaml` |全局配置：方案列表、按键绑定、候选页大小、中英切换键    |
|`weasel.custom.yaml`  |Windows UI 样式：配色方案、字体、字号、候选窗布局|
|`squirrel.custom.yaml`|macOS UI 样式（本仓库保留供跨平台使用）      |
|`installation.yaml`   |安装信息：发行版名称、版本号、安装 ID          |
|`color_schemes.yaml`  |自定义配色方案集合（通过 `__include` 引入）  |

### default.custom.yaml 关键配置项

```yaml
patch:
  # 中英切换键设定
  "ascii_composer/good_old_caps_lock": true
  "ascii_composer/switch_key":
    Caps_Lock: clear          # Caps Lock 清除输入
    Control_L: noop           # 左 Ctrl 无操作
    Shift_L: commit_code      # 左 Shift 提交编码（上屏）
    Shift_R: noop             # 右 Ctrl 无操作

  # 候选项标签
  "menu/alternative_select_labels": ["①","②","③","④","⑤","⑥","⑦","⑧","⑨"]
  "menu/page_size": 6         # 每页候选数

  # 候选选择键
  key_binder:
    select_first_character: bracketleft   # [ 选第一个
    select_last_character: bracketright   # ] 选最后一个

  # 翻页键
  "key_binder/bindings":
    - {accept: minus, send: Page_Up, when: has_menu}    # - 上翻页
    - {accept: equal, send: Page_Down, when: has_menu}  # = 下翻页

  # 输入方案列表
  schema_list:
    - {schema: rime_ice}              # 雾凇拼音
    - {schema: double_pinyin_flypy}   # 小鹤双拼
    - {schema: double_pinyin_abc}     # 智能 ABC 双拼
    - {schema: double_pinyin_mspy}    # 微软双拼
    - {schema: double_pinyin_sogou}   # 搜狗双拼
    - {schema: double_pinyin_ziguang} # 紫光双拼
    - {schema: zrm2000}               # 自然码2000
    - {schema: wubi86_jidian}         # 五笔86极点版
    - {schema: openfly}               # 开源小鹤
    - {schema: latex}                 # LaTeX 符号
    - {schema: melt_eng}              # 英文输入

  # 方案选单呼出键
  "switcher/hotkeys": ["Control+grave"]
```

### weasel.custom.yaml 关键配置项

```yaml
patch:
  "style/+":
    color_scheme: catppuccin_frappe          # 浅色配色
    color_scheme_dark: catppuccin_mocha      # 深色配色
    font_face: "LXGW WenKai Mono GB,文津宋体..."  # 候选字体
    font_point: 20                           # 字号
    horizontal: false                        # 竖排候选
    inline_preedit: true                     # 内嵌编码
    label_format: "%s."                      # 候选序号格式

  # 按应用强制英文模式
  # app_options:
  #   chrome.exe: {ascii_mode: true}
  #   WindowsTerminal.exe: {ascii_mode: true}
```

### 部署与生效

修改任何 `.yaml` 配置文件后，必须重新部署才能生效：

- 右键托盘图标 →「部署」（或按快捷键 `Ctrl+Grave` 呼出方案选单后关闭也会触发部署）
- 部署时间取决于词库大小，自然码词库较大可能需要 1-3 分钟

---

## 自然码双拼输入法教程

### 什么是自然码

自然码由周志农先生于 1986 年发明，是一种**音形结合**的输入法。它将汉字的拼音用双拼压缩为两键输入，同时提供形码（辅助码）用于快速筛选同音字。自然码是国内最早的双拼方案之一，影响深远。

### 自然码双拼键位映射

自然码双拼的核心规则：**声母一键 + 韵母一键 = 一个音节**。

#### 声母键位

|键|声母|说明|
|-|--|--|
|b|b |  |
|p|p |  |
|m|m |  |
|f|f |  |
|d|d |  |
|t|t |  |
|n|n |  |
|l|l |  |
|g|g |  |
|k|k |  |
|h|h |  |
|j|j |  |
|q|q |  |
|x|x |  |
|r|r |  |
|z|z |  |
|c|c |  |
|s|s |  |
|y|y |  |
|w|w |  |

#### 特殊声母

|键 |声母|说明    |
|--|--|------|
|zh|i |「知」的声母|
|ch|u |「吃」的声母|
|sh|v |「诗」的声母|

#### 韵母键位

|键|韵母       |示例         |
|-|---------|-----------|
|a|a        |啊 aa       |
|o|o        |哦 oo       |
|e|e        |额 ee       |
|i|i        |一 i（零声母）   |
|u|u        |五 u（零声母）   |
|v|ü        |鱼 jv（ju→jv）|
|b|ou       |走 zb       |
|c|iao      |笑 xc       |
|d|iang/uang|将 jd / 狂 kd|
|f|en       |分 ff       |
|g|eng      |更 gg       |
|h|ang      |航 hh       |
|j|an       |千 qj       |
|k|ao       |考 kk       |
|l|ai       |来 ll       |
|m|ian      |面 mj       |
|n|in       |新 xn       |
|p|un/ün    |春 cp / 军 jp|
|q|iu       |秋 qq       |
|r|uan/üan  |穿 cr / 圈 qr|
|s|ong/iong |送 ss / 兄 xs|
|t|ue/üe    |绝 jt / 缺 qt|
|w|ua/ia    |化 hw / 家 jw|
|x|ie       |些 xx       |
|y|ing/uai  |星 xy / 快 ky|
|z|ei       |贼 zz       |

#### 零声母处理

没有声母的音节，双拼时声母键即韵母键本身：

- a → aa，o → oo，e → ee
- ai → el（注意不是 al），an → ej，ang → eh，ao → ek
- ou → eb，en → ef，eng → eg

### 自然码辅助码（形码）

辅助码是自然码的灵魂——当双拼输入后同音字过多时，追加 1-2 个形码即可快速定位目标字。

#### 辅助码编码规则

自然码形码取字的首部和尾部偏旁的声母：

- **码3 = 主形码**：取字的第一个部件（偏旁部首）的声母
- **码4 = 次形码**：取字的最后一个部件的声母

#### 常用偏旁部首对应键

|部首 |键|部首   |键|部首 |键|
|---|-|-----|-|---|-|
|日/曰|r|月    |y|金/钅|j|
|木  |m|水/氵/氺|u|火/灬|h|
|土/士|t|草/艹  |c|竹/⺮|v|
|口  |k|手/扌  |f|女  |n|
|石  |i|王/玉/𤣩|w|心/忄|x|
|目  |u|虫    |i|走/辶|z|
|足/⻊|z|车    |e|弓  |g|
|纟/糸|s|贝    |b|食/饣|i|
|犭  |q|衤    |i|鱼/⺈|y|

#### 辅助码使用示例

|字|双拼|主形码   |次形码 |完整编码|解释            |
|-|--|------|----|----|--------------|
|胡|hu|o（月/肉）|g（古）|huog|月=肉旁(o) + 古(g)|
|湖|hu|u（氵）  |g（古）|huug|水(氵=u) + 古(g) |
|蝴|hu|i（虫）  |g（古）|huig|虫(i) + 古(g)   |
|壶|hu|k（口）  |y（业）|huky|口(k) + 业形(y)  |
|虎|hu|i（虍）  |g（几）|huig|虎头(i) + 几(g)  |

#### 辅助码查字（反查）

在自然码方案中，输入 `oi` 前缀可以切换到拼音反查模式，通过拼音查到对应自然码编码。例如输入 `oi'hu'` 可查所有发音为 hu 的字的自然码完整编码。

### 词组输入规则

|词组类型   |编码规则    |示例              |
|-------|--------|----------------|
|二字词    |声+韵+声+韵 |「中国」→ vsgo      |
|二字词（简码）|声+声     |「中」+「国」→ vg（二简词）|
|三字词    |声+声+声   |「计算机」→ jsj      |
|四字词及以上 |声+声+声+末声|「显而易见」→ ysej    |

### 本仓库自然码方案特点

本仓库的 `zrm2000` 方案基于《自然码2009新春版》V7.27 码表，包含：

- **完整的自然码双拼 + 辅助码**编码
- 8105 通用规范汉字 + 41448 大字表
- 多领域扩展词库（计算机、医学、法律、财经、地理、成语、动物、食物等 30+ 子词库）
- 万象语言模型（`wanxiang-lts-zh-hans.gram`）提供智能语句预测
- 自定义短语（`custom_phrase.txt`）
- Lua 扩展：以词定字、Vim 模式

---

## 五笔86输入法教程

### 什么是五笔

五笔字型由王永民先生于 1983 年发明，是纯正的**形码**输入法，不依赖读音，按汉字的笔画和字根进行编码。五笔86是最广泛使用的版本。

### 五笔基本概念

#### 五种笔画

|笔画    |代号|键区       |
|------|--|---------|
|横（一）  |1 |G F D S A|
|竖（丨）  |2 |H J K L M|
|撇（丿）  |3 |T R E W Q|
|捺/点（丶）|4 |Y U I O P|
|折（乙）  |5 |N B V C X|

#### 字根分布

键盘分为 5 个区，每区 5 个键位，共 25 个键位对应约 200 个基本字根：

|区      |键        |主要字根     |
|-------|---------|---------|
|1区（横）  |G F D S A|王 土 大 木 工|
|2区（竖）  |H J K L M|目 日 口 田 山|
|3区（撇）  |T R E W Q|禾 白 月 人 金|
|4区（捺/点）|Y U I O P|言 立 水 火 之|
|5区（折）  |N B V C X|已 子 女 又 幺|

> 完整字根表请参考五笔86标准字根图。

### 单字编码规则

#### 键名字

每个键位上有一个「键名字」（字根表第一个字），连击 4 次该键即可输入：

- GGGG → 王，FFFF → 土，DDDD → 大，SSSS → 木，AAAA → 工
- HHHH → 目，JJJJ → 日，KKKK → 口，LLLL → 田，MMMM → 山

#### 成字字根

字根表中除键名外的独立汉字，编码规则：**键位码 + 第一笔画 + 第二笔画 + 末笔画**

- 「五」：G（字根所在键）+ G（横）+ H（竖）+ G（横）= GGHG
- 「雨」：F + G + H + Y = FGHY

#### 合体字（最常见情况）

取码规则：**按书写顺序，取 1/2/3/末 共四个字根**

- 「型」：GA+J+H → 一 廾 刂 土 → GAJF
- 「照」：J+V+K+O → 日 刀 口 灬 → JVKO

不足四码的字，补末笔识别码：

| 结构 \ 末笔 | 横 | 竖 | 撇 | 捺/点 | 折 |
|-------------|----|----|----|----|----|
| 左右结构 | G | H | T | Y | N |
| 上下结构 | F | J | R | U | B |
| 杂合结构 | D | K | E | I | V |

- 「叭」：K W（口+八）+ 末笔捺+左右型 = Y → KWY
- 「只」：K W（口+八）+ 末笔捺+上下型 = U → KWU

### 词组编码规则

| 词组类型 | 编码规则 | 示例 |
|----------|----------|------|
| 二字词 | 每字取前两码 | 「中国」→ K H L G |
| 三字词 | 前两字各取首码 + 第三字取前两码 | 「计算机」→ T Y S M |
| 四字词 | 每字各取首码 | 「科学技术」→ T I R S |
| 多字词 | 前三字各取首码 + 末字首码 | 「中华人民共和国」→ K W W L |

### 本仓库五笔方案特点

`wubi86_jidian` 方案基于极点五笔86码表（KyleBing 维护），包含：

- 四码自动上屏（`auto_select: true`）
- 极爽版优化词库
- 反查拼音（输入拼音码可查五笔编码）
- 简繁切换
- 扩展字符集支持
- Lua 扩展：日期时间、简易计算器（`coco` 前缀）、重复上一次输入
- 附加词库：个人词库、Hamster 词库、扩展词库、行政区域词库

---

## 小鹤音形输入法教程

### 什么是小鹤音形

小鹤音形由何海峰先生设计，是一种**双拼+形码**的输入方案。与小鹤双拼（纯双拼）不同，小鹤音形在双拼基础上增加了形码部分，实现四码定字、极少重码的高效输入。

### 小鹤双拼键位映射

小鹤双拼与自然码双拼不同，以下是键位对照：

#### 声母

| 标准声母 | 键 | 说明 |
|---------|---|------|
| zh | u | |
| ch | i | |
| sh | v | |
| 其余 | 原键 | b p m f d t n l g k h j q x r z c s y w |

#### 韵母

| 键 | 韵母 | 键 | 韵母 | 键 | 韵母 |
|----|------|----|------|----|------|
| a | a | b | ou | c | in |
| d | uang/iang | e | e | f | en |
| g | eng | h | ang | i | i |
| j | an | k | uai/ing | l | ai |
| m | ian | n | iao | o | uo |
| p | un/ün | q | iu | r | uan/üan |
| s | ong/iong | t | ue/üe | u | u |
| v | ü | w | ia/ua | x | ie |
| y | ao | z | ei |

### 小鹤形码（辅助码）

小鹤形码取字的首部件和末部件编码：

#### 主形码（第3码）

取字的第一个部件对应键位，规则如下：

| 类别 | 部件举例 | 键 |
|------|---------|---|
| 横起 | 一 丁 工 大 木 王 | a |
| 竖起 | 丨 卜 止 占 且 | o |
| 撇起 | 丿 千 禾 白 月 人 | e |
| 点起 | 丶 主 立 辛 门 之 | i |
| 折起 | 乙 己 民 巴 马 巨 | u |

#### 次形码（第4码）

取字的最后一个部件，规则同上。

### 小鹤音形使用示例

| 字 | 双拼 | 主形码 | 次形码 | 完整编码 |
|----|------|--------|--------|----------|
| 的 | de | a（白横起） | | dea |
| 是 | vi | a（日横起） | | via |
| 我 | wo | e（撇起） | | woe |
| 不 | bu | a（横起） | | bua |

> 小鹤音形四码自动上屏，无重码时直接出字。

### 本仓库小鹤方案特点

`openfly` 方案是开源小鹤 Rime 配方（amorphobia 维护），包含：

- 完整的小鹤双拼 + 形码编码
- 自动四码上屏（`auto_select: true`）
- 形码提示（`openfly_hint_filter`）
- Lua 扩展：日期、时间、快捷符号
- 反查功能（通过 `openfly_reverse` 词库）
- 历史输入重复（`;f` 触发）

---

## 各种不带辅助码的双拼方案

本仓库基于雾凇拼音（rime-ice）适配了 6 种双拼方案，它们共享相同的词库和功能，仅双拼键位映射不同。**不带辅助码**意味着只需双拼两键输入音节，不加形码，适合纯双拼用户。

### 方案列表

| 方案名 | schema_id | 说明 |
|--------|-----------|------|
| 小鹤双拼 | double_pinyin_flypy | 小鹤键位，无辅助码 |
| 自然码双拼 | double_pinyin | 自然码键位，无辅助码（注意与 zrm2000 方案不同） |
| 微软双拼 | double_pinyin_mspy | Windows 系统内置双拼键位 |
| 搜狗双拼 | double_pinyin_sogou | 搜狗输入法双拼键位 |
| 智能 ABC 双拼 | double_pinyin_abc | 智能 ABC 双拼键位 |
| 紫光双拼 | double_pinyin_ziguang | 紫光/华宇双拼键位 |

### 各方案双拼键位对照

#### 声母对照

| 方案 | zh | ch | sh |
|------|----|----|-----|
| 自然码 | i | u | v |
| 小鹤 | u | i | v |
| 微软 | u | i | v |
| 搜狗 | v | i | u |
| 智能 ABC | a | e | v |
| 紫光 | u | i | o |

#### 韵母对照（部分重点差异）

| 韵母 | 自然码 | 小鹤 | 微软 | 搜狗 | ABC | 紫光 |
|------|--------|------|------|------|-----|------|
| iang/uang | d | d | d | d | t | d |
| ing/uai | y | k | ; | y | s | y |
| iong/ong | s | s | s | s | d | s |
| ian | m | m | m | m | j | m |
| iao | c | n | c | n | z | n |
| uan/üan | r | r | r | r | c | r |
| ue/üe | t | t | t | t | v | t |
| un/ün | p | p | p | p | y | p |
| ou | b | b | b | b | p | b |
| ai | l | l | l | l | s | l |
| ei | z | z | z | z | w | z |
| ao | k | y | k | k | h | k |
| en | f | f | f | f | r | f |
| eng | g | g | g | g | t | g |
| an | j | j | j | j | f | j |
| ang | h | h | h | h | g | h |

### 共享功能

所有双拼方案均继承自雾凇拼音，共享以下功能：

- **英文混输**：`melt_eng` 次翻译器，中英文无需切换
- **部件拆字反查**：输入 `uU` + 部件拼音（如 `uUkh` → 「口」），查字并显示编码
- **辅码查词**：输入编码后按 `` ` `` 引导辅码，筛选候选（`search.lua`）
- **自定义短语**：`custom_phrase_double.txt`
- **日期时间**：`rq`（日期）、`sj`（时间）、`xq`（星期）
- **农历**：`nl` + 数字
- **数字大写**：`R` + 数字
- **Unicode**：`U` + 十六进制编码
- **符号**：`v` 模式（`v` + 数字/字母组合）
- **简繁切换**、**Emoji 开关**
- **错音错字提示**（`corrector.lua`）
- **长词优先**、**英文自动大写**

### 如何切换方案

按 `Ctrl+Grave` 呼出方案选单，选择目标方案即可。或右键托盘图标 →「输入法设定」中调整方案顺序。

---

## 雾凇拼音（rime_ice）

### 简介

[雾凇拼音](https://github.com/iDvel/rime-ice) 是由 Dvel 维护的高质量 Rime 全拼方案，以开箱即用、词库丰富、功能完善著称。本仓库的雾凇拼音配置在此基础上进行了个性化调整。

### 核心特性

- **全拼输入**，支持简拼、超级简拼
- **自动纠错**：常见的拼写错误自动纠正（如 `hzi` → `zhi`、`wie` → `wei`）
- **英文混输**：中文状态下直接输入英文，无需切换
- **部件拆字反查**：`uU` 前缀，通过拆字查拼音和编码
- **辅码筛选**：`` ` `` 引导辅码，快速缩小候选范围
- **自定义短语置顶**：`custom_phrase.txt` 中定义的短语权重最高
- **候选项置顶**：`pin_cand_filter` 支持按编码置顶指定字词
- **长词优先**：自动将长词插入候选列表靠前位置
- **降低英文冲突**：`reduce_english_filter` 将与拼音冲突的英文单词降位
- **Emoji 支持**：候选中自动显示 Emoji
- **简繁切换**：基于 OpenCC 的高质量简繁转换
- **日期/时间/星期**：`rq` / `sj` / `xq` 快捷输入
- **农历**：`N` + 8位日期（如 `N20240115` → 农历日期）
- **数字金额大写**：`R` + 数字
- **Unicode 输入**：`U` + 十六进制编码
- **V模式符号**：`v` + 数字/字母组合快速输入特殊符号

### 词库结构

```
rime_ice.dict.yaml        → 主词库（导入以下子词库）
├── cn_dicts/8105.dict    → 通用规范汉字表 8105 字
├── cn_dicts/base.dict    → 基础词库
├── cn_dicts/ext.dict     → 扩展词库
├── cn_dicts/tencent.dict → 腾讯词向量（大词库）
└── cn_dicts/others.dict  → 杂项词库
```

### 使用技巧

| 输入 | 效果 | 说明 |
|------|------|------|
| `rq` | 2026-07-16 | 当前日期 |
| `sj` | 14:30 | 当前时间 |
| `xq` | 星期四 | 当前星期 |
| `dt` | 2026-07-16T14:30:11+08:00 | ISO 8601 |
| `ts` | 1669716794 | Unix 时间戳 |
| `nl` | 二〇二六年六月廿二 | 农历 |
| `R1234` | 壹仟贰佰叁拾肆 | 金额大写 |
| `U4e2d` | 中 | Unicode 字符 |
| `uUkh` | 口（显示拼音 kǒu） | 部件拆字反查 |
| `he` + `` ` `` + 辅码 | 筛选「he」同音字 | 辅码查词 |

### 配置定制

通过 `rime_ice.custom.yaml` 补丁文件定制，修改后重新部署生效：

```yaml
patch:
  # 开启模糊音
  speller/algebra:
    - derive/^([zcs])h/$1/     # zh→z, ch→c, sh→s
    - derive/^([zcs])([^h])/$1h$2/  # z→zh, c→ch, s→sh
```

---

## 快速开始

1. 安装小狼毫（Weasel）0.17.4+
2. 将本仓库所有文件复制到 `%APPDATA%\Rime`
3. 右键托盘图标 →「部署」
4. 按 `Ctrl+Grave` 选择输入方案
5. 开始输入

## 文件结构总览

```
%APPDATA%\Rime\
├── default.custom.yaml          # 全局配置
├── weasel.custom.yaml           # Windows UI 样式
├── color_schemes.yaml           # 配色方案集合
├── installation.yaml            # 安装信息
├── rime.lua                     # Lua 入口脚本
│
├── rime_ice.schema.yaml         # 雾凇拼音方案
├── rime_ice.dict.yaml           # 雾凇拼音词库
├── rime_ice.custom.yaml         # 雾凇拼音补丁
│
├── double_pinyin_flypy.*        # 小鹤双拼
├── double_pinyin_abc.*          # 智能 ABC 双拼
├── double_pinyin_mspy.*         # 微软双拼
├── double_pinyin_sogou.*        # 搜狗双拼
├── double_pinyin_ziguang.*      # 紫光双拼
├── double_pinyin.*              # 自然码双拼（纯双拼版）
│
├── zrm2000.schema.yaml          # 自然码2000方案
├── zrm2000.dict.yaml            # 自然码主码表
├── zrm2000.all.dict.yaml        # 自然码总词库入口
├── zrm2000.custom.yaml          # 自然码补丁
├── zrm2000.dicts/               # 自然码子词库目录
│   ├── zrm2000.8105.dict.yaml   # 8105字表
│   ├── zrm2000.base.dict.yaml   # 基础词库
│   ├── zrm2000.ext.dict.yaml    # 扩展词库
│   ├── zrm2000.tencent.dict.yaml # 腾讯词向量
│   ├── zrm2000.computer.dict.yaml # 计算机
│   ├── zrm2000.medical.dict.yaml  # 医学
│   ├── ... (30+ 子词库)
│   └── ziranma_mapping.json     # 双拼映射表
│
├── wubi86_jidian.schema.yaml    # 五笔86极点方案
├── wubi86_jidian.dict.yaml      # 五笔86主码表
├── wubi86_jidian.ico            # 方案图标
│
├── openfly.schema.yaml          # 开源小鹤方案
├── openfly.dict.yaml            # 小鹤主码表
├── openfly.primary.dict.yaml    # 一级简码
├── openfly.secondary.dict.yaml  # 二级简码
│
├── melt_eng.schema.yaml         # 英文输入方案
├── melt_eng.dict.yaml           # 英文词库
├── radical_pinyin.schema.yaml   # 部件拆字方案
├── latex.schema.yaml            # LaTeX 符号方案
├── numbers.schema.yaml          # 数字方案
├── t9.schema.yaml               # T9 九宫格方案
│
├── lua/                         # Lua 扩展脚本
│   ├── select_character.lua     # 以词定字
│   ├── date_translator.lua      # 日期时间
│   ├── lunar.lua                # 农历
│   ├── number_translator.lua    # 数字大写
│   ├── unicode.lua              # Unicode 输入
│   ├── corrector.lua            # 错音错字提示
│   ├── search.lua               # 辅码查词
│   ├── pin_cand_filter.lua      # 置顶候选
│   ├── long_word_filter.lua     # 长词优先
│   ├── reduce_english_filter.lua # 降低英文冲突
│   ├── v_filter.lua             # V模式符号优先
│   ├── autocap_filter.lua       # 英文自动大写
│   ├── vim_mode.lua             # Vim 编辑模式
│   ├── openfly_*.lua            # 小鹤专用扩展
│   ├── wubi86_jidian_*.lua      # 五笔专用扩展
│   └── ...
│
├── cn_dicts/                    # 雾凇拼音中文词库
├── en_dicts/                    # 英文/中英混合词库
├── opencc/                      # OpenCC 转换配置
├── symbols_v.yaml               # V模式符号映射
├── symbols_caps_v.yaml          # 大写V模式符号
├── custom_phrase.txt            # 自定义短语（全拼用）
├── custom_phrase_double.txt     # 自定义短语（双拼用）
└── wanxiang-lts-zh-hans.gram    # 万象语言模型
```

## 参考链接

- [Rime 官网](https://rime.im/)
- [Rime Wiki](https://github.com/rime/home/wiki)
- [雾凇拼音（rime-ice）](https://github.com/iDvel/rime-ice)
- [极点五笔86 Rime 方案](https://github.com/KyleBing/rime-wubi86-jidian)
- [开源小鹤 Rime 方案](https://github.com/amorphobia/openfly)
- [自然码官网](http://www.zrm.com.cn/)
- [小狼毫 Weasel](https://github.com/rime/weasel)
