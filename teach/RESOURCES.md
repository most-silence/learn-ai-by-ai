# 机器学习 / 深度学习 / LLM / Agent 资源

> 规则：只用高信任来源。每条都要注明"什么时候该翻它"。
> 本仓库的课程结论一律以**跑出来的数字**为准，资源只用来校准方向。

## Knowledge

### 机器学习基础

- [scikit-learn 官方用户指南](https://scikit-learn.org/stable/user_guide.html)
  实现的权威说明。**什么时候翻**：任何"这个参数默认值是什么"、"这个评估器怎么算的"的问题。本课 `max_features` 默认 `sqrt` 就是从这里查的。
- [Breiman & Cutler, *Random Forests*（伯克利官方说明）](https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm)
  随机森林作者本人的定义与解释。**什么时候翻**：讨论森林为什么有效、OOB 是什么、变量重要性怎么算。本课 §2 的两个旋钮（correlation / strength）直接出自这里。
- [Breiman (2001), *Random Forests*, Machine Learning 45:5–32](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf)
  原始论文，含方差上界 ρσ² + (1−ρ)σ²/B。**什么时候翻**：想搞清"树多了方差的下降极限在哪"。
- [Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*（免费 PDF）](https://hastie.su.domains/ElemStatLearn/)
  统计学习标准教材，第 15 章讲随机森林、第 7 章讲偏差-方差分解。**什么时候翻**：需要严格推导时。偏数学，不必逐页读。
- [An Introduction to Statistical Learning (ISLR)](https://www.statlearning.com/)
  ESL 的易读版，有 R/Python labs。**什么时候翻**：ESL 读不动时先看这本。

### 深度学习 / LLM / Agent

- [PyTorch 官方教程](https://pytorch.org/tutorials/)
  阶段 3 的主参考。**什么时候翻**：张量、autograd、`nn.Module`、`DataLoader` 的任何用法问题。
- [3Blue1Brown · 神经网络系列](https://www.3blue1brown.com/topics/neural-networks)
  反向传播的直觉讲解，可视化的梯度下降。**什么时候翻**：阶段 3 学反向传播前先看一遍，比公式好懂。
- [Deep Learning Book (Goodfellow et al.)](https://www.deeplearningbook.org/)
  深度学习权威教材，偏理论。**什么时候翻**：需要查概念定义时，不适合从头读。

### 数据

- [Titanic - Machine Learning from Disaster（Kaggle）](https://www.kaggle.com/c/titanic)
  本仓库阶段 1-2 一直在用的数据集。**什么时候翻**：想看看别人的特征工程思路，或提交一次排行榜。
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/)
  找练手数据集的可靠来源。**什么时候翻**：想做新项目但不知道用什么数据。

## Wisdom (Communities)

- [Cross Validated (Stack Exchange)](https://stats.stackexchange.com/)
  统计学问答，回答质量高、有严格投票机制。**什么时候去**：概念性问题（"bagging 和 boosting 的本质区别"）。提问前先搜，大概率已有答案。
- [r/MachineLearning](https://www.reddit.com/r/MachineLearning/)
  论文与工程实践讨论。**什么时候去**：想知道某个方法在真实项目里好不好用。
- [scikit-learn GitHub Discussions](https://github.com/scikit-learn/scikit-learn/discussions)
  **什么时候去**：怀疑是库的 bug，或想搞清某个行为为什么这么设计。
- [Kaggle Discussions](https://www.kaggle.com/discussions)
  **什么时候去**：想看真实竞赛里的调参思路、别人怎么处理同一份数据。

> 用户偏好：暂无明确表态是否愿意参与社区。**待确认** —— 下次讨论到"该去哪儿问"时问一次。

## Gaps

- **中文高质量 ML 教程**：目前只有英文源。若用户希望中文，需要补找（候选：李宏毅课程、吴恩达中文字幕）。
- **偏差-方差的可视化材料**：本课用数字讲了，但缺一张"高偏差 vs 高方差"的经典图。后续补。
- **Agent 阶段的资源**：完全空缺，到阶段 5 再补。
