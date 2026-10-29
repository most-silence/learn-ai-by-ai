# ════════════════════════════════════════════════════════════
#  阶段 2 · 机器学习 ｜ 第 4 课 · 随机森林（集成学习入门）
#  日期：2026-10-29　配套教材：notes/phase2_lesson4.md
#  状态：✅ 完成（预测 4 条 + 代码全跑通，验收 2026-10-29）　规则：code-last
# ════════════════════════════════════════════════════════════
# 主题：RandomForestClassifier / n_estimators / bagging 只治方差 / CV 裁判森林 vs 单树
#
# 开场复习（凭记忆，口答）：
#   R1 cross_val_score 返回什么？mean 和 std 各代表什么？ 交叉验证后预测的数组，每个值代表一次考试结果，平均数代表这几次考试的平均水平，std代表标准差 即结果偏离程度以及稳定性   → ✅ 对
#   R2 混淆矩阵里 FN 是什么含义（用 Titanic 的话说）？ 预测死亡但实际生还的人   → ✅ 对（且"漏掉的生还人"因果也说对了）
#   R3 森林的"集体智慧"靠哪两个随机？（教材§1）train_test_split(random_state),model(random_state)   → ❌ 错，见对比记录 1
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
# 预测①：test score 相比单棵树（约 0.75-0.78）升还是降？ 上升   → ⚠️ 碰对（理由没写）
# 预测②：train-test 分数差相比单棵树变大还是变小？说明什么？单棵树小，采用了随机森林算法降低了单个树出现过拟合的情况   → ⚠️ 半对（比错了对象）
model_forest = RandomForestClassifier(n_estimators=100, random_state=42)
model_forest.fit(X_train, y_train)
pred_forest = model_forest.predict(X_test)

model_tree = DecisionTreeClassifier(random_state=42)
model_tree.fit(X_train, y_train)
pred_tree = model_tree.predict(X_test)

# ── 任务 2：森林的"证词"——特征重要性 ────────────────────
# 预测③：Sex 还是第一吗？森林的排序和单树的排序像不像？应该不是了，在其他树出现其他feature第一的情况，反复对比下来取分数最高的频率的特征   → ✅ 结论对 / ❌ 机制错，见对比记录 3
print(dict(zip(X.columns, model_forest.feature_importances_)))
print(f"forest_train_accuracy={model_forest.score(X_train, y_train):.4f}\nforest_test_accuracy={model_forest.score(X_test, y_test):.4f}")

# ── 任务 3：CV 裁判——森林 vs depth=3 单树 ───────────────
# 预测④：谁 mean 高？谁 std 小（更稳）？肯定是森林   → ❌ 错，方向反了
cross_val_score_forest = cross_val_score(model_forest, X_train, y_train, cv=5)
cross_val_score_tree = cross_val_score(model_tree, X_train, y_train, cv=5)
print(f"forest_mean={cross_val_score_forest.mean():.4f} forest_std={cross_val_score_forest.std():.4f}")
print(f"tree_mean={cross_val_score_tree.mean():.4f} tree_std={cross_val_score_tree.std():.4f}")

# ── 任务 4：思考题（不写代码）───────────────────────────
# 一棵树过拟合是"背题"，为什么 100 棵树投票就不容易背题了？
# 原答：因为一颗树背题可能恰好考的题目没考到，100棵树背的题覆盖范围更广，考到的几率更大   → ❌ "覆盖更广"不是抵消机制

# ══ 标准答案区 ════════════════════════════════════════════
# 【任务 1】三行对照，一次看全
#   for 名字, 模型 in [("满树", DecisionTreeClassifier(random_state=42)),
#                      ("d3树", DecisionTreeClassifier(max_depth=3, random_state=42)),
#                      ("森林", RandomForestClassifier(n_estimators=100, random_state=42))]:
#       m = 模型.fit(X_train, y_train)
#       print(f"{名字} train={m.score(X_train,y_train):.4f} "
#             f"test={m.score(X_test,y_test):.4f}")
#
#   实测：
#     满树   train=0.9789  test=0.7542   差距 22.5pp
#     d3树   train=0.8343  test=0.7989   差距  3.5pp
#     森林   train=0.9789  test=0.7989   差距 18.0pp
#
#   关键：森林的 train 和满树**一模一样**（0.9789）。它没有减少背题，
#        只是让 100 个背题的人一起投票。
#
# 【任务 2】森林 vs 单树的 importance
#   森林 : Fare .305  Sex .271  Age .260  Pclass .078  SibSp .050  Parch .037
#   d3树 : Sex  .606  Pclass .210  Age .075  Fare .061  SibSp .048  Parch .000
#
#   机制：forest.feature_importances_ = 100 棵树各自 importance 的**平均值**，
#        不是"看谁当第一的次数多"。没有投票选第一这一步。
#
#   为什么排序差别这么大：单棵树的观点很偏（Sex 一枝独大 60.6%），
#   100 棵平均之后偏见被摊平 → Fare/Sex/Age 三分天下（30/27/26）。
#   Fare 从小配角升到第一，说明票价里确实有信息，只是单树没看见。
#   （注意：Fare 与 Pclass 高度相关，本质可能还是阶级。importance 告诉你
#    "模型用了谁"，不告诉你"谁在真实世界重要"。）
#
# 【任务 3】CV 必须拿 d3 树当对手，不能拿满树
#   本题问的是"森林 vs depth=3 单树"，代码里用的是 model_tree（满树），比错了对象：
#
#     forest     mean=0.8020  std=0.0129
#     d3单树      mean=0.8202  std=0.0087    ← 两项都赢森林
#     满树         mean=0.7557  std=0.0204
#
#   正确写法：
#     tree_d3 = DecisionTreeClassifier(max_depth=3, random_state=42)
#     s = cross_val_score(tree_d3, X_train, y_train, cv=5)
#     print(f"d3_mean={s.mean():.4f} d3_std={s.std():.4f}")
#
# 【任务 4】正解：不是"覆盖更广"，是"错得不一样"
#   100 棵树各自用 bootstrap 抽 712 个样本（有放回，约 63.2% 不重复）、
#   每次分叉只看随机 2 个特征（max_features='sqrt'，6 个特征时）。
#   → 它们在不同的人身上犯错。
#   → 投票时 A 树在甲身上错、B 树在乙身上错，互相救回来。
#
#   证据：100 棵树单挑平均 0.7672（最差 0.6872），投票后 0.7989，+3.2pp。
#        这 3.2pp 就是"错误互相抵消"的收益。
#
#   一句话：不是 100 棵树"见得多"，而是 100 棵树"错得不一样"；
#          投票时各家的错误互相抵消，剩下的共识才是真规律。
#
# 【加餐·任务 5】森林限深才追上单树（本课最重要的一节）
#   from sklearn.model_selection import RepeatedStratifiedKFold
#   cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=10, random_state=0)
#   for md in [None, 8, 5, 3]:
#       s = cross_val_score(DecisionTreeClassifier(max_depth=md, random_state=42), X_train, y_train, cv=cv)
#       f = cross_val_score(RandomForestClassifier(n_estimators=100, max_depth=md, random_state=42), X_train, y_train, cv=cv)
#       print(f"depth={str(md):4s} 单树={s.mean():.4f} 森林={f.mean():.4f} 增益={100*(f.mean()-s.mean()):+.2f}pp")
#
#   实测：
#     depth=None  单树 0.7656  森林 0.8017  +3.61pp
#     depth=8     单树 0.8007  森林 0.8267  +2.60pp
#     depth=5     单树 0.8096  森林 0.8260  +1.64pp
#     depth=3     单树 0.8277  森林 0.8063  -2.14pp   ← 翻负
#
#   机制：bagging 只治**方差**。满树方差大（20 个种子极差 2.23pp）→ 有东西可削；
#        d=3 树方差**恰好为 0**（20 个种子极差 0.0000）→ 没东西可削，
#        却还要付"每棵树只看 63.2% 数据"的代价 → 净亏。
#   详细推导见 teach/lessons/0001-bagging-only-fixes-variance.html

# ══ 对比记录（不标准/错误写法 + 原因 + 改进写法）══════════
# 1) R3 把"随机性的开关"当成了"随机性的来源"
#    写：train_test_split(random_state), model(random_state)
#    原因：random_state 是控制随机怎么抽的**参数**，不是随机本身。
#          森林的两个随机是【数据随机 bootstrap】+【特征随机 max_features】。
#    改：森林的集体智慧 = 每棵树看不同的样本 + 每次分叉看不同的特征。
#        random_state 只决定这两处怎么抽。
#
# 2) 预测②"单棵树小"——比错了参照物
#    写：单棵树小，森林降低了过拟合
#    原因：没说是哪棵单树。跟满树比（22.5→18.0）确实变小；
#          但 d3 树只有 3.5pp，比森林还小。
#          更关键：森林 train=0.9789 与满树**完全一样**，它一点没少背题。
#    改：森林不治"背题"，治"背错了没有别人纠正"。train 分数不该期待它下降。
#
# 3) 预测③机制错：以为森林是"投票选第一"
#    写：反复对比下来取分数最高的频率的特征
#    原因：没有"投票选第一"这一步。feature_importances_ 是 100 棵树
#          各自数值的**算术平均**。
#    改：imp = 100 棵树的 importance 求平均，不是数谁当第一的次数。
#
# 4) 预测④"肯定是森林"被数据推翻——本课最重要的一条
#    写：肯定是森林
#    实测：森林 0.8020±0.0129  vs  d3 单树 0.8202±0.0087（两项都输）
#    原因：Titanic 只有 712 行训练数据，满树森林的每棵树都在重度过拟合
#          （单棵 test 平均仅 0.7672），投票只能救到 0.7989，
#          刚好是一棵正经正则化 d3 树的水平。
#    改：小数据上"一棵限深的树"常常打平甚至赢过 100 棵满树。
#        别默认森林更强，跑 CV 再说。
#
# 5) 任务 3 的对手选错（满树 vs d3 树）
#    写：cross_val_score(model_tree, ...)  // model_tree 是满树
#    原因：题目要的是"森林 vs depth=3 单树"，拿满树比等于打了一个更弱的对手。
#    改：比较前先确认 `模型.get_params()['max_depth']` 是不是你要的那个值。
#
# 6) `pred_forest` / `pred_tree` 算了但没用
#    写：pred_forest = model_forest.predict(X_test)
#    原因：没报错，但白算——后面用的是 .score()，不是预测数组。
#    改：要么删掉，要么真的用它算混淆矩阵（第 2 课学过）。
#        "跑了但没输出"的代码是隐形负债。
