# HCI Research Guide - 测试指南

## 方式 1: Trae Skill 安装测试

### 步骤 1: 复制 SKILL.md
```powershell
# 在 PowerShell 中运行
Copy-Item "E:\desktop-E\y4\surf\skill\hci-research-guide\adapters\trae\SKILL.md" -Destination "E:\desktop-E\y4\.trae\skills\hci-research-guide\SKILL.md" -Force
```

### 步骤 2: 在 Trae 中使用
- 输入 `/hci-research-guide` 激活 Skill
- 然后描述你的研究需求

---

## 方式 2: 直接对话测试（现在就可以试）

直接告诉我你的研究场景，我会读取知识库来帮你。以下是测试场景：

### 场景 A: 可用性测试
```
我想测试一个新设计的移动App界面，看看用户是否能顺利完成注册流程
```

### 场景 B: 用户访谈
```
我想了解用户对现有购物网站的使用体验，找出他们的痛点
```

### 场景 C: 对比实验
```
我想比较两种不同的按钮设计方案，看哪个更有效
```

### 场景 D: 问卷调查
```
我想大规模收集用户对我产品满意度的反馈
```

---

## 方式 3: 知识库内容验证

### 验证 L1 摘要
```powershell
# 查看第10章可用性测试摘要
Get-Content "E:\desktop-E\y4\surf\skill\hci-research-guide\knowledge-base\summaries\zh\ch10-summary.md"
```

### 验证 L2 知识点
```powershell
# 查看第3章实验设计知识点
Get-Content "E:\desktop-E\y4\surf\skill\hci-research-guide\knowledge-base\knowledge-points\zh\ch03-knowledge-points.md" | Select-Object -First 50
```

### 验证 Prompt 文件
```powershell
# 查看系统提示词
Get-Content "E:\desktop-E\y4\surf\skill\hci-research-guide\prompts\system-prompt.md" | Select-Object -First 30
```

---

## 方式 4: 跨平台测试

### Claude Code
```bash
# 复制到项目根目录
cp E:\desktop-E\y4\surf\skill\hci-research-guide\adapters\claude\CLAUDE.md E:\your-project\CLAUDE.md
```

### Cursor
```bash
# 复制到项目根目录
cp E:\desktop-E\y4\surf\skill\hci-research-guide\adapters\cursor\.cursorrules E:\your-project\.cursorrules
```

### GitHub Copilot
```bash
# 复制到 .github 目录
cp E:\desktop-E\y4\surf\skill\hci-research-guide\adapters\copilot\copilot-instructions.md E:\your-project\.github\copilot-instructions.md
```

---

## 测试检查清单

- [ ] SKILL.md 能否正常加载
- [ ] 交互式问答是否流畅
- [ ] 方法推荐是否准确
- [ ] 知识点引用是否正确
- [ ] 中英文术语是否正确标注
- [ ] 伦理提醒是否包含

---

## 快速测试命令

### 测试 1: 验证文件完整性
```powershell
# 统计各层文件数量
Write-Host "L1 英文摘要: $((Get-ChildItem 'E:\desktop-E\y4\surf\skill\hci-research-guide\knowledge-base\summaries\en\*.md').Count) files"
Write-Host "L1 中文摘要: $((Get-ChildItem 'E:\desktop-E\y4\surf\skill\hci-research-guide\knowledge-base\summaries\zh\*.md').Count) files"
Write-Host "L2 英文知识点: $((Get-ChildItem 'E:\desktop-E\y4\surf\skill\hci-research-guide\knowledge-base\knowledge-points\en\*.md').Count) files"
Write-Host "L2 中文知识点: $((Get-ChildItem 'E:\desktop-E\y4\surf\skill\hci-research-guide\knowledge-base\knowledge-points\zh\*.md').Count) files"
Write-Host "章节原文: $((Get-ChildItem 'E:\desktop-E\y4\surf\skill\hci-research-guide\knowledge-base\chapters\*.md').Count) files"
```

### 测试 2: 验证章节映射
```powershell
# 检查第10章内容是否是可用性测试
$content = Get-Content "E:\desktop-E\y4\surf\skill\hci-research-guide\knowledge-base\chapters\ch10-usability-testing.md" -First 5
Write-Host "Ch10 首行: $content"
```

### 测试 3: 验证中文术语标注
```powershell
# 检查中文知识点是否有英文标注
$content = Get-Content "E:\desktop-E\y4\surf\skill\hci-research-guide\knowledge-base\knowledge-points\zh\ch03-knowledge-points.md" -First 20
$content | Select-String "Experimental Design|实验设计"
```
