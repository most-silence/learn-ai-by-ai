# 练习索引（EXERCISES_INDEX）

> 练习文件统一命名 `ex_phase{阶段}_lesson{课序}_{主题}.py`，与教材 `notes/phaseN_lessonM.md` 直接对应：看到 `ex_phase2_lesson3_crossval.py` 就知道配 `notes/phase2_lesson3.md`。阶段 1 的 numpy 初始练习记为 lesson0（阶段内第 1 课从 pandas 起算，与 PROGRESS.md 课序一致）。

## 阶段 1：Python 数据分析基础（2026-09-29 ~ 2026-10-01）

| 课序 | 主题 | 练习文件 | 配套教材 | 日期 | 状态 |
|-----|------|---------|---------|------|------|
| 第 0 课 | numpy 基础（数组/索引/切片/条件筛选） | `ex_phase1_lesson0_numpy.py` | —（初始练习） | 09-29 | ✅ 完成 |
| 第 1 课 | pandas DataFrame 入门 | `ex_phase1_lesson1_pandas_basics.py` | `notes/phase0.md` | 10-01 | ✅ 完成 |
| 第 2 课 | pandas 数据清洗 | `ex_phase1_lesson2_clean.py` | —（详见 PROGRESS 卡点表） | 10-01 | ✅ 完成 |
| 第 3 课 | Titanic 真实数据体检 | `ex_phase1_lesson3_titanic_inspect.py` | — | 10-01 | ✅ 完成 |
| 第 4 课 | 亲手清洗 Titanic | `ex_phase1_lesson4_titanic_clean.py` | — | 10-01 | ✅ 完成 |
| 第 5 课 | 可视化 + groupby | `ex_phase1_lesson5_visualize.py` | — | 10-01 | ✅ 完成 |

## 阶段 2：机器学习（2026-10-02 ~ 进行中）

| 课序 | 主题 | 练习文件 | 配套教材 | 日期 | 状态 |
|-----|------|---------|---------|------|------|
| 第 1 课 | 第一个模型（决策树 + train_test_split） | `ex_phase2_lesson1_decision_tree.py` | `notes/phase2_lesson1.md` | 10-02 | ✅ 完成（含对比记录 6 条） |
| 第 2 课 | 模型的成绩单 + 治过拟合 max_depth | `ex_phase2_lesson2_metrics_overfit.py` | `notes/phase2_lesson2.md` | 10-03 | ✅ 完成（标准答案+对比记录 2026-10-10） |
| 第 3 课 | 交叉验证 cross_val_score（周日轻课） | `ex_phase2_lesson3_crossval.py` | `notes/phase2_lesson3.md` | 10-04 排期 → 实际 10-15 做 / 10-20 验收 | ✅ 完成（标准答案+对比记录 2026-10-20） |
| 第 4 课 | 随机森林（集成学习入门） | `ex_phase2_lesson4_random_forest.py` | `notes/phase2_lesson4.md` | 10-05 排期 → 顺延 10-20 | 🔵 进行中 |
| 第 5 课 | 线性回归（回归 + MSE/R²） | `ex_phase2_lesson5_regression.py` | `notes/phase2_lesson5.md` | 10-06 | ⬜ 未开始 |

---

## 使用说明

- 每课练习按 **code-last 规则**：标题头注释（阶段/课/日期）→ 开场复习 → 任务预测 → 自己写代码 → 运行 → 「标准答案区」→ 文末「对比记录」。
- 数据文件统一在 `data/`（titanic.csv / titanic_clean.csv / tips.csv）。
- 配套教材在 `notes/`，命名 `phaseN_lessonM.md`，与练习一一对应。
- 进度详见 `PROGRESS.md`，路线见 `ROADMAP.md`。
