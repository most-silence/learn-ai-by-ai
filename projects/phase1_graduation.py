# ═══ 阶段 1 毕业考：Titanic 独立分析（2026-10-01）═══
# 规则：不看 ex1~ex5 任何旧文件，全部代码自己从头写
# 数据：data/titanic.csv（891 名乘客）
#
# 考题：回答一个你自己提出的问题（三选一或自拟）
#   A. 孩子（Age < 12）真的更容易生还吗？
#   B. 带家属的（SibSp+Parch > 0）比独行的生还率高吗？
#   C. 登船港口（Embarked）和生还有关吗？
#
# 我选的题：三个都选
# 我的预测（先写！）：
# A 不容易，验证思路，可以计算生还者小于12岁的比例
# B 是的，可以相互照顾
# C 无关 理论上来说只要登上船了，在哪里登船不影响是否生还
# 评分点（全链路，每项 1 分，6 分毕业）：
#   □ 1. read_csv 读入数据
#   □ 2. 先预测后分析（预测写在上面）
#   □ 3. 必要的清洗（用到什么洗什么，不用的列不用洗）
#   □ 4. 分析：groupby 或条件筛选（A 题需要造新列，提示：df['IsKid'] = df['Age'] < 12）
#   □ 5. 一张图（图型选对：比较类别用 bar）
#   □ 6. 一句话结论（数字支撑，写在下面）
#
# 结论区（跑完后写）：
# A结果显示小于12小孩生还概率57%，确实更高
#
# B结果显示带家属的 概率生还 50.5% 比独行生还率高
#
# C暂无结果支持，初步推断 C Embarked 0.55 显著高于Q0.38 S0.33
#
# ══ 我的代码 ══

import pandas as pd
import matplotlib.pyplot as plt

# 排除点点点，全部显示 max?
df = pd.read_csv('data/titanic.csv')

# 3. Clean duplicates first and then nan or nan

df = df.drop_duplicates() # Drop duplicates

print(df.isna().sum())

df = df.drop(columns=['Cabin']) # Drop 'Cabin' which contains too much na value

# df[df['Age'].isna()]['Age']= df['Age'].median() # Or fina in the same way, this is a bool 特性 of DataFrame
df['Age']= df['Age'].fillna(df['Age'].median())
# df[df['Embarked'].isna()]['Embarked']= df['Embarked'].mode()[0] # Or fina in the same way, this is a bool 特性 of DataFrame
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
print(df.isna().sum())

# 4. 
# A

# df['IsKid'] = df['Age']<12
# # print(df['IsKid'])
# answer_a = df.groupby('IsKid')['Survived'].mean()
# print(answer_a) # 结果显示小于12小孩生还概率57%，确实更高
# answer_a.plot(kind='bar')
# plt.show()

# B
df['SibSpParch'] = (df['SibSp']+ df['Parch'])>0
# print(df['SibSpParch'])
answer_b = df.groupby('SibSpParch')['Survived'].mean()
print(answer_b) # 结果显示带家属的 概率生还 50.5% 比独行生还率高
answer_b.plot(kind='bar')
plt.show()

# C 无法直接判断相关性，所以直接统计各个港口登船的人数/生还率，通过直接展示出来判断相关性

answer_c = df.groupby('Embarked')['Survived'].mean()
Embarked_sum = df.groupby('Embarked').sum()
# print(pd.count(df.groupby('Embarked'))) 判断每个登船港口的总数
print(answer_c) # C 的生还率显著高于其他地方，可能有关，但前提是每个地方上船人数差不多
answer_c.plot(kind='bar')
# answer_c.plot(kind='hist', bins=20)
plt.show()

# ══ 阅卷意见（2026-10-01，5.5/6 毕业）══════════════════
# 评分：读入✅ 预测✅(三题全预测) 清洗✅(顺序正确!) 分析✅(B题无提示自创布尔列)
#       图✅(bar选对) 结论✅A✅B / C半分(停在"初步推断")
# 亮点：
#   1. 先 drop_duplicates 再填充——第2课"清洗顺序"知识独立落地
#   2. B 题自己造 SibSpParch 布尔列，未用提示举一反三
#   3. C 题意识到"前提是各港人数差不多"——样本量/混淆变量直觉萌芽
#   4. 第46/48行自己发现链式赋值不生效并改正——那是 pandas 最著名的坑
# 对比记录：
#   1.【链式赋值】df[df['Age'].isna()]['Age']=x 不生效：先[]筛选返回的是
#      临时副本，赋值落在副本上原表不动（SettingWithCopyWarning）。
#      正确：整列 fillna（你的写法）或 df.loc[条件, 'Age'] = x
#   2.【数个数用 size】groupby().sum() 是对数值列求和；数每组几行用
#      .size()（推荐）或 .count()。Embarked_sum 算完没用上
#   3.【pd.count 不存在】count 是方法（df['x'].count()），不是 pd 模块函数
#   4.【C题真相】C港0.55≠港口救命，是混淆变量：C港(瑟堡)登船的多为
#      一等舱富豪。验证：df.groupby(['Embarked','Pclass']).size()
#      ——相关≠因果，这是机器学习特征思维第一课