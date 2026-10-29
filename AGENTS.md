# 学习仓库约定（AGENTS.md）

个人 AI 学习仓库。所有文档与笔记用中文写。

## 核心原则（改任何文件前先读这一节）

### 1. 输入 → 产出 → 反馈，一个闭环

每学一课必须留下**三样东西**，缺一样这节课不算完成：

| 要素 | 落在哪 |
|---|---|
| 我的**预测**（学之前押的注） | 练习文件顶部「预测区」 |
| 我的**代码/答案**（自己写的） | 练习文件「代码区」 |
| **对比与纠正**（错在哪、为什么） | 练习文件末尾「对比记录」+ `PROGRESS.md` 卡点表 |

### 2. code-last：练习文件里永远不预置答案

练习文件开始时只有：任务说明 + 预测区（留空）+ 代码区（留空）。
学生提交后，才补「标准答案区」和「对比记录」。
**预测写了才算开始**；没有预测直接写代码 = 绕过了这节课真正考的东西。

### 3. 预测分两类

- **可推导预测**（必做）：从工具语义必然推出的结果。例："5 折 CV 每份数据当几次考卷"。
- **校准预测**（选做，可标"弃权"）：未知数字凭直觉猜。例："森林 test 会涨到多少"。

### 4. 卡点必须两个不同日子各答对一次才退休

同一卡点只答对一次不算固化。`PROGRESS.md` 卡点表每行都记着"待几号复查"。
**答对过的题隔 3 天要重问机制，不能只问结论**（10-20 答对、10-29 退回的教训）。

### 5. 结论必须有真实运行数据

不接受"一般来说"。任何"X 比 Y 好"的说法，都要附一段在本机跑出来的代码输出。
Titanic 上森林输给单棵限深树，就是靠这个原则抓出来的。

### 6. 一课不占超过 2 个学习日

第 3 天还没通过就降级为"★3 能照着做"，往下走，记入待补清单。防止一课卡死整条线。

### 7. 节奏：工作日 1 小时 × 5 + 周末 3 小时 × 2

逐日课表见 [`SCHEDULE.md`](SCHEDULE.md)。每天开场 10 分钟做间隔重复（D1/D3/D7 三档）。

---

## 目录结构

```
Learn AI By AI/
├── README.md           # 怎么用这个仓库（新手从这里开始）
├── AGENTS.md           # 本文件：仓库约定
├── ROADMAP.md          # 路线图（阶段 / 里程碑日期 / 状态）
├── PROGRESS.md         # 进度（掌握度表 / 周回顾 / 卡点表）
├── SCHEDULE.md         # 逐日课表（11 小时/周，含补课规则）
├── data/               # 数据集（titanic.csv / titanic_clean.csv / tips.csv）
├── notes/              # 教材（phaseN_lessonM.md）
│   ├── cheatsheet.md   #   口诀卡：所有要背的结论压缩在这里
│   ├── demos/          #   教学演示脚本（可复现实验，不是练习）
│   └── reviews/        #   按日期归档的复习题（YYYY-MM-DD.md）
├── exercises/          # 练习（code-last）
│   ├── README.md       #   练习索引：哪个练习配哪份教材
│   ├── phase1/         #   lesson0_numpy.py … lesson5_visualize.py
│   └── phase2/         #   lesson1_decision_tree.py … lesson5_regression.py
├── projects/           # 阶段项目
├── docs/               # 仓库配置（agent 协作规则、issue tracker 等）
└── teach/              # 教学型课程工作区（HTML 课程 + 速查卡 + 学习记录）
    ├── MISSION.md      #   为什么学、成功什么样、什么不做
    ├── NOTES.md        #   教学偏好 + 反复出错点
    ├── RESOURCES.md    #   高信任来源清单
    ├── lessons/        #   自包含 HTML 课程
    ├── reference/      #   速查卡（HTML，可打印）
    ├── assets/         #   共享样式与组件（course.css / quiz.js）
    └── learning-records/  # 学习记录（决策级洞察，不是流水账）
```

### 文件放哪的判断标准

| 类型 | 去哪 | 例子 |
|---|---|---|
| 每天要看的 | 仓库根 | `PROGRESS.md` `SCHEDULE.md` `ROADMAP.md` |
| 学到的东西 | `notes/` | 教材、口诀卡 |
| 要动手做的 | `exercises/` | 练习文件 |
| 要跑但不用改的 | `notes/demos/` | 教学演示脚本 |
| 阶段成果 | `projects/` | 毕业项目 |
| 讲给人听的 | `teach/lessons/` | HTML 课程 |
| 仓库约定 | `docs/` | agent 规则 |

---

## 命名约定

| 东西 | 规则 | 例 |
|---|---|---|
| 练习 | `exercises/phaseN/lessonM_主题.py` | `exercises/phase2/lesson4_random_forest.py` |
| 教材 | `notes/phaseN_lessonM.md` | `notes/phase2_lesson4.md` |
| 复习 | `notes/reviews/YYYY-MM-DD.md` | `notes/reviews/2026-10-02.md` |
| 课程 | `teach/lessons/NNNN-dash-case.html` | `teach/lessons/0001-bagging-only-fixes-variance.html` |
| 学习记录 | `teach/learning-records/NNNN-dash-case.md` | `0001-bagging-only-fixes-variance.md` |

练习与教材**编号严格对应**：看到 `lesson4_` 就找 `phase2_lesson4.md`。

---

## 运行练习

**从仓库根目录运行**（`data/` 是相对根目录的）：

```powershell
cd 'E:\AIProjetct\Learn AI By AI'
python exercises\phase2\lesson4_random_forest.py
```

在 `exercises/phase2/` 里直接跑会报 `FileNotFoundError` —— 这是预期行为，不是 bug。

---

## 每次学习会话的固定流程

1. **开场复习**（10 分钟）：D1/D3/D7 三档各 1 题，口答，不翻文件
2. **写预测**（5 分钟）：只填预测区，不写代码
3. **主体**（35 分钟）：写代码 → 运行 → 卡 5 分钟要脚手架，卡 15 分钟记卡点先过
4. **收尾**（10 分钟）：验收 + `PROGRESS.md` 加一行 + 卡点表更新
5. 周末额外做：卡点总复查（20 分钟）+ 周回顾（30 分钟）

---

## Agent skills

### Issue tracker

Issues and specs live as GitHub issues in `most-silence/learn-ai-by-ai`, operated with the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

Five canonical triage roles, spelled exactly as the role names (`needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`). See `docs/agents/triage-labels.md`.

### Domain docs

single-context — one `GLOSSARY.md` at the repo root, architecture decisions in `docs/adr/`. See `docs/agents/domain.md`.
