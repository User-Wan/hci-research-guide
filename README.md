# HCI Research Guide

> **HCI 研究方法指导助手** — 基于教科书的 AI 辅助研究方法指导系统
>
> An AI-assisted HCI research methodology guide based on *Research Methods in Human-Computer Interaction, 2nd Edition* (Lazar, Feng, Hochheiser, 2017).

---

## 目录 / Table of Contents

- [这是什么 / What Is This](#这是什么--what-is-this)
- [功能说明 / Capabilities](#功能说明--capabilities)
- [快速开始 / Quick Start](#快速开始--quick-start)
  - [方式一：作为 Trae Skill 使用](#方式一作为-trae-skill-使用)
  - [方式二：作为 Claude Code 使用](#方式二作为-claude-code-使用)
  - [方式三：作为 Cursor 使用](#方式三作为-cursor-使用)
  - [方式四：作为 GitHub Copilot 使用](#方式四作为-github-copilot-使用)
  - [方式五：直接对话使用](#方式五直接对话使用)
- [项目结构 / Project Structure](#项目结构--project-structure)
- [内容分层 / Content Layers](#内容分层--content-layers)
- [章节参考 / Chapter Reference](#章节参考--chapter-reference)
- [方法选择指南 / Method Selection Guide](#方法选择指南--method-selection-guide)
- [文件统计 / File Statistics](#文件统计--file-statistics)
- [优化方向 / Future Improvements](#优化方向--future-improvements)
- [许可证 / License](#许可证--license)

---

## 这是什么 / What Is This

**给人用的**：一套结构化的 HCI 研究学习资料，包含 16 章教科书内容、学习指南、常用量表速查。

**给 AI 用的**：一套跨平台 Prompt 系统，让 AI 成为 HCI 研究方法专家，帮你设计实验、选择方法、分析数据、写论文。

---

**For humans**: A structured HCI research learning resource with 16 chapters of textbook content, learning guides, and quick-reference scales.

**For AI**: A cross-platform prompt system that turns AI into an HCI research methodology expert — helping you design experiments, choose methods, analyze data, and write papers.

---

## 功能说明 / Capabilities

### 能做什么 / What It Can Do

| 功能 / Feature | 说明 / Description | 示例 / Example |
|----------------|-------------------|----------------|
| **实验方案设计** | 通过交互式问答引导你设计完整的研究方案 | "我想比较两种界面设计哪个更好" |
| **方法推荐** | 根据研究目标、数据类型、环境推荐合适的 HCI 研究方法 | "我应该用访谈还是问卷？" |
| **统计方法指导** | 根据你的数据类型推荐统计分析方法 | "我有两组定量数据，该用什么检验？" |
| **知识点解答** | 回答 HCI 研究方法相关问题，引用教科书内容 | "什么是 SUS 量表？怎么计分？" |
| **论文写作辅助** | 提供论文结构框架、方法描述规范、结果报告格式 | "实验方法部分怎么写？" |
| **伦理审查提醒** | 始终提醒研究伦理注意事项 | 知情同意、数据隐私、IRB 审批 |

### 交互流程 / Interaction Flow

```
你：我想研究两种界面设计哪个更好

AI：你的主要研究目标是什么？
    A) 评估设计  B) 比较方案  C) 探索需求  D) 测量性能

你：B

AI：你需要什么类型的数据？
    A) 定量  B) 定性  C) 混合

你：A

AI：基于你的回答，推荐以下方法：
    1. 实验研究（Ch 3）★★★★★ — 因果关系、受控比较
    2. A/B 测试（Ch 5）★★★★☆ — 大规模对比
    
    你想深入了解哪个方法？

你：1

AI：（引导你逐步设计实验：变量、设计类型、样本量、统计方法...）
```

### 不能做什么 / Limitations

| 不能做 / Cannot Do | 原因 / Reason |
|-------------------|---------------|
| 运行统计代码 | 这是方法指导工具，不是编程工具 |
| 代写完整论文 | 只能提供框架和建议，不能替代你的写作 |
| 替代专家判断 | 复杂研究仍需咨询有经验的研究者 |
| 超出教科书范围 | 眼动仪、深度学习等高级主题不在教科书内 |
| 收集和分析你的数据 | 无法访问你的实际数据文件 |

---

## 快速开始 / Quick Start

选择你使用的工具，按对应步骤操作：

### 方式一：作为 Trae Skill 使用

**适用**：Trae IDE 用户

**步骤 1：复制配置文件**

```bash
cp adapters/trae/SKILL.md .trae/skills/hci-research-guide/SKILL.md
```

**步骤 2：开始对话**

在 Trae 中切换到 SOLO 模式，输入研究问题：

```
我想研究两种界面设计哪个更好，应该用什么方法？
```

---

### 方式二：作为 Claude Code 使用

**适用**：Claude Code 用户

**步骤 1：复制配置文件**

```bash
cp adapters/claude/CLAUDE.md ./CLAUDE.md
```

**步骤 2：开始对话**

```bash
claude
> 我想研究两种界面设计哪个更好，应该用什么方法？
```

---

### 方式三：作为 Cursor 使用

**适用**：Cursor IDE 用户

**步骤 1：复制配置文件**

```bash
cp adapters/cursor/.cursorrules ./.cursorrules
```

**步骤 2：开始对话**

在 Cursor 的 AI 对话框中输入研究问题：

```
我想研究两种界面设计哪个更好，应该用什么方法？
```

---

### 方式四：作为 GitHub Copilot 使用

**适用**：VS Code + GitHub Copilot 用户

**步骤 1：复制配置文件**

```bash
mkdir -p .github
cp adapters/copilot/copilot-instructions.md ./.github/copilot-instructions.md
```

**步骤 2：开始对话**

在 VS Code 的 Copilot Chat 中输入研究问题：

```
我想研究两种界面设计哪个更好，应该用什么方法？
```

---

### 方式五：直接对话使用

**适用**：任何 AI 助手（ChatGPT、Gemini、Claude 等）

**步骤 1：复制 Prompt**

复制 `prompts/system-prompt.md` 的内容。

**步骤 2：开始对话**

将 Prompt 粘贴到 AI 对话框，然后输入研究问题：

```
你：（粘贴 system-prompt.md 内容）
你：我想研究两种界面设计哪个更好，应该用什么方法？
```

---

## 项目结构 / Project Structure

```
hci-research-guide/
├── README.md                              ← 本文件
│
├── prompts/                               ← AI 行为规则（给 AI 用）
│   ├── system-prompt.md                   # 系统提示词
│   ├── interactive-guide.md               # 对话流程
│   ├── method-decision-tree.md            # 方法决策树
│   └── analysis-template.md               # 数据分析模板
│
├── knowledge-base/                        ← 知识库（给 AI 用）
│   ├── index.md                           # 章节索引
│   ├── chapters/                          # L3: 章节原文（16 个文件）
│   ├── summaries/                         # L1: 章节摘要
│   │   ├── en/                            # 英文版（16 个文件）
│   │   └── zh/                            # 中文版（16 个文件）
│   └── knowledge-points/                  # L2: 知识点详解
│       ├── en/                            # 英文版（16 个文件）
│       └── zh/                            # 中文版（16 个文件）
│
├── learning-guide/                        ← 学习指南（给人读）
│   ├── README.md                          # 学习指南首页
│   ├── 00-快速入门大纲.md                  # 基于思维导图的完整大纲
│   ├── 01-启发式用户实验/                  # 第一部分
│   ├── 02-实验技术性能实验/                # 第二部分
│   ├── 03-评估式实验/                      # 第三部分
│   ├── 04-常用量表速查/                    # 附录：NASA-TLX、SUS、李克特
│   └── 05-参考文献/                        # 补充资源
│
├── adapters/                              ← 平台适配器（给 AI 用）
│   ├── trae/SKILL.md                      # Trae Skill 格式
│   ├── claude/CLAUDE.md                   # Claude Code 格式
│   ├── cursor/.cursorrules                # Cursor 格式
│   └── copilot/copilot-instructions.md    # GitHub Copilot 格式
│
└── scripts/
    └── split-chapters.py                  # 章节拆分脚本
```

---

## 内容分层 / Content Layers

| 层级 | 目录 | 内容 | 用途 |
|------|------|------|------|
| **L1 摘要** | `summaries/{en,zh}/` | 500-1000 字 | 快速了解章节要点 |
| **L2 知识点** | `knowledge-points/{en,zh}/` | 2000-5000 字 | 详细学习，含 6 个标准部分 |
| **L3 原文** | `chapters/` | 完整内容 | 深入研究，引用原文 |

### L2 知识点的 6 个标准部分

1. **Core Concept Definitions** / 核心概念定义
2. **Theoretical Frameworks** / 理论框架
3. **Methodology Steps** / 方法步骤
4. **Decision Criteria** / 决策标准
5. **Book Cases and Examples** / 书本案例与示例
6. **Common Errors and Pitfalls** / 常见错误与陷阱

---

## 章节参考 / Chapter Reference

| Ch | 主题 (ZH) | Topic (EN) | 最适合 / Best For |
|----|-----------|------------|-------------------|
| 1 | HCI 研究导论 | Introduction | 研究基础 |
| 2 | 研究伦理与规范 | Research Ethics | IRB、知情同意 |
| 3 | 实验研究 | Experimental Research | 因果关系、受控比较 |
| 4 | 问卷调查 | Surveys | 大规模数据、态度 |
| 5 | 可用性测试 | Usability Testing | 界面评估、任务设计 |
| 6 | 访谈与焦点小组 | Interviews & Focus Groups | 用户视角、深度理解 |
| 7 | 日记研究 | Diary Studies | 纵向追踪、现场数据 |
| 8 | 启发式评估 | Inspection Methods | 专家评审、认知走查 |
| 9 | 田野研究与民族志 | Field Studies | 自然观察、情境调查 |
| 10 | 儿童研究 | Research with Children | 年龄适配方法 |
| 11 | 老年人研究 | Research with Older Adults | 可访问性、认知因素 |
| 12 | 残障人士研究 | Research with Disabilities | 包容性设计 |
| 13 | 统计分析 | Statistical Analysis | 假设检验、效应量 |
| 14 | 论文写作与发表 | Writing & Publishing | 学术写作 |
| 15 | 复制研究与开放科学 | Replication & Open Science | 可重复性 |
| 16 | 结论 | Conclusion | 未来方向 |

---

## 方法选择指南 / Method Selection Guide

### 按研究目标 / By Research Goal

| 目标 / Goal | 推荐方法 / Recommended | 章节 |
|-------------|------------------------|------|
| 评估设计 / Evaluate design | 可用性测试 / Usability Testing | Ch 5 |
| 比较方案 / Compare alternatives | 实验研究 / Experiment | Ch 3 |
| 探索需求 / Explore needs | 访谈 / Interview | Ch 6 |
| 测量性能 / Measure performance | 实验研究 / Experiment | Ch 3 |
| 大规模反馈 / Large-scale feedback | 问卷调查 / Survey | Ch 4 |

### 按数据类型 / By Data Type

| 类型 / Type | 推荐方法 / Recommended | 章节 |
|-------------|------------------------|------|
| 定量 / Quantitative | 实验、问卷 / Experiment, Survey | Ch 3, 4, 13 |
| 定性 / Qualitative | 访谈、观察 / Interview, Observation | Ch 6, 9 |
| 混合 / Mixed | 混合方法 / Mixed Methods | Ch 3 + 6 |

### 按研究环境 / By Setting

| 环境 / Setting | 推荐方法 / Recommended | 章节 |
|----------------|------------------------|------|
| 实验室 / Lab | 实验、可用性 / Experiment, Usability | Ch 3, 5, 13 |
| 现场 / Field | 日记、民族志 / Diary, Ethnography | Ch 7, 9 |
| 远程 / Remote | 问卷、分析 / Survey, Analytics | Ch 4, 5 |

---

## 文件统计 / File Statistics

| 类别 / Category | 数量 / Count |
|-----------------|-------------|
| L1 英文摘要 / English summaries | 16 |
| L1 中文摘要 / Chinese summaries | 16 |
| L2 英文知识点 / English knowledge points | 16 |
| L2 中文知识点 / Chinese knowledge points | 16 |
| 章节原文 / Full chapter text | 16 |
| Prompt 文件 / Prompt files | 4 |
| 适配器 / Adapters | 4 |
| 学习指南 / Learning guide | 12 |
| **总计 / Total** | **100** |

---

## 优化方向 / Future Improvements

### 内容扩展 / Content Expansion

| 方向 / Direction | 说明 / Description | 优先级 |
|------------------|-------------------|--------|
| 补充学习指南缺失章节 | 创建启发式实验、参与式观察、日记研究等指南文件 | 高 |
| 添加更多量表速查 | PANAS、NASA-TLX 详细版、SUS 中文版等 | 中 |
| 补充第二部分学习资料 | 数据采集、数据分析、算法优化指南 | 中 |
| 添加实际案例库 | 真实的 HCI 研究案例分析 | 中 |

### 交互体验 / Interaction Experience

| 方向 / Direction | 说明 / Description | 优先级 |
|------------------|-------------------|--------|
| 增加示例对话 | 添加更多典型场景的对话示例 | 高 |
| 优化方法决策树 | 增加更多分支和判断条件 | 中 |
| 添加模板生成 | 知情同意书、研究方案、问卷模板 | 中 |
| 支持多轮对话记忆 | 记住用户之前的研究背景 | 低 |

### 知识更新 / Knowledge Update

| 方向 / Direction | 说明 / Description | 优先级 |
|------------------|-------------------|--------|
| 补充新方法 | 远程用户测试、AI 辅助研究等新方法 | 中 |
| 更新教科书引用 | 如果有新版教科书，更新内容 | 低 |
| 添加中文术语对照表 | 统一 HCI 领域中英术语 | 中 |

### 技术改进 / Technical Improvement

| 方向 / Direction | 说明 / Description | 优先级 |
|------------------|-------------------|--------|
| 添加自动化测试脚本 | 验证知识库完整性和正确性 | 中 |
| 支持更多平台适配器 | Windsurf、Cline 等新工具 | 低 |
| 优化 Prompt 性能 | 减少 token 消耗，提高响应速度 | 低 |
| 添加 CI/CD | 自动验证和部署 | 低 |

### 需要收集的数据 / Data to Collect

| 数据类型 / Data Type | 用途 / Purpose | 收集方式 |
|---------------------|---------------|---------|
| 用户反馈 | 了解哪些功能有用，哪些需要改进 | GitHub Issues |
| 使用场景 | 记录用户的实际使用方式 | 对话记录 |
| 错误报告 | 发现知识库中的错误或遗漏 | 用户反馈 |
| 方法推荐准确性 | 验证推荐方法是否合适 | 用户评价 |

---

## 许可证 / License

MIT
