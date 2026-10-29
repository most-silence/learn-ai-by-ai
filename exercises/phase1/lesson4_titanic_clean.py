# ════════════════════════════════════════════════════════════
#  阶段 1 · Python 数据分析基础 ｜ 第 4 课 · 亲手清洗 Titanic
#  日期：2026-10-01　配套教材：—　状态：✅ 完成　规则：code-last
# ════════════════════════════════════════════════════════════
# 主题：drop 删列 + 重赋值 / mode() / 验收推理 / 清洗顺序（去重 vs 填充）
import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('data/titanic.csv')

# ── 任务 1：删掉 Cabin 列（上节课决策 a：77% 缺失 → 删整列）──
# 预测①：执行后 df.shape = ?print(len(df.columns)-1)=11列 看看还有哪些列
# 你的代码：
df = df.drop(columns='Cabin')

# ── 任务 2：用 median 填 Age（决策 c：约 20% 缺失 → 中位数填充）──
# 预测②：Age 的 median = ?（先猜个数再运行）猜中位数没价值
# 预测③：填充后 df['Age'].isnull().sum() = ? 这个没法用尝试预测，没价值
# 你的代码：
df['Age'] =  df['Age'].fillna(df['Age'].median())

# ── 任务 3：用 mode 填 Embarked（决策 b：只缺 2 个 → 众数填充）──
# 预测④：df['Embarked'].mode() 输出什么？为什么取值时要加 [0]？输出没必要预测这个没价值直接计算即可，众数一般有多个数值数量相同构成一个数组，默认取第一个但这个数是最大还是最小无法确定
# 你的代码：
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# ── 任务 4：清洗验收 ──
# 预测⑤：三步之后 isnull().sum() 还剩谁？都不为空了，最终 df.shape = ? 891*11
# 你的代码：

print(df.isnull().sum())
print(df.shape)

# ══ 标准答案区（2026-10-01 验收时补）═════════════════════
# 任务 1
# df = df.drop(columns=['Cabin'])       # 单列也可写 columns='Cabin'（你的写法✅）
# print(df.shape)                       # (891, 11)

# 任务 2
# print(df['Age'].median())             # 28.0 —— 和你的直觉差多少？
# df['Age'] = df['Age'].fillna(df['Age'].median())
# print(df['Age'].isnull().sum())       # 0

# 任务 3
# print(df['Embarked'].mode())          # 输出一个 Series：0    S  (Name: Embarked)
# df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
# print(df['Embarked'].isnull().sum())  # 0

# 任务 4
# print(df.isnull().sum())              # 所有列全 0 → 清洗验收通过
# print(df.shape)                       # (891, 11)

# ══ 对比记录（不标准/错误写法 + 原因 + 改进写法）══════════
# 1.【拼写+缺括号】.meadian → 两层错：
#    a) 拼写应为 median；b) 即使拼对，.median 不加 () 只是"引用方法本身"不执行，
#       fillna 拿到的是方法对象而不是数值 → 报错。
#    改进：df['Age'].median() —— 方法必须带 () 才会执行
# 2.【拼写】.sun() → 应为 .sum()（AttributeError）。用 IDE 自动补全可根除此类 bug
# 3.【mode 排序】.mode() 返回的 Series 是按值排序的（并列时 [0] 取排序最前 =
#    字母序/数值最小），不是"无法确定"——规则是确定的；本例 S 票数 644 无并列
# 4.【预测价值】预测③（填充后缺失数=0）不是猜测，是从 fillna 语义推导的必然结果
#    ——可推导的预测检验的是"你是否真正理解工具"，这类预测最有价值
