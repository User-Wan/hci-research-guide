# Chapter 2: Research Ethics and Regulation - Knowledge Points

## 1. Core Concept Definitions

### Experimental Research
Experimental research allows the identification of causal relationships between entities or events. Unlike descriptive investigations (observations, surveys, focus groups) that describe what is happening, and relational investigations that identify relationships between factors, experimental research can determine causality. This is achieved through controlled conditions where researchers can manipulate independent variables while keeping other factors constant.

### Research Hypothesis
A hypothesis is a precise problem statement that can be directly tested through empirical investigation. Compared to a theory, a hypothesis is a smaller, more focused statement that can be examined by a single experiment. A theory covers a larger scope and requires a sequence of empirical studies. For example, Fitts' law is a theory that has been validated through hundreds of user studies, each testing specific hypotheses about different pointing devices and tasks.

### Null Hypothesis (H₀)
The null hypothesis typically states that there is no difference between experimental treatments. For example: "There is no difference between the pull-down menu and the pop-up menu in the time spent locating pages." The goal of an experiment is to find statistical evidence to refute or nullify the null hypothesis in order to support the alternative hypothesis.

### Alternative Hypothesis (H₁)
The alternative hypothesis is always a statement that is mutually exclusive with the null hypothesis. For example: "There is a difference between the pull-down menu and the pop-up menu in the time spent locating pages." If the null hypothesis is true, the alternative hypothesis must be false, and vice versa.

### Independent Variables
Independent variables refer to factors that researchers are interested in studying or the possible "cause" of changes in dependent variables. The term "independent" suggests that the variable is independent of participant behavior. Independent variables are usually treatments or conditions that researchers can control. In HCI, typical independent variables include different types of technology/devices, different types of design, user characteristics (age, gender, experience), and context of use.

### Dependent Variables
Dependent variables refer to outcomes or effects that researchers are interested in. The term "dependent" suggests that the variable is dependent on participant behavior or changes in independent variables. Dependent variables are usually outcomes that researchers need to measure. In HCI, frequently measured dependent variables include efficiency (task completion time), accuracy (error rates), subjective satisfaction, ease of learning and retention rate, and physical/cognitive demand.

### Treatments
Treatments, or conditions, refer to the different techniques, devices, or procedures that researchers want to compare in an experiment. For example, in a keyboard comparison experiment, the treatments would be QWERTY keyboard versus DVORAK keyboard.

### Units
Units are the objects to which experiment treatments are applied. In HCI research, units are normally human subjects with specific characteristics such as gender, age, or computing experience.

### Assignment Method
Assignment method refers to the way in which experimental units are assigned different treatments. This should be done through randomization to ensure fair comparison and control for hidden factors.

### Randomization
Randomization refers to the random assignment of treatments to experimental units or participants. In a totally randomized experiment, no one can predict the condition to which a participant will be assigned. Traditional methods include tossing coins, throwing dice, or drawing capsules from urns. Modern methods include random digit tables and software-driven randomization.

### Counterbalancing
Counterbalancing is commonly used to address systematic differences between successive conditions. Researchers rotate sequences of treatments using a Latin Square Design, where each condition appears only once in each row and column, ensuring order is completely counterbalanced across participants.

### Type I Error (α Error)
A Type I error, also called an α error or "false positive," refers to the mistake of rejecting the null hypothesis when it is true and should not be rejected. In the judicial analogy, this is convicting an innocent person. Statistically, Type I errors are considered worse than Type II errors, so the alpha threshold is kept low (typically 0.05).

### Type II Error (β Error)
A Type II error, also called a β error or "false negative," refers to the mistake of not rejecting the null hypothesis when it is false and should be rejected. In the judicial analogy, this is acquitting a guilty person. Type II errors involve "blindness" and cost opportunities to improve current states.

### Significance Level (P Value)
The probability of making a Type I error is called alpha or significance level. A significance test returning P < 0.05 means the probability of mistakenly rejecting the null hypothesis is below 0.05. This widely adopted threshold controls the occurrence of Type I errors.

### Statistical Power
Statistical power is defined as 1 − β, referring to the probability of successfully rejecting a null hypothesis when it is false and should be rejected. To reduce Type II errors, researchers should use relatively large sample sizes so differences can be observed even when effect sizes are small.

### Confounding Variables
Confounding variables are factors other than independent variables that may impact dependent variables. These must be kept constant under different experiment conditions. When studying age differences, confounding factors include educational background, computer experience, frequency of use, and living conditions.

### Hawthorne Effect
The Hawthorne effect describes how participants may behave differently in lab-based experiments due to stress of being observed, different environments, or rewards for participation. This phenomenon was documented around 60 years ago and can cause short-term improvements that typically don't last once observation is over.

### Fitts' Law
Fitts' law states that in movement tasks, movement time increases as movement distance increases and target size decreases. Movement time has a log linear relationship with movement distance and target width. This theory has been validated through hundreds of studies on various pointing devices and tasks, including mouse, eye tracker, and finger touch input.

## 2. Theoretical Frameworks

### Three Types of Behavioral Research Framework
All empirical investigation methods can be categorized into three groups: (1) Descriptive investigations (observations, surveys, focus groups) that focus on constructing accurate descriptions of what is happening; (2) Relational investigations that enable identification of relations between multiple factors; (3) Experimental investigations that identify causes of situations or events. These three types are highly intertwined, with descriptive investigations often being the first step, relational investigations discovering connections, and experimental research providing fundamental causal relations.

### Hypothesis Testing Framework
This framework involves formulating null and alternative hypotheses, conducting experiments with proper randomization and control, collecting data, and using significance tests to determine whether observed differences are statistically significant. The framework emphasizes that hypotheses should be precise, testable within one experiment, and clearly state control groups or conditions.

### Variables Classification Framework
Variables in experiments are classified as independent variables (factors researchers can control or manipulate) and dependent variables (outcomes researchers need to measure). This framework helps researchers clearly define what they are studying (independent variables) and what effects they are measuring (dependent variables).

### Experimental Design Components Framework
Every experiment consists of three components: treatments (different techniques/devices/procedures to compare), units (objects to which treatments are applied, typically human subjects), and assignment method (how units are assigned treatments, ideally through randomization).

### Error Types Framework
All significance tests are subject to Type I errors (rejecting true null hypothesis, "gullibility") and Type II errors (not rejecting false null hypothesis, "blindness"). This framework helps researchers understand that Type I errors are generally considered worse, leading to the adoption of low alpha thresholds (0.05), while Type II errors can be reduced through larger sample sizes.

### Validity Concerns Framework
This framework addresses concerns about experimental validity in HCI, recognizing that controlling all possible factors is more difficult than in physics or chemistry. However, it maintains that experimental research and significance testing remain the only approach enabling judgments with systematically measured confidence and reliability.

### Research Method Selection Framework
Choosing research methods depends on factors including primary purpose of study, time constraints, funding, participant pool, and researcher experience. Each method has strengths and weaknesses: observation may be time-consuming but captures natural behavior; surveys reach many participants but may lack depth; interviews allow clarification but cost more time and money; usability tests identify key problems but cannot guarantee finding all critical issues.

## 3. Methodology Steps

### Step 1: Develop Research Hypotheses
Start with one or more good hypotheses that are presented in precise language, focused on testable problems, and clearly state control groups or conditions. Begin with exploratory descriptive investigations (observations, interviews, focus groups) to identify key research issues and appropriate control groups and dependent variables.

### Step 2: Identify Variables
Clearly identify independent variables (factors you can control) and dependent variables (outcomes you need to measure). Typical independent variables in HCI include technology types, design variations, user characteristics, and use context. Typical dependent variables include efficiency, accuracy, subjective satisfaction, learning ease/retention, and physical/cognitive demand.

### Step 3: Design Experiment Components
Define the three components: treatments (what you're comparing), units (who participates), and assignment method (how participants are assigned to conditions). Ensure treatments are clearly defined and units are appropriate for the research questions.

### Step 4: Implement Randomization
Use randomization methods to assign participants to conditions. Options include random digit tables (like the RAND Corporation's million random digits), software-driven randomization (available at randomization.com or in statistical packages like SAS, SPSS, SYSTAT), or traditional methods (coin tosses, dice). Randomize not only condition assignment but also other factors like scenario order in longitudinal studies.

### Step 5: Apply Counterbalancing When Needed
Use Latin Square Design when there are systematic differences between successive conditions. Each condition appears only once in each row and column, ensuring order effects are balanced across participants. This is particularly important in within-subject designs.

### Step 6: Control for Confounding Variables
Identify potential confounding variables and take steps to control them. During data collection, take extra caution with known confounding factors. Increase sample size to reduce confounding factor impact. Conduct prescreening to make participant groups as homogeneous as possible. When confounding factors are inevitable, use analysis of covariables to filter out their impact.

### Step 7: Collect Data
Run the experiment following the designed protocol. Ensure data collection is systematic and consistent across all conditions. Measure all defined dependent variables accurately and record data in a structured format suitable for analysis.

### Step 8: Conduct Significance Tests
Use appropriate significance tests (t-tests, ANOVA, etc.) to determine whether observed differences between groups are statistically significant. Interpret results in terms of Type I and Type II error probabilities. Report results with appropriate statistics (e.g., F(1,25) = 20.83, p < 0.01).

### Step 9: Interpret Results
Draw conclusions based on significance test results. If results are significant at P < 0.05, you can be 95% confident the test result correctly applies to the entire population. Consider both practical and statistical significance when interpreting findings.

### Step 10: Address Limitations
Acknowledge limitations including difficulty identifying testable hypotheses, controlling confounding factors, and the Hawthorne effect. Consider whether lab-based results represent real-world behavior and take precautions to minimize observation effects.

## 4. Decision Criteria

### When to Use Experimental Research
Use experimental research when you need to identify causal relationships between entities or events. This is appropriate when you can define clear hypotheses with controllable independent variables and measurable dependent variables, and when you can control confounding factors through randomization and experimental design.

### When to Use Descriptive Investigations
Use descriptive investigations (observations, surveys, focus groups, interviews) when you need to construct accurate descriptions of what is happening. These are appropriate as the first step in research programs to identify interesting phenomena, establish cornerstones, and identify future research directions.

### When to Use Relational Investigations
Use relational investigations when you need to identify relations between multiple factors. These are appropriate when you want to discover connections between events or variables, though they cannot establish causality. Correlation analysis can show relationships but cannot determine whether X causes Y, Y causes X, or hidden factors cause both.

### When to Use Between-Subject Designs
Use between-subject designs when you want different participants in each condition. This is appropriate when you're concerned about carryover effects or when participants cannot experience all conditions. Randomization assigns different participants to different treatments.

### When to Use Within-Subject Designs
Use within-subject designs when you want the same participants to experience all conditions. This requires counterbalancing (Latin Square Design) to address order effects. This design reduces participant variability but may introduce practice or fatigue effects.

### When to Set Alpha at 0.05
Set alpha at 0.05 when you want to control Type I errors at a 5% probability level. This widely adopted threshold balances the risk of false positives with the need to detect real effects. Lower alpha (e.g., 0.01) further reduces Type I error risk but increases Type II error risk.

### When to Use Large Sample Sizes
Use large sample sizes when you want to reduce Type II errors and detect smaller effect sizes. Statistical power increases with sample size, allowing you to observe differences even when effect sizes are relatively small. This is important when you expect small but meaningful differences between conditions.

### When to Conduct Prescreening
Conduct prescreening when you want to make participant groups as homogeneous as possible, reducing the impact of confounding variables. This is appropriate when studying specific populations (e.g., age groups) where factors like experience and background might confound results.

### When to Use Latin Square Design
Use Latin Square Design when you need to counterbalance order effects in within-subject experiments. This is appropriate when the order in which participants experience conditions might influence results, such as practice effects or fatigue.

### When to Consider the Hawthorne Effect
Consider the Hawthorne effect when participants know they're being observed, which might cause them to behave differently than in natural settings. This is particularly relevant in lab-based experiments where observation stress, different environments, or participation rewards might influence behavior.

### When to Combine Research Methods
Combine research methods when you need comprehensive understanding. Use descriptive investigations first to identify phenomena, relational investigations to discover connections, and experimental research to establish causality. Multiple methods provide triangulation and more complete understanding.

### When Experimental Research May Not Be Appropriate
Experimental research may not be appropriate when problems are not clearly defined, involve many potentially influential factors, or when studying innovative techniques or new user populations in early development stages. It's also less appropriate when strict control of confounding factors is impossible.

## 5. Book Cases and Examples

### Case 1: Mobile Phone Information Entry Research
The book presents a scenario where researchers studying how users enter information into mobile phones could choose multiple approaches: observing users in natural settings (company lobby, airport, park), developing surveys, interviewing users, running usability tests in labs, or conducting controlled experiments. Each method has strengths and weaknesses regarding time, depth of understanding, and participant bias.

### Case 2: Computer Game and Typing Speed
The book uses an example of observing that 8 out of 10 teenagers who frequently play a specific computer game can touch type while only 2 out of 12 who don't play can touch type. This descriptive observation raises questions but doesn't establish relationships. A relational investigation could correlate game hours with typing speed, but only experimental research (randomly assigning teenagers to play or not play for 3 months) can determine causality.

### Case 3: Menu Design Comparison
The book describes a research case where website developers want to determine whether to use pull-down or pop-up menus. Hypotheses are formulated: H₀ states no difference in time spent locating pages; H₁ states there is a difference. Additional hypotheses examine user satisfaction ratings. This illustrates how experiments can address practical design decisions.

### Case 4: QWERTY vs. DVORAK Keyboard Experiment
The book uses a keyboard comparison example to illustrate experiment components. Treatment is keyboard type (QWERTY or DVORAK), units are participants (who must have no previous experience with either keyboard), and assignment method is randomization (coin toss). This simple between-subject design with two conditions demonstrates the three fundamental experiment components.

### Case 5: Fitts' Law Validation Studies
The book describes how Fitts' law, a general theory about movement time, distance, and target size, has been validated through hundreds of specific hypotheses. Miniotas (2000) examined hypotheses about mouse vs. eye tracker performance. Accot and Zhai (2003) investigated Fitts' law with 2D targets. Bi et al. (2013) developed FFitts law for finger touch input. Each study tested focused hypotheses within the broader theory.

### Case 6: Randomization in Longitudinal Study
The book describes a longitudinal study by Feng et al. (2005) investigating recognition software for text documents. Fifteen participants completed nine tasks on different days, each composing ~500-word documents responding to predefined scenarios. Researchers randomized scenario order to cancel out potential errors from scenario differences.

### Case 7: ATM Touch-Screen vs. Buttons Evaluation
The book presents a case where a bank hires HCI researchers to evaluate whether touch-screen ATMs are easier to use than button ATMs. H₀ states no difference in ease of use; H₁ states touch-screen ATMs are easier. Type I error would mean deciding touch-screens are better when they're not (bank wastes money switching). Type II error would mean deciding they're no better when they are (bank misses improvement opportunity).

### Case 8: Judicial Analogy for Type I/II Errors
The book uses the US justice system to illustrate error types: defendant presumed innocent (H₀: innocent, H₁: guilty). Type I error: convicting innocent person (rejecting true null). Type II error: acquitting guilty person (not rejecting false null). Each error has costs: Type I sends innocent to prison; Type II frees criminal who may reoffend.

### Case 9: Hawthorne Effect Considerations
The book discusses the Hawthorne effect documented 60 years ago, where participants behave differently when observed. However, it notes significant differences from HCI experiments: Hawthorne studies were longitudinal (most HCI aren't), observed expert users (HCI typically studies novices), focused on efficiency (HCI values error rates and other measures), and participants had vested interest in outcomes (HCI participants typically don't).

### Case 10: Validity of HCI Experiments
The book addresses concerns about experimental validity in HCI compared to physics/chemistry. While controlling all factors is harder in HCI, experimental research and significance testing remain the only approach enabling judgments with systematically measured confidence. The book acknowledges limitations but maintains overall validity is well-grounded.

### Case 11: Significance Test Reporting
The book provides examples of how significance tests are reported in HCI literature: "participants performed significantly better (F(1,25) = 20.83, p < 0.01)" and "A t test showed significant difference (t(11) = 6.28, p < 0.001)." These examples illustrate standard reporting formats for experimental results.

### Case 12: Spam Filter Threshold Example
The book presents a spam filter scenario for discussion: filter assigns ratings 1-10 to emails, deleting those above threshold. Type I error: deleting legitimate email (rejecting true null that email isn't spam). Type II error: letting spam through (not rejecting false null). Threshold setting involves trade-offs between these error types.

## 6. Common Errors and Pitfalls

### Error 1: Confusing Correlation with Causation
A significant correlation between two factors does not establish causation. Playing a computer game might correlate with typing speed, but the relationship could be reversed (good typists like the game) or caused by hidden factors (good readers type faster and like the game). Only experimental research with randomization can establish causality.

### Error 2: Inappropriate Sampling
Using small or non-representative samples can lead to misleading conclusions. The book's height example shows how comparing averages of three males and three females might incorrectly suggest females are taller. Randomization and large sample sizes reduce this possibility.

### Error 3: Confusing Theory with Hypothesis
A theory (like Fitts' law) covers large scope and requires many studies to validate. A hypothesis is a focused, testable statement for single experiments. Researchers should formulate specific hypotheses within broader theoretical frameworks, not attempt to validate entire theories in single studies.

### Error 4: Poor Hypothesis Formulation
Bad hypotheses are vague, overly broad, or don't clearly state control groups. Good hypotheses are presented in precise language, focused on testable problems, and clearly state control groups or conditions. Starting with exploratory descriptive investigations helps identify appropriate hypotheses.

### Error 5: Not Randomizing All Factors
Researchers may randomize condition assignment but forget to randomize other factors like scenario order. In longitudinal studies, non-randomized scenario order can introduce systematic errors. All factors that might influence results should be randomized.

### Error 6: Ignoring Counterbalancing Needs
In within-subject designs, not using counterbalancing (Latin Square Design) can introduce order effects. Practice effects, fatigue effects, or other systematic differences between successive conditions can bias results. Counterbalancing ensures order effects are balanced across participants.

### Error 7: Inadequate Control of Confounding Variables
Failing to control confounding variables can invalidate results. When studying age differences, factors like education, experience, frequency of use, and living conditions must be controlled. Prescreening participants and using analysis of covariables can reduce confounding factor impact.

### Error 8: Setting Alpha Too High
Setting alpha above 0.05 increases Type I error risk. Since Type I errors are generally considered worse than Type II errors, the widely accepted threshold is 0.05. Higher thresholds increase the probability of false positives (concluding effects exist when they don't).

### Error 9: Insufficient Sample Size
Small sample sizes increase Type II error risk and reduce statistical power. With small samples, real effects may not be detected, especially when effect sizes are small. Larger samples increase the ability to observe true differences.

### Error 10: Ignoring the Hawthorne Effect
Not considering that participants may behave differently when observed can lead to results that don't represent real-world behavior. While the Hawthorne effect's impact in HCI may be smaller than in original studies (due to differences in study design, participant expertise, and motivation), researchers should still take precautions to minimize observation effects.

### Error 11: Over-Reliance on Single Methods
Using only experimental research without preliminary descriptive or relational investigations can lead to testing poorly formulated hypotheses. Descriptive investigations help identify phenomena, relational investigations discover connections, and experimental research establishes causality. Using all three types provides more complete understanding.

### Error 12: Assuming Lab Results Transfer to Real World
Lab-based experiments may not represent users' typical interaction behavior due to observation stress, different environments, or participation rewards. Researchers should consider whether findings from controlled settings will apply in real-world contexts and may need to conduct field studies to validate lab findings.

### Error 13: Not Addressing Limitations
Failing to acknowledge limitations like difficulty identifying testable hypotheses, controlling confounding factors, or the Hawthorne effect weakens research credibility. All research methods have limitations, and experimental research in HCI has specific challenges compared to traditional scientific fields.

### Error 14: Poor Variable Definition
Not clearly defining independent and dependent variables makes it difficult to design experiments, collect data, and interpret results. Independent variables should be factors researchers can control; dependent variables should be measurable outcomes. Clear variable definition is essential for successful experiments.

### Error 15: Testing Too Many Hypotheses
While there's no limit on hypotheses in one experiment, testing too many increases complexity and risk of design flaws. More hypotheses mean more factors to control and more variables to measure, resulting in complicated experiments. Researchers should focus on manageable numbers of well-defined hypotheses.