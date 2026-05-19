# HCI Research Methods - Knowledge Base Index

Source: "Research Methods in Human-Computer Interaction, 2nd Edition" (Lazar, Feng, Hochheiser, 2017)

## Chapter Index

| Chapter | Title | Key Topics |
|---------|-------|------------|
| 1 | Introduction to HCI Research | Research process, literature review, research questions |
| 2 | Research Ethics and Regulation | IRB, informed consent, data privacy, ethical principles |
| 3 | Experimental Research | Variables, hypotheses, experimental design, validity |
| 4 | Surveys and Questionnaires | Scale development, question types, sampling, distribution |
| 5 | Usability Testing | Task design, metrics, think-aloud, test planning |
| 6 | Interviews and Focus Groups | Interview types, topic guides, qualitative analysis |
| 7 | Diary Studies | Longitudinal research, self-report, in-situ data |
| 8 | Inspection Methods | Heuristic evaluation, cognitive walkthrough, expert review |
| 9 | Field Studies and Ethnography | Observation, contextual inquiry, naturalistic research |
| 10 | Research with Children | Age-appropriate methods, ethics, engagement strategies |
| 11 | Research with Older Adults | Accessibility, cognitive factors, inclusive design |
| 12 | Research with Disabilities | Assistive technology, universal design, accommodations |
| 13 | Statistical Analysis | Descriptive/inferential statistics, hypothesis testing |
| 14 | Writing and Publishing Research | Paper structure, peer review, academic writing |
| 15 | Replication and Open Science | Reproducibility, open data, pre-registration |
| 16 | Conclusion | Future directions, integrating methods |

## Content Layers

### Layer 1: Chapter Summaries (500-1000 words)
Quick overview of each chapter's main concepts.

- English: `summaries/en/ch{XX}-summary.md`
- Chinese: `summaries/zh/ch{XX}-summary.md`

### Layer 2: Knowledge Points (2000-5000 words)
Structured knowledge extraction with 6 sections:
1. Core Concept Definitions
2. Theoretical Frameworks
3. Methodology Steps
4. Decision Criteria
5. Book Cases and Examples
6. Common Errors and Pitfalls

- English: `knowledge-points/en/ch{XX}-knowledge-points.md`
- Chinese: `knowledge-points/zh/ch{XX}-knowledge-points.md` (with English annotations)

### Layer 3: Full Chapter Text
Complete textbook content for deep reference.

- Location: `chapters/ch{XX}-{topic-slug}.md`

## Quick Access by Topic

### By Research Goal
- **Evaluate a design**: Ch 5 (Usability Testing), Ch 8 (Inspection)
- **Compare alternatives**: Ch 3 (Experiment)
- **Explore user needs**: Ch 6 (Interview), Ch 9 (Field Study)
- **Measure performance**: Ch 3 (Experiment), Ch 13 (Statistics)
- **Large-scale feedback**: Ch 4 (Survey)

### By Data Type
- **Quantitative**: Ch 3 (Experiment), Ch 4 (Survey), Ch 13 (Statistics)
- **Qualitative**: Ch 6 (Interview), Ch 7 (Diary), Ch 9 (Ethnography)
- **Mixed methods**: Ch 3 + Ch 6, Ch 4 + Ch 6

### By Population
- **General adults**: All methods
- **Children**: Ch 10
- **Older adults**: Ch 11
- **People with disabilities**: Ch 12

### By Setting
- **Lab**: Ch 3 (Experiment), Ch 5 (Usability)
- **Field**: Ch 7 (Diary), Ch 9 (Ethnography)
- **Remote/Online**: Ch 4 (Survey), Ch 5 (Remote Usability)

## File Structure

```
hci-research-guide/
├── README.md
├── prompts/
│   ├── system-prompt.md          # Main system prompt
│   ├── interactive-guide.md      # Conversation flow
│   ├── method-decision-tree.md   # Method selection framework
│   └── analysis-template.md      # Analysis planning template
├── adapters/
│   ├── trae/SKILL.md            # Trae adapter
│   ├── claude/CLAUDE.md         # Claude Code adapter
│   ├── cursor/.cursorrules      # Cursor adapter
│   └── copilot/copilot-instructions.md  # Copilot adapter
└── knowledge-base/
    ├── index.md                  # This file
    ├── summaries/
    │   ├── en/                   # English L1 summaries
    │   └── zh/                   # Chinese L1 summaries
    ├── knowledge-points/
    │   ├── en/                   # English L2 knowledge points
    │   └── zh/                   # Chinese L2 knowledge points (with English annotations)
    └── chapters/                 # Full chapter text (L3)
```
