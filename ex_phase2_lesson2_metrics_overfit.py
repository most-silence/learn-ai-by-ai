# ════════════════════════════════════════════════════════════
#  阶段 2 · 机器学习 ｜ 第 2 课 · 模型的成绩单 + 治过拟合第一刀
#  日期：2026-10-03　配套教材：notes/phase2_lesson2.md
#  状态：✅ 完成（标准答案 + 对比记录补于 2026-10-10）　规则：code-last
# ════════════════════════════════════════════════════════════
# 主题：基线 / 混淆矩阵(TN/FP/FN/TP) / 精确率·召回率 / max_depth 治过拟合
#
# 开场复习（凭记忆，口答）：
#   R1 一列整数全是 85.0 结尾 → 这列发生过什么？（通用版，10-03 到期复查）
#   R2 bar / hist 的精确口诀（x 轴分别画什么）？
#   R3 裸 groupby（不接聚合）得到什么？print 长什么样？
#   R4 昨天预习思考：train 95% / test 70% 是好消息还是坏消息？
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score

# ── 准备代码（昨天你已独立写过，直接复用）────────────────
df = pd.read_csv('data/titanic_clean.csv')
df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
X = df.drop(columns=['Survived', 'PassengerId', 'Name', 'Ticket', 'Embarked'])
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
pred = model.predict(X_test)
print('accuracy:', model.score(X_test, y_test))

# ── 任务 1：基线——先问"无脑模型"能考多少分 ──────────────
# 要做：算"全判遇难"（pred 全 0）在测试集上的正确率
# 预测①：≈ ? （提示：61.7% 是全量死亡率，179 人的测试集里比例略有浮动）
# 判断：你的树比基线高出多少个百分点？赢了基线才叫"有本事"
# 你的代码：
# print((179-sum[pred])/179) # 统计 y_test 为0的个数占179的比例，即为无脑模型，除非无脑模型还按比例划分了，这个就得单独验证每行数据pred的正确性
baseline = (y_test == 0).mean()  
# ── 任务 2：混淆矩阵——把对错拆成四格 ────────────────────
# 要做：print(confusion_matrix(y_test, pred))
# 预测②：2×2 矩阵四个格的含义（哪个是 TP/FP/FN/TN？行列各代表什么？）
# 你的代码：
print(confusion_matrix(y_test, pred))

# ── 任务 3：精确率 & 召回率 ─────────────────────────────
# 要做：print(precision_score(y_test, pred)) 和 print(recall_score(y_test, pred))
# 预测③：用 Titanic 的话各说一遍这两个数的语义
# 判断：你是救生艇指挥官（怕漏掉活人），更该优化哪个指标？
# 你的代码：
print(precision_score(y_test, pred))
print(recall_score(y_test, pred))

# ── 任务 4：治过拟合第一刀 max_depth ─────────────────────
# 要做：再造两棵树——depth=3 和 depth=None，各自打印 train 和 test 的 score
# 预测④：depth=3 相比默认（None）：train score 升/降？test score 升/降？为什么？
# 你的代码：
model_depth3 = DecisionTreeClassifier(random_state=42, max_depth=3).fit(X_train, y_train)
pred_depth3 = model_depth3.predict(X_test)
print('train_score', model_depth3.score(X_train, y_train)) # 不太了解打分规则是什么
print('test_score', model_depth3.score(X_test, y_test))


# ── 任务 5（加餐）：depth 扫描，看倒 U ───────────────────
# 要做：for d in range(1, 11)——每个深度造模型、打印 d 和 test score
# 预测⑤：曲线什么形状？最高点大概在哪个深度？
# 你的代码：
for d in range(1, 11):
    model_d = DecisionTreeClassifier(random_state=42, max_depth=d).fit(X_train, y_train)
    pred_d = model_d.predict(X_test)
    print('test_score', model_d.score(X_test, y_test))


# ══ 标准答案区（2026-10-10 补，所有数字均为真实运行结果）═══════════════
# 【数据底账】测试集 179 人 = 实际遇难 105（58.7%）+ 实际生还 74
#
# 任务 1 正解：baseline = (y_test == 0).mean()          # → 0.5866（105/179）
#   模型 0.7542 − 基线 0.5866 = +16.8 个百分点 → 这棵树真有本事
#   巧的是：(pred == 0).mean() 今天也 = 0.5866，但那是"模型预测成遇难的比例"
#   （输出分布），跟基线（实际分布）是两回事；今天恰好相等（模型判死的
#   恰好也是 105 人 = 83+22），纯属巧合，概念不能混
# 任务 2 正解：print(confusion_matrix(y_test, pred))    # → [[83 22]
#                                                       #     [22 52]]
#   行 = 实际（上排实际遇难 105、下排实际生还 74），列 = 预测（左列判死、右列判活）
#   TN=83 判死✓　FP=22 判活✗（其实死了）　FN=22 判死✗（其实活着）　TP=52 判活✓
#   对角线 (83+52)/179 = 0.7542 = accuracy → 混淆矩阵就是"把 accuracy 拆成四格"
# 任务 3 正解：precision = 52/(52+22) = 0.7027；recall = 52/(52+22) = 0.7027
#   这次 FP = FN = 22 → 两个指标碰巧相等（不是普遍规律！）
#   precision：模型判活的 74 人里真活了几人 → "判活名单的可信度"
#   recall：实际活着的 74 人里模型找到几人 → "救生艇指挥官的救回率"
#   判断：怕漏掉活人 → 优化 recall（22 个 FN 是"其实活着却被判死"）
# 任务 4 正解：.score() = 分类器时就是 accuracy（在该批数据上 (pred==y真) 的均值）；
#   回归器时返回 R²——同名方法不同默认，阶段 2 第 5 课回归会再撞见它
#   默认 None：train 0.9789 / test 0.7542 → 差距 22.5 个百分点（背题）
#   depth=3   ：train 0.8343 / test 0.7989 → 差距  3.5 个百分点（理解题）
#   → 砍深度 = train↓ 而 test↑，预测④方向完全正确——这就是治过拟合
# 任务 5 正解：depth 扫描实测（每个深度都真跑了）：
#   d      1      2      3      4      5*     6      7      8      9      10
#   test  .7821 .7654 .7989 .7989 .8045 .7877 .7542 .7933 .7654 .7877
#   峰值 d=5（0.8045）。曲线是"坑坑洼洼的倒 U"不是教材上平滑的倒 U——测试集
#   只有 179 人，1 个人 = 0.56%，每个 ±2% 的起伏就是几名乘客，别过度解读。
#   站得住的结论只有：depth≥7 以后不再变好，过拟合真实存在
#
# 流程记录：五处预测①-⑤全部没填。code-last 一半的价值在"运行前先猜"——
# 下一课（交叉验证）从预测①开始补上这个习惯。

# ══ 对比记录（不标准/错误写法 + 原因 + 改进写法）═══════════
# 1.【sum[pred] → TypeError】sum 是内置函数，函数调用用 ()，[] 是给序列取元素用的。
#    sum[pred] 会被理解成"给 sum 函数下标" → 当场报错，后面所有任务被它挡住没跑。
#    正确调用：sum(pred == 0)。但就算改成这个也不是基线——见第 2 条
# 2.【pred 和 y_test 张冠李戴】你注释里写的意图（统计 y_test 为 0 的个数）是对的，
#    代码却算在 pred 上：sum(pred==0)/179 度量的是"模型判死的比例"（输出分布），
#    而"全判遇难"基线要用实际标签：(y_test == 0).mean()。
#    今天两个数碰巧都是 0.5866——别让重合的数字掩盖概念错误
# 3.【手写魔法数 179】179 是 test_size=0.2 切出来的结果，改切分比例或换数据就失效。
#    写 len(y_test) 或直接 .mean()，让 Python 自己算分母
# 4.【挂号回答：.score() 打分规则】你写"不太了解打分规则是什么"——分类器时 .score()
#    = accuracy；回归器时 = R²。所以任务 4 里它可以直接当 test 分数用
# 5.【收了没用中间变量】pred_depth3、pred_d 定义了但没用——不是 bug，但代码要跟
#    意图一致：只要 score 就别接 predict；接了就用（比如给 depth=3 那棵树也算一遍
#    混淆矩阵，跟默认树对比 FP/FN 变化）
# 6.【本课头号结论】max_depth 是治过拟合第一刀：默认树 train 97.9 / test 75.4
#    （差 22.5 分）→ depth=3 train 83.4 / test 79.9（差 3.5 分）。方向口诀：
#    train↓+test↑ = 泛化在变好；train↑+test↓ = 过拟合加深。
#    扫描曲线坑坑洼洼不是失败——179 人的测试集撑不起平滑曲线
