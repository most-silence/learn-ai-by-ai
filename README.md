# Learn AI By AI

以动手做项目为主，边学 AI 边用 AI 记录进度、评估掌握度、迭代学习路线。

> 目标：从 Python 熟练 → 机器学习 → 深度学习 → NLP → 大模型 → **AI Agent**
> 节奏：工作日 1 小时 × 5 + 周末 3 小时 × 2 = **11 小时/周**
> 当前：阶段 2（机器学习）第 4 课 · 随机森林

---

## 先看这四个文件

| 文件 | 什么时候看 |
|---|---|
| [SCHEDULE.md](SCHEDULE.md) | **每天开始前**：今天该学什么、做多久 |
| [PROGRESS.md](PROGRESS.md) | 学完一课后：登记一行；周末看周回顾与卡点表 |
| [ROADMAP.md](ROADMAP.md) | 月初 / 阶段切换时：整体进度与里程碑日期 |
| [notes/cheatsheet.md](notes/cheatsheet.md) | 复习时先默写，再对照 |

---

## 目录结构

```
Learn AI By AI/
├── README.md           # 本文件
├── AGENTS.md           # 仓库约定（核心原则 / 命名 / 目录规范）
├── ROADMAP.md          # 路线图：阶段、里程碑日期、状态
├── PROGRESS.md         # 进度：掌握度表、周回顾、卡点表
├── SCHEDULE.md         # 逐日课表：11 小时/周 + 补课规则
│
├── data/               # 数据集
│   ├── titanic.csv         # 原始 891 行
│   ├── titanic_clean.csv   # 清洗后
│   └── tips.csv            # 回归练习用
│
├── notes/              # 教材与笔记
│   ├── cheatsheet.md       # 口诀卡（所有要背的结论）
│   ├── phase0.md
│   ├── phase2_lesson1.md … phase2_lesson5.md
│   ├── demos/              # 可复现的教学演示脚本（不是练习）
│   └── reviews/            # 按日期归档的复习题
│
├── exercises/          # 练习（code-last：不预置答案）
│   ├── README.md           # 练习索引：哪个练习配哪份教材
│   ├── phase1/             # lesson0_numpy.py … lesson5_visualize.py
│   └── phase2/             # lesson1_decision_tree.py … lesson5_regression.py
│
├── projects/           # 阶段项目（phase1_graduation.py …）
│
├── docs/               # 仓库配置
│   └── agents/             #   issue tracker / triage labels / domain docs
│
└── teach/              # 教学型课程工作区
    ├── MISSION.md          #   为什么学、成功什么样、什么不做
    ├── NOTES.md            #   教学偏好 + 反复出错点
    ├── RESOURCES.md        #   高信任来源清单
    ├── lessons/            #   HTML 课程（可打印）
    ├── reference/          #   HTML 速查卡
    ├── assets/             #   course.css / quiz.js 共享组件
    └── learning-records/   #   决策级学习记录
```

**命名一一对应**：`exercises/phase2/lesson4_random_forest.py` ↔ `notes/phase2_lesson4.md`。

---

## 怎么运行练习

从**仓库根目录**运行（`data/` 是相对根目录的路径）：

```powershell
cd 'E:\AIProjetct\Learn AI By AI'
python exercises\phase2\lesson4_random_forest.py
```

---

## 使用方法

### 每天（1 小时）

1. **开场复习 10 分钟**：看 [SCHEDULE.md](SCHEDULE.md) 今天栏，口答 D1/D3/D7 三档各 1 题，**不翻笔记**。
2. **写预测 5 分钟**：打开今天的练习文件，只填预测区，**先不写代码**。
3. **主体 35 分钟**：写代码 → 运行。卡 5 分钟要脚手架，卡 15 分钟记卡点先过。
4. **收尾 10 分钟**：验收 + [PROGRESS.md](PROGRESS.md) 加一行 + 卡点表补一行。

### 周末（3 小时）

- 卡点总复查 20 分钟（两个不同日子答对才退休）
- 大块推进 / 项目 2 小时
- 周回顾 + 排下周 40 分钟（只周日）

### 没时间时

只做 10 分钟开场复习也算打卡，当天课程顺延到周末，记"最小日"。**保持连续比补进度重要。**

---

## 每课的三条硬规则

1. **code-last**：练习文件只含任务说明 + 预测区 + 空代码区。先写预测、再写代码，提交后才补标准答案与对比记录。
2. **预测分两类**：可推导预测（必做，检验理解）；校准预测（选做，可凭直觉猜，没把握可标"弃权"）。
3. **卡点两日退休**：同一卡点需在**两个不同日子**各答对一次才算固化。

---

## 掌握度评分（自评）

| 分值 | 含义 |
|------|------|
| ★1 | 听说过 |
| ★2 | 看得懂资料 |
| ★3 | 能照着做 |
| ★4 | 能独立完成小项目 |
| ★5 | 能教别人 / 解决新问题 |

---

## 协作方式

在这个目录打开 Claude / DSH，直接说：

- 「继续学习」→ 按 SCHEDULE 推进今天的课
- 「更新进度」→ 登记到 PROGRESS
- 「回顾这周」→ 填周回顾、判定卡点退休
- 「下一步学什么」→ 读 ROADMAP 给建议
