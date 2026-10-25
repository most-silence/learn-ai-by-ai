# ════════════════════════════════════════════════════════════
#  阶段 2 · 机器学习 ｜ 第 1 课 · 训练你的第一个模型
#  日期：2026-10-02　配套教材：notes/phase2_lesson1.md
#  状态：✅ 完成（含对比记录 6 条）　规则：code-last
# ════════════════════════════════════════════════════════════
# 主题：决策树 / train_test_split / 六步骨架 / 数据泄漏铁律（X 里不能有 y 的影子）
# （语法忘了可以翻教材，但先凭记忆写）
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('data/titanic_clean.csv')   # 你昨天亲手清洗的干净表

# ── 任务 1：特征工程——把表变成模型能吃的 X / y ──────────
# 要做：a) y = Survived 列
#       b) X = 剔除 Survived + 无效列（PassengerId / Name / Ticket / Embarked）
#       c) Sex 文本变数字：map({'male': 1, 'female': 0})
# 预测①：X.shape = ? 891 - 1 - 1 - 1 - 1- 1=886
# 预测②：y.mean()（整体生还率）大概 = ? 50%
# 你的代码：
print(df.isna().sum()) # 验证是清洗完后的数据
y = df['Survived']
X =  df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Embarked'])
X['Sex'] = X['Sex'].map({'male' : 1 ,'female': 0}) # 常规在C++或者其他语言的基础方法是循环遍历，但是Python有更高效的书写方法，同时这一步通常可以作为onehot编码的最后一步，即将连续数据分桶后进行数学形式转化

# 脚手架（凭记忆填空，不是抄）：
# X = df.drop(columns=['Survived', ?, ?, ?, ?])

# ── 任务 2：切分训练/测试集——考试不能用原题 ─────────────
# 要做：train_test_split(X, y, test_size=0.2, random_state=42) random_state 
# 预测③：X_train 和 X_test 各多少行？（算得出，不是猜）X_train = 0.8*886=708,X_test = 0.2*886=178
# 你的代码：
X_train, X_test,y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # 随机数种子，结果可复现
# 脚手架（两处陷阱：等号左边要用几个变量"接住"返回值？参数拼写）：
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=?, random_state=?)

# ── 任务 3：训练 + 预测 ──────────────────────────────
# 要做：造模型 → fit(X_train, y_train) → predict(X_test) 得到 pred
# 预测④：pred 是什么类型的东西？长度多少？里面装的值长什么样？ pred是一个使用测试集预测后的结果，X_test每个人是否生还，是整数0遇难，1生还，长度与测试集的数量一致178
# 你的代码：
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(pred)
# 脚手架（sklearn 三步曲）：
# model = DecisionTreeClassifier()
# model.fit(?, ?)
# pred = model.predict(?)

# ── 任务 4：打分——真实水平 vs 复习原题成绩 ──────────────
# 要做：分别输出 model.score(X_test, y_test) 和 model.score(X_train, y_train)
# 预测⑤：哪个分数更高？一句话说明你的理由后者，参数本就是通过训练集得到的，与训练集拟合程度更高
# 你的代码：
# 脚手架：print(model.score(?, ?))   ← 写两行，两行参数不同
print(model.score(X_test,y_test))
print(model.score(X_train, y_train))

# ── 任务 5（加餐）：模型的"证词"——特征重要性 ────────────
# 要做：print(dict(zip(X.columns, model.feature_importances_)))
# 预测⑥：模型认为最重要的特征是哪个？（提示：lady first）性别
# 你的代码：
print(dict(zip(X.columns, model.feature_importances_)))

# ── 补充小练：shape 心算器（预测①的根因修复）─────────────
# df 是 891 行 11 列。心算，别运行：
# a) df2 = df.drop(columns=['Name'])     → df2.shape = ?
# b) df3 = df[df['Age'] > 60]            → df3.shape = ?（行数用 k 表示）
# c) 一句话：drop(columns=...) 改变的是行数还是列数？

# ══ 标准答案区（2026-10-03 验收时补）═════════════════════
# 任务 1（关键：Survived 必须从 X 剔除！你的代码漏了它 → 见对比记录#4）
# y = df['Survived']
# X = df.drop(columns=['Survived', 'PassengerId', 'Name', 'Ticket', 'Embarked'])
# X['Sex'] = X['Sex'].map({'male': 1, 'female': 0})   # 你的写法✅
# print(X.shape)     # (891, 6)——drop 删列不删行！
# print(y.mean())    # 0.3838 → 38.4%（你预测 50%）

# 任务 2（你的写法✅：四变量接住返回值、test_size 拼写这次对了）
# X_train: 712 行 / X_test: 179 行（891×0.2=178.2 → 向上取整）

# 任务 3（三步曲✅，建议加 random_state=42）
# model = DecisionTreeClassifier(random_state=42)
# model.fit(X_train, y_train)
# pred = model.predict(X_test)    # numpy 数组(int64)，长 179，值全为 0/1

# 任务 4（修复泄漏后的真实水平，跑完核对）
# print(model.score(X_test, y_test))    # ≈ 0.75~0.78
# print(model.score(X_train, y_train))  # ≈ 0.98 ← 过拟合，今天先认识它

# 任务 5（修复后 Sex 应升为第一——lady first 得到模型确认）
# print(dict(zip(X.columns, model.feature_importances_)))

# ══ 对比记录（不标准/错误写法 + 原因 + 改进写法）══════════
# 1.【shape 根因】预测①写 886=891-5：drop(columns=...) 删的是"列"，行数不变。
#    正确：X.shape = (891, 6)——11列 − Survived/PassengerId/Name/Ticket/Embarked = 6列，行仍 891
# 2.【接住返回值】train_test_split 一次返回 4 个值，必须用
#    X_train, X_test, y_train, y_test = ... 四个变量接住；只调用不接收 = 结果被扔掉
# 3.【拼写四连】meadian→sun→test_sie→colums：同类 bug 第 4、5 次。
#    对策：只打前几个字母按 Tab 补全，永不手打完整单词
# 4.【数据泄漏 ★本课头号教训】X 漏删 'Survived' → 答案列混进特征 →
#    模型学会"看着答案答题"。三个铁证（全中）：score 双 1.0；
#    feature_importances 里 Survived=1.0 其余全 0；连"考试"都满分。
#    修复：drop 里加 'Survived'。泛化铁律：X 里不能有 y 的影子（任何与
#    标签同源的列）。看到 score≈1.0 的第一反应 = 查泄漏，不是庆祝
# 5.【未固定树的 random_state】DecisionTreeClassifier() 构建时也有随机性
#    （特征打平时随机挑），加 random_state=42 与 train_test_split 同理：可复现
# 6.【map 注释的概念挂号】你注释里说 map 是"onehot 编码的最后一步"——不对但值得挂号：
#    map 类别→数字 = 标签编码；one-hot = 每个类别拆成一列 0/1（后面特征工程课学）；
#    连续数据分桶 = 分箱 binning（另一个概念）。三者各有一课，到时回收
