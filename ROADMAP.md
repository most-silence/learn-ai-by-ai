# AI 学习路线图（总览）

> 目标：从 Python 熟练 → 掌握机器学习 / 深度学习 / NLP / 大模型 / AI Agent
> 节奏：碎片化学习，每天 30-60 分钟，以项目驱动
> 更新：2026-09-29

---

## 路线总览

| 阶段 | 主题 | 预计周期 | 产出/里程碑 | 状态 |
|------|------|---------|------------|------|
| 0 | 环境搭建 + AI 全景图 | 1 周 | 可运行的 Python 环境、理解 AI 各领域关系 | ✅ 2026-09-29 |
| 1 | Python 数据分析基础 | 3-4 周 | 数据分析小项目 | ✅ 2026-10-01 毕业考 5.5/6（提前） |
| 2 | 机器学习（ML） | 6-8 周 | 端到端 ML 项目 | ⬜ |
| 3 | 深度学习（DL） | 6-8 周 | PyTorch + 图像分类项目 | ⬜ |
| 4 | NLP | 4-6 周 | 文本分类/情感分析项目 | ⬜ |
| 5 | 大模型（LLM） | 6-10 周 | 微调 + Prompt 项目 | ⬜ |
| 6 | AI Agent | 6-8 周 | 个人助手 Agent | ⬜ |
| 7 | 进阶方向（长期） | 持续 | 多模态 / 论文阅读 / 参赛 | ⬜ |

> 说明：阶段之间有依赖（如 2 依赖 1），但可并行推进，例如学习 ML 同时每天用 10 分钟接触 LLM/Agent 前沿，保持兴趣。

---

## 各阶段模块分解

### 阶段 0：环境搭建 + AI 全景图（约 7 天）
- [ ] 安装 Python 3.10+，创建虚拟环境（conda 或 venv）
- [ ] 安装 Jupyter Notebook / VSCode 配置
- [ ] 安装 numpy / pandas / matplotlib / scikit-learn / torch
- [ ] 理解 AI → ML → DL → NLP → LLM → Agent 的层级关系
- [ ] 了解常用学习资源与术语表

### 阶段 1：Python 数据分析基础（3-4 周）
- [ ] numpy：数组、索引、广播机制、向量化
- [ ] pandas：DataFrame 操作、清洗、分组聚合、合并
- [ ] matplotlib / seaborn：常用图表
- [ ] 项目：真实数据集探索性分析（EDA）
  - 候选：鸢尾花、Titanic、任意 Kaggle 数据集

### 阶段 2：机器学习（6-8 周）

> **本周排期（2026-10-20 起，按"课"排不按"天"排）**
> - ✅ 第一课：第一个模型（决策树 + train_test_split）—— notes/phase2_lesson1.md（10-02）
> - ✅ 第二课：混淆矩阵/精确率/召回率 + max_depth 治过拟合 —— notes/phase2_lesson2.md（10-03，验收 10-10）
> - ✅ 第三课：交叉验证 cross_val_score —— notes/phase2_lesson3.md（代码 10-15，验收 10-20）
> - 🔵 第四课：随机森林（集成学习入门）—— notes/phase2_lesson4.md（10-20）
> - ⬜ 第五课：线性回归（回归 + MSE/R²，tips 数据集）—— notes/phase2_lesson5.md（下一课）
> - ⬜ 之后：特征工程 → GridSearchCV → 端到端里程碑项目（Titanic 生存预测）
>
> 节奏说明：排期只定顺序、不定日期；一课的标准答案 + 对比记录当天补齐，不再拖到下一次。

- [ ] 机器学习方法论：训练/验证/测试集、过拟合、偏差-方差
- [ ] 回归：线性回归、正则化（Ridge/Lasso）、评估指标（MSE/R²）
- [ ] 分类：逻辑回归、决策树、随机森林、XGBoost/LightGBM、评估（准确率/精确率/召回率/F1/ROC）
- [ ] 聚类：KMeans、DBSCAN（选修：对 Agent 目标优先级最低，时间紧可自学跳过）
- [ ] 特征工程与模型选择（交叉验证、GridSearch）
- [ ] 项目（二选一或都做）：
  - Titanic 生存预测（经典入门，完整流程）
  - 房价预测（回归）
- [ ] 里程碑：能独立完成一个端到端 ML 项目

### 阶段 3：深度学习（6-8 周）
- [ ] 神经网络基础：感知机→多层网络、激活函数、损失函数
- [ ] 反向传播直觉理解（会算、不钻太深数学）
  - 推荐：3Blue1Brown 神经网络系列 + 手写一次纯 numpy 网络
- [ ] PyTorch 基础：张量、autograd、nn.Module、Dataset/DataLoader、优化器
- [ ] CNN：卷积/池化直觉，用 CNN 做图像分类
- [ ] 训练技巧：早停、Dropout、BatchNorm、学习率调整、GPU/Colab 使用
- [ ] RNN / LSTM 基础（为 NLP 铺垫）
- [ ] 项目：CIFAR-10 或猫狗图像分类

### 阶段 4：NLP（4-6 周）
- [ ] 文本表示：BOW → TF-IDF → Word2Vec → 词嵌入直觉
- [ ] 用 LSTM/GRU 做序列建模
- [ ] 注意力机制（Attention）核心思想
- [ ] Transformers 库（HuggingFace）上手
- [ ] 项目：微博/IMDB 情感分析 或 垃圾邮件分类
- [ ] 里程碑：理解"文本如何变成向量、模型如何学习语义"

### 阶段 5：大模型（6-10 周）
- [ ] Transformer 架构：Self-Attention、多头、位置编码（配合图解理解）
- [ ] 预训练 vs 微调：为什么开源大模型这么强
- [ ] Prompt Engineering：few-shot、CoT、角色设定
- [ ] 调用 API：OpenAI / DeepSeek / 通义等各家 API 熟悉一个
- [ ] 本地部署开源模型（Ollama 等）
- [ ] 微调入门：LoRA / PEFT，用现有数据集微调小模型
- [ ] RAG（检索增强生成）：文档问答体系
- [ ] 评估与幻觉：量化模型输出的好坏
- [ ] 项目：个人知识库问答机器人（RAG）

### 阶段 6：AI Agent（6-8 周）★ 用户核心目标
- [ ] Agent 概念：LLM 作为大脑 + 规划 + 工具调用 + 记忆
- [ ] Function Calling / Tool Use 机制
- [ ] 手写一个最小 Agent（不带框架，理解原理）
- [ ] LangChain / LlamaIndex（或更轻量的 LangGraph）入门
- [ ] Agent 记忆（对话记忆、长期记忆）
- [ ] 多 Agent 协作概念
- [ ] 项目：个人助理 Agent（能查资料、调工具、记住你的偏好）

### 阶段 7：进阶方向（长期，按兴趣选 2-3 个）
- [ ] 多模态模型（图文/语音）
- [ ] Agent 系统设计：评估、可观测、安全
- [ ] 大模型高效推理 / 量化为服
- [ ] 读经典论文（每周 1 篇 + 做笔记）
- [ ] 参加 Kaggle 比赛或开源贡献

---

## 学习资源推荐

| 主题 | 资源 |
|------|------|
| 机器学习 | 吴恩达《Machine Learning》专项课程 / 李航《统计学习方法》（作查疑） |
| 深度学习 | 3Blue1Brown 神经网络动画、《动手学深度学习》(d2l.ai) ★推荐 |
| PyTorch | 官方教程 60min blitz、《深度学习入门：基于PyTorch》 |
| NLP | 李沐《动手学深度学习》NLP 章节、HuggingFace 官方课程 |
| LLM | 《大模型基础》、Anthropic/OpenAI 官方文档、Andrej Karpathy 视频 |
| Agent | ChatGPT 官方文档 Function Calling 教程、LangChain docs、Anthropic Cookbook |
| 中文社区 | Datawhale(开源教程)、Machine Learning 菜菜、B站李沐视频 |

---

## 迭代机制

1. 每完成一个模块 → 更新 `PROGRESS.md` 的进度与掌握度评级
2. 每完成一个阶段 → 与本仓库 Claude 会话复盘，根据实际情况调整本路线图
3. 每周日做 5 分钟周回顾：本周学了什么 → 难点 → 下周计划
4. 路线图是活的：某个阶段发现没兴趣或没用到，可以降级或跳过，核心是保持每天有产出
