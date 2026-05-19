# Chapter 13: Statistical Analysis

Chapter 13

Measuring the human

## Abstract

Although fingers and hands working keyboards, touchscreens, and mice may be the primary means of measuring human activity for human-computer interaction (HCI) studies, researchers have successfully used a variety of other sensors to act as input devices and to measurements of human responses. Eye-tracking tools are capable of measuring user attention and workload, as well as for acting as input devices, particularly with virtual reality and mobile devices. Sensors measuring body position and motion can be used both in games and to measure activity during tasks involving motion. Physiological measurements of skin conductance, heart rate, respiration, and even brain activity can provide insight into cognitive and emotional responses to computer tasks. Challenges in using such data include calibration and use of complex devices and interpretation of potentially overwhelming amounts of raw data which must often be mapped to screen contents and records of task completion activity.

Keywords

Eye tracking; Motion and position tracking; Physiological measurements; Data capture; Analysis

## 13.1 Introduction

As the study of human-computer interaction (HCI) is all about understanding how users interact with computer and information systems, it is obvious that participation of those users is vital to our research. Previous chapters have outlined how we might involve participants in surveys, case studies, interviews, usability studies, and empirical studies, leading to both quantitative and qualitative data that provide vital insights. However, these chapters barely scratch the surface of the rich and varied data that human participants can provide for research studies.

This chapter broadens the focus, describing the numerous ways that the bodies of research participants can act as data-generating devices, providing us with measures of attention, emotional response, and brain activity. A wide variety of physical and emotional measurements can help us gain significant insight into the way that users work with our interfaces. Although we always, of course, strive to treat participants with the respect and dignity that they deserve (Chapter 15), they can also be treasure troves of detailed information that may otherwise be hard—if not impossible—to acquire. This makes familiarity with human data collection an important skill for any HCI researcher.

Automated human data collection techniques cover a range of complexity, cost, and invasiveness. Some of the simplest techniques involve data from familiar input devices, such as mice and keyboards. These familiar tools can help us understand how people navigate in graphical environments and provide textual input. More complicated approaches include eye-tracking tools for studying patterns in eye movements, galvanic skin response, and blood-volume and heart-rate measurements for the study of physical and emotional responses. At the high end, functional magnetic resonance imaging (fMRI) tools can be used to examine how different parts of the brain react and interact in various circumstances.

Although many of these techniques involve expensive equipment and may require training that is beyond the reach of many HCI researchers, they present intriguing possibilities for gaining understanding that would otherwise be elusive. Eye-tracking tools that tell us where people are looking on a screen can help us understand visual processes involved in navigating lists of options. Skin response or cardiovascular monitors can provide insight into a user's level of arousal or frustration. The rich, detailed information about user activities and responses provided by these tools can help extend our understanding of human use of computer interfaces.

This chapter discusses a variety of options, with an eye toward cost-benefit trade-offs: as some tools are clearly more difficult and expensive than others, we strive to use the simplest and least expensive tools suitable for a given job.

## 13.2 Eye Tracking

### 13.2.1 Background

Countless traditional HCI studies used—and continue to use—measurements of mouse or keyboard interactions in an attempt to see how users control computers. This approach can be very useful, but it paints a necessarily incomplete picture, as simply knowing which keys were pressed and where the mouse was moved does not help us understand what's going on—where were they looking? Which aspects of the system drew their attention?

Eye-tracking systems can help us begin to answer these questions. Using cameras or other sensors, these systems continuously track the orientation of the fovea—the center of the field of vision. This information can be used to identify where the user is looking, which is in turn assumed to be the center of their attention. Although perhaps overly simplistic, this simplified model provides the basis for all eye-tracking work ([820]). Generally, eye-tracking systems will use transform raw data regarding gaze direction into a series of coordinates mapping direction into (x, y) coordinates on the display being viewed. These coordinates can then be further transformed into trails identifying where the user looked and when (Figure 13.1), providing information that can help us understand how user attention relates to task completion, and possibly how aspects of the interface command attention and influence whether or not tasks are completed successfully and how long they take.

Technologies and applications have progressed significantly since the first use of eye tracking in the early 20th century ([821]). Modern systems use sensors based on the desktop or on head-mounted devices to track the reflection of infrared light from the cornea or retina ([822]; [823]). Eye-tracking devices have become increasingly inexpensive, with highly functional commercial systems now available for less than $200. Open-source university-developed systems costing less than $100 have shown performance comparable to more expensive commercial systems ([824]; [825]). The advent of low-cost cameras and other inexpensive hardware have reduced the costs of eye trackers ([826]), although inexpensive systems may lack collect data at a lower frequency than higher-end alternatives. Systems are often hard to use, requiring calibration for each user and inconvenience such as head-mounted devices or restrictions on the range of movement allowed to the user ([827]).

Interpretation of eye movements is a nontrivial challenge, due to the constant motion of our eyes. Rapid motions known as saccades last anywhere from 10 to 100 ms ([828]). These movements are used to reposition the eyes to a new viewpoint ([829])—perhaps in anticipation of a new task or in response to some stimulus. These transitions lead to fixation—focus on a new area of interest. However, fixation does not mean lack of motion—even when focused on a target; eyes will continue to move in small microsaccades, which are essentially random noise ([830]). Following a moving target (as in a video game) leads to a final class of eye movements known as smooth pursuits.

Sophisticated software uses the geometry of the eye and the related optics to filter out the noise and to identify saccades and fixations, providing highly accurate measures of where the user is looking at any given time. The first step in this process is generally to remove noise, often by ignoring measurements that are not plausible given the operating characteristics of the eye tracker. De-noised movements are then separated into saccades and fixations through one of two approaches. Dwell-time methods look for periods of little or no variance in eye position. Low-variance intervals lasting for more than some minimal amount of time are classified as fixations, with other intervals classified as saccades. Velocity-based methods take the opposite approach, classifying saccades as intervals when eye-movement velocity exceeds a given threshold. Experience from prior literature can be used to select appropriate parameters for fixation intervals, saccade velocity, and other thresholds ([831]). Although custom implementations are always possible, many users will adopt saccade and fixation detection approaches, along with corresponding thresholds, directly from software tools provided with eye-tracking hardware.

Identifying eye-movement features is only the first step in an eye-tracking study. As where the user's eyes are looking and what they are looking at on the screen are both important ([832]), appropriate use of eye-tracking data often requires mapping eye-gaze data to screen coordinates ([833]), and then integrating that data with information regarding the contents of the screen display at each time point and any additional interaction about mouse and keyboard interaction. Software tools that automatically synchronize these data streams can simplify the data interpretation process ([834]). Systems that can overlay “trails” indicating the path of a user's gaze onto screen shots can be particularly useful (Figure 13.1). As data analysis tools are often tied to specific hardware platforms, eye-gaze research studies should be carefully designed and controlled ([835]), so as to minimize the risk of artifacts in data collection and interpretation that might influence interpretation and results.

### 13.2.2 Applications

When interpretation and analysis challenges are handled appropriately, eye-gaze data can present researchers with intriguing possibilities. If we can understand how users move their eyes when completing various interface tasks, we might gain some insight into where attention is focused and how choices are made. This additional data can take us beyond the relatively uninformative traces of mouse and keyboard events, filling in the holes: just where did the user look before she moved her mouse from one menu to the next? Which portions of a web page initially attract user attention?

These possibilities have led to the application of eye tracking in many domains, both as new forms of computer input and as the basis for research projects aimed at using eye movements as a source of data for studying HCIs ([836]; [837]). Eye tracking has been widely used as an assistive technology for people with quadriplegia and others who are unable to use motor functions to operate a mouse, keyboard, or other adaptive input device ([838]; [839]). The use of gaze control for pointing and selecting objects—eye gaze as complementing ([840]; [841]) or replacing ([842]; [843]; [844]) mice—has been suggested by many researchers, leading to a variety of proposed designs. Others have explored taking eye tracking one step further, using gaze as an input or control signal. One study of immersive, collaborative environments used eye trackers to make virtual avatars “look” where users in virtual environments were looking ([845]). Other studies have used eye-gaze history data to help users monitor semiautonomous agents, using visual cues from prior gaze information to highlight where users should look for a monitoring task ([846]). Eye-tracking systems have also been developed for GUI interface control including pointing and clicking ([847]), window selection ([848]), multimodal interfaces ([849]; [850]), and for remote collaboration ([851]).

Researchers have used eye tracking to study user behavior with a wide range of computer interfaces. Web browsing and navigation have been particularly well-studied in this regard. In a pair of studies, researchers at Microsoft used an eye-tracking system to examine the impact of factors such as the placement of a target link in a list of results and the length of the contextual text snippet that accompanies the results ([852]; [853]). In study of placement, users were observed to be more likely to look at links early in a list than later and to spend more time looking at the earlier links ([854]). Consideration of the length of text summaries led to interesting results: when looking for a specific link, users tended to focus on more search results as the summaries got longer. This effect was less notable for open-ended “informational” tasks that were not focused on a specific goal. The researcher speculated that this difference was due to the relevance of the summaries in each case: summaries that were useful in the informational task were distractions that obscured the specific link name in the other tasks ([855]). Other studies have examined patterns in eye movements as users interact with websites, moving both within individual pages and across multiple pages ([856]; [857]; [858]).

Other experiments have used eye tracking to understand the progression of eye focus during menu selection tasks. One study found that eye-focus patterns in tasks involving reading menu items differed significantly from selecting items. Although users fixated on each item when reading menus, they tended to use sequences of eye movements in a given direction—known as “sweeps”—when performing selection tasks ([859]). Eye tracking has also been used to study differences in how user attention differs for alternative visualizations of hierarchical structures ([860]), and to build document summaries based on eye-gaze data describing areas that were the focus of user attention ([861]).

Given the complexity of eye tracking, some researchers might be tempted to look for other measurements that might provide hints as to where a user's attention is focused. For GUI-based systems, mouse position and movement might be seen as a proxy for eye gaze, as we might tend to look where the pointer goes as we move the mouse. A strong correlation between mouse movement and gaze might completely eliminate the need for eye tracking in some GUI-based contexts. Alas, the reality is somewhat more complicated. A number of studies have attempted to track the relationship between gaze and mouse movement, developing algorithms for using mouse position to predict gaze ([862]; [863]; [864]; [865]; [866]), although the nature of the relationship might be somewhat task dependent ([867]).

Of course, studies that use eye tracking, mouse movements, or other measurements as proxies for attention run into all of the usual problems associated with indirect measurements. Before undertaking such a study, consider triangulation approaches such as postfact review of screen video with participants, asking them to describe what they were thinking while they were interacting with the system. This “retrospective think-aloud” approach ([868]) might be preferable to real-time feedback, which might distract users from the task at hand. Interestingly, eye-tracking analyses have been used to validate retrospective think-aloud ([869]).

Although eye tracking has been successfully used for both top-down, hypothesis-driven experiments and bottom-up exploratory work ([870]), appropriate experimental design may increase the odds of success. Exploratory analysis offers the possibility of generating novel, unexpected insights, at the potential cost of open-ended searching for illusive needles in haystacks of data. Hypothesis-driven experiments constrain the analysis needed, helping avoid fruitless searches down blind alleys.

A narrow focus can also help simplify exploratory work. A study of the effectiveness of browser feedback for secure websites used eye tracking to study the use of security indicators, including the secure web protocol indicator (“https://”), lock or key icons, and security certificates ([871]). Focusing on these areas, researchers learned that users often looked at the lock icon on the browser window before or after looking at the HTTPS header in the web location bar. Eye tracking also identified potential confusion due to browser designs, as some users looked at the lower left-hand corner of the browser (where the lock is on Netscape/Mozilla browsers) rather than the lower right-hand corner (where it could be found on the Internet Explorer browser used in the study) ([872]).

Eye tracking can also be a vitally useful tool for understanding complex and cognitively challenging workflows and tasks (see the “Measuring Workload” sidebar), as demonstrated by explorations of the use of eye tracking in studying electronic medical records (EMRs) and other clinical information tools. Examples include the use of eye tracking to improve EMR design, through investigations of the detrimental impact of layout clutter on task performance ([873]) and in conjunction with retrospective think-aloud, to understand information search and access patterns during the use of EMRs ([874]). Other studies have investigated the use of eye tracking to identify the skill levels of EMR users ([875]); to understand EMR workflow ([876]; [877]) and visual search patterns ([878]); to explore how EMRs are used during patient visits ([879]) and particularly the impact that they might have on communication between patients and physicians ([880]); and to examine how emergency physicians interpret test results ([881]). Comparable studies with consumers of health information have examined understand how audiences read and interpret health information, including antialcohol messages ([882]) and public safety guidelines ([883]). An eye-tracking study of reading patterns for users of a health discussion found that gaze patterns differ between user seeking information regarding their own health, as compared to those seeking for information about someone else's symptoms ([884]). Eye tracking has also been used extensively to understand visual processes involved in interpreting complex biomedical data, such as cardiovascular data from electrocardiograms ([885]) and medical imaging, including virtual pathology slides ([886]), cranial scans ([887]), and other volumetric imaging ([888]).

Beyond traditional desktop environments, eye tracking presents myriad opportunities for augmented reality, particularly as lower-cost devices such become available as commodity hardware. Sensors mounted on eyeglasses and headsets can track gaze direction as users work in specialized environments or carry on day-to-day activities, presenting opportunities for input, object recognition, and control. As a relatively low-cost commodity system capable of gaze-tracking, Google Glass inspired significant interest, leading to the development of novel software approaches for data collection and analysis ([889]). Although Glass was not a commercial success, and has since been discontinued, the increased of goggles for virtual reality and augmented availability seems almost inevitable—commercial successes may be just around the corner. Additional examples of the use of Google Glass in HCI research can be found in Chapter 14.

Alternative approaches leverage the power of smartphones to enable mobile eye tracking. Commercially available eye-tracking goggles have been combined with smartphone software to map eye-gaze coordinates to locations on a wearer's smartphone screen ([890]). Of course, the logical conclusion would be to use the smartphone camera to do the eye tracking. Kyle Krafka and colleagues presented such a system, based on data models collected from over 1450 people and trained via a convolutional neural network, in a 2016 paper ([891]).

Measuring Workload

Workload is the effort associated with completing a task. As much of user interaction design aims to develop tools that are easy to use, HCI researchers and designers are often interested in assessing workload. Understanding when and where a tool makes mental demands on users can help us identify opportunities for improvement through redesign.

Unfortunately, workload can be very difficult to assess, as our mental processes are not easily observed. To work around this limitation, researchers have expended significant effort developing surveys such as the Subjective Workaround Assessment Technique (SWAT) ([892]), and the NASA Task Load Index, or NASA-TLX ([893]; [894]). The NASA-TLX is the most widely used of these instruments, having been used in hundreds of studies. The TLX scale includes six questions assessing mental demand, physical demand, temporal demand, performance, effort, and frustration level, along with a protocol for assessing the relative importance of these six measures to each specific task.

Despite their wide acceptance, these instruments suffer from the same shortcomings as other surveys. Asking users to rate the workload after they have completed a task relies on fallible human memory, leading to potentially inconsistent assessments that fail to account for much of the nuanced workload requirements inherent in many complex tasks.

These shortcomings have led to the development of a variety of approaches for using physiological sensors to measure workload. One possible approach involves the use of eye-gaze tracking to measure pupil diameter, which has been shown to increase with stress or frustration ([895]; [896]; [897]). Links between pupil dilation and mental load have been used to explore user interactions in contexts such as web content, where relevant content has been associated with larger pupil dilation than less relevant content, indicating that more mental effort is involved when content is pertinent ([898]). Other efforts have looked at the use of microsaccades and saccadic intrusions—deviations from a gaze point followed by a short fixation and then a return to the original point—to derive similar measures ([899], [900]).

Other physiological measures—many of which are discussed in this chapter—have also been used to assess workload. One 2010 study investigated the utility of several simultaneous measures, including an eye tracker, an electrocardiogram armband, a wireless electroencephalogram headset, and a heart-rate monitor, along with NASA-TLX ratings, to determine which combination of signals best measured workload. The average of the heat flux (as measured by the armband) and the variability of the electrocardiogram provided the highest classification accuracy ([901]), suggesting that combinations of measurements may be useful in measuring complex phenomena such as workload. Alternative approaches to assessing workload through physiological signals, including more direct measures of brain activity, are discussed later in the chapter.

## 13.3 Motion and Position Tracking

If the study of the motions of our eyes can provide insights into attention, workload, and other important processes, what else can we learn from the human body? Human bodies are constantly moving: even when we are “sitting still,” our torsos move slightly with each breath. Movements of our hands, arms, heads, torsos, and even legs and feet can be measured by multiple types of sensors, providing useful opportunities for studying and changing how we interact with computers.

### 13.3.1 Muscular and Skeletal Position Sensing

The Wii remote, introduced by Nintendo in 2005, introduced a new era of consumer electronics capable of sensor position and motion. Using a combination of accelerometers and optical sensing, the Wii remote provides multiple degrees of freedom, allowing natural inputs for games such as tennis and bowling. In addition to commercial success, the Wii was quickly adopted by HCI researchers who explored the possibility of enhancing the range of applications to include possibilities such as gesture recognition ([902]), and studied the use and adoption of the new games, particularly in social contexts ([903]).

Although the Wii might have been the first notable commercial success, HCI researchers have been working with novel sensing devices for years. Early published HCI work with accelerometers predates the Wii by several years ([904]). The use of accelerometers in HCI research exploded with the advent of ubiquitous availability in smartphones. Applications have included sensing posture to help stroke survivors ([905]), identifying repetitive and troublesome behavior from students with autism spectrum disorder ([906]), fall detection ([907]; [908]; [909]), and even detecting bad driving ([910]). Smartphone accelerometers have also been used as mouse-like input devices ([911]) and for gesture recognition ([912]).

Moving beyond accelerometers in smartphones, recent years have seen an explosion in the availability of wrist-worn sensors. Although wrist-watch heart-rate monitors have been available for years, the current generation of fitness sensors go much further, adding the capability to track steps, sleep, floor-climbing, and energy usage, in combination with integrated smartphone functionality. Although concerns about the accuracy of some measurements may limit the utility of these devices for some purposes ([913]; [914]), feedback provided by these tools may help users understand and increase the efficacy of their habits. The challenge of understanding how these tools are used over time can be significant, as technical challenges, nuanced user behavior often involving multiple devices, accuracy, inappropriate mental models, and other challenges complicate effective use of the tools and interpretation of resulting data ([915]; [916]; [917]). As these devices continue to grow in capability and popularity, further research will undoubtedly continue to ask how these monitoring capabilities can be used more effectively. For example, one study of physical activity monitors found that customized plans that encouraged users to reflect on exercise strategies were more effective than automatically constructed plans ([918]).

Smartwatches such as the Apple Watch provide wrist-worn easy access to a wider range of smartphone facilities than those provided by fitness sensors. These watches have been used to develop approaches for sensing gestures made by fingers ([919]; [920]; [921]; [922]). The 2016 example of the Apple Watch presents more opportunities for HCI researchers, particularly as new tools are developed to explore the use of the watch as an unobtrusive computing device in everyday settings ([923]; [924]). Exercise and fitness sensors provide similar capabilities—see Chapter 14 for additional discussion of these sensors.

Microsoft's Kinect takes a different approach to sensing position and motion. Like the Wii remote, Kinect comes out of the gaming world—in this case, Microsoft's Xbox. Kinect includes a depth sensor, cameras, and microphones capable of capture body motion in 3D, and recognizing faces and voices ([925]). Kinect sensors have been used in a wide range of contexts, including for assessing posture and movement ([926]; [927]), observing audience responses to interactive displays ([928]), providing feedback to speakers giving public presentations ([929]), interacting with large displays ([930]), and, of course, playing games, both for entertainment ([931]; [932]) and for rehabilitation ([933]; [934]; [935]). Data complexity can make analysis of Kinect interactions somewhat challenging as several types of analyses are needed to extract objects, human activities, gestures, and even surroundings from Kinect data ([936]). Toolkits such as Kinect Analysis ([937]) might simplify this analysis, but proper design and interpretation will always be a key component of any study using Kinect or similar data. For a discussion of the challenges involved in using Kinect data in natural (non-lab) settings, see the LAB-IN-A-BOX sidebar below.

The Wii, smartphone accelerometers, smart watches, fitness monitors, and Kinect all provide examples of consumer technologies used in HCI research. These commodity tools provide researchers with commercial-quality, ready-to-use hardware and software that can be readily integrated into research, without requiring any of the engineering work required to collect data using home-grown or assembled components. For further discussion of smart watches and fitness trackers, see Chapter 14.

The need to transcend the limitations of commercial tools has inspired countless tinkerers and experimenters to develop and adapt novel motion and position sensing tools to both collect input from users and to measure activity. The accessibility community has been developing novel interfaces enabling users with reduced motor capacity to control computers since at the 1970s ([938]). Other recent efforts have involved the development of any number of innovative sensors. Fiber optics ([939]), flexible sensors ([940]), and sensors mounted on chairs ([941]) have been used to assess posture. Foam sensors stitched into clothing can detect both respiration and shoulder and arm movements ([942]). Wheel rotation sensors' on wheelchairs can be used to collect motion data suitable for classification of different types of activity ([943]). One study published in 2015 explored the use of a system for detecting magnetic radiation from electrical devices. Using an array of sensors worn on a wrist-band, this system collects and classifies data, identifying electrical devices used by the wearer ([944]). Although the initial design is often somewhat cumbersome, these early prototypes pave the way for future refinements that may themselves lead to commercial innovations. Other efforts might suggest novel uses of existing technology to collect otherwise unavailable data, such as the use of commercial Doppler radar devices to sense sleep patterns without placing sensors on the body ([945]).

These custom sensing approaches might require help from engineers and signal-processing efforts not necessarily found in HCI research teams, but the broad possibilities for innovation and insight can often be well worth the effort.

Motion and position-sensing devices have many potential applications in HCI research, from assessing everyday activity such as posture, to studying activity while using a system, to forming the basis for new input modalities. Although custom-designed sensors will likely be the approach of choice to those with the engineering capability who are truly interested in pushing the envelope, the availability of cheaper and smaller sensors places these tools within the reach of many HCI researchers.

### 13.3.2 Motion Tracking for Large Displays and Virtual Environments

Some forms of HCI inherently require users to move around in space. Users of wall-sized displays routinely move from one side to another, or up and down, just as teachers in a classroom move to different parts of the room. Users of virtual environments turn their heads, walk around, and move their hands to grasp objects. Collecting data that will help understand patterns of motion—where do users move, how do they move, and when do they do it?—requires data collection tools and techniques beyond those used with desktop systems.

Motion-tracking tools using cameras and markers worn by study participants can track motion through a large space. As the participant moves through space, the cameras use the marker to create a record of where the participant went and when. One study used this approach to examine activity in the course of using a wall-sized display (24 monitors, arranged as 8 columns of 3 monitors each, see Figure 13.2) to search and explore real-estate data. Researchers were interested to see whether users would move around more (physical navigation) or use zooming and panning mechanisms (virtual navigation).

Participants wore a hat with sensors for the motion-tracking system (Figure 13.3), which recorded their activity. Different display widths—ranging from one column to all eight columns—were used to study the effect of the width of the display. Participants generally used virtual navigation less and physical navigation more with wider displays. They also preferred physical navigation ([946]).

Researchers have used sensors that directly measure the position and orientation of various body parts to answer questions about movement and activity in immersive virtual environments. In one study, participants used a head-mounted display and a 3D mouse to interact with an immersive environment. Sensors monitored the position of the head, arms, legs, or other appropriate body parts. This approach provided insights into user activity in a variety of applications of virtual environments, including the diagnosis of attention deficit hyperactivity disorder (ADHD) and neurological rehabilitation of stroke patients ([947]).

## 13.4 Physiological Tools

Our bodies are intricate devices, with numerous interrelated systems that change their behavior as we are excited, frustrated, or otherwise aroused. Each cell in our body is part of an electrical system, with voltage levels that differ across cell membranes and change under the right conditions ([948]). Blood flow, heart rate, rate of breathing, and electrical conductivity of various parts of the body are just a few of the measures that have been studied in an attempt to better understand these responses. The combination of these physiological measures with more traditional study of task performance and subjective responses is known as psychophysiology ([949]).

Psychophysiology brings the possibility of using concrete measurements of the state of the human body to accompany assessments captured through surveys or observations. Imagine a study of user frustration levels with a series of alternative interface designs. You might start by asking participants to complete a series of tasks with each interface. After they complete the tasks, you could ask the users to complete one or more questionnaires aimed at understanding frustration levels. You might even ask them which features of the designs were more or less frustrating.

Even though this might be a fine design for your study, it misses some potentially important and interesting information. For example, when were the users most frustrated? Were they frustrated on the same task for each interface or did some designs cause less frustration on some tasks and more frustration on others? Postfact questionnaires are simply too coarse-grained to address these questions. The retrospective nature of questionnaires means that you are relying on the participants' fallible and incomplete memories to get your results.

Suppose your careful and thorough reading of the appropriate literature tells you that increases in frustration lead to increases in heart rate. With some sensors, recording equipment, and appropriate training in their use, you could change your experiment to monitor heart rate during task completion time. Appropriate tools for synchronizing the physiological data with other data that you collect during the tasks—such as task completion time or fine-grained records of all activities—will let you see exactly what the participant was doing when he became most frustrated. Correlating this information with feedback from the subjective questionnaire will provide you with a much fuller picture than you would have been able to get from only the task performance data and subjective responses.

### 13.4.1 Physiological Data

Appropriate use of physiological data for research requires an understanding of the types of data that can be collected, the tools required for data collection, and the ways in which these data sources respond to various stimuli. Skin conductivity, blood flow, and respiration rate (to name a few examples) are very different measures, each presenting a variety of challenges in terms of both collection and interpretation.

Approaches to collecting data from various parts of the body require different classes of sensor for measuring responses. Broadly speaking, these sensors fall into two classes: electrodes, which directly record electrical signals, and transducers, which convert mechanical or physical measurements into an electrical form ([950]). In both cases, the resulting analog signals are converted to digital form by an analog-to-digital converter and stored on computers for filtering and analysis.

Complex physiological responses to different stimuli can make interpretation a challenge: there is no single, monolithic interpretation of these signals. Although measurements of heart rate, electric conductance of skin, respiration, or brain activity may be well-defined in terms of the underlying mechanical or biological activity, the meaning of those phenomena may be much harder to interpret. If an activity causes a person's heart rate to increase and changes activation patterns of different areas in their brain, is that because the task was hard? Establishing links between these physiological methods and concepts of interest to HCI researchers is often difficult. Understanding the limits of any particular measurements, and any debates over the interpretation of those measurements, is critical for conducting reliable and valid research with physiological data. Although some of these issues are discussed later, careful researchers will dive into more recent work in these rapidly evolving areas before rushing into conduct studies.

The sources of physiological data that have been used in HCI research can be classified according to the type of signal involved, the location on the body, and the kinds of sensors required (see Table 13.1). The range of data sources and their applications are likely to continue to expand as researchers find creative applications for new and evolving technologies.

Table 13.1

+-----------------------------------+----------------------------------------------------------+------------------------+--------------------+---------------------------------------+
| Data Source                       | Technique                                                | Signal Type            | Possible Locations | Sensors                               |
+===================================+==========================================================+========================+====================+=======================================+
| Electrodermal activity            | Galvanic skin response (GSR) ([951]; [952])              | Electrical             | Fingers, toes      | Surface electrodes                    |
+-----------------------------------+----------------------------------------------------------+------------------------+--------------------+---------------------------------------+
| Cardiovascular data               | Blood-volume pressure ([953])                            | Light absorption       | Finger             | Surface electrodes                    |
|                                   +----------------------------------------------------------+------------------------+--------------------+---------------------------------------+
|                                   | Electrocardiography ([954])                              | Electrical             | Chest, abdomen     | Surface electrodes                    |
+-----------------------------------+----------------------------------------------------------+------------------------+--------------------+---------------------------------------+
| Respiration                       | Chest contraction and expansion ([955])                  | Physical               | Thorax             | Stress sensor                         |
+-----------------------------------+----------------------------------------------------------+------------------------+--------------------+---------------------------------------+
| Muscular and skeletal positioning | Pressure or position sensing ([956]; [957],[958]; [959]) | Physical or electrical | Varied             | Pressure sensor, fiber optics, others |
+-----------------------------------+----------------------------------------------------------+------------------------+--------------------+---------------------------------------+
| Muscle tension                    | Electromyography ([960])                                 | Electrical             | Jaw, face          | Surface electrodes                    |
+-----------------------------------+----------------------------------------------------------+------------------------+--------------------+---------------------------------------+
| Brain activity                    | Electroencephalography ([961])                           | Electrical             | Head               | Electrodes in helmet                  |
|                                   +----------------------------------------------------------+------------------------+--------------------+---------------------------------------+
|                                   | Evoked responses ([962])                                 | Electrical             | Head               | Surface electrodes                    |
+-----------------------------------+----------------------------------------------------------+------------------------+--------------------+---------------------------------------+

: Types of Physiological Data Used in HCI Research {#TABC000133t0010 .tbody}

13.4.1.1 Electrodermal activity or galvanic skin response

As many science-museum exhibits demonstrate, human bodies can act as conductors for electricity. Glands in our hands and feet produce sweat in response to emotional and cognitive stimuli. The salty sweat increases conductivity, allowing more electricity to flow ([963]; [964]). Conductivity is a measure of how well electricity flows through a substance: higher conductivity means a greater flow of electricity. Electrodermal activity is the measurement of the flow of electricity through the skin. Electrodermal systems use a pair of electrodes on the skin—usually connected to fingers—to measure the conductivity between two points (Figure 13.4). Research efforts have linked conductance level to arousal, cognitive activity ([965]), and frustration ([966]). Some studies have established differences in the magnitudes of changes associated with different emotions. For example, fear leads to smaller increases in skin conductance than sadness ([967]).

13.4.1.2 Cardiovascular signals

Anyone who has ridden a roller coaster or watched a suspenseful movie has first-hand knowledge of how the heart responds to stimuli. Increased heart rate is one part of a complex set of reactions that may involve changes in the variability of the heart rate, blood pressure, and blood-volume pressure (BVP) ([968]). Heart-rate variability has been used to measure mental effort and stress ([969]; [970]; [971]) as well as emotional responses including fear, happiness, and anger ([972]).

Commonly used techniques for measuring cardiovascular activity include BVP monitoring and electrocardiography (EKG). BVP sensors worn on fingers measure changes in reflect light associated with changes in blood volume in finger capillaries. These measurements can be used as indirect measures of anxiety and other emotional responses such as that have been found to be correlated with blood. Heart-rate variability information can also be inferred from BVP data ([973]). Electrocardiography measures the electrical current that causes the heart to pump. Using sensors placed on different places on the body, EKG can measure heart rate, the interval between heartbeats, and heart-rate variability ([974]).

13.4.1.3 Respiration

Just as certain stimuli can make our hearts beat faster, changes in mood can affect our breathing. Arousal may make us breathe faster and some emotions can cause irregular breathing ([975]). Respiratory measures are strongly linked to cardiovascular activity ([976]).

A relatively straightforward approach to measuring respiration involves tracking the expansion and contraction of the chest cavity. Sensors that can measure how far and how rapidly the chest moves with each breath can be attached to the thorax ([977]; [978]) and even integrated into clothing ([979]).

13.4.1.4 Muscle tension

The contraction of muscles creates electrical signals that can be detected through electrodes placed on the muscle of interest, a technique known as electromyography (EMG). Measurements on the jaw can reveal tensions associated with a clenched jaw. Sensors on eyebrows or cheeks can detect muscle movements associated with frowns or smiles, respectively. Mildly positive emotions lead to lower EMG readings over the eyebrow and mildly higher activity over the cheek, relative to mildly negative emotions. Reactions to specific emotional moods including sadness, fear, and happiness have been studied as well, with less clear results ([980]). EMG has also been used as an input modality: one project investigated the use of an EMG armband as a means of unobtrusively controlling a digital media player ([981]).

13.4.1.5 Brain activity

Numerous techniques for directly and indirectly measuring brain activity have been developed. Brain-imaging techniques provide detailed displays, but expensive equipment and required medical expertise have limited their use in HCI research. Indirect measures that use changes in electrical signals on the head to measure brain activity provide less detail, but they are significantly easier to work with.

Electroencephalography (EEG) involves the use of electrodes distributed across the scalp to measure brain activity in the cerebral cortex. Typically, this involves placing a cap containing 128–256 electrodes on a participant's scalp (Figure 13.5). These electrodes are used to measure electrical activity in various locations, with differences between locations or relative to some average baseline used as indicators of various types of activity ([982]). Evoked response measurements involve measurements of differentials between electrodes in two locations (perhaps earlobe and scalp), in response to auditory or visual responses ([983]).

Functional near-infrared spectroscopy (fNIRS) uses the reflectivity characteristics of the skull, scalp, and brain to measure mental activity. Near-infrared light can travel 2–3 cm into the brain before being either absorbed or reflected. Wavelengths that are reflected by hemoglobin can be used to measure mental activity ([984]; [985]). An fNIRS measurement system generally includes light sources and detectors mounted on a flexible headband.

Preliminary applications to HCI research have examined the ability of fNIRS to measure mental effort. An examination of the mental effort involved in solving rotating cube puzzles found that fNIRS measured distinguishable differences when comparing tasks with a graphical cube on a screen to tasks involving a physical cube. fNIRS was able to distinguish between tasks at three different levels of difficulty, with better-than-random accuracy ([986]). The application of fNIRS to a military command-and-control task found that fNIRS could be used to predict workload ([987]). The results from these studies were interpreted as demonstrating the utility of fNIRS for HCI research. fNIRS has subsequently been used in a number of HCI studies, addressing topics such as the impact of think-aloud protocols ([988]) and web-form layout ([989]) on mental workload; evaluating information visualization systems ([990]); and even as a form of input ([991]; [992]).

Functional magnetic resonance imaging (fMRI) has also been used in HCI research. fMRI works by tracking blood flow through the brain: as blood will flow to areas of the brain involved in relevant cognitive processes, locations associated with particular classes of problems can be identified. One study used fMRI to observe an emotional response to emoticons, even when regions of the brain associated with face recognition were inactive, indicating that participants did not recognize the emoticons as faces ([993]). Other HCI studies have applied fMRI to study the effect of multiple exposure to security warnings ([994]), the extent to which participants feel that they are “present” in virtual reality ([995]); mental loads associated with 3D motion and interactivity in virtual reality ([996]); perception of the quality of design ([997]), processes involved in learning new tools ([998]) and information search processes ([999]); and validation of think-aloud protocols ([1000]), among others.

Measurements of brain activity present tantalizing prospects for HCI research, presenting the possibility of getting “under the hood” and gaining otherwise unavailable understanding of mental states and cognitive processes. However, these techniques are not without their drawbacks. Although EEGs may be used reasonably inexpensively, fMRI research requires often expensive access to complex machinery. Data are often quite noisy, and interpretation can be challenging. Collaboration with neuroscientists trained in these techniques is often a winning strategy for HCI studies.

## 13.5 Data Collection, Analysis, and Interpretation

Whether eye tracking; motion and posture sensing; or one of the several types of physiological data discussed earlier, studies measuring human activity will generally follow the same set of steps as any other study: designing, configuring, and testing data collection approaches; analyzing captured data; and interpreting the results. Despite these similarities to other studies, studies using the techniques described in this chapter present their own specific challenges at each of these stages (Figure 13.6)

### 13.5.1 Data Collection

Physiological data collection presents some challenges that are not generally encountered in more traditional HCI research. To make use of the data sources that literally measure the body, researchers must be in direct physical contact with their subjects. For galvanic skin response or blood-volume measurements, this may be as simple as placing an electrode on a finger tip. Surface electrodes (for EKG or EMG) and chest-mounted sensors (for respiration measurements) are substantially more complicated. These electrodes must be attached carefully in the appropriate position to ensure high-quality recording of the desired data.

Measurements based on body-mounted sensors involving pressure ([1001]) or skeletal positioning ([1002]) present a different set of challenges. As these approaches are relatively new and the technology is rapidly evolving, off-the-shelf tools with clear guidance may be few and far between. You may need to familiarize yourself with the pros and cons of a variety of sensors before conducting this sort of work. Before using any of these tools for measuring physiological data, you should make sure that you have appropriate training in their use. Partnering with an experienced health professional is an attractive means of ensuring correct use of sensors and other—probably expensive—equipment.

Although electrodes and sensors are not physically invasive, they may cause some discomfort and unease for some participants in your study. You may want to take extra care to be sensitive to participant's concerns, particularly involving the placement and attachment of electrodes. Some researchers suggest that electrodes should be attached only by someone of the same gender as the participant, in order to reduce anxiety and embarrassment ([1003]). As some participants may become uncomfortable, your informed consent forms (Chapter 15) should be particularly explicit regarding potential risks. Take extra care to observe the participants' moods: when faced with a particularly distressed subject, you may wish to remind them that they can withdraw if they are uncomfortable. In addition to being considerate, this approach may save you from difficulties in data interpretation: if a participant's anxiety levels are high due to concern about the experiment, it may be difficult or impossible to identify anxiety responses caused by your stimuli.

These logistical challenges are even greater for more invasive techniques that require the involvement of a trained expert. Although surface electrodes are widely used in EMG measurements, needles placed in muscles are a possible alternative for many applications ([1004]). Although the needles are safe, they must be used correctly, making them a strictly “don't try this at home” proposition. HCI researchers have shied away from this approach ([1005]); unless your team has an experienced EMG professional, you would be well-advised to do so as well.

Even if you are not using needles or electrodes, more prosaic restrictions might apply. Eye-tracking devices might require that users be seated within an optimal distance range from the monitor, wired sensors might have limited ranges, and external distractions must be controlled to minimize confounding stimuli that might distract users and add unwanted cognitive load.

If you want to use physiological data to identify arousal, frustration, or other responses to specific interactions with a computer, you need to be able to synchronize changes in physiology with user actions. Plainly speaking, if you know that the variability in a user's heart rate increased at a certain point in time, you won't be able to interpret that change unless you know what the user was doing at the time. You are likely to be keeping a textual log of user actions, tracking mouse movements, key presses, and related information about the state of the application. Your physiological data would similarly be recorded via software that would create fine-grained records containing multiple measurements per second.

The first measurement challenge involves fine-grained measurements. Whereas physiological data are essentially continuous, tracking of events on the computer may not be. Fine-grained timing information may require using system clocks which operate on the order of milliseconds. Recording the number of internal clock “ticks” between events is one way to get high-resolution event data ([1006]). Due to processing or hardware requirements, physiological data might be captured on one computer while tasks are completed on another. This arrangement presents the challenge of managing a fairly complex experimental setup. Besides the two computers (one for the application and one for data collection), you have sensors, analog-to-digital converters for converting the physiological signals into a form suitable for storage on the computer, potentially modified input devices, and possibly other equipment for audio and video recording (Figure 13.7).

Data collection challenges often lead researchers to choose to conduct physiological studies in the comfort and convenience of the lab. Working in surroundings that are well-lit, well-organized and well-stocked with all needed supplies is a good strategy for minimizing the uncertainty associated with these data collection techniques. However, lab studies have their limits. The idealized settings may not reflect “real-world” situations where technologies might be used, leading to results that may be somewhat artificial. This disconnect between the environment of the study and the environment of use is described as reducing the ecological validity of the study. For studies addressing how interfaces are used in practice, lab settings might simply be unable to capture all of the richness of real usage environments. See the “LAB-IN-A-BOX” sidebar for a description of a suite of tools developed to address these challenges.

### 13.5.2 Data Analysis

Like other naturally occurring signals, eye-tracking data, motion detection systems, and physiological measurements are all very noisy, containing artifacts and variability that can make interpretation difficult. EMG signals, for example, suffer from significant amounts of distortion and random noise from other muscles ([1007]). Tonic activity levels measure physiological responses in the absence of specific responses. These “baseline” measurements can differ significantly from one individual to the next and sometimes within individuals, due to factors such as headaches. Furthermore, the magnitude of response to a specific condition may be influenced by the tonic levels of a given signal: the response to any given stimulus might be lesser for a heart that is already beating quickly. Habituation is another concern: the magnitude of response to a stimulus decreases after repeated presentation ([1008]). This can present a challenge for both experimental design and data interpretation. Eye-tracking and motion detection systems face similar challenges in distinguishing between intentional actions including saccades, pursuits, and fixations and seemingly random noise (microsaccades) ([1009]). Appropriate use of software tools accompanying eye-tracking hardware can help address these difficulties.

Although a wide variety of methods has been proposed for extracting the signal from the surrounding noise ([1010]), their use might require additional expertise: without a basis in a solid understanding, the application of signal-processing tools to noisy data streams can become a case of “garbage-in, garbage-out.”

Once you have extracted the signal in your physiological data from the noise, your next challenge is to determine the granularity of the data that you will analyze. Some experiments call for relatively coarse data: if you are interested in comparing average responses for various testing conditions, you can just process data as it arrives, without worrying about specific correspondences between physiological data points and events in the computer interface. In cases where you want more detail, you might find that capturing all of the data available from your sensors is overwhelming. Some form of downsampling (capturing one out of every n data points instead of all data points) can often provide a useful means of reducing data volume without sacrificing fidelity or accuracy ([1011]).

If you are trying to link physiological responses to specific actions or events, you may face the stream of integrating data streams that are collected separately—perhaps even on different computers. Although your application data may be fine-grained logs of individual events, physiological data streams may not have access to that information. If all data collection is done on one computer, the timestamp might be used with both data streams. When physiological data is captured on a separate computer, some clever engineering might be necessary. One set of experimenters used a modified mouse to solve this problem: in addition to sending control signals to the computer running the application, the mouse had a second wire that sent a pulse to the computer collecting physiological data. These pulses were used to synchronize the two streams ([1012]).

Appropriate use of tools and validated approaches can simplify matters somewhat. Many eye-tracking systems will come with associated software that will collect and analyze data, potentially sparing you from the need to clean noisy data streams and identify fixations. Ideally, such tools will provide access to raw data along with summarized data, providing you with the means to conduct your own detailed analyses as needed.

### 13.5.3 Data Interpretation

Given multiple streams of complex, synchronized data involving one or more physiological signals and interactions with one or more computer programs, potentially alongside complementary data including survey data and audio/video recording, how can this data be interpreted?

One initial possibility is manual review. Particularly in earlier stages of interpretation, looking at the signals to find examples of any anomalies, episodes of interactions that might be informative, or other similar items of interest can often be a good way to decide where to explore in more details. Tools that facilitate comparison and alignment of multiple data streams can be very helpful in this regard. ChronoViz ([1013]) provides features for alignment and side-by-side review of multiple temporal data streams, allowing users to, for example, review synchronized displays of screen-capture video alongside physiological measurements. The “LAB-IN-A-BOX” sidebar discusses the use of the ChronoViz tool to analyze complex, synchronized data streams.

Identification of specific items or actions is often a first step. For example, you might be interested in seeing how often the user in an eye-tracking study looks in a certain region of the screen. When criteria are clearly and objectively defined, the identification of relevant intervals or incidents is generally straightforward.

Data granularity can also influence analysis and interpretation. For simple comparisons involving overall responses to differing conditions, averages might be sufficient ([1014]). More complex analyses might attempt to model and classify episodes of emotional reaction ([1015]), potentially using machine learning techniques to automatically identify actions and reactions with high degrees of confidence. Such classification methods may require manual identification of desired outputs, to be used as training sets for supervised learning.

A final interpretive challenge lies in the difficulty of understanding physiological signals. Even if you have a clear difference in some measure that seems to come in response to a specific event, interpreting that measure may prove challenging. You may be tempted to classify a response as specific emotional state—happiness, sadness, disgust, fear, or other examples—but data for many measures is inconclusive ([1016]). Although triangulation through the use of multiple signals can be a promising approach, there is no guarantee that any combination of responses will be sufficient. Mixed or incomplete measures are a very real possibility: some stimuli may lead to a response in one measure, with no change in another ([1017]).

Physiological data presents tantalizing possibilities for researchers. Although the challenges of collecting and interpreting data from these sources are considerable, the possibility of identifying fine-grained, real-time responses to interfaces is often hard to resist. Before committing your valuable human and financial resources to such an effort, you may want to ask yourself if there is an easier way to observe the phenomena of interest. You may legitimately decide that your study of user frustration requires fine-grained detail about specific events, making posttest questionnaires insufficiently detailed. Before concluding that physiological data measures are required to identify incidences of frustration in real-time, you should consider using simpler methods such as videotapes, observations, think-aloud protocols, or time diaries. You may find that simpler methods get the job done with much less headache and expense. For a more detailed discussion of the use of eye tracking and physiological data into HCI design and evaluation, see Bergstrom and Schall's practical book Eye Tracking in User Experience Design ([1018]).

LAB-IN-A-BOX

Studies involving human data collection can be particularly challenging when they involve either realistic locations or collection and correlation of multiple data streams. Combining these two challenges can make matters even more interesting, leading often to innovative techniques. Nadir Weibel and colleagues struggled with these questions as they developed a multimodal set of data collection and analysis techniques to examine a complex and multifaceted set of HCIs: the use of electronic medical records (EMRs) by physicians during outpatient medical visits.

Although the use of electronic medical records has expanded substantially in recent years, the impact of this change on medical care is far from well understood. Although researchers have known for quite some time that physicians see EMRs as bringing changes in documentation, communication, and work processes, along with concerns about data quality ([1019]), understanding the dynamics of how these records impact care is more challenging. A 2016 literature review found that although some studies found that although EMR use involved a range of both positive and negative communication behaviors, there was no conclusive evidence of any negative impact on patient perceptions of satisfaction or communication with physicians ([1020]).

Although these results suggest that in-depth studies of the use of EMRs during patient visits are needed to understand specific behaviors and to separate negative from positive impacts, conducting such studies presents several challenges. Lab-based simulations are likely too artificial, lacking the open-ended challenges associated with medical practice. Some researchers have resorted to video and audio recordings providing data capture from multiple perspectives ([1021]). This approach is informative, but limited, as these captures might be able to identify where users are looking and how they are interacting, but details of interactions with the EMR will not be recorded, leaving researchers with the challenge of inferring how the details of the computer use might impact communication with patients.

Noting these difficulties, Nadir Weibel and colleagues developed a data and analysis infrastructure known as LAB-IN-A-BOX, designed to capture multiple streams of data detailing the dynamics of interactions between the physician, the patient, and the computer during medical visits. LAB-IN-A-BOX combines directional audio through a microphone array; eye tracking; full-room video, screen capture, mouse movements, mouse clicks, and other computer interactions through Techsmith Morae usability software (https://www.techsmith.com/morae.html); and Kinect for Windows to measure orientation of the user's body ([1022]). Realizing that using this device in physician examination rooms would require a great deal of flexibility in transportation and installation, Weibel and colleagues configured a hard plastic rolling case to hold all of the equipment, wiring, and connectors, enabling setup and data collection in 10 minutes or less ([1023]) (Figure 13.8).

To address the challenge of analyzing the various data streams, Weibel and colleagues started with a synchronization algorithm that aligns audio and video components. Kinect data is segmented to differentiate (when possible) between the clinician, the patient, and objects in the room such as chairs—all problems that would not be faced in an idealized lab environment with only one participant and no furniture. This data is then further processed to determine where the physician is looking at any given time, and to identify any gestures. Directional audio is processed to distinguish physician speech from patient speech. Mouse, keyboard, and other computer activities also are analyzed to identify when the computer is being used and, through screen capture, what the user is doing. The resulting data streams can be viewed using the ChronoViz analysis tool ([1024]) (Figure 13.9). Noting the utility of using this data to develop deeper understandings than would be available from either lab-based studies or traditional ethnography, the LAB-IN-A-BOX team described this approach as “Computational Ethnography” ([1025]).

## 13.6 Examples

Despite the challenges, numerous HCI researchers have used physiological data to observe user interactions in ways that would not otherwise be possible. An examination of some of these studies indicates the common theme of using these techniques to record real-time observations of a task in progress, as opposed to subjective, posttest response.

A study of cognitive load and multimodal interfaces used three different traffic control interfaces with three different task complexity levels to investigate the possibility of using galvanic skin response (GSR) to measure cognitive load. Participants used gesture-based, speech-based, or multimodal (speech and gesture) interfaces to complete tasks. Initial analysis of data from five participants indicated that average response levels were lowest for the multimodal interface, followed by speech and then gesture interfaces. For all three interfaces, the total response increased with task complexity. This was interpreted as providing evidence for the utility of using GSR to indicate cognitive loads. Analysis of specific recordings found GSR peaks to be correlated with stressful or frustrating events, with responses decreasing over time. Peaks were also correlated with major events that were thought to be cognitively challenging, including reading instructions and competing tasks ([1026]).

Another study used both galvanic skin response (GSR) and blood-volume pressure (BVP) to measure user frustration in an explicit attempt to develop methods for using multiple sensing technologies. The experimental design involved a game with several puzzles. Participants were told that the experimenters were interested in how brightly colored graphics would influence physiological variables in an online game. Unbeknown to the participants, the game software was rigged to randomly introduce episodes of unresponsiveness. As participants were being timed and had been offered a reward if they had the fastest task completion times, these delays would presumably cause frustration.^([1027]) BVP and GSR responses were used to develop models that could distinguish between frustrating and nonfrustrating states ([1028]).

Interaction with computer games is a natural topic for physiological data. As anyone who has played video games knows, players can become excited while driving race cars, hunting aliens, or playing basketball on the computer. However, the fast-paced nature of these games limits the applicability of many techniques. Intrusive data collection techniques, such as “think-aloud” descriptions, interfere with the game-playing experience and posttest questionnaires fail to recapture all of the nuances of the playing experience ([1029]).

One study used various physiological data sources—GSR, EKG, cardiovascular rate, respiration rate, and facial EMG—to measure responses to computer games played against a computer and against a friend. Starting from the premise that the physiological data would provide objective measures that would be correlated to players' subjective reports of experiences with video games, the researchers hypothesized that preferences and physiological responses would differ when comparing playing against a computer to playing against a friend. Specifically, they hypothesized that participants would prefer playing against friends, GSR and EMG values would be higher (due to increased competition), and that differences between GSR readings in the two conditions would correspond to subjective ratings ([1030]).

To test these hypotheses, they asked participants to play a hockey video game, against the computer and against a friend. Participants were recruited in pairs of friends, so each person knew their opponent. The hypotheses were generally confirmed: participants found playing against a friend to be more exciting, and most had higher GSR and facial EMG levels when playing with a friend. Cardiovascular and respiratory measures did not show any differences. Investigation of specific incidents also revealed differences—participants had a greater response to a fight when playing a friend. Examination of the relationship between GSR, fun, and frustration revealed a positive correlation with fun and a negative correlation with frustration ([1031]). The use of multiple coordinated sensors to measure frustration in game playing continues to be an active area of research, with more recent papers exploring topics such as the impact of system delays ([1032]).

EEGs have been also used by HCI researchers to develop brain-computer interfaces that use measurable brain activity to control computers ([1033]). Machine-learning algorithms applied to EEG signals have been used to distinguish between different types of activity. Similar to the study of cooperative gaming described earlier ([1034]), one study found that EEG signals could be used to distinguish between resting states, solo game play, and playing against an expert player ([1035]). Other HCI applications involving EEG signals include identifying images of interest from a large set ([1036]) and measurement of memory and cognitive load in a military command-and-control environment ([1037]).

Electromyography has been used to measure a variety of emotional responses to computer interfaces. One study of web surfing tasks found strong correlations between facial EMG measures of frustration and incorrectly completed tasks or home pages that required greater effort to navigate ([1038]). Similar studies used EMG to measure emotional responses to videos describing new software features, tension in using media-player software ([1039]), and task difficulty or frustration in word processing ([1040]). An experiment involving boys playing racing games on the Microsoft Xbox established the validity of facial EMG for distinguishing between positive and negative events ([1041]). Combinations of multiple physiological measures, including EMG, have also been used to study emotional responses ([1042]).

A broad body of work has explored the use of body sensing in a variety of healthcare domains, including assessment of disability, rehabilitation, and in use by clinicians. Several of these applications have been discussed in this chapter; for a more in-depth discussion, see “Body Tracking in Healthcare” in [1043].

## 13.7 Summary

Many HCI questions involve digging deeper than the level of individual tasks. Instead of simply asking whether a task was completed correctly or how quickly it was completed, these efforts hope to understand what happened during the completion of the task. Such questions may involve examination of what the user is doing (which keys they are pressing, where they are moving the mouse, where they are looking) and how they are reacting (are they happy, sad, frustrated, or excited)?

Traditional measurement and observation techniques can be used to address these questions, but they are limited in their applicability. Even the most careful observations and video recording are very limited in determining which keys a user presses and how quickly they are pressed. Observation and video tape present similar limitations for tracking mouse movements or eye gazes. Inferring emotional states is similarly challenging: we may be able to identify excitement simply by watching someone playing a video game, but more subtle responses such as frustration may not be apparent. Asking users after the fact provides some detail, but questionnaires or interviews are limited to details that the participant remembers after the fact, making fine-grained data collection difficult, if not impossible.

Automated data collection approaches provide data that are unavailable through these more traditional approaches. For studies of mice and keyboard usage, actions that are intrinsically part of user tasks can be recorded for further analysis. Relatively simple data collection software can collect data tracking exactly what the user did (mouse press, mouse movement, key press) and when she did it. This information can be used to describe accuracy, identify problems in task completion, and classify task completion into periods of activity and inactivity. Combinations of multiple input devices—such as keyboard and mouse—can provide richer details.

Other interesting sources of human data may require a larger investment, potentially in analysis and possibly in equipment. Costs of eye-tracking systems have decreased significantly, but data analysis and interpretation can be a challenge. These concerns are even more pronounced for physiological measurements, which require equipping participants with electrodes, sensors, gauges, headbands, even helmets, or even more complex machinery. Interpreting the resulting noisy data is another challenge that requires substantial experience in signal processing.

You might want to start with simpler, less expensive techniques before you commit to the expense and difficulty associated with eye-tracking or physiological approaches. You might try simpler measures such as observation, video recording, or interviews, to see if they can be used to generate the insights that you need. Another approach would be to find proxies: although you might be tempted to use eye gaze to track a user's attention, tracking mouse movements might be a workable alternative. Eye tracking and galvanic skin response are tools that (perhaps with a little help from appropriate experts) many HCI researchers should be able to adopt for their own work.

For some research problems, the temptation of fine-grained physiological data using neuroimaging or other advanced techniques may be too great to resist. If you find yourself faced with such a question, be sure to work with experts: the assistance of collaborators who are familiar with both the equipment and the data interpretation challenges will be crucial to your success.

## Discussion Questions

 

1. Physiological data measurement tools present an interesting dilemma for researchers. Electrodes, helmets, chest-mounted sensors, and other tools used to measure these signals may be unfamiliar to many participants in research studies. Particularly for head-mounted equipment, the unfamiliarity and potential discomfort associated with these data collection tools may cause some individuals to become nervous, upset, or otherwise ill at ease. These responses might create a problem for studies aimed at understanding emotional responses to computer tasks. How would you go about distinguishing between measurable physiological responses that result from the use of unfamiliar, and potentially uncomfortable, monitoring hardware from responses to the task in question? How might factors such as the length of the experimental session and characteristics of the tasks complicate the challenge of distinguishing between these types of reactions?

2. Collaborative systems have the potential for generating a wide range of emotional reactions. When two or more people use a single computer system to work together on a problem of common interest (known as “colocated, synchronous collaboration”), some tasks may cause conflict, tension, excitement, or a variety of other emotional reactions. System behavior can also influence user reactions, as technical glitches and encouraging or discouraging feedback may lead to feelings of frustration. Technical concerns are even greater for collaboration between users at different locations (“distributed collaboration”), as network latencies, dropped connections, and slow responses are just a few of the problems that might be encountered. How would you go about measuring these emotional responses? Discuss the advantages and disadvantages of physiological data in this context, as opposed to self-reports, observation, or video recording. How might you use physiological data to study frustration in distributed collaboration?

Research Design Exercise

Commonly available, inexpensive heart-rate monitors used for monitoring exercise might be usable for measuring physiological responses to computer use. Use one of these monitors to measure your pulse while you do a variety of computer tasks. First, measure your pulse while you are relaxed. Then, try some increasingly demanding and stressful tasks. You might try performing a simple task, such as completing an email message, a more complex task involving an advanced tool, such as a photo editor, a mentally challenging task, such as a math puzzle, and a fast-paced, exciting video game. How does your pulse change with each of these activities? As the act of pausing to read the display of the monitor may change your activity level, you might want to ask a friend to do the measurement and take notes.

## References

Aaltonen A, Hyrskykari A, Räihä K-J. 101 spots, or how do users read menus? In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Los Angeles, California, United States. New York: ACM Press/Addison-Wesley Publishing Co.; 1998;132–139.

Afergan D. Using brain-computer interfaces for implicit input. In: Proceedings of the Adjunct Publication of the 27th Annual ACM Symposium on User Interface Software and Technology, Honolulu, Hawaii, USA. New York: ACM; 2014;13–16.

Agustin JS, Skovsgaard H, Mollenbach E, et al. Evaluation of a low-cost open-source gaze tracker. In: Proceedings of the 2010 Symposium on Eye-Tracking Research and Applications, Austin, Texas. New York: ACM; 77–80.

Albinali F, Goodwin MS, Intille SS. Recognizing stereotypical motor movements in the laboratory and classroom: a case study with children on the autism spectrum. In: Proceedings of the 11th International Conference on Ubiquitous Computing, Orlando, Florida, USA. New York: ACM; 2009;71–80.

Alkureishi MA, Lee WW, Lyons M, et al. Impact of electronic medical record use on the patient-doctor relationship and communication: a systematic review. Journal of General Internal Medicine. 2016;31(5):548–560.

Anderson BB, Kirwan CB, Jenkins JL, Eargle D, Howard S, Vance A. How polymorphic warnings reduce habituation in the brain: insights from an fMRI study. In: Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems, Seoul, Republic of Korea. New York: ACM; 2015;2883–2892.

Arteaga S, Chevalier J, Coile A, et al. Low-cost accelerometry-based posture monitoring system for stroke survivors. In: Proceedings of the 10th International ACM SIGACCESS Conference on Computers and Accessibility, Halifax, Nova Scotia, Canada. New York: ACM; 2008;243–244.

Asan O, Montague E. Technology-mediated information sharing between patients and clinicians in primary care encounters. Behaviour & Information Technology. 2014;33(3):259–270.

Ball R, North CN, Bowman DA. Move to improve: promoting physical navigation to increase user performance with large displays. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, San Jose, California, USA. New York: ACM; 2007;191–200.

Barreto A, Gao Y, Adjouadi M. Pupil diameter measurements: untapped potential to enhance computer interaction for eye tracker users? In: Proceedings of the 10th International ACM SIGACCESS Conference on Computers and Accessibility, Halifax, Nova Scotia, Canada. New York: ACM; 2008;269–270.

Bass SB, Gordon TF, Gordon R, Parvanta C. Using eye tracking and gaze pattern analysis to test a “dirty bomb” decision aid in a pilot RCT in urban adults with limited literacy. BMC Medical Informatics and Decision Making. 2016;16(1):1–13.

Bergstrom JR, Schall A. Eye Tracking in User Experience Design. Amsterdam: Morgan Kaufmann; 2014.

Berka C, Levendowski DJ, Cvetinovic MM, et al. Real-time analysis of EEG indexes of alertness, cognition, and memory acquired with a wireless EEG headset. International Journal of Human–Computer Interaction. 2004;17(2):151–170.

Bernaerts Y, Druwé M, Steensels S, Vermeulen J, Schöning J. The office smartwatch: development and design of a smartwatch app to digitally augment interactions in an office environment. In: Proceedings of the 2014 Companion Publication on Designing Interactive Systems, Vancouver, BC, Canada. New York: ACM; 41–44.

Bieg H-J. Gaze-augmented manual interaction. In: Proceedings of the 27th International Conference Extended Abstracts on Human Factors in Computing Systems, Boston, MA, USA. New York: ACM; 2009;3121–3124.

Bieg H-J, Chuang LL, Fleming RW, et al. Eye and pointer coordination in search and selection tasks. In: Proceedings of the 2010 Symposium on Eye-Tracking Research and Applications, Austin, Texas. New York: ACM; 89–92.

Bond RR, Kligfield PD, Zhu T, et al. Novel approach to documenting expert ECG interpretation using eye tracking technology: a historical and biographical representation of the late Dr Rory Childers in action. Journal of Electrocardiology. 2015;48:43–44.

Bowers VA, Snyder HL. Concurrent versus retrospective verbal protocol for comparing window usability. Proceedings of the Human Factors and Ergonomics Society Annual Meeting. 1990;34(17):1270–1274.

Brady S, Dunne LE, Tynan R, Diamond D, Smyth B, O'Hare G. Garment-based monitoring of respiration rate using a foam pressure sensor. In: Proceedings of the Ninth IEEE International Symposium on Wearable Computers. Los Alamitos: IEEE Computer Society; 2005;214–215.

Branco P, Firth P, Miguel EL, Bonato P. Faces of emotion in human-computer interaction. In: CHI '05 Extended Abstracts on Human Factors in Computing Systems, Portland, OR, USA. New York: ACM; 2005;1236–1239.

Brown SL, Richardson M. The effect of distressing imagery on attention to and persuasiveness of an anti-alcohol message: a gaze-tracking approach. Health Education & Behavior. 2012;39:8–17.

Buscher G, Cutrell E, Morriss MR. What do you see when you're surfing?: using eye tracking to predict salient regions of web pages. In: Proceedings of the 27th International Conference on Human Factors in Computing Systems, Boston, MA, USA. New York: ACM; 2009; pp. 21–30.

Cacioppo JT, Bernston GG, Larsen JT, Poehlmann KM, Ito TA. The psychophysiology of emotion. In: Lewis M, Haviland-Jones JM, eds. Handbook of Emotions. New York: The Guilford Press; 2000;173–191.

Card SK, Pirolli P, Van Der Wege M, et al. Information scent as a driver of Web behavior graphs: results of a protocol analysis method for Web usability. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Seattle, Washington, United States. New York: ACM; 2001;498–505.

Chen MC, Anderson JR, Sohn MH. What can a mouse cursor tell us more?: correlation of eye/mouse movements on web browsing. In: CHI '01 Extended Abstracts on Human Factors in Computing Systems, Seattle, Washington. New York: ACM; 2001;281–282.

Clark RA, Pua Y-H, Fortin K, et al. Validity of the Microsoft Kinect for assessment of postural control. Gait & Posture. 2012;36(3):372–377.

Clemente M, Rey B, Rodríguez-Pujadas A, et al. An fMRI study to analyze neural correlates of presence during virtual reality experiences. Interacting with Computers. 2014;26(3):269–284.

Costanza E, Inverso SA, Allen R, Maes P. Intimate interfaces in action: assessing the usability and subtlety of EMG-based motionless gestures. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, San Jose, California, USA. New York: ACM; 2007;29–36.

Crowe EC, Narayanan NH. Comparing interfaces based on what users watch and do. In: Proceedings of the 2000 Symposium on Eye Tracking Research & Applications, Palm Beach Gardens, Florida, United States. New York: ACM;.

Cutrell E, Guan Z. What are you looking for?: an eye-tracking study of information usage in web search. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, San Jose, California, USA. New York: ACM; 2007;407–416.

Demmans C, Subramanian S, Titus J. Posture monitoring and improvement for laptop use. In: CHI '07 Extended Abstracts on Human Factors in Computing Systems, San Jose, CA, USA. New York: ACM; 2007;2357–2362.

Diaz F, White R, Buscher G, Liebling D. Robust models of mouse movement on dynamic web search results pages. In: Proceedings of the 22nd ACM International Conference on Information & Knowledge Management, San Francisco, California, USA. New York: ACM; 2013;1451–1460.

Ding D, Hiremath S, Chung Y, Cooper R. Detection of wheelchair user activities using wearable sensors. In: Stephanidis C, ed. Universal Access in Human-Computer Interaction, Context Diversity: 6th International Conference, UAHCI 2011, Held as Part of HCI International 2011, Orlando, FL, USA, July 9–14, 2011, Part III. Berlin: Springer; 2011;145–152.

Doberne JW, He Z, Mohan V, Gold JA, Marquard J, Chiang MF. Using high-fidelity simulation and eye tracking to characterize EHR workflow patterns among hospital physicians. In: AMIA Annual Symposium Proceedings 2015. 2015;1881–1889.

Duchowski A. Eye-Tracking Methodology: Theory and Practice. New York: Springer; 2007.

Dunne LE, Smyth B. Psychophysical elements of wearability. In: Proceedings of the SIGCHI Conference on Human factors in Computing Systems, San Jose, California, USA. New York: ACM; 2007;299–302.

Dunne LE, Brady S, Tynan R, et al. Garment-based body sensing using foam sensors. In: Proceedings of the 7th Australasian User Interface Conference, Volume 50. Hobart, Australia. Darlinghurst: Australian Computer Society; 2006a;165–171.

Dunne LE, Walsh P, Smyth B, Caulfield B. Design and Evaluation of a Wearable Optical Sensor for Monitoring Seated Spinal Posture. In: 10th IEEE International Symposium on Wearable Computers, Montreux, Switzerland, IEEE. 2006b;65–68.

Durning SJ, Artino AR, Beckman TJ, et al. Does the think-aloud protocol reflect thinking? Exploring functional neuroimaging differences with thinking (answering multiple choice questions) versus thinking aloud. Medical Teacher. 2013;35(9):720–726.

Dutta T. Evaluation of the Kinect™ sensor for 3-D kinematic measurement in the workplace. Applied Ergonomics. 2012;43(4):645–649.

Embi PJ, Yackel TR, Logan JR, Bowen JL, Cooney TG, Gorman PN. Impacts of computerized physician documentation in a teaching hospital: perceptions of faculty and resident physicians. Journal of the American Medical Informatics Association. 2004;11(4):300–309.

Fong A, Hoffman DJ, Zachary Hettinger A, Fairbanks RJ, Bisantz AM. Identifying visual search patterns in eye gaze data; gaining insights into physician visual workflow. Journal of the American Medical Informatics Association. 2016;23(6):1180–1184.

Fono D, Vertegaal R. EyeWindows: evaluation of eye-controlled zooming windows for focus selection. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Portland, Oregon, USA. New York: ACM; 2005;151–160.

Fouse A, Weibel N, Hutchins E, Hollan JD. ChronoViz: a system for supporting navigation of time-coded data. In: CHI '11 Extended Abstracts on Human Factors in Computing Systems, Vancouver, BC, Canada. New York: ACM; 2011;299–304.

Fudickar S, Karth C, Mahr P, Schnor B. Fall-detection simulator for accelerometers with in-hardware preprocessing. In: Proceedings of the 5th International Conference on PErvasive Technologies Related to Assistive Environments, Heraklion, Crete, Greece. New York: ACM; 2012;1–7.

Goldberg JH, Stimson MJ, Lewenstein M, Scott N, Wichansky AM. Eye tracking in web search tasks: design implications. In: Proceedings of the 2002 Symposium on Eye Tracking Research & Applications, New Orleans, Louisiana. New York: ACM; 51–58.

Guan Z, Cutrell E. An eye tracking study of the effect of target rank on web search. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, San Jose, California, USA. New York: ACM; 2007;417–420.

Guan Z, Lee S, Cuddihy E, Ramey J. The validity of the stimulated retrospective think-aloud method as measured by eye tracking. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Montreal, Quebec, Canada. New York: ACM; 2006;1253–1262.

Gwizdka J, Zhang Y. Differences in eye-tracking measures between visits and revisits to relevant and irrelevant web pages. In: Proceedings of the 38th International ACM SIGIR Conference on Research and Development in Information Retrieval, Santiago, Chile. New York: ACM; 2015;811–814.

Haapalainen E, Kim S, Forlizzi JF, Dey AK. Psycho-physiological measures for assessing cognitive load. In: Proceedings of the 12th ACM International Conference on Ubiquitous computing, Copenhagen, Denmark. New York: ACM; 2010;301–310.

Han J, Shao L, Xu D, Shotton J. Enhanced computer vision with microsoft Kinect sensor: a review. IEEE Transactions on Cybernetics. 2013;43(5):1318–1334.

Harrison D, Marshall P, Berthouze N, Bird J. Tracking physical activity: problems related to running longitudinal studies with commercial devices. In: Proceedings of the 2014 ACM International Joint Conference on Pervasive and Ubiquitous Computing: Adjunct Publication, Seattle, Washington. New York: ACM; 699–702.

Hart SG. Nasa-Task Load Index (NASA-TLX); 20 years later. Proceedings of the Human Factors and Ergonomics Society Annual Meeting. 2006;50(9):904–908.

Hart SG, Staveland LE. Development of NASA-TLX (Task Load Index): results of empirical and theoretical research. In: Peter AH, Najmedin M, eds. Amsterdam: North-Holland; 1988;139–183. Advances in Psychology. vol. 52.

Hazlett R. Measurement of user frustration: a biologic approach. In: CHI '03 Extended Abstracts on Human Factors In Computing Systems, Ft. Lauderdale, Florida, USA. New York: ACM; 2003;734–735.

Hazlett R. Measuring emotional valence during interactive experiences: boys at video game play. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Montréal, Québec, Canada. New York: ACM; 2006;1023–1026.

Hazlett RL, Benedek J. Measuring emotional valence to understand the user's experience of software. International Journal of Human–Computer Studies. 2006;65(4):306–314.

Higuch K, Yonetani R, Sato Y. Can eye help you?: effects of visualizing eye fixations on remote collaboration scenarios for physical tasks. In: Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, Santa Clara, California, USA. New York: ACM; 5180–5190.

Hirshfeld LM, Girouard A, Solovey ET, et al. Human-computer interaction and brain measurement using functional near-infrared spectroscopy (poster paper). In: ACM Symposium on User Interface Software and Technology (UIST). 2007.

Hornof A, Cavender A, Hoselton R. Eyedraw: a system for drawing pictures with eye movements. In: Proceedings of the 6th International ACM SIGACCESS Conference on Computers and Accessibility, Atlanta, GA, USA. New York: ACM; 2004;86–93.

Huang J, White R, Buscher G. User see, user point: gaze and cursor alignment in web search. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Austin, Texas, USA. New York: ACM; 2012;1341–1350.

Huang L-L, Chen M-H, Wang C-H, Lee C-F. Developing a digital game for domestic stroke patients' upper extremity rehabilitation—design and usability assessment. In: Antona M, Stephanidis C, eds. Universal Access in Human-Computer Interaction. Access to Learning, Health and Well-Being: 9th International Conference, UAHCI 2015, Held as Part of HCI International 2015, Los Angeles, CA, USA, August 2–7, 2015, Part III. Cham: Springer International Publishing; 2015;454–461.

Izzetoglu K, Bunce S, Onaral B, Pourrezaei K, Chance B. Functional optical brain imaging using near-infrared during cognitive tasks. International Journal of Human–Computer Interaction. 2004;17(2):211–231.

Jacob RJK, Karn KS. Commentary on section 4 Eye tracking in human-computer interaction and usability research: ready to deliver the promises. In: Hyona J, Radach R, Deubel H, eds. The Mind's Eyes: Cognitive and Applied Aspects of Eye Movements. Oxford: Elsevier Science; 2003.

Jalaliniya S, Mardanbegi D, Sintos I, Garcia DG. EyeDroid: an open source mobile gaze tracker on Android for eyewear computers. In: Adjunct Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2015 ACM International Symposium on Wearable Computers, Osaka, Japan. New York: ACM; 873–879.

Jiang X, Atkins MS, Tien G, Bednarik R, Zheng B. Pupil responses during discrete goal-directed movements. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Toronto, Ontario, Canada. New York: ACM; 2014;2075–2084.

Johansen SA, Agustin JS, Skovsgaard H, Hansen JP, Tall M. Low cost vs high-end eye tracking for usability testing. In: CHI '11 Extended Abstracts on Human Factors in Computing Systems, Vancouver, BC, Canada. New York: ACM; 2011;1177–1182.

Kaewkannate K, Kim S. A comparison of wearable fitness devices. BMC Public Health. 2016;16(1):1–16.

Kim J-W, Kim H-J, Nam T-J. M Gesture: an acceleration-based gesture authoring system on multiple handheld and wearable devices. In: Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, Santa Clara, California, USA. New York: ACM; 2307–2318.

Kitamura Y, Yamaguchi Y, Hiroshi I, Kishino F, Kawato M. Things happening in the brain while humans learn to use new tools. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Ft. Lauderdale, Florida, USA. New York: ACM; 2003;417–424.

Klingner J, Kumar R, Hanrahan P. Measuring the task-evoked pupillary response with a remote eye tracker. In: Proceedings of the 2008 Symposium on Eye Tracking Research & Applications, Savannah, Georgia. New York: ACM; 69–72.

Kocejko T, Goforth K, Moidu K, Wtorek J. Visual attention distribution based assessment of user's skill in electronic medical record navigation. Journal of Medical Imaging and Health Informatics. 2015;5:951–958.

Krafka K, Khosla A, Kellnhofer P, et al. Eye tracking for everyone. In: IEEE Conference on Computer Vision and Pattern Recognition (CVPR). 2016.

Krupinski EA, Tillack AA, Richter L, et al. Eye-movement study and human performance using telepathology virtual slides: implications for medical education and differences with experience. Human Pathology. 2006;37:1543–1556.

Kumar M. Reducing the Cost of Eye Tracking Systems. Stanford University Computer Science Technical Report 2006.

Kumar M, Paepcke A, Winograd T. EyePoint: practical pointing and selection using gaze and keyboard. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, San Jose, California, USA. New York: ACM; 421–430.

Lee JC, Tan DS. Using a low-cost electroencephalograph for task classification in HCI research. In: Proceedings of the 19th Annual ACM Symposium on User Interface Software and Technology, Montreux, Switzerland. New York: ACM; 2006;81–90.

Lee H, Lee J, Seo S. Brain response to good and bad design. In: Jacko JA, ed. Human-Computer Interaction. New Trends: 13th International Conference, HCI International 2009, San Diego, CA, USA, July 19–24, 2009, Part I. Berlin, Heidelberg: Springer; 2009;111–120.

Lee MK, Kim J, Forlizzi J, Kiesler S. Personalization revisited: a reflective approach helps people better personalize health services and motivates them to increase physical activity. In: Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing, Osaka, Japan. New York: ACM; 743–754.

Levin G, Yarin P. Bringing sketching tools to keychain computers with an acceleration-based interface. In: CHI '99 Extended Abstracts on Human Factors in Computing Systems, Pittsburgh, Pennsylvania. New York: ACM; 1999;268–269.

Liebling DJ, Dumais ST. Gaze and mouse coordination in everyday work. In: Proceedings of the 2014 ACM International Joint Conference on Pervasive and Ubiquitous Computing Adjunct Publication, UbiComp '14 Adjunct, New York, NY, USA. New York: ACM Press; 1141–1150.

Lukanov K, Maior HA, Wilson ML. Using fNIRS in usability testing: understanding the effect of web form layout on mental workload. In: Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, Santa Clara, California, USA. New York: ACM; 4011–4016.

Mahlke S, Minge M, Thüring M. Measuring multiple components of emotions in interactive contexts. In: CHI '06 Extended Abstracts on Human Factors in Computing Systems, Montréal, Québec, Canada. New York: ACM; 2006;1061–1066.

Mandryk RL, Inkpen K. Physiological indicators for the evaluation of co-located collaborative play. In: Proceedings of the 2004 ACM Conference on Computer Supported Cooperative Work, Chicago, Illinois, USA. New York: ACM; 102–111.

Marshall J, Linehan C, Hazzard A. Designing brutal multiplayer video games. In: Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, Santa Clara, California, USA. New York: ACM; 2669–2680.

Mathan S, Whitlow S, Erdogmus D, Pavel M, Ververs P, Dorneich M. Neurophysiologically driven image triage: a pilot study. In: CHI '06 Extended Abstracts on Human Factors in Computing Systems, Montréal, Québec, Canada. New York: ACM; 2006;1085–1090.

Mazur LM, Mosaly PR, Moore C, et al. Toward a better understanding of task demands, workload, and performance during physician-computer interactions. Journal of the American Medical Informatics Association. 2016;23(6):1113–1120.

Mehner S, Klauck R, Koenig H. Location-independent fall detection with smartphone. In: Proceedings of the 6th International Conference on Pervaise Technologies Related to Assistive Environments, Rhodes, Greece. New York: ACM; 2013;1–8.

Meiselwitz G, Wentz B, Lazar J. Universal usability: past, present, and future. Foundations and Trends in Human-Computer Interaction. 2010;3(4):213–333.

Millán JDR. Adaptive brain interfaces. Communications of the ACM. 2003;46(3):74–80.

Moacdieh N, Sarter N. Clutter in electronic medical records: examining its performance and attentional costs using eye tracking. Human Factors. 2015;57:591–606.

Montague E, Asan O. Dynamic modeling of patient and physician eye gaze to understand the effects of electronic health records on doctor-patient communication and attention. International Journal of Medical Informatics. 2014;83(3):225–234.

Mostafa J, Gwizdka J. Deepening the role of the user: neuro-physiological evidence as a basis for studying and improving search. In: Proceedings of the 2016 ACM on Conference on Human Information Interaction and Retrieval, Carrboro, North Carolina, USA. New York: ACM; 63–70.

Muñoz JE, Chavarriaga R, Lopez DS. Application of hybrid BCI and exergames for balance rehabilitation after stroke. In: Proceedings of the 11th Conference on Advances in Computer Entertainment Technology, Funchal, Portugal. New York: ACM; 2014;1–4.

Murata A. Eye-gaze input versus mouse: cursor control as a function of age. International Journal of Human–Computer Interaction. 2006;21(1):1–14.

Mutlu B, Krause A, Forlizzi J, Guestrin C, Hodgins J. Robust, low-cost, non-intrusive sensing and recognition of seated postures. In: Proceedings of the 20th Annual ACM Symposium on User Interface Software and Technology, Newport, Rhode Island, USA. New York: ACM; 2007;149–158.

Navalpakkam V, Jentzsch L, Sayres R, Ravi S, Ahmed A, Smola A. Measurement and modeling of eye-mouse behavior in the presence of nonlinear page layouts. In: Proceedings of the 22nd International Conference on World Wide Web, Rio de Janeiro, Brazil, May 13–17. New York: ACM; 2013;953–964.

Nebeling M, Ott D, Norrie MC. Kinect analysis: a system for recording, analysing and sharing multimodal interaction elicitation studies. In: Proceedings of the 7th ACM SIGCHI Symposium on Engineering Interactive Computing Systems, Duisburg, Germany. New York: ACM; 2015;142–151.

Nielsona JA, Mamidala RN, Khan J. In-situ eye-tracking of emergency physician result review. Studies in Health Technology and Informatics. 2013;192:1156.

Ogata M, Imai M. SkinWatch: skin gesture interaction for smart watch. In: Proceedings of the 6th Augmented Human International Conference, Singapore, Singapore. New York: ACM; 2015;21–24.

O'Hara K, Morrison C, Sellen A, Bianchi-Berthouze N, Craig C. Body tracking in healthcare. Synthesis Lectures on Assistive, Rehabilitative, and Health-Preserving Technologies. 2016;5(1):1–151.

Paletta L, Neuschmied H, Schwarz M, et al. Smartphone eye tracking toolbox: accurate gaze recovery on mobile displays. In: Proceedings of the Symposium on Eye Tracking Research and Applications, Safety Harbor, Florida. New York: ACM; 2014;367–368.

Peck EMM, Yuksel BF, Ottley A, Jacob RJK, Chang R. Using fNIRS brain sensing to evaluate information visualization interfaces. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Paris, France. New York: ACM; 2013;473–482.

Pfeuffer K, Alexander J, Gellersen H. Partially-indirect bimanual input with gaze, pen, and touch for pan, zoom, and ink interaction. In: Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, Santa Clara, California, USA. New York: ACM; 2845–2856.

Pian W, Khoo SGC, Chang Y-K. The criteria people use in relevance decisions on health information: an analysis of user eye movements when browsing a health discussion forum. Journal of Medical Internet Research. 2016;18e136.

Pike MF, Maior HA, Porcheron M, Sharples SC, Wilson ML. Measuring the effect of think aloud protocols on workload using fNIRS. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Toronto, Ontario, Canada. New York: ACM; 2014;3807–3816.

Pirolli P, Card SK, Van Der Wege MM. The effect of information scent on searching information: visualizations of large tree structures. In: Proceedings of the Working Conference on Advanced Visual Interfaces, Palermo, Italy. New York: ACM; 2000;161–172.

Porzi L, Messelodi S, Modena CM, Ricci E. A smart watch-based gesture recognition system for assisting people with visual impairments. In: Proceedings of the 3rd ACM International Workshop on Interactive Multimedia on Mobile & Portable Devices, Barcelona, Spain. New York: ACM; 2013;19–24.

Quintana R, Quintana C, Madeira C, Slotta JD. Keeping watch: exploring wearable technology designs for K-12 teachers. In: Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in Computing Systems, Santa Clara, California, USA. New York: ACM; 2272–2278.

Raez MBI, Hussain MS, Mohd-Yasin F. Techniques of EMG signal analysis: detection, processing, classification and applications. Biological Procedures Online. 2006;8.

Rahman T, Adams AT, Ravichandran RV, et al. DoppleSleep: a contactless unobtrusive sleep sensing system using short-range Doppler radar. In: Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing, Osaka, Japan. New York: ACM; 39–50.

Reid GB, Nygren TE. The subjective workload assessment technique: a scaling procedure for measuring mental workload. In: Peter AH, Najmedin M, eds. Advances in Psychology. Amsterdam: North-Holland; 1988;185–218.

Ren L, Zhang Q, Shi W. Low-power fall detection in home-based environments. In: Proceedings of the 2nd ACM International Workshop on Pervasive Wireless Healthcare, Hilton Head, South Carolina, USA. New York: ACM; 2012;39–44.

Rick S, Calvitti A, Agha Z, Weibel N. Eyes on the clinic: accelerating meaningful interface analysis through unobtrusive eye tracking. In: 9th International Conference on Pervasive Computing Technologies for Healthcare. 2015;213–216.

Rooksby J, Rost M, Morrison A, Chalmers MC. Personal tracking as lived informatics. In: Proceedings of the 32nd Annual ACM Conference on Human Factors in Computing Systems, Toronto, Ontario, Canada. New York: ACM; 2014;1163–1172.

Rowe DW, Sibert J, Irwin D. Heart rate variability: indicator of user state as an aid to human-computer interaction. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Los Angeles, California, United States. New York: ACM Press/Addison-Wesley Publishing Co.; 1998;480–487.

Scheirer J, Fernandez R, Klein J, Picard RW. Frustrating the user on purpose: a step toward building an affective computer. Interacting with Computers. 2002;14:93–118.

Schlömer T, Poppinga B, Henze N, Bolll S. Gesture recognition with a Wii controller. In: Proceedings of the 2nd International Conference on Tangible and Embedded Interaction, Bonn, Germany. New York: ACM; 2008;11–14.

Shahabi C, Kiyoung Y, Hyunjin Y, et al. Immersidata analysis: four case studies. Computer. 2007;40(7):45–52.

Shi J, Alt F. The anonymous audience analyzer: visualizing audience behavior in public space. In: Proceedings of the 2016 CHI Conference Extended Abstracts on Human Factors in Computing Systems, Santa Clara, California, USA. New York: ACM; 3766–3769.

Shi Y, Ruiz N, Taib R, Choi E, Chen F. Galvanic skin response (GSR) as an index of cognitive load. In: CHI '07 Extended Abstracts on Human Factors in Computing Systems, San Jose, CA, USA. New York: ACM; 2007;2651–2656.

Singh P, Juneja N, Kapoor S. Using mobile phone sensors to detect driving behavior. In: Proceedings of the 3rd ACM Symposium on Computing for Development, Bangalore, India. New York: ACM; 2013;1–2.

Sjölie D, Bodin K, Elgh E, Eriksson J, Janlert L-E, Nyberg L. Effects of interactivity and 3D-motion on mental rotation brain activity in an immersive virtual environment. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Atlanta, Georgia, USA. New York: ACM; 2010;869–878.

Solovey E, Schermerhorn P, Scheutz M, Sassaroli A, Fantini S, Jacob R. Brainput: enhancing interactive systems with streaming fNIRS brain input. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Austin, Texas, USA. New York: ACM; 2012;2193–2202.

Stellmach S, Dachselt R. Still looking: investigating seamless gaze-supported selection, positioning, and manipulation of distant targets. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Paris, France. New York: ACM; 2013;285–294.

Steptoe W, Wolff R, Murgia A, et al. Eye-tracking for avatar eye-gaze and interactional analysis in immersive collaborative virtual environments. In: Proceedings of the ACM 2008 Conference on Computer Supported Cooperative Work, San Diego, CA, USA. New York: ACM; 2008;197–200.

Stern RM, Ray WJ, Quigley KS. Psychophysiological Recording. Oxford: Oxford University Press; 2001.

Tang TY, Winoto P, Wang YF. Alone together: a multiplayer augmented reality online ball passing game. In: Proceedings of the 18th ACM Conference Companion on Computer Supported Cooperative Work & Social Computing, Vancouver, BC, Canada. New York: ACM; 2015;37–40.

Tanveer MI, Zhao R, Chen K, Tiet Z, Hoque ME. AutoManner: An Automated Interface for Making Public Speakers Aware of Their Mannerisms. In: Proceedings of the 21st International Conference on Intelligent User Interfaces, Sonoma, California, USA. New York: ACM; 2016;385–396.

Taylor P. EyeFrame: real-time memory aid improves human multitasking via domain-general eye tracking procedures. Frontiers in ICT. 2015;2.

Taylor B, Dey A, Siewiorek D, Smailagic A. Using physiological sensors to detect levels of user frustration induced by system delays. In: Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing, Osaka, Japan. New York: ACM; 517–528.

Tokuda S, Palmer E, Merkle E, Chaparro A. Using saccadic intrusions to quantify mental workload. Proceedings of the Human Factors and Ergonomics Society Annual Meeting. 2009;53(12):809–813.

Tokuda S, Obinata G, Palmer E, Chaparro A. Estimation of mental workload using saccadic eye movements in a free-viewing task. In: 2011 Annual International Conference of the IEEE Engineering in Medicine and Biology Society. 2011.

Venjakob AC, Mello-Thoms CR. Review of prospects and challenges of eye tracking in volumetric imaging. Journal of Medical Imaging. 2015;3(1):011002.

Venjakob AC, Marnitz T, Phillips P, Mello-Thoms CR. Image size influences visual search and perception of hemorrhages when reading cranial CT: an eye-tracking study. Human Factors: The Journal of the Human Factors and Ergonomics Society. 2016;58(3):441–451.

Voida A, Greenberg S. Wii all play: the console game as a computational meeting place. In: Proceedings of the 27th International Conference on Human Factors in Computing Systems, Boston, MA, USA. New York: ACM; 2009;1559–1568.

Wallen MP, Gomersall SR, Keating SE, Wisløff U, Coombes JS. Accuracy of heart rate watches: implications for weight management. PLoS ONE. 2016;11e0154420.

Wang Y-X, Lo L-Y, Hu M-C. Eat as much as you can: a Kinect-based facial rehabilitation game based on mouth and tongue movements. In: Proceedings of the 22nd ACM International Conference on Multimedia, Orlando, Florida, USA. New York: ACM; 2014;743–744.

Wang EJ, Lee T-J, Mariakakis A, Goel M, Gupta S, Patel SN. MagnifiSense: inferring device interaction using wrist-worn passive magneto-inductive sensors. In: Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing, Osaka, Japan. New York: ACM; 15–26.

Wastell DG, Newman M. Stress, control and computer system design: a psychophysiological field study. Behaviour & Information Technology. 1996;15:183–192.

Weibel N, Rick S, Emmenegger C, Ashfaq S, Calvitti A, Agha Z. LAB-IN-A-BOX: semi-automatic tracking of activity in the medical office. Personal and Ubiquitous Computing. 2014;19:317–334.

Wen H, Rojas JR, Dey AK. Serendipity: finger gesture recognition using an off-the-shelf smartwatch. In: Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, Santa Clara, California, USA. New York: ACM; 3847–3851.

Whalen T, Inkpen KM. Gathering evidence: use of visual security cues in web browsers. In: Proceedings of Graphics Interface 2005, Victoria, BC. Canadian Human-Computer Communications Society 2005.

Wright MC, Dunbar S, Moretti EW, Schroeder RA, Taekman J, Segall N. Eye-tracking and retrospective verbal protocol to support information systems design. Proceedings of the International Symposium on Human Factors and Ergonomics in Health Care. 2013;2:30–37.

Xu S, Jiang H, Lau F. User-oriented document summarization through vision-based eye-tracking. In: Proceedings of the 13th International Conference on Intelligent User Interfaces, Sanibel Island, Florida, USA. New York: ACM; 2009;7–16.

Xu C, Pathak PH, Mohapatra P. Finger-writing with smartwatch: a case for finger and hand gesture recognition using smartwatch. In: Proceedings of the 16th International Workshop on Mobile Computing Systems and Applications, Santa Fe, New Mexico, USA. New York: ACM; 2015;9–14.

Yang R, Shin E, Newman MW, Ackerman MS. When fitness trackers don't ‘fit’: end-user difficulties in the assessment of personal tracking device accuracy. In: Proceedings of the 2015 ACM International Joint Conference on Pervasive and Ubiquitous Computing, Osaka, Japan. New York: ACM; 623–634.

Yuasa M, Saito K, Mukawa N. Emoticons convey emotions without cognition of faces: an fMRI study. In: CHI '06 Extended Abstracts on Human Factors in Computing Systems, Montréal, Québec, Canada. New York: ACM; 2006;1565–1570.

Yun S, Chen Y-C, Qiu L. Turning a mobile device into a mouse in the air. In: Proceedings of the 13th Annual International Conference on Mobile Systems, Applications, and Services, Florence, Italy. New York: ACM; 2015;15–29.

Zhai S, Morimoto C, Ihde S. Manual and gaze input cascaded (MAGIC) pointing. In: SIGCHI Conference on Human Factors in Computing Systems, Pittsburgh, PA, USA. New York: ACM; 1999;246–253.

Zhang Z. Microsoft Kinect sensor and its effect. IEEE MultiMedia. 2012;19(2):4–10.

Zhang Z. Vision-enhanced immersive interaction and remote collaboration with large touch displays. In: Proceedings of the 23rd ACM International Conference on Multimedia, Brisbane, Australia. New York: ACM; 2015;3–4.

Zheng K, Hanauer DA, Weibel N, Agha Z. Computational ethnography: automated and unobtrusive means for collecting data in situ for human-computer interaction evaluation studies. In: Patel LV, Kannampallil GT, Kaufman RD, eds. Cognitive Informatics for Biomedicine: Human Computer Interaction in Healthcare. Cham: Springer International Publishing; 2015;111–140.

