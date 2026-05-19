# Chapter 4 Summary: Surveys and Questionnaires (Statistical Analysis)

## Main Topic

This chapter focuses on statistical analysis methods essential for processing and interpreting data collected through various HCI research methods. It provides a comprehensive guide to selecting appropriate statistical tests based on research design and data characteristics, emphasizing that correct method selection and accurate interpretation are critical for deriving valid conclusions from user studies.

## Key Concepts Introduced

- **Data Preparation Pipeline**: The chapter establishes a three-step preprocessing workflow — cleaning (identifying and correcting errors, handling missing values), coding (converting categorical data to numerical form for software processing), and organizing (structuring data according to the requirements of specific statistical procedures).

- **Descriptive Statistics**: Central tendency measures (mean, median, mode) and spread measures (range, variance, standard deviation) are introduced as foundational tools for understanding data distribution. The concept of normal distribution is highlighted as a critical factor in determining which statistical tests to apply.

- **Parametric vs. Nonparametric Tests**: A fundamental distinction is drawn between parametric tests (which assume normal distribution and interval-scaled data) and nonparametric tests (which relax these assumptions but sacrifice some statistical power by collapsing data into ranks).

- **Significance Testing Framework**: The chapter introduces the logic of null hypothesis testing, confidence intervals (typically 95%), and the interpretation of p-values as the probability that observed differences occurred by chance.

## Main Methods and Frameworks

The chapter presents a systematic framework for selecting statistical tests based on two dimensions: experimental design (between-group, within-group, or mixed) and the number of independent variables with their conditions.

**For Comparing Means (Parametric)**:
- **t Tests**: Independent-samples t test (between-group, 2 conditions) and paired-samples t test (within-group, 2 conditions), with distinction between one-tailed and two-tailed tests based on whether directional hypotheses exist.
- **One-Way ANOVA**: For between-group designs with one independent variable having 3+ conditions, returning an omnibus F value.
- **Factorial ANOVA**: For between-group designs with 2+ independent variables, enabling examination of main effects and interaction effects.
- **Repeated Measures ANOVA**: For within-group designs, available in one-level (single IV) and multi-level (multiple IVs) variants.
- **Split-Plot ANOVA**: For mixed designs combining between-group and within-group factors, offering benefits of reduced participant burden and controlled learning effects.

**For Identifying Relationships**:
- **Correlation Analysis**: Pearson's r (ranging from -1 to 1) measures linear relationships between two variables; r² represents shared variance proportion. The chapter strongly warns that correlation does not imply causation, illustrated through an income-performance example with age as an intervening variable.
- **Regression Analysis**: Simultaneous entry regression examines how independent variables collectively predict a dependent variable (via R²), while hierarchical regression enters variables sequentially based on theoretical models to assess individual contributions through R² change.

**For Nonparametric Situations**:
- **Chi-Squared Test**: Analyzes frequency counts in contingency tables for categorical data, requiring independent data points and sample size ≥ 20.
- **Mann-Whitney U Test**: Nonparametric alternative to independent-samples t test for comparing two independent groups.
- **Wilcoxon Signed-Rank Test**: Nonparametric alternative to paired-samples t test for comparing two dependent groups.
- **Kruskal-Wallis Test**: Nonparametric alternative to one-way ANOVA for 3+ independent groups.
- **Friedman's Test**: Nonparametric alternative to repeated measures ANOVA for 3+ dependent conditions.

## Important Takeaways

1. **Data quality is paramount**: Thorough data cleaning, consistent coding, and proper organization must precede any statistical analysis; errors at this stage can render even sophisticated analyses meaningless.

2. **Test selection follows from design**: The choice of statistical test is determined by the experimental design (between/within/mixed), the number of independent variables, and the number of conditions per variable — the chapter's summary table (Table 4.3) provides an invaluable decision guide.

3. **Three assumptions govern parametric tests**: Independence of errors, homogeneity of variance, and normal distribution must all be verified; violation of these assumptions necessitates data transformation or switching to nonparametric alternatives.

4. **Correlation ≠ causation**: Researchers must resist the temptation to claim causal relationships from correlational findings; hidden intervening variables may explain observed associations, and analyses should be hypothesis-driven rather than data-driven.

5. **Nonparametric tests trade power for flexibility**: While they have less strict data requirements, they collapse data into ranks, losing interval information — they should be used only when parametric assumptions are genuinely violated, not as a default safer option.

6. **Proper reporting requires context**: Statistical results must be reported with degrees of freedom, effect sizes, and significance levels (e.g., t(15) = 2.169, p < 0.05) to enable proper evaluation and replication.
