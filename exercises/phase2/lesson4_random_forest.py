# ════════════════════════════════════════════════════════════
#  阶段 2 · 机器学习 ｜ 第 4 课 · 随机森林（集成学习入门）
#  日期：2026-10-05 排期 / 2026-10-29 实际做　配套教材：notes/phase2_lesson4.md
#  状态：✅ 已完成（预测 + 代码 + 批改）　规则：code-last
# ════════════════════════════════════════════════════════════
# 主题：RandomForestClassifier / n_estimators / bagging 只治方差 / CV 裁判森林 vs 单树
#
# ╔══════════════════════════════════════════════════════════╗
# ║  预测区（你写下的原文，一字未改）                          ║
# ╚══════════════════════════════════════════════════════════╝
#
# 开场复习（凭记忆，口答）：
#   R1 cross_val_score 返回什么？mean 和 std 各代表什么？ 交叉验证后预测的数组，每个值代表一次考试结果，平均数代表这几次考试的平均水平，std代表标准差 即结果偏离程度以及稳定性
#   R2 混淆矩阵里 FN 是什么含义（用 Titanic 的话说）？ 预测死亡但实际生还的人
#   R3 森林的"集体智慧"靠哪两个随机？（教材§1）train_test_split(random_state),model(random_state)
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
# 预测①：test score 相比单棵树（约 0.75-0.78）升还是降？ 上升
# 预测②：train-test 分数差相比单棵树变大还是变小？说明什么？单棵树小，采用了随机森林算法降低了单个树出现过拟合的情况
# 你的代码：
model_forest = RandomForestClassifier(n_estimators=100, random_state=42)
model_forest.fit(X_train, y_train)
pred_forest =  model_forest.predict(X_test)

model_tree = DecisionTreeClassifier(random_state=42)
model_tree.fit(X_train, y_train)
pred_tree =  model_tree.predict(X_test)

# ── 任务 2：森林的"证词"——特征重要性 ────────────────────
# 要做：print(dict(zip(X.columns, model.feature_importances_)))
#       （再造一棵 max_depth=3 的单树对比它的 importances）
# 预测③：Sex 还是第一吗？森林的排序和单树的排序像不像？应该不是了，在其他树出现其他feature第一的情况，反复对比下来取分数最高的频率的特征，不太理解森林的排序、和单棵树的排序
# 你的代码：
print(dict(zip(X.columns, model_forest.feature_importances_)))
print(f"forest_train_accuracy={model_forest.score(X_train, y_train):.4f}\nforest_test_accuracy={model_forest.score(X_test, y_test):.4f}")

# ── 任务 3：CV 裁判——森林 vs depth=3 单树 ───────────────
# 要做：两个模型各做 cv=5 交叉验证，打印各自的 mean 和 std
# 预测④：谁 mean 高？谁 std 小（更稳）？肯定是森林
# 你的代码：
cross_val_score_forest =  cross_val_score(model_forest, X_train, y_train, cv = 5)
cross_val_score_tree =  cross_val_score(model_tree, X_train, y_train, cv = 5)
print(f"forest_mean={cross_val_score_forest.mean():.4f} forest_std={cross_val_score_forest.std():.4f}")
print(f"tree_mean={cross_val_score_tree.mean():.4f} tree_std={cross_val_score_tree.std():.4f}")

# ── 任务 4：思考题（不写代码）───────────────────────────
# 一棵树过拟合是"背题"，为什么 100 棵树投票就不容易背题了？
# 一句话，用"偏见互相抵消"的思路回答 因为一颗树背题可能恰好考的题目没考到，100棵树背的题覆盖范围更广，考到的几率更大

# ╔══════════════════════════════════════════════════════════╗
# ║  代码批改（先说代码，因为代码决定了预测能不能被检验）      ║
# ╚══════════════════════════════════════════════════════════╝
#
# 【最重要的一条】你的代码**无法检验**你自己的预测②③④。
#   题目要求"分别打印 train score 和 test score"、"再造一棵 max_depth=3 的单树对比"。
#   你都没做：
#     - 单棵树的 train/test 一次都没打印        → ② 的"差变大变小"无从算起
#     - 没有 d3 单树，也没有它的 importances    → ③ 的"像不像"无从比
#     - model_tree 是满树，不是 d3              → ④ 的对手根本不对
#   结果：三条预测全是凭感觉写的，跑完代码也没法知道自己对不对。
#   这不是"答错了"，是"答题和验证脱钩了"——比答错更值得修。
#
# 【最危险的一条】那个 bug 让错的预测看起来是对的。
#   model_tree = DecisionTreeClassifier(random_state=42)   ← 满树，不是 d=3
#   cross_val_score(model_tree, ...) → 0.7557 ± 0.0204
#   森林 → 0.8020 ± 0.0129
#   → 0.8020 > 0.7557 ✅   0.0129 < 0.0204 ✅
#   → 于是"肯定是森林"在你的屏幕上是**被验证通过**的。
#   换成题目要的 d3 树：0.8202 ± 0.0087 → 森林两项全输。
#   ★ 一个 bug 不只是算错，它还能生产"假的确认"。这类 bug 最难发现，
#     因为它不报错、还给好数据。
#
# 【清单】
#   ❌ 1. 任务 1 只打了森林的分，没打单树的分 —— 对照缺失，②无法验证
#   ❌ 2. 任务 2 少做一半：没造 d3 单树、没打它的 importances —— ③无法验证
#   ❌ 3. 任务 3 对手错：model_tree 是满树（max_depth=None），题目要 d=3
#   ⚠️ 4. pred_forest / pred_tree 算完没用 —— 后面用的是 .score()，白算
#   ⚠️ 5. 变量名 cross_val_score_forest 和函数 cross_val_score 只差一个后缀，读起来费劲
#        建议：cv_forest / cv_tree，或 scores_forest / scores_tree
#   ⚠️ 6. 森林那一行 print 里塞了 \n 打两行，后面又单独打 CV 分数 ——
#        同一模型的信息散在三处，核对时要在屏幕上跳来跳去。
#        建议一次打齐：f"{name}: train={tr:.4f} test={te:.4f} cv={cv:.4f}±{sd:.4f}"
#   ✅ 7. f-string 用对了，:.4f 也对了 —— 10-20 的卡点，这次没再犯

# ══ 标准答案区 ════════════════════════════════════════════
# 【任务 1】三个模型一次看全（这才是"对比"该有的样子）
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
#   关键：森林的 train 和满树**一模一样**（0.9789）。
#        它没有减少背题，只是让 100 个背题的人一起投票。
#
# 【任务 2】森林 vs 单树的 importances —— 你问的"像不像"，答案在深度里
#
#   深度扫描（同一个训练集，只改 max_depth）：
#     depth=3     Sex .606  Pclass .210  Age .075  Fare .061   ← Sex 一枝独大
#     depth=5     Sex .536  Pclass .186  Fare .133
#     depth=8     Sex .435  Pclass .161  Fare .167
#     depth=None  Sex .310  Fare .290    Age .194  Pclass .119  ← 摊得最平
#     森林        Fare .305 Sex .271     Age .260  Pclass .078  ← 比满树还平
#
#   ★ 规律：**树越深，Sex 权重越低、Fare 权重越高。**
#     这正是你说"不太理解"的地方 —— 不是森林排序变了，是**深度**在改排序。
#     森林默认 max_depth=None，100 棵树实际深度 15~25（平均 18.2，满树是 23），
#     所以森林长得**像满树**，完全不像 d3 树。
#     你把"森林 vs 满树"当成一回事（任务 2 该这么比），
#     又把"森林 vs 满树"当成了"森林 vs d3"（任务 3 不该这么比）——
#     同一个混淆，一次帮了你、一次害了你。
#
#   机制：feature_importances_ = 100 棵树各自 importance 的**算术平均**。
#        不是"数谁当第一的次数"。
#        （附：你的数次数法在 8 个种子里 7 个给出相同前三，只有 seed=7 分家：
#          数次数 → Sex>Fare>Age，算术平均 → Fare>Sex>Age。
#          所以这个错法"通常看起来能用"，但拿不到数值——后三名 Pclass/SibSp/Parch
#          数次数法全是 0，分不出来。）
#
# 【任务 3】CV 必须拿 d3 树当对手
#     forest     mean=0.8020  std=0.0129
#     d3单树      mean=0.8202  std=0.0087    ← 两项都赢森林
#     满树         mean=0.7557  std=0.0204    ← 你实际比的是这个
#
#   正确写法：
#     tree_d3 = DecisionTreeClassifier(max_depth=3, random_state=42)
#     s = cross_val_score(tree_d3, X_train, y_train, cv=5)
#     print(f"d3_mean={s.mean():.4f} d3_std={s.std():.4f}")
#
# 【任务 4】正解：不是"覆盖更广"，是"错得不一样"
#   100 棵树各自 bootstrap 抽 712 个样本（有放回，约 63.2% 不重复）、
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
#    写：单棵树小，森林降低了单个树出现过拟合的情况
#    原因：没说是哪棵单树。跟满树比（22.5→18.0）确实变小；
#          但 d3 树只有 3.5pp，比森林还小。
#          更关键：森林 train=0.9789 与满树**完全一样**，它一点没少背题。
#    改：森林不治"背题"，治"背错了没有别人纠正"。train 分数不该期待它下降。
#
# 3) 预测③结论对、机制错：以为森林是"投票选第一"
#    写：反复对比下来取分数最高的频率的特征
#    原因：没有"投票选第一"这一步。feature_importances_ 是 100 棵树
#          各自数值的**算术平均**。
#    改：imp = 100 棵树的 importance 求平均，不是数谁当第一的次数。
#        （唯一真正投票的是 predict()；predict_proba 和 feature_importances_ 都是平均）
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
#    原因：题目要的是"森林 vs depth=3 单树"，拿满树比等于打了一个更弱的对手，
#          而且这个小便宜刚好让 ④ 看起来是对的。
#    改：比较前先 print(模型.get_params()['max_depth']) 确认对手是谁。
#
# 6) `pred_forest` / `pred_tree` 算了但没用
#    写：pred_forest = model_forest.predict(X_test)
#    原因：没报错，但白算——后面用的是 .score()，不是预测数组。
#    改：要么删掉，要么真的用它算混淆矩阵（第 2 课学过）。
#        "跑了但没输出"的代码是隐形负债。
#
# 7) 三条预测都没留下可检验的依据
#    写：②③④ 全靠直觉
#    原因：代码里没有产生验证它们所需的数字（单树分数、d3 的 importances、d3 的 CV）。
#    改：**先想"要验证这句话需要哪个数"，再写代码去打那个数。**
#        这一步做对了，预测对错都有收获；做错了，跑完一万行也不知道自己对不对。
