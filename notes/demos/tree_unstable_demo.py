# -*- coding: utf-8 -*-
"""
阶段 2 · 教学演示：单棵决策树为什么会"背名单"、为什么"不稳"
不是练习，是给第 4 课做铺垫的可复现实验。直接 `python notes/demos/tree_unstable_demo.py`（在仓库根目录运行）

四个实验：
  1. 叶子解剖：满树 170 个叶子里，70 个只代表 1 个人
  2. 切点漂移：多 1 个乘客，切点就从 11.5 挪到 12.5
  3. 留一法：只删掉 1 个训练样本重训，满树 test 晃 3.35 个百分点，d=3 晃 0
  4. 结构变动：同样删 1 个人，满树节点数从 331 跳到 355（差 24 个节点）
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

df = pd.read_csv('data/titanic_clean.csv')
df['Sex'] = df['Sex'].map({'male': 1, 'female': 0})
X = df.drop(columns=['Survived', 'PassengerId', 'Name', 'Ticket', 'Embarked'])
y = df['Survived']
names = df['Name']
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

full = DecisionTreeClassifier(random_state=42).fit(Xtr, ytr)
d3 = DecisionTreeClassifier(max_depth=3, random_state=42).fit(Xtr, ytr)
t, t3 = full.tree_, d3.tree_

print('=' * 60)
print('实验 1：叶子解剖——满树到底学到了什么')
print('=' * 60)
leaves = [i for i in range(t.node_count) if t.children_left[i] == -1]
counts = np.array([t.n_node_samples[i] for i in leaves])
print(f'满树 {t.node_count} 个节点，{len(leaves)} 个叶子')
print(f'  只有 1 人的叶子：{(counts == 1).sum()} 个')
print(f'  只有 2 人的叶子：{(counts == 2).sum()} 个')
print(f'  叶子平均人数  ：{counts.mean():.2f} 人')
print()
print('举几个"1 人叶子"（这棵树的这 8 条规则，各自只对应 1 名乘客）：')
leaf_of = full.apply(Xtr)
shown = 0
for nd in leaves:
    if t.n_node_samples[nd] != 1:
        continue
    for j in np.where(leaf_of == nd)[0]:
        row = Xtr.iloc[j]
        nm = names.iloc[Xtr.index[j]][:38]
        print(f'  {nm:38s} 生还={ytr.iloc[j]} Age={row.Age:5.1f} Fare={row.Fare:6.1f}')
    shown += 1
    if shown >= 6:
        break

print()
print('对比 d=3 的 8 个叶子：')
l3 = [i for i in range(t3.node_count) if t3.children_left[i] == -1]
for i in l3:
    n = t3.n_node_samples[i]
    pred = 1 if t3.value[i][0][0] < t3.value[i][0][1] else 0
    print(f'  训练样本 {n:3d} 人 → 预测 {"生还" if pred else "遇难"}')

print()
print('=' * 60)
print('实验 2：切点漂移——多 1 个乘客，切点就挪')
print('=' * 60)
data = [(5, 1), (8, 1), (10, 1), (13, 0), (25, 0), (30, 0), (40, 0), (45, 0)]
for label, dd in [('原 8 人', data), ('加 1 个 12 岁生还者', data + [(12, 1)])]:
    Xi = pd.DataFrame({'Age': [d[0] for d in dd]})
    yi = pd.Series([d[1] for d in dd])
    m = DecisionTreeClassifier(max_depth=1, random_state=0).fit(Xi, yi)
    print(f'{label:20s} → 切点 Age <= {m.tree_.threshold[0]}')

print()
print('=' * 60)
print('实验 3 & 4：留一法——每次只删 1 个训练样本')
print('=' * 60)
print(f'基准：满树 test={full.score(Xte, yte):.4f} nodes={t.node_count} | '
      f'd=3 test={d3.score(Xte, yte):.4f} nodes={t3.node_count}')
rng = np.random.RandomState(0)
res_f, res_d, nodes_f = [], [], []
for _ in range(15):
    drop = rng.choice(len(Xtr), 1, replace=False)
    Xa, ya = Xtr.drop(Xtr.index[drop]), ytr.drop(ytr.index[drop])
    f = DecisionTreeClassifier(random_state=42).fit(Xa, ya)
    d = DecisionTreeClassifier(max_depth=3, random_state=42).fit(Xa, ya)
    res_f.append(f.score(Xte, yte))
    res_d.append(d.score(Xte, yte))
    nodes_f.append(f.tree_.node_count)
print(f'满树 test 范围: {min(res_f):.4f} ~ {max(res_f):.4f}  极差 {max(res_f)-min(res_f):.4f}')
print(f'满树节点数范围 : {min(nodes_f)} ~ {max(nodes_f)}  极差 {max(nodes_f)-min(nodes_f)} 个节点')
print(f'd=3  test 范围: {min(res_d):.4f} ~ {max(res_d):.4f}  极差 {max(res_d)-min(res_d):.4f}')
print()
print('结论：满树对"训练集里少一个人"极度敏感；d=3 纹丝不动。')
print('      不稳不是 random_state 的错，是"一路分裂到叶子只剩 1 人"的必然结果。')
