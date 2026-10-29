# 练习索引

> 命名 `phaseN/lessonM_主题.py`，与教材 `notes/phaseN_lessonM.md` **编号严格对应**：看到 `lesson4_` 就去 `notes/phase2_lesson4.md`。
> 阶段 1 的 numpy 初始练习记为 lesson0（阶段内第 1 课从 pandas 起算，与 `PROGRESS.md` 课序一致）。

**运行方式**（`data/` 是相对仓库根目录的路径）：

```powershell
cd 'E:\AIProjetct\Learn AI By AI'
python exercises\phase2\lesson4_random_forest.py
```

---

## 阶段 1：Python 数据分析基础（2026-09-29 ~ 2026-10-01）

| 课序 | 主题 | 练习文件 | 配套教材 | 日期 | 状态 |
|-----|------|---------|---------|------|------|
| 第 0 课 | numpy 基础（数组/索引/切片/条件筛选） | `phase1/lesson0_numpy.py` | —（初始练习） | 09-29 | ✅ |
| 第 1 课 | pandas DataFrame 入门 | `phase1/lesson1_pandas_basics.py` | `notes/phase0.md` | 10-01 | ✅ |
| 第 2 课 | pandas 数据清洗 | `phase1/lesson2_clean.py` | —（详见 PROGRESS 卡点表） | 10-01 | ✅ |
| 第 3 课 | Titanic 真实数据体检 | `phase1/lesson3_titanic_inspect.py` | — | 10-01 | ✅ |
| 第 4 课 | 亲手清洗 Titanic | `phase1/lesson4_titanic_clean.py` | — | 10-01 | ✅ |
| 第 5 课 | 可视化 + groupby | `phase1/lesson5_visualize.py` | — | 10-01 | ✅ |

## 阶段 2：机器学习（2026-10-02 ~ 进行中）

| 课序 | 主题 | 练习文件 | 配套教材 | 日期 | 状态 |
|-----|------|---------|---------|------|------|
| 第 1 课 | 第一个模型（决策树 + train_test_split） | `phase2/lesson1_decision_tree.py` | `notes/phase2_lesson1.md` | 10-02 | ✅ 含对比记录 6 条 |
| 第 2 课 | 模型的成绩单 + 治过拟合 max_depth | `phase2/lesson2_metrics_overfit.py` | `notes/phase2_lesson2.md` | 10-03 | ✅ 验收 10-10 |
| 第 3 课 | 交叉验证 cross_val_score | `phase2/lesson3_crossval.py` | `notes/phase2_lesson3.md` | 10-15 | ✅ 验收 10-20 |
| 第 4 课 | 随机森林（集成学习入门） | `phase2/lesson4_random_forest.py` | `notes/phase2_lesson4.md` | **10-29** | 🔵 进行中 |
| 第 5 课 | 线性回归（回归 + MSE/R²） | `phase2/lesson5_regression.py` | `notes/phase2_lesson5.md` | 10-31 排期 | ⬜ 未开始 |

---

## 使用说明

- **code-last**：标题头注释 → 开场复习 → 任务预测 → 自己写代码 → 运行 → 「标准答案区」→ 文末「对比记录」。
- 数据统一在 `data/`：`titanic.csv`（原始 891 行）/ `titanic_clean.csv`（清洗后）/ `tips.csv`（回归用）。
- 配套教材在 `notes/`，命名 `phaseN_lessonM.md`。
- 进度见 `PROGRESS.md`，路线见 `ROADMAP.md`，课表见 `SCHEDULE.md`。
