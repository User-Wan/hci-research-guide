# HCI Research Guide

> **HCI 研究方法指导助手** — 基于教科书的 AI 辅助研究方法指导系统
>
> An AI-assisted HCI research methodology guide based on *Research Methods in Human-Computer Interaction, 2nd Edition* (Lazar, Feng, Hochheiser, 2017).

---

## 目录 / Table of Contents

- [这是什么 / What Is This](#这是什么--what-is-this)
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
- [许可证 / License](#许可证--license)

---

## 这是什么 / What Is This

**给人用的**：一套结构化的 HCI 研究学习资料，包含 16 章教科书内容、学习指南、常用量表速查。

**给 AI 用的**：一套跨平台 Prompt 系统，让 AI 成为 HCI 研究方法专家，帮你设计实验、选择方法、分析数据、写论文。

---

**For humans**: A structured HCI research learning resource with 16 chapters of textbook content, learning guides, and quick-reference scales.

**For AI**: A cross-platform prompt system that turns AI into an HCI research methodology expert — helping you design experiments, choose methods, analyze data, and write papers.

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

## 许可证 / License

MIT
