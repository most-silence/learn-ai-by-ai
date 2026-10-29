# 阶段 2 · 第四课教材：随机森林——让 100 棵树投票

> 配套练习：`exercises/phase2/lesson4_random_forest.py` · 新 API：`sklearn.ensemble.RandomForestClassifier`

---

## 0. 单棵树的毛病

昨天 depth 扫描时你应该感觉到：单棵决策树**成绩不太稳**（换个 random_state 就抖动）。
本质：一棵树把自己的判断**全押在训练数据上**，训练数据有点噪声，它就跟着跑偏。

## 1. 集体智慧：三个臭皮匠，顶个诸葛亮

随机森林 = **100 棵各不相同的树 + 投票**：

1. **数据随机**：每棵树用"有放回抽样"（bootstrap）从训练集抽一份自己的数据 → 每棵树看到的样本略不同
2. **特征随机**：每次分叉只从**随机一部分特征**里挑最优 → 每棵树的"思路"不同
3. **投票**：100 棵树各自给结论，少数服从多数

单棵树各有偏见，但偏见方向不同，**投票时互相抵消**——这叫 **Bagging**（Bootstrap Aggregating）。

## 2. 三步曲一个字没变

```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
model.predict(X_test)          # score() 仍然 = accuracy
```

`n_estimators` = 树的棵数（超参数）；你只需把类名换掉，其余流程照旧——**这是 sklearn 设计的精髓：模型可换，骨架不变**。

## 3. 为什么森林不容易过拟合

- 单棵树的背题噪声在投票中被**稀释**（100 票里 30 棵背错不要紧）
- 所以森林的 train-test 差距**更小**，test 分数**更高更稳**

## 4. feature_importances_ 更可信了

单棵树的重要性排序带偶然性；100 棵树平均后**稳定得多**。看看森林眼中的 Titanic：Sex 还是最重要的吗？Age 和 Fare 谁高？

## 5. 集成学习家族（地图）

- **Bagging**（本课）：并行造树 + 投票 → 随机森林
- **Boosting**（后面学）：串行造树，每棵专修上一棵的错误 → XGBoost / LightGBM（Kaggle 竞赛之王）
