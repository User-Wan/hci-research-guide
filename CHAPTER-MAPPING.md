# 章节文件名与内容映射分析

## 当前状态（严重错位）

| 文件名 | 实际内容 | 状态 |
|--------|----------|------|
| ch01-introduction.md | Introduction | ✅ 正确 |
| ch02-experimental-research.md | Research Ethics and Regulation | ❌ 错位 |
| ch03-experimental-design.md | Experimental Research | ❌ 错位 |
| ch04-statistical-analysis.md | Surveys and Questionnaires | ❌ 错位 |
| ch05-surveys.md | Usability Testing | ❌ 错位 |
| ch06-diary-studies.md | Interviews and Focus Groups | ❌ 错位 |
| ch07-case-studies.md | Diary Studies | ❌ 错位 |
| ch08-interviews-and-focus-groups.md | Inspection Methods | ❌ 错位 |
| ch09-field-studies-and-ethnography.md | Field Studies and Ethnography | ✅ 正确 |
| ch10-usability-testing.md | Research with Children | ❌ 错位 |
| ch11-qualitative-data-analysis.md | Research with Older Adults | ❌ 错位 |
| ch12-automated-data-collection.md | Research with People with Disabilities | ❌ 错位 |
| ch13-sensors-and-measurements.md | Statistical Analysis | ❌ 错位 |
| ch14-online-and-ubiquitous-research.md | Writing and Publishing Research | ❌ 错位 |
| ch15-working-with-human-subjects.md | Replication and Open Science | ❌ 错位 |
| ch16-research-with-disabilities.md | Conclusion | ❌ 错位 |

## 正确映射（基于实际内容）

| 实际内容 | 正确文件名 |
|----------|------------|
| Introduction | ch01-introduction.md ✅ |
| Research Ethics and Regulation | ch02-research-ethics.md |
| Experimental Research | ch03-experimental-research.md |
| Surveys and Questionnaires | ch04-surveys-and-questionnaires.md |
| Usability Testing | ch05-usability-testing.md |
| Interviews and Focus Groups | ch06-interviews-and-focus-groups.md |
| Diary Studies | ch07-diary-studies.md |
| Inspection Methods | ch08-inspection-methods.md |
| Field Studies and Ethnography | ch09-field-studies-and-ethnography.md ✅ |
| Research with Children | ch10-research-with-children.md |
| Research with Older Adults | ch11-research-with-older-adults.md |
| Research with People with Disabilities | ch12-research-with-disabilities.md |
| Statistical Analysis | ch13-statistical-analysis.md |
| Writing and Publishing Research | ch14-writing-and-publishing.md |
| Replication and Open Science | ch15-replication-and-open-science.md |
| Conclusion | ch16-conclusion.md |

## 影响分析

### 需要重新生成的文件
1. L1 英文摘要 (16 files) - 基于错误的章节文件名
2. L1 中文摘要 (16 files) - 基于错误的章节文件名
3. L2 英文知识点 (16 files) - 基于错误的章节文件名
4. L2 中文知识点 (16 files) - 基于错误的章节文件名
5. Prompt 文件 - 引用了错误的章节映射
6. 索引文件 - 引用了错误的章节映射

### 不受影响的文件
1. 原始教科书 MD 文件 - 内容正确，只是文件名错误
2. 适配器文件 - 不引用具体章节
3. 脚本文件 - 不引用具体章节

## 修复方案

### 方案 A: 重新命名章节文件 + 重新生成所有内容
- 优点：一次性解决所有问题
- 缺点：工作量大，需要重新生成 64 个文件

### 方案 B: 保持当前文件名，更新所有引用
- 优点：不需要重新生成内容
- 缺点：文件名和内容不匹配，容易混淆

### 方案 C: 创建映射表，保持现状
- 优点：工作量最小
- 缺点：问题依然存在

**推荐方案 A**：一次性彻底解决问题。
