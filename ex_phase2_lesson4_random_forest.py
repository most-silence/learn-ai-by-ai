# ════════════════════════════════════════════════════════════
#  阶段 2 · 机器学习 ｜ 第 4 课 · 随机森林（集成学习入门）
#  日期：2026-10-05　配套教材：notes/phase2_lesson4.md
#  状态：⬜ 未开始　规则：code-last
# ════════════════════════════════════════════════════════════
# 主题：RandomForestClassifier / n_estimators / 偏见互相抵消 / CV 裁判森林 vs 单树
#
# 开场复习（凭记忆，口答）：
#   R1 cross_val_score 返回什么？mean 和 std 各代表什么？
#   R2 混淆矩阵里 FN 是什么含义（用 Titanic 的话说）？
#   R3 森林的"集体智慧"靠哪两个随机？（教材§1）
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# ── 准备代码（同前三天）────────────────────────────────
df = pd.read_csv('data/titanic_clean.csv')
df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
X = df.drop(columns=['Survived', 'PassengerId', 'Name', 'Ticket', 'Embarked'])
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# ── 任务 1：训练森林，和单棵树对比 ────────────────────────
# 要做：RandomForestClassifier(n_estimators=100, random_state=42)
#       → fit → 分别打印 train score 和 test score
# 预测①：test score 相比单棵树（约 0.75-0.78）升还是降？
# 预测②：train-test 分数差相比单棵树变大还是变小？说明什么？
# 你的代码：


# ── 任务 2：森林的"证词"——特征重要性 ────────────────────
# 要做：print(dict(zip(X.columns, model.feature_importances_)))
#       （再造一棵 max_depth=3 的单树对比它的 importances）
# 预测③：Sex 还是第一吗？森林的排序和单树的排序像不像？
# 你的代码：


# ── 任务 3：CV 裁判——森林 vs depth=3 单树 ───────────────
# 要做：两个模型各做 cv=5 交叉验证，打印各自的 mean 和 std
# 预测④：谁 mean 高？谁 std 小（更稳）？
# 你的代码：


# ── 任务 4：思考题（不写代码）───────────────────────────
# 一棵树过拟合是"背题"，为什么 100 棵树投票就不容易背题了？
# 一句话，用"偏见互相抵消"的思路回答


# ══ 标准答案区（你提交预测+代码后由我补上）════════════════

# ══ 对比记录（不标准/错误写法 + 原因 + 改进写法）══════════
