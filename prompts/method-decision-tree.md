# Method Decision Tree

A structured decision framework for selecting HCI research methods based on study characteristics.

## Decision Flow

```
START
│
├─ Q1: Primary goal?
│  ├─ A: Evaluate → Q2
│  ├─ B: Compare → Q3
│  ├─ C: Explore → Q4
│  └─ D: Measure → Q5
│
├─ Q2: Evaluate what?
│  ├─ A: Usability → Usability Testing (Ch 5)
│  ├─ B: User satisfaction → Survey (Ch 4) + Usability Testing (Ch 5)
│  ├─ C: Accessibility → Inspection (Ch 8) + User Testing (Ch 12)
│  └─ D: Expert quality → Inspection Methods (Ch 8)
│
├─ Q3: Compare what?
│  ├─ A: Design alternatives → Experiment (Ch 3)
│  ├─ B: User groups → Comparative Study (Ch 3)
│  └─ C: Over time → Longitudinal Study (Ch 7 Diary / Ch 9 Field)
│
├─ Q4: Explore what?
│  ├─ A: User needs → Interview (Ch 6) / Field Study (Ch 9)
│  ├─ B: Behavior patterns → Diary Study (Ch 7) / Ethnography (Ch 9)
│  ├─ C: Attitudes/opinions → Focus Group (Ch 6) / Survey (Ch 4)
│  └─ D: Context of use → Field Study (Ch 9) / Contextual Inquiry
│
├─ Q5: Measure what?
│  ├─ A: Performance metrics → Experiment (Ch 3)
│  ├─ B: Usage data → Analytics + Survey (Ch 4)
│  ├─ C: Physiological data → Lab Experiment (Ch 3)
│  └─ D: Subjective ratings → Questionnaire (Ch 4)
│
END
```

## Quick Decision Table

| If you need to... | Primary method | Supporting method | Chapter |
|-------------------|---------------|-------------------|---------|
| Test if design A is better than B | Controlled experiment | Usability testing | 3, 5 |
| Understand why users struggle | Think-aloud usability test | Interview | 5, 6 |
| Learn about user needs in context | Field study | Interview | 9, 6 |
| Get large-scale feedback | Survey | - | 4 |
| Evaluate without users | Heuristic evaluation | Cognitive walkthrough | 8 |
| Track behavior over time | Diary study | Interview | 7, 6 |
| Compare user groups | Between-subjects experiment | Survey | 3, 4 |
| Test with children | Modified usability test | Observation | 10 |
| Test with older adults | Accessibility evaluation | Interview | 11 |
| Test with disabilities | Inclusive design evaluation | Assistive tech testing | 12 |
| Analyze data statistically | Statistical analysis | - | 13 |
| Write up research | Academic writing | - | 14 |
| Ensure reproducibility | Open science practices | - | 15 |

## Method Combination Patterns

### Pattern 1: Sequential Mixed Methods
```
Explore (Interview Ch 6) → Confirm (Survey Ch 4) → Validate (Experiment Ch 3)
```
Best for: New research domains where little is known.

### Pattern 2: Parallel Mixed Methods
```
Quantitative (Experiment Ch 3) + Qualitative (Think-aloud Ch 5)
```
Best for: Understanding both "what" and "why" simultaneously.

### Pattern 3: Iterative Evaluation
```
Inspection (Ch 8) → Usability Test (Ch 5) → Redesign → Usability Test (Ch 5)
```
Best for: Design improvement cycles.

### Pattern 4: Triangulation
```
Same question → Multiple methods → Compare findings
```
Best for: Increasing confidence in findings.

## Special Population Considerations

| Population | Key Considerations | Recommended Adjustments | Chapter |
|------------|-------------------|------------------------|---------|
| Children | Consent/assent, engagement, attention span | Shorter sessions, game-like tasks, parental presence | 10 |
| Older Adults | Cognitive load, physical abilities, tech experience | Larger fonts, patient instructions, familiar contexts | 11 |
| People with Disabilities | Assistive tech, accessibility, communication | Compatible materials, flexible formats, universal design | 12 |
| Domain Experts | Time constraints, domain knowledge | Contextual settings, expert-appropriate tasks | General |

## Experimental Design Quick Reference (Ch 3)

| Design | When to Use | Advantage | Disadvantage |
|--------|-------------|-----------|--------------|
| Between-subjects | Learning effects likely | No order effects | Requires more participants |
| Within-subjects | Limited participants | More statistical power | Risk of order effects |
| Factorial | Multiple IVs | Reveals interactions | Complex analysis |
| Latin Square | Order effect control | Balanced presentation | Assumes no interaction |

## Statistical Analysis Quick Reference (Ch 13)

| Comparison | Parametric Test | Non-parametric Alternative |
|------------|-----------------|---------------------------|
| 2 independent groups | Independent t-test | Mann-Whitney U |
| 2 paired groups | Paired t-test | Wilcoxon signed-rank |
| 3+ independent groups | One-way ANOVA | Kruskal-Wallis |
| 3+ paired groups | Repeated measures ANOVA | Friedman test |
| Categorical data | Chi-square | Fisher's exact test |
