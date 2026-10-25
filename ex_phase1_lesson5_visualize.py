# ════════════════════════════════════════════════════════════
#  阶段 1 · Python 数据分析基础 ｜ 第 5 课 · 可视化 + groupby
#  日期：2026-10-01　配套教材：—　状态：✅ 完成　规则：code-last
# ════════════════════════════════════════════════════════════
# 主题：bar vs hist 口诀；groupby 必须接聚合；从数据读出故事
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
df = pd.read_csv('data/titanic.csv')

# ── 任务 1：哪个性别生还率高？────────────────
# 思路：按 Sex 分组 → 每组算 Survived 的平均（0/1 平均 = 生还率）→ 画柱状图
# 预测①：男、女谁生还率高？各大概百分之几？（凭历史/电影常识猜具体数字）尝试男性生还率高代码显示女性生还概率0.7 男性0.1
# 你的代码：
# 1分组数据
sex_group=df.groupby('Sex')['Survived'].mean()
print(sex_group)
#2画图
sex_group.plot(kind='bar')
plt.show()
# ── 任务 2：花钱多（舱位高）活下来的概率更大吗？──────────
# 思路：把任务 1 的分组依据从 Sex 换成 Pclass
# 预测②：Pclass 1/2/3 的生还率从高到低排序是？1 等舱大概多少？
# 你的代码：
Pclass_group=df.groupby('Pclass')['Survived'].mean()
print(Pclass_group)
#2画图
Pclass_group.plot(kind='bar') # 横坐标无法直接展示分组
plt.show()

# ── 任务 3：乘客年龄分布长什么样？──────────────
# 工具：对 Age 列画直方图（kind='hist'，分 20 个桶），画完要 plt.show() 才显示
# 预测③：直方图的峰值大概在哪个年龄段？分布偏向年轻还是年长？
# 你的代码：
df['Age'].plot(kind='hist', bins=20) # 没说存活与否，只是统计各个年龄段
# print(Age_group)
#2画图
# Age_group.plot(kind='hist', bins=20) # 横坐标无法直接展示分组
plt.show() 


# ══ 标准答案区（2026-10-01 验收时补）═════════════════════
# 任务 1（分组聚合 = 你的写法✅，图型应为柱状图）
# sex_group = df.groupby('Sex')['Survived'].mean()
# print(sex_group)          # female 0.742028 / male 0.188908
# sex_group.plot(kind='bar')
# plt.show()

# 任务 2
# pclass_group = df.groupby('Pclass')['Survived'].mean()
# print(pclass_group)       # 1等 0.629630 / 2等 0.472826 / 3等 0.242363
# pclass_group.plot(kind='bar')
# plt.show()

# 任务 3（不需要 groupby！直方图自己会分桶）
# df['Age'].plot(kind='hist', bins=20)
# plt.show()

# ══ 对比记录（不标准/错误写法 + 原因 + 改进写法）══════════
# 1.【图型选错】比较"类别"的少量结果 → kind='bar'（x 轴显示分组标签，高度=数值）；
#    看"一个连续列"的分布 → kind='hist'（x 轴是数值分桶，高度=落在桶里的个数）。
#    两个值的 Series 画 20 桶直方图 = 无意义的图。你在注释里写"横坐标无法直接
#    展示分组"——观察完全正确，根因就是 bar 被写成了 hist
# 2.【groupby 过度泛化】任务 3 不需要 groupby：hist 的本职就是自动分桶。
#    裸 groupby（不接聚合）只是"分组配方"对象，print 只显示对象内存地址
# 3.【GroupBy.plot 的行为】对 GroupBy 对象直接 .plot() = 每个组各画一张图
#    （88 个不同年龄 → 88 张图）→ 触发 "More than 20 figures" 警告（是警告非报错，
#    但行为已不对：每张图都只画了 1 个年龄的数据）
# 4.【预测①反馈】猜男性生还率高 → 实际女性 74% vs 男性 19%：数据讲出 "lady first"。
#    预测错 = 学到真实世界知识，这正是预测的价值
