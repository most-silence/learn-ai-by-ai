# 阶段 2 · 机器学习第一课教材：你的第一个会预测的模型

> 配套练习：`exercises/phase2/lesson1_decision_tree.py`（先读教材再做题）
> 数据：`data/titanic_clean.csv`（你昨天亲手清洗的表：891 行 × 11 列，零缺失）
> 预计：教材 10 分钟 + 练习 20-30 分钟

---

## 0. 你站在哪里

阶段 1 你学会的是**回答关于过去的问题**（谁生还了？年龄怎么分布？）。
阶段 2 开始回答**关于未来的问题**：看到一个新乘客的资料，**预测**他能不能活下来。
从"描述数据"到"预测未知"，这就是机器学习。

## 1. 监督学习，正式落地

第 1 天你说过："预测会不会还款，如果历史数据带标签就是监督学习。"
Titanic 正是如此——每个乘客的生死是史实（标签），今天我们把这句话变成代码：

```
监督学习 = 给模型看大量「特征 → 答案」的配对，让它自己悟出规律
         = 训练（fit）：X_train + y_train → 模型
         = 考试（predict）：只给 X_test → 模型答出 y_pred → 和 y_test 对答案
```

## 2. 一张表的四个角色

| 角色 | 本表例子 | 说明 |
|------|---------|------|
| **标签 y** | `Survived` | 要预测的"答案"列（只有 1 列） |
| **特征 X** | Pclass、Age、Fare… | 用来做预测的"证据"列 |
| **必须剔除的列** | `PassengerId`、`Name`、`Ticket` | ID 是纯编号无规律；Name 是文本；它们不是有效证据 |
| **要变成数字的列** | `Sex`（male/female） | sklearn 模型只吃数字，文本要先编码（如 male→1, female→0） |

造 X 的标准写法：`X = df.drop(columns=['Survived', ...剔除列])`，`y = df['Survived']`。
Sex 编码：`df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})`。

## 3. train_test_split：考试不能用原题

模型**不能**用见过的数据考成绩——就像不能拿复习原题当期末考。
所以先把数据切成两份：

```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
```

- `test_size=0.2` → 20% 当期末考卷（179 人），80% 拿来学习（712 人）
- `random_state=42` → 固定"洗牌"的随机种子，**保证你每次运行切出来的都是同一份**（结果可复现，写 42 或任何数都行）
- 返回 4 个东西，顺序固定：训练特征、测试特征、训练答案、测试答案

## 4. 决策树：一棵会自己生长的"是非流程图"

决策树（DecisionTreeClassifier）就是一连串"如果…那么…"：

```
Sex = female?
 ├─ 是 → Age < 13? → 生还概率高…
 └─ 否 → Pclass = 1? → …
```

**树不是人画的，是模型从训练数据里自己长出来的**（哪个问题分得最开就先问哪个）：

```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()        # 1. 造一个空模型
model.fit(X_train, y_train)             # 2. 学习：用训练集把树"长"出来
pred = model.predict(X_test)            # 3. 考试：对测试集逐人给出 0/1 预测
```

sklearn 所有模型都是这三步：**造 → fit → predict**（以后换模型只换第一行）。

## 5. 打分 & 第一次见到过拟合

```python
model.score(X_test, y_test)    # 测试集正确率 —— 这是真实水平
model.score(X_train, y_train)  # 训练集正确率 —— 这是"复习原题的成绩"
```

留意一个现象：**训练集分数通常明显高于测试集**——模型把训练数据的细节（甚至噪声）背得太死，考新题就露怯。这个现象叫**过拟合**，今天只观察、先不深究，下一课专治它。

## 6. 加餐：让模型自己"作证"

决策树能告诉你它最依赖哪个特征：

```python
dict(zip(X.columns, model.feature_importances_))
```

`feature_importances_` 是每个特征的重要性分数（和为 1）。跑完对照一下：模型的判断和你毕业考发现的 "lady first" 一致吗？

## 7. 今天的完整工作流（背下来）

```
读数据 → 造 X/y（清洗+编码）→ train_test_split → fit → predict → score
```

这 6 步是之后**所有** sklearn 项目的骨架，换数据不换流程。

---

### 延伸阅读（可选，不占用今日时间）
- scikit-learn 官方入门：https://sklearn.org/stable/getting_started.html
- 吴恩达《Machine Learning》2022 版 · Week 1（监督学习概念对应本课）
