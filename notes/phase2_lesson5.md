# 阶段 2 · 第五课教材：回归——当答案是数字

> 配套练习：`exercises/phase2/lesson5_regression.py` · 数据：`data/tips.csv`（244 张真实餐馆账单）
> 新 API：`sklearn.linear_model.LinearRegression`、`sklearn.metrics.r2_score`

---

## 0. 回收第 1 天的口诀

预测"会不会生还" → 答案是**类别标签** → **分类**。
预测"小费给多少" → 答案是**连续数字** → **回归**。
（第 1 天你答过：会不会还款=分类，还多少金额=回归——今天做后者。）

## 1. 数据：tips

每行一张账单：`total_bill`（账单金额）→ 预测 `tip`（小费金额）。直觉上小费应该随账单涨——多涨？让模型自己算。

## 2. 线性回归：模型自己找一条直线

```
tip ≈ w × bill + b
```

`w`（斜率）和 `b`（截距）**不是人定的，是 fit 从数据里算出来的**：

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
model.coef_        # w：账单每多 1 美元，小费平均多多少
model.intercept_   # b：零账单时的"底薪"
```

## 3. 一个经典坑：单特征也要二维

`X = df['total_bill']` 会报错——sklearn 要求特征是二维（行×列）。
**双层括号**：`X = df[['total_bill']]`。
回收第一课口诀：**一层括号出列（Series），两层括号出表（DataFrame）**——模型吃的是"表"。

## 4. 回归怎么打分：MSE 与 R²

| 指标 | 含义 |
|------|------|
| **MSE**（均方误差） | 预测值与真值之差的平方的平均，**越小越好** |
| **R²** | 和"无脑永远猜平均值"比，你强多少：**1=完美，0=和瞎猜均值持平，负数=还不如瞎猜** |

```python
from sklearn.metrics import r2_score, mean_squared_error
r2_score(y_test, pred)
```

顺手的巧合：分类模型的 `.score()` 自动 = accuracy；**回归模型的 `.score()` 自动 = R²**。

## 5. 多特征只是多几列

`X = df[['total_bill', 'size']]` → `coef_` 变成两个数（每个特征一个）。R² 通常更高。
**给模型喂什么列，就是特征工程**——这个话题下周展开。

## 6. 主旋律

六步工作流依旧不变。阶段 2 的套路已经清晰：**骨架永远不变，换模型类名 + 换评估指标而已**。
