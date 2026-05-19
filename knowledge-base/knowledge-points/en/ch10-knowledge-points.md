# Chapter 10: Usability Testing — Knowledge Points

## 1. Core Concept Definitions

**Usability Testing** involves representative users attempting representative tasks in representative environments on early prototypes or working versions of computer interfaces. The basic goal is to improve interface quality by finding flaws—areas of the interface that are confusing, misleading, or generally suboptimal based on collected data. Usability testing ranges from hundreds of users with strict controls to a researcher watching three users and taking notes.

**Representative Users** are participants who accurately represent the target user population for an interface. Common criteria for determining representativeness include age, gender, education, job responsibility, domain expertise, technical experience, and experience with specific software or hardware. Using inappropriate participants (e.g., business students for a hospital nursing interface) is both inappropriate and potentially unethical.

**Representative Tasks** are activities that reflect the key features and goals of the interface being tested. Tasks should be clear, unambiguous, have one clear solution, and relate to key interface features. Tasks should not be questions users could answer without using the interface.

**Interface Flaw** is an aspect, component, or widget of the interface that is confusing, misleading, or generally suboptimal. This is distinct from stylistic preferences—a usability problem exists when design elements cause problems for a majority of users, not when someone simply prefers a different color.

**Formative Testing** is usability testing that takes place early in development, testing early design concepts using paper prototypes or wireframes (low-fidelity prototypes). It is more informal, involves more communication between moderators and participants, and focuses on qualitative feedback and problem discovery.

**Summative Testing** is usability testing conducted when more formal, high-fidelity prototypes are available. It evaluates the effectiveness of specific design choices and focuses more on task-level measurements, metrics, and quantitative data.

**Validation Testing** takes place right before an interface is released, comparing it to benchmarks for other interfaces to ensure performance targets are met (e.g., 90% of users can complete each task within 1 minute).

**Paper Prototypes** are low-fidelity prototypes made of paper that represent screen layouts. They are low cost, allow multiple designs to be quickly presented, and users feel more comfortable criticizing them since little development work has been invested.

**Wizard of Oz** is a method where users perceive they are interacting with an actual system, but a human "wizard" behind the scenes provides responses. Used when functionality has not been built due to cost, when technology doesn't exist yet, or for testing concepts prior to development.

**Technology Probes** are technologies installed in real-world settings to collect information about people, evaluate new technology, and inspire new design ideas. Unlike cultural probes, technology probes focus on what can be learned about users rather than the probe itself.

**Usability Inspection** refers to expert-based or automated methods for finding interface flaws without involving users. Includes heuristic reviews, consistency inspections, cognitive walkthroughs, and guidelines reviews.

**Heuristic Review** is an expert inspection method where interface experts compare a set of heuristics (rules of thumb, typically no more than 10) against an interface. Shneiderman's 8 Golden Rules of Interface Design is a well-known example.

**Cognitive Walkthrough** is an expert review where interface experts simulate users and "walk through" a series of tasks. It provides understanding of how users might interact with an interface the first time they use it.

**Think Aloud Protocol** is a usability testing technique where users verbalize their thoughts, feelings, frustrations, and progress as they navigate the interface. This qualitative data is more common in formative testing than summative testing.

**Intervention** occurs when a moderator helps a stuck participant move forward by providing advice or suggesting an action. Researchers should decide in advance whether interventions will be allowed, under what circumstances, and how they will be documented.

**Reflection Session** (also called interpretation or retrospective session) is a post-task activity where users watch raw video of themselves and work with evaluators to interpret problems encountered and identify major interface flaws.

**A/B Testing** involves making minor tweaks to interfaces already in daily use, where different users receive slightly different versions, with data collected about usage patterns to determine which changes are most effective.

## 2. Theoretical Frameworks

**Engineering vs. Research Paradigm**: Wixon argues that usability testing has more in common with engineering than traditional research. Like engineering, usability testing aims to build a successful product in the shortest time with fewest resources and fewest risks while optimizing trade-offs. Schedule and resource issues, rather than methodological theory, drive the development process. This paradigm accepts practices like modifying interfaces after every user test—unacceptable in experimental design but standard in usability engineering.

**Usability as Competitive Advantage**: Usability testing is primarily an industrial approach to improving interfaces. The practical goal of impacting the financial bottom line means companies often treat usability findings as confidential competitive advantages. This contrasts with academic research where findings are published for general benefit.

**Iterative Design Cycle**: Usability testing operates within an iterative cycle where findings from each test session feed directly into interface modifications, which are then evaluated in subsequent sessions. This contrasts with experimental design where all participants must receive identical treatment. The iterative cycle can begin as early as paper prototypes, when changes are cheapest and have the greatest potential impact.

**Formative-Summative Continuum**: The testing approach exists on a spectrum from early qualitative formative testing to later quantitative summative testing. Earlier testing focuses on design direction and problem discovery; later testing focuses on metrics and benchmarks. The position on this continuum determines whether qualitative observation or quantitative measurement is prioritized.

**Triangulation of Methods**: Usability testing borrows methods from multiple research traditions: experimental design (task/time performance metrics), ethnography (observation and contextual understanding), survey research (user satisfaction measurement), and automated data collection (key logging, clickstream analysis). The practical combination of these methods serves the goal of comprehensive interface improvement.

**Practical Sufficiency**: The concept that not all discovered flaws will or need to be fixed. The goal should be finding major flaws that cause the most problems, not exhaustively cataloging every issue. From an industry perspective, finding flaws without the capacity to fix them provides no value. Time must be balanced between finding and fixing flaws.

## 3. Methodology Steps

### Step 1: Develop the Test Plan

Determine the goals of the usability test, what stage of development the interface is in, and what type of test (formative, summative, or validation) is most appropriate. Consider budget, timeline, and available resources. Decide what methods will be used and what data will be collected.

### Step 2: Select and Recruit Representative Users

Identify who the typical users are based on user personas and task scenarios. Use criteria such as age, gender, education, job responsibility, domain expertise, and technical experience. Recruitment methods are more flexible than in experimental design—samples of convenience are appropriate. Users expect payment for participation.

### Step 3: Prepare Test Materials

Create the task list with clear, unambiguous tasks that have clear solutions. Prepare test accounts and dummy identities so users don't need to use personal data. Set up recording equipment and configure the test environment. Prepare informed consent forms and any confidentiality agreements.

### Step 4: Choose the Testing Location

Options include:
- **Fixed usability laboratory**: Two-room setup with one-way mirror, recording equipment, and separate moderator area
- **User's workplace or home**: More natural setting, easier recruitment, but more challenging for moderators to manage data collection
- **Remote testing**: Users separated from evaluators by space, time, or both; works better for summative than formative testing
- **Mobile research lab**: Google's research van example—equipped like standard usability labs but driven to diverse locations

### Step 5: Conduct Test Sessions

Before the session: confirm participant attendance, verify all equipment is working, obtain informed consent, and clarify time constraints. During the session: remind participants they are testing the interface, not being tested. Collect both quantitative metrics (task performance, time performance) and qualitative data (think-aloud comments, moderator observations, facial expressions). Decide in advance whether interventions are allowed. Note that the more participants talk, the more their task times are affected.

### Step 6: Debrief Participants

After testing, conduct debriefing to gather additional feedback. Consider reflection/interpretation sessions where users watch video of themselves and help interpret problems. Ensure participants are paid regardless of whether they completed all tasks.

### Step 7: Analyze Data and Report Findings

Use descriptive statistics (inferential statistics may not be possible with small samples). Prioritize discovered flaws by severity and impact. For each flaw, describe the problem, present data, identify priority, suggest a fix, and estimate fix time. Split reports into: why you did testing, what happened, and implications/recommendations. Keep reports short and oriented toward developers and managers. Never include identifying information about participants.

## 4. Decision Criteria

**When to Use Usability Testing**: Use when you have an interface (or prototype) to evaluate and need to find and fix specific flaws. It is most effective when started early in development when changes are cheapest. Different from ethnography (which seeks to understand problems) and experimental design (which seeks generalizable knowledge).

**Usability Testing vs. Experimental Design**: Usability testing shares methods with experimental design (metrics, measurement) but differs in goals. Experimental design seeks generalizable knowledge with strict controls; usability testing seeks to improve specific interfaces with practical flexibility. Usability testing accepts small samples, interface modification during testing, and samples of convenience.

**Usability Testing vs. Usability Inspection**: Expert-based inspections (heuristic review, consistency inspection, cognitive walkthrough, guidelines review) should precede user-based testing. Experts find obvious interface flaws first, allowing users to focus on deeper, task-related flaws that experts cannot identify. Automated testing works for guideline compliance checking but cannot assess wording quality or layout appropriateness.

**Choosing Test Type**:
- **Formative**: Early development, paper prototypes/wireframes, qualitative focus, informal, more moderator-participant interaction
- **Summative**: Later development, high-fidelity prototypes, quantitative focus, formal, evaluates specific design choices
- **Validation**: Pre-release, benchmark comparison, ensures performance targets are met

**Number of Participants**: The "five users finds 80% of problems" rule is debated. Practical recommendations range from 3.2 users (best benefit-to-cost ratio) to 10±2 users. The actual number depends on project size, problem discovery goals, available participants, and budget. Multiple user groups may each need their own set of participants.

**Location Decision**: Consider participant comfort, data quality needs, and logistical constraints. Fixed labs provide controlled environments with rich data capture. User environments provide naturalistic settings. Remote testing reaches geographically distributed participants but loses nonverbal cues. Choose based on what location is available, where participants are, and what data type is needed.

**Intervention Policy**: Decide in advance whether moderators will help stuck participants. Interventions allow more interface feedback but must be documented and accounted for in results. Generally discouraged, but useful when early interface barriers prevent access to later features.

**Use of Personal Data**: Generally avoid using participants' real financial, health, or contact information in tasks. Create test accounts and dummy identities. Using real data provides more realistic testing but raises privacy concerns, may cause participant dropout, and could be rejected by IRB. Some legal contexts (e.g., government emergency systems) prohibit even test data submission.

## 5. Book Cases and Examples

**Airline Check-in Interface (Figure 10.1)**: An airline website's online check-in page where the large yellow arrow appears to continue to the next screen but actually upgrades the seat to "economy plus." The non-upgrade option is a small text link on the left. This demonstrates how a minor flaw (misleading visual hierarchy) causes major usability problems.

**Kodak Website Testing**: Both formative and summative testing were conducted. Formative testing used 20 participants with 30 tasks on a paper prototype of the home page—participants identified which links would lead to desired content and rated label-content match quality. Summative testing with 33 participants used a working prototype with 22 tasks (each participant completed 10). Task completion ranged from 100% to 9% in 3 minutes. Results led to removing left-side images, adding longer link descriptors, and labeling major information chunks.

**Fidelity Investments Benefits Interface**: 27 participants tested the first prototype of a benefits management interface with 15 tasks. Task success rates were 64.2% (under 55) and 44.8% (55 and older). After improvements to terminology, link consistency, instructions, and navigation, a second round with 22 new participants showed success rates improved to 80.6% and 58.2% respectively. This demonstrates iterative testing and improvement.

**Leescircus Educational Software**: 70 Dutch children aged 6-7 tested educational software using think-aloud protocol. Four sets of 8-9 tasks were used (each child performed one set). Sessions were limited to 30 minutes due to children's attention spans. Only 28 children spoke aloud, with novices making more comments than experts. Findings included the need to enlarge clickable objects, clarify icon meanings, and improve consistency.

**Yahoo User Nights**: Up to 100 external users are paired individually with product team members for one-hour sessions. Teams are briefed with detailed scripts and coaching. Events are held evenings to encourage participation, with food provided to relax nervous participants. After sessions, all team members conduct debriefing to discuss findings. Reports are created and shared with the entire product team. This innovative approach enables rapid, larger-scale feedback than traditional five-user studies.

**Google Research Van**: A mobile usability lab equipped with audio/video recording, multiple camera angles, HDMI screen capture, and seating for moderator, participant, note taker, and two stakeholders. A 6-week cross-country tour visited 10 cities, reaching over 300 in-van study participants and 500+ video interview/survey participants. The van addressed participant diversity concerns by reaching people unwilling or unable to travel to fixed labs.

**Automated Usability Testing Tools**: Standalone applications (Deque WorldSpace, Cryptzone ComplianceSherriff, SSB Accessibility Management Platform) and free web-based tools (A-Checker, WAVE, Functional Accessibility Evaluator) check interfaces for WCAG 2.0 compliance. These tools can quickly examine large numbers of pages and provide high-level overviews, but cannot assess whether alternative text is clear and useful—only whether it exists.

**Shneiderman's 8 Golden Rules**: Strive for consistency, cater to universal usability, offer informative feedback, design dialogs to yield closure, prevent errors, permit easy reversal of actions, support internal locus of control, and reduce short-term memory load. These serve as a widely used heuristic set for expert reviews.

## 6. Common Errors and Pitfalls

**Confusing Usability Testing with Research**: Usability testing has different goals than traditional research. It seeks to improve specific interfaces, not generate generalizable knowledge. Applying experimental design requirements (strict controls, large samples, no interface modification during testing) can make usability testing impractical and discourage organizations from doing it at all.

**Using Non-Representative Participants**: Testing with whoever is available (e.g., undergraduate business students for a nursing interface) produces misleading results. Participants must match the target user population in relevant characteristics. Convenience sampling is acceptable but only within the appropriate user population.

**Creating Poor Task Lists**: Tasks that are too vague, require knowledge users already have (without using the interface), have multiple valid solutions, or don't relate to key interface features will produce unhelpful data. Tasks must be clear, goal-directed, and require interface use.

**Testing Too Late**: Waiting until the interface is nearly complete before testing means changes are expensive and major design flaws may be impossible to fix. Start testing as early as paper prototypes when changes are cheapest and have the greatest potential impact.

**Not Using Expert Reviews First**: Skipping expert-based testing means users will be distracted by obvious interface flaws (confusing wording, inconsistent layouts) and may be unable to help identify deeper, task-related problems. Expert reviews should always precede user-based testing.

**Over-reliance on "Five Users" Rule**: The commonly cited "five users find 80% of problems" is debated and may be insufficient. The appropriate number depends on project size, complexity, number of user groups, and problem discovery goals. Insufficient participants may miss important flaws.

**Ignoring Qualitative Data in Summative Testing**: Focusing exclusively on quantitative metrics (task completion, time) misses valuable insights from user comments, observations, and facial expressions. Even in summative testing, moderator observations about user behavior provide important context for interpreting quantitative results.

**Failing to Distinguish Testing from Being Tested**: Participants must be explicitly told that they are testing the interface, not being tested. This reduces anxiety, encourages honest feedback, and increases willingness to criticize the interface. Reminder may be needed multiple times during a session.

**Not Prioritizing Discovered Flaws**: Presenting a long list of all discovered flaws without prioritization overwhelms developers and may result in no fixes at all. Reports should prioritize flaws by severity, impact, and fix difficulty, focusing attention on the most critical issues.

**Using Participants' Real Personal Data**: Asking users to provide their own financial, health, or contact information raises privacy concerns, may cause dropout, and could be rejected by IRB review. Always prepare test accounts and dummy identities in advance.

**Over-moderating Think-Aloud Sessions**: Interrupting participants too frequently to prompt them to speak makes them feel watched, breaks cognitive flow, and causes behavior to deviate from normal. Allow natural pauses and use gentle prompts only when necessary.

**Neglecting to Document Interventions**: When moderators help stuck participants, the intervention circumstances, content, and impact on data must be clearly documented. Undocumented interventions compromise the validity of results and make it impossible to accurately interpret findings.

**Identifying Participants in Reports**: Including names or identifying information about participants violates confidentiality. Even combinations of age, gender, and job title can identify individuals in small organizations. Use participant numbers and aggregate demographics only.
