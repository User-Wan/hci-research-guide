# 第四章：调查与问卷 — 摘要

## 主题概述

本章聚焦于处理和解释通过各种HCI研究方法收集的数据所必需的统计分析方法 (Statistical Analysis Methods)。它提供了基于研究设计和数据特征选择适当统计检验的综合指南，强调正确的方法选择和准确的解释对于从用户研究中得出有效结论至关重要。

## 核心概念

- **数据准备流程 (Data Preparation Pipeline)：** 本章建立了三步预处理工作流——清洗 (Cleaning)（识别和纠正错误，处理缺失值）、编码 (Coding)（将分类数据转换为数值形式以便软件处理）和组织 (Organizing)（根据特定统计程序的要求结构化数据）。

- **描述性统计 (Descriptive Statistics)：** 集中趋势度量 (Central Tendency Measures)（均值 (Mean)、中位数 (Median)、众数 (Mode)）和离散度量 (Spread Measures)（范围 (Range)、方差 (Variance)、标准差 (Standard Deviation)）作为理解数据分布的基础工具被引入。正态分布 (Normal Distribution) 的概念被强调为确定应用何种统计检验的关键因素。

- **参数检验与非参数检验 (Parametric vs. Nonparametric Tests)：** 参数检验（假设正态分布和等距数据）与非参数检验（放宽这些假设，但通过将数据压缩为秩次 (Ranks) 来牺牲一些统计功效）之间存在根本区别。

- **显著性检验框架 (Significance Testing Framework)：** 本章介绍了零假设 (Null Hypothesis) 检验的逻辑、置信区间 (Confidence Intervals)（通常为95%）以及p值 (p-values) 作为观察到的差异由随机因素产生的概率的解释。

## 主要方法与框架

本章提出了一个基于两个维度选择统计检验的系统框架：实验设计（被试间、被试内或混合）以及自变量的数量及其条件。

**均值比较（参数方法）：**
- **t检验 (t Tests)：** 独立样本t检验 (Independent-Samples t Test)（被试间，2个条件）和配对样本t检验 (Paired-Samples t Test)（被试内，2个条件），根据是否存在方向性假设区分单尾检验 (One-Tailed) 和双尾检验 (Two-Tailed)。
- **单因素方差分析 (One-Way ANOVA)：** 用于被试间设计，一个自变量有3个或更多条件，返回综合F值 (Omnibus F Value)。
- **因子方差分析 (Factorial ANOVA)：** 用于被试间设计，2个或更多自变量，可检验主效应和交互效应。
- **重复测量方差分析 (Repeated Measures ANOVA)：** 用于被试内设计，有单水平（单个自变量）和多水平（多个自变量）变体。
- **裂区方差分析 (Split-Plot ANOVA)：** 用于结合被试间和被试内因素的混合设计，具有减少参与者负担和控制学习效应的优势。

**关系识别：**
- **相关分析 (Correlation Analysis)：** 皮尔逊相关系数 (Pearson's r)（范围从-1到1）测量两个变量之间的线性关系；r²代表共享方差比例。本章强烈警告相关不等于因果 (Correlation does not imply causation)，通过收入与绩效的关系以年龄作为中介变量的例子加以说明。
- **回归分析 (Regression Analysis)：** 同时进入回归 (Simultaneous Entry Regression) 检验自变量如何共同预测因变量（通过R²），而层次回归 (Hierarchical Regression) 基于理论模型按顺序引入变量，通过R²变化评估各变量的单独贡献。

**非参数方法：**
- **卡方检验 (Chi-Squared Test)：** 分析列联表 (Contingency Tables) 中分类数据的频次计数，要求数据点独立且样本量≥20。
- **曼-惠特尼U检验 (Mann-Whitney U Test)：** 独立样本t检验的非参数替代方法，用于比较两个独立组。
- **威尔科克森符号秩检验 (Wilcoxon Signed-Rank Test)：** 配对样本t检验的非参数替代方法，用于比较两个相关组。
- **克鲁斯卡尔-沃利斯检验 (Kruskal-Wallis Test)：** 单因素方差分析的非参数替代方法，用于3个或更多独立组。
- **弗里德曼检验 (Friedman's Test)：** 重复测量方差分析的非参数替代方法，用于3个或更多相关条件。

## 重要启示

1. **数据质量至关重要：** 彻底的数据清洗、一致的编码和适当的组织必须先于任何统计分析；此阶段的错误可能使即使是最复杂的分析也变得毫无意义。

2. **检验选择取决于设计：** 统计检验的选择由实验设计（被试间/被试内/混合）、自变量数量和每个变量的条件数决定——本章的汇总表（表4.3）提供了宝贵的决策指南。

3. **三个假设决定参数检验的适用性：** 误差独立性 (Independence of Errors)、方差齐性 (Homogeneity of Variance) 和正态分布 (Normal Distribution) 都必须被验证；违反这些假设需要进行数据转换或改用非参数替代方法。

4. **相关≠因果：** 研究者必须抵制从相关性发现中声称因果关系的诱惑；隐藏的中介变量可能解释观察到的关联，分析应以假设为驱动而非以数据为驱动。

5. **非参数检验以功效换取灵活性：** 虽然它们对数据要求不那么严格，但会将数据压缩为秩次，丢失等距信息——它们应仅在参数假设确实被违反时使用，而不是作为默认的安全选项。

6. **规范报告需要上下文：** 统计结果必须报告自由度 (Degrees of Freedom)、效应量 (Effect Sizes) 和显著性水平（如 t(15) = 2.169, p < 0.05），以便进行适当的评估和复制。
