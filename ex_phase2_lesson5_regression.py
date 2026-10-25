# ════════════════════════════════════════════════════════════
#  阶段 2 · 机器学习 ｜ 第 5 课 · 线性回归（回归 + MSE/R²）
#  日期：2026-10-06　配套教材：notes/phase2_lesson5.md
#  状态：⬜ 未开始　规则：code-last
# ════════════════════════════════════════════════════════════
# 主题：LinearRegression / coef·intercept / 二维坑(双层括号) / R² 三档口诀 / tips 数据集
#
# 开场复习（凭记忆，口答）：
#   R1 森林 vs 单棵树：test 分数谁高？train-test 差距谁小？
#   R2 R² 还没学——先猜：R²=0 的模型是什么水平？（学完教材§4 再核对）
#   R3 第 1 天口诀："会不会还款"和"还款金额"分别是什么学习问题？
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

dft = pd.read_csv('data/tips.csv')   # 244 张真实餐馆账单

# ── 任务 1：造 X 和 y——小心那个二维的坑 ─────────────────
# 要做：y = tip 列；X = total_bill 列（注意双层括号！）
# 预测①：为什么必须写 df[['total_bill']] 而不是 df['total_bill']？X.shape = ?
# 你的代码：


# ── 任务 2：切分 + 训练 ───────────────────────────────
# 要做：train_test_split(test_size=0.2, random_state=42) → fit
# 预测②：斜率（coef_）是正还是负？量级大概多少（个位/十分位/百分位）？
# 你的代码：


# ── 任务 3：读懂模型的"心算公式" ────────────────────────
# 要做：print(model.coef_, model.intercept_)
#       然后心算 bill=30 的小费，再用模型预测对比：
#       model.predict(pd.DataFrame({'total_bill': [30]}))
# 预测③：你的心算和模型的输出差多少？（应该完全一致，为什么？）
# 你的代码：


# ── 任务 4：R² 打分 ──────────────────────────────────
# 要做：分别打印 r2_score 在 train 和 test 上的值
# 预测④：R²=0.5 是什么水平？R²=0 呢？（口诀：1/0/负数 三档）
# 你的代码：


# ── 任务 5（加餐）：多特征 ─────────────────────────────
# 要做：X 加上 'size' 列重训，对比 R²
# 预测⑤：R² 升还是降？coef_ 变成几个数？
# 你的代码：


# ══ 标准答案区（你提交预测+代码后由我补上）════════════════

# ══ 对比记录（不标准/错误写法 + 原因 + 改进写法）══════════
