# Interactive Research Guide

## Conversation Flow

This document defines the interactive questioning pattern for guiding HCI research design.

### Phase 1: Research Context Discovery

```markdown
**Question 1: What is your primary research goal?**

A) Evaluate an existing design/interface
B) Compare two or more design alternatives
C) Explore user behaviors, needs, or attitudes
D) Measure specific performance metrics
E) Validate a hypothesis or theory
F) Other (please describe)

**Question 2: What type of data best answers your research question?**

A) Quantitative (numbers, measurements, statistics)
B) Qualitative (interviews, observations, themes)
C) Mixed methods (both quantitative and qualitative)
D) Not sure yet — help me decide

**Question 3: What is your study context?**

A) Controlled lab environment
B) In the field (naturalistic setting)
C) Online / Remote (web-based tools)
D) Not sure yet — help me decide

**Question 4: Who are your participants?**

A) General adult population
B) Children (under 18)
C) Older adults (65+)
D) People with disabilities
E) Domain experts / professionals
F) Mixed population
G) Not sure yet
```

### Phase 2: Method Recommendation

Based on Phase 1 answers, generate a method recommendation table:

```markdown
Based on your answers, here are the recommended research methods:

| Rank | Method | Fit Score | Chapter Ref | Key Advantage |
|------|--------|-----------|-------------|---------------|
| 1 | [Method A] | ★★★★★ | Ch X | [Brief reason] |
| 2 | [Method B] | ★★★★☆ | Ch Y | [Brief reason] |
| 3 | [Method C] | ★★★☆☆ | Ch Z | [Brief reason] |

**Which method would you like to explore further?** (Enter 1, 2, or 3)
```

### Phase 3: Method-Specific Deep Dive

After user selects a method, guide through these sub-sections:

#### For Experimental Research (Ch 2-3):
```
1. Independent variables — What will you manipulate?
2. Dependent variables — What will you measure?
3. Hypotheses — What do you expect to find?
4. Experimental design — Within-subjects / Between-subjects / Mixed?
5. Controls — What confounds need to be addressed?
6. Pilot study plan
```

#### For Surveys (Ch 5):
```
1. Construct identification — What constructs to measure?
2. Scale selection — Existing scales vs. new development?
3. Question types — Open-ended / Likert / Multiple choice / Ranking?
4. Survey length — Target completion time?
5. Distribution method — Email / Web / In-person?
6. Pilot testing plan
```

#### For Usability Testing (Ch 10):
```
1. Test objectives — What aspects of usability to evaluate?
2. Task design — Real-world scenarios to test?
3. Metrics — Task success / Time / Errors / Satisfaction?
4. Test format — Think-aloud / Retrospective / Co-discovery?
5. Participant profile — Target user characteristics?
6. Environment — Lab / Remote / Contextual?
```

#### For Interviews/Focus Groups (Ch 8):
```
1. Interview type — Structured / Semi-structured / Unstructured?
2. Topic guide — Key themes to explore?
3. Sampling strategy — Purposive / Snowball / Theoretical?
4. Recording method — Audio / Video / Notes?
5. Analysis approach — Thematic / Content / Grounded theory?
6. Group dynamics (if focus group) — Size and composition?
```

#### For Diary Studies (Ch 6):
```
1. Duration — How long will participants keep diaries?
2. Format — Paper / Digital / Mixed?
3. Prompts — What questions to ask at each entry?
4. Reminder strategy — How to ensure compliance?
5. Data collection — When and how to retrieve diaries?
6. Follow-up — Post-diary interview needed?
```

#### For Case Studies (Ch 7):
```
1. Case selection — Why this case? Typical / Extreme / Critical?
2. Data sources — Interviews / Documents / Observations / Artifacts?
3. Duration — Single point or longitudinal?
4. Boundaries — What's included and excluded?
5. Triangulation — How to validate findings?
6. Reporting — Single case or multiple cases?
```

#### For Field Studies / Ethnography (Ch 9):
```
1. Entry strategy — How to gain access to the field?
2. Role — Participant observer / Non-participant / Complete observer?
3. Duration — Short-term immersion or long-term engagement?
4. Data collection — Field notes / Audio / Video / Artifacts?
5. Focus — Broad exploration or targeted observation?
6. Analysis — When and how to analyze field data?
```

#### For Qualitative Data Analysis (Ch 11):
```
1. Analysis approach — Thematic / Content / Grounded theory?
2. Coding strategy — Inductive / Deductive / Hybrid?
3. Codebook — Initial codes or emergent?
4. Reliability — Single coder or inter-coder agreement?
5. Software — Manual coding or CAQDAS?
6. Reporting — Themes with supporting quotes?
```

#### For Automated Data Collection (Ch 12):
```
1. Data source — Web analytics / Log files / API?
2. Metrics — What to measure automatically?
3. Volume — Expected data size and processing needs?
4. Privacy — How to handle user data ethically?
5. Integration — Combine with other data sources?
6. Validation — How to verify data quality?
```

#### For Sensors & Physiological Measurements (Ch 13):
```
1. Sensor type — Eye tracker / GSR / EEG / Heart rate?
2. Equipment — What hardware/software needed?
3. Calibration — How to calibrate for each participant?
4. Data quality — How to handle noise and artifacts?
5. Analysis — What metrics to extract?
6. Interpretation — How to link physiological data to behavior?
```

### Phase 4: Plan Summary and Validation

```markdown
## Research Plan Summary

### Research Question
[User's stated goal]

### Methodology
[Selected method with chapter reference]

### Participants
- Population: [description]
- Sample size: [recommendation with justification]
- Recruitment: [strategy]

### Study Design
[Detailed design based on Phase 3 answers]

### Data Collection
[Instruments, procedures, timeline]

### Analysis Plan
[Statistical or qualitative analysis approach]

### Ethical Considerations
- [ ] Informed consent designed
- [ ] Data privacy plan in place
- [ ] Risk assessment completed
- [ ] IRB/Ethics submission prepared
- [ ] Special population considerations addressed (if applicable)

### Next Steps
1. [Action item 1]
2. [Action item 2]
3. [Action item 3]

**Does this plan look good?** (A: Yes, proceed / B: Need modifications / C: Start over)
```

## Quick Reference: Method Selection Matrix

| Goal | Quantitative | Qualitative | Mixed |
|------|-------------|-------------|-------|
| Evaluate design | Usability Testing (Ch 10), Experiment (Ch 2-3) | Think-aloud Testing (Ch 10) | Combined approach |
| Compare alternatives | A/B Testing (Ch 12), Experiment (Ch 2-3) | Comparative Evaluation | Sequential design |
| Explore behavior | Survey (Ch 5), Analytics (Ch 12) | Field Study (Ch 9), Interview (Ch 8) | Ethnography (Ch 9) + Survey (Ch 5) |
| Measure performance | Experiment (Ch 2-3), Benchmark | - | Usability (Ch 10) + Interview (Ch 8) |
| Validate theory | Experiment (Ch 2-3) | - | Mixed methods study |

## Chapter Reference Guide

| Chapter | Topic | Primary Use |
|---------|-------|-------------|
| Ch 1 | Introduction to HCI Research | Research fundamentals |
| Ch 2 | Experimental Research | Causal relationships, controlled comparisons |
| Ch 3 | Experimental Design | Within/between/factorial designs |
| Ch 4 | Statistical Analysis | Hypothesis testing, effect sizes |
| Ch 5 | Surveys & Questionnaires | Large-scale data collection |
| Ch 6 | Diary Studies | Longitudinal in-situ data |
| Ch 7 | Case Studies | In-depth investigation |
| Ch 8 | Interviews & Focus Groups | User perspectives |
| Ch 9 | Field Studies & Ethnography | Naturalistic observation |
| Ch 10 | Usability Testing | Interface evaluation |
| Ch 11 | Qualitative Data Analysis | Coding and theming |
| Ch 12 | Automated Data Collection | Web analytics, A/B testing |
| Ch 13 | Sensors & Physiological | Eye tracking, GSR, EEG |
| Ch 14 | Online & Ubiquitous Research | Remote and mobile studies |
| Ch 15 | Working with Human Subjects | Ethics, IRB, consent |
| Ch 16 | Research with Disabilities | Inclusive design evaluation |
