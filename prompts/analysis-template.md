# Research Analysis Planning Template

Use this template to plan the data analysis approach for HCI research studies.

## Analysis Plan Structure

### 1. Research Questions Mapping

| Research Question | Data Source | Variable Type | Analysis Method |
|-------------------|------------|---------------|-----------------|
| RQ1: [question] | [source] | IV: [type], DV: [type] | [method] |
| RQ2: [question] | [source] | IV: [type], DV: [type] | [method] |

### 2. Variable Identification

**Independent Variables (IV):**
- Name: [variable name]
- Type: Categorical / Continuous
- Levels: [list levels if categorical]
- Measurement: [how measured]

**Dependent Variables (DV):**
- Name: [variable name]
- Type: Categorical / Continuous / Ordinal
- Scale: [measurement scale]
- Expected distribution: [normal / skewed / etc.]

**Control Variables:**
- [List variables to control for]

**Covariates:**
- [List potential covariates]

### 3. Statistical Method Selection (Ch 13)

#### For Comparing Groups:
| Condition | Parametric | Non-parametric |
|-----------|-----------|----------------|
| 2 independent groups | Independent t-test | Mann-Whitney U |
| 2 paired groups | Paired t-test | Wilcoxon signed-rank |
| 3+ independent groups | One-way ANOVA | Kruskal-Wallis |
| 3+ paired groups | Repeated measures ANOVA | Friedman test |

#### For Relationships:
| Condition | Method |
|-----------|--------|
| 2 continuous variables | Pearson/Spearman correlation |
| Predict continuous from categorical | Regression (linear) |
| Predict categorical from continuous | Logistic regression |
| Multiple predictors | Multiple regression |

#### For Categorical Data:
| Condition | Method |
|-----------|--------|
| 2 categorical variables | Chi-square test |
| Small sample categorical | Fisher's exact test |

### 4. Sample Size Justification

```
Effect size: [small / medium / large]
Alpha level: [typically 0.05]
Power: [typically 0.80]
Required N: [calculated value]
Tool used: [G*Power / online calculator]
Reference: [power analysis source]
```

### 5. Qualitative Analysis Plan (if applicable)

**Approach:** [Thematic Analysis / Content Analysis / Grounded Theory / Framework Analysis]

**Coding Strategy:**
1. Open coding — Identify initial codes
2. Axial coding — Group codes into categories
3. Selective coding — Identify themes

**Reliability Measures:**
- [ ] Inter-coder agreement planned
- [ ] Codebook developed
- [ ] Pilot coding conducted

### 6. Data Visualization Plan

| Finding Type | Visualization | Tool |
|-------------|---------------|------|
| Group comparisons | Bar chart with error bars | [tool] |
| Distributions | Box plot / violin plot | [tool] |
| Relationships | Scatter plot | [tool] |
| Time series | Line chart | [tool] |
| Qualitative themes | Thematic map | [tool] |

### 7. Reporting Checklist

- [ ] Descriptive statistics reported first
- [ ] Effect sizes reported (not just p-values)
- [ ] Confidence intervals included
- [ ] Assumptions checked and reported
- [ ] Missing data handled and described
- [ ] Multiple comparisons corrected (if applicable)
- [ ] Visualizations support text descriptions
- [ ] Limitations acknowledged

## Template: Experiment Results Table

```markdown
| Measure | Condition A (M, SD) | Condition B (M, SD) | Test Statistic | p-value | Effect Size (d) | 95% CI |
|---------|--------------------|--------------------|----------------|---------|-----------------|--------|
| [DV1] | M=X.XX, SD=X.XX | M=X.XX, SD=X.XX | t(df)=X.XX | p=.XXX | d=X.XX | [X.XX, X.XX] |
| [DV2] | M=X.XX, SD=X.XX | M=X.XX, SD=X.XX | t(df)=X.XX | p=.XXX | d=X.XX | [X.XX, X.XX] |
```

## Template: Usability Metrics Summary

```markdown
| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Task Success Rate | XX% | >85% | ✅/⚠️/❌ |
| Average Task Time | XXs | <[target] | ✅/⚠️/❌ |
| Error Rate | XX% | <5% | ✅/⚠️/❌ |
| SUS Score | XX | >68 (average) | ✅/⚠️/❌ |
| Satisfaction (1-5) | X.X | >4.0 | ✅/⚠️/❌ |
```
