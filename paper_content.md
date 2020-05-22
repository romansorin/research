# Textual content for research paper

- [Textual content for research paper](#textual-content-for-research-paper)
  - [Details](#details)
    - [Title: Identification and Measurement of Hierarchical Layout Patterns on User Experience](#title-identification-and-measurement-of-hierarchical-layout-patterns-on-user-experience)
    - [Author: Roman Sorin](#author-roman-sorin)
    - [Email: roman@romansorin.com](#email-romanromansorincom)
    - [Affiliation: Mentor High School](#affiliation-mentor-high-school)
  - [Introduction](#introduction)
  - [Method](#method)
    - [Participants](#participants)
    - [Design](#design)
    - [Analytical Procedure](#analytical-procedure)
    - [Experimental Procedure](#experimental-procedure)
  - [Results](#results)
  - [Discussion and Conclusion](#discussion-and-conclusion)
  - [Appendix](#appendix)
  - [References](#references)

## Details

### Title: Identification and Measurement of Hierarchical Layout Patterns on User Experience

### Author: Roman Sorin

### Email: roman@romansorin.com

### Affiliation: Mentor High School

## Introduction

User experience (UX) has continually developed in the field of software engineering and is seen as being highly integral to the success and usability of an application [5]. Alongside concepts such as accessibility and presence of I18n in interfaces, perceived user experiences—notable traits such as design, animation, and usability—are one of the most important aspects to consider in the development and analysis of interactions [10]. Seen both within and beyond software, reputable products and services are known to utilize effective user experience in creating a product that attracts and retains consumers, subsequently expanding the product influence. User experience drives both offline and online interactions that result in psychological and economic impact on consumers and businesses. User experience is a broad and highly expansive field that can take the form of layouts; colors; fonts; copy; animations; and more granular aspects of design and interaction, making UX highly complex to assess and properly execute. In this study, the impact which hierarchical layout structure and design patterns have will be of focus to approach user experience in web interfaces from a bottom-up approach and architectural stance, addressing the fundamental integration of components in the presentational layer.

From one perspective, user experience is derived from the physiological interaction between user and system [11]. As interfaces and applications are developed further to suit the needs of consumers and developers alike, there exists a significant need to address the psychological implications of human-computer interaction (HCI) in a more focused and detailed pursuit. Conversely, this continual development of products and experiences creates a significant amount of both practical and technical applications for user experience to manifest itself within, providing for new theses and findings. Within the previous decades, several studies have explored the importance of user experience on this success of products and applications [9, 8, 3] in various facets. A common pattern that exists in much of the current research on user experience regards the aesthetics and appearance of a website with consideration of both higher and lower-level abstraction. When analyzing judgment and response by users, aesthetic and appearance is a large determinant in utilization and rates of recurrence [7]. In the domain of product and application development, the quality of the experience is extremely vital in progressive rates of user retention, user satisfaction, revenues from sales and advertising, and other analytical measures that are used to determine the relative success of a product or application. Of the serious need for appealing and usable interfaces are businesses that rely on online traffic for customers, and identification and use of these interfaces may provide an advantage over the competition; increasing revenue and attraction by customers to the respective site [7]. Consequently, definitive data on optimal layouts by use cases can serve as being beneficial to businesses in both financial and social capital. Moreover, synonymous with the DRY and SOLID principles used in software engineering,designers may look to these data to optimize their processes and focus on more granular parts of the system; and developers can be more oriented towards releasing minimum viable products (MVPs) with confidence and reasoning for utilizing a given layout.

Correspondingly, machine learning (ML) and deep learning algorithms have undergone significant developments and continue to advance in their rates of application [15]. The use of deep learning in machine learning has allowed for solving more complex artificial intelligence tasks, including object and pattern recognition [6], a concept that will be fundamental in the findings within this paper [15]. More specifically, applications of machine learning such as convolutional neural networks (CNNs) [12], pattern recognition, and image classification establish opportunities for automated image caption and description generation [14], labeling of features and objects [2], and identifying common patterns within a set of images [13]. In this context, hierarchical features describe the components found within a layout, and a layout may thus be referred to as layout hierarchy.

A major limitation of UX and its applicability is the granularity found within even the foundational layouts, ignoring any higher-level or specific abstractions. Layouts are recursive and cascading, consisting of components which contain a great degree of subjectivity, development, and iterative processes. These iterative processes take a significant amount of time to implement and analyze, relating to the engineering debt that occurs within design and development [4]. Considering the complexity of an interface composed of several different components (all of which are recursive and componentized themselves), the difficulty in achieving an optimal layout in terms of UX is quite evident. As such, the fluidity of design is likely a reason behind the lack of data and definition of layouts, despite patterns in layouts being common and each being utilized in thousands of cases. Even as UX expands as a field and significant area of focus within software engineering, research is relatively limited and restricted to case studies and internal data at best, suggesting a need for a method for identifying these data.

While the fields of software engineering and machine learning have been individually addressed and developed, there has yet to be studies that consider the integration of machine learning with the user experience facet in software engineering. Moreover, there are no definite data on how layout hierarchies affect UX metrics. The capability for pattern recognition and hierarchical analysis using machine learning is of high importance concerning layouts and user experience, as models may present possible solutions for identifying patterns within layouts using models and generating labels that may be implemented to identify these desired metrics. Consequently, two research questions are presented:

(1) How does layout hierarchy impact user experience, and what metrics are potentially associated with hierarchical features?
(2) How can hierarchical features best be implemented to optimize overall user experience?

In data sets which contain a large number of samples, such as a set of the highest indexed sites on the web (minimum 10,000+ indices), manual identification of both common and more intricate patterns are incredibly difficult to find and waste resources. In contrast, statistical methods and the use of trained algorithmic models will have higher rates of success in identifying patterns that may otherwise not be seen. Thus, there is a chance that integrating algorithmic models into site analysis to identify patterns may more significantly benefit the field of software engineering. Because of the aforementioned limitations of manual analysis, layouts and structures which are deemed to be efficient and successful are strictly subjective and reported on an "at-will" basis; this information may come from individual analyses or findings by user experience researchers within case studies or companies. Thus, this paper proposes an approach to find objective data through the collection of existing sites from Alexa Top Sites [1], then programmatically collect screenshots of every site, which will then be fed into a model to identify patterns in layouts. By itself, these data will be of little value to the purpose of this paper and therefore requires implementation and an experimental investigation to identify what metrics are associated in practice rather than strict ranking. Thus, this paper seeks to identify the most common layout hierarchies and patterns seen in the highest-indexing sites and measure which UX metrics can be best associated with a given layout or features.

## Method

### Participants

The study involved 57 individuals who voluntarily participated in the experimental portion of layout analysis. Individuals were age 18 and older, with all participants being from the United States. All participants were expected to have familiarity and experience with navigating layouts and websites, and several individuals had several years of work experience in software engineering and computer science. No compensation or reimbursement was provided for voluntary involvement in the study. All participants successfully completed the experiment. Participants were recruited through direct and indirect advertisement/sharing of the study. Participation was limited to devices with a minimum screen width of 1024px (large breakpoint), as only desktop-based layout interfaces were presented. After the experiment, participants were thanked and then provided with an email for further inquiries.


### Design

A paired analytical and experimental approach was taken to identify common layouts and their potential association to user behavior. The analytical procedure utilized scripts and applications [repository] built specifically for this study to query various APIs, collect visual screenshot site data, and manipulate/process screenshots for use in KMeans clustering and image overlaying. These KMeans clusters were then assessed and analyzed to identify potential commonalities in layouts. Experimentally, a site dedicated to the experiment was built [mysite] to track user interaction with presented interfaces. In order to track user behavior, different analytics tools to identify demographics (location, estimated age), heatmaps and recordings were installed on the site (Google Analytics [ga] and Hotjar [hotjar], respectively). As the participant worked through the experiment, the timestamps of their session start and session end were collected and set in a document collection provided by Google Firebase's Cloud Firestore [firestore].

### Analytical Procedure

Analysis began by querying the AWS Alexa Top Sites API for an initial 1002 sites. The Top Sites API provides the highest ranking sites by region, and the region chosen was "global" for this experiment. After 1002 sites were returned, the responses had to be parsed and cleaned up to identify if there were any sites that were no longer active (i.e., a 500 error) or could not be connected to. Each of the sites were queried for status, and if they existed, an RGB screenshot of the home page (root URL) was taken. Due to lazy loading, infinite scroll, and asynchronous calls, screenshot height was limited to 30000 pixels. The driver then scrolled from each max scroll height every five seconds up until the screenshot maximium height, which upon reaching max height the driver jumped to the 0th pixel and rescrolled in increments of 200 pixels every 0.5 seconds and took a full page screenshot. This secondary scroll pass ensured that content would have loaded by the time the screenshot was taken. Pages that were not active were ignored by the driver, and the function moved to the next site. After all RGB screenshots were taken, a secondary image processing step was taken: conversion of all RGB sites to greyscale to eliminate the influence of color on clustering and image similarity. Many sites were found to have a presence of subdomains or TLDs due to regional or content differences, however these could not be automatically eliminated due to the fact that different subdomains could serve different purposes — a subdomain may map to a dashboard, another may handle support channels, etc. Instead, sites with the same root domain (ignoring both the subdomain and TLDs) were compared using an image similarity API provided by OpenAI. The greyscale versions of these same root domains but differing subdomains or TLDs were compared to each other; if the site similarity surpassed the arbitrary threshold of fifteen, the higher ranking site/screenshot was kept, and the comparison image was removed from the dataset. However, before image comparisons were done, every greyscale screenshot, regardless of comparison, or unique domains, was cropped to some found height. Filtered domains were sorted using insertion sort to identify base domain and duplicates. Width of the site remained constant due to all screenshots being taken on a single device (width of 2560px), though heights were dependent on the site. Screenshots were iterated over and a flag variable was created to identify the shortest/smallest height dimension to be used for cropping. In order to circumvent any technical glitches, a minimum height of 1440px was set using the opencv cv2 image manipulation lib. Images below this minimum height were removed. After ensuring that all screenshots can be considered "unique" content, these images were then fed into a Keras vgg16 K-Means clustering algorithm with k=4 clusters selected. Due to some clusters containing several hundred images, an image overlaying function was run inside of each cluster to generate subclusters of maximum 50 images each. Subclusters were displayed as a PNG, where the denser parts of the image (greyscale, overlayed weighted 50/50) represented the commonalities of objects/features in layouts. These features were then manually extracted and represented in a mockup. After each cluster's subclusters had mockups generated, mockups were analyzed and some features were detracted from the mockup due to overlapping features/clarity of the layout. After mockups From four clusters, three common layouts could be realistically created and identified, and mockups were then converted into web components with TailwindUI provided components. Each layout was then built out into a web app and a random string identifier was created for each variant. Session length was collected and inserted into Firebase Cloud Store.
Subdomain and root domain were split with a hyphen delimiter. Subdomain and TLD were analyzed separately.


### Experimental Procedure

The experiment was conducted on a website [cite my site] built to host the experiment and information related to the experiment. Upon viewing on the homepage, users were presented with a message describing the entire study in brief, directions for participation, and information on what data is collected and how it will be used. Consent was provided as users had to manually input their email and press "begin". Upon pressing begin, the participant was randomly assigned to one of three aforementioned layout variants, and they could not assign themselves to another interface. Participants were instructed to navigate and read through the information and structure of the interface as they typically would with a real-world product, and then attempt to register or purchase the presented product or service. After they pressed the relevant buttons/links to begin registration, they were then redirected to the final screen confirming that their participation in the experiment was finished.

## Results


A one way anova test for analysis of variance on the session lengths was used. It was found that not be to statistically significant at p < .10.

- kmeans may have not been the best approach
- possibly use feature / object detection/extraction for future studies


This paper proposes a potential approach to identifying common layouts in a given domain (e.g., ecommerce, business, healthcare, media) and optimization/analysis of the effectiveness of layouts.

explain how the selection of already computer and interface savvy users may have resulted in figures that were less representative of the actual market


Ideas for data analysis:
- Scatter plots of variants and session times (variant by color, Y axis is session length)
- correlation between session time and variant; abstract the reasoning out for whyu this could be (i.e., one variant has clearly presented information CTA over another)


Stage 0 site count:
1002
Stage 1 site count:
975
Stage 2 site count:
908

Cluster counts:
0 : 242 | 5 subclusters
1 : 125 | 3 subcl.
2 : 111 | 3 subcl.
3 : 385 | 8 subcl.

Implications:

Limitations:

Directions for research:

8nqXhdl3JD8u:
7
5
3
60
59
24
5
55
30
24
80
5
3
2
35
28
15
9
6
18
17


Minimum	min =	2
Maximum	max =	80
Range	range =	78
Size	n =	21
Sum	sum =	490
Mean	x¯¯¯ =	23.3333333333
Median	x˜ =	17
Mode	mode =	5
Standard Deviation	s =	22.621523674
Variance	s2 =	511.733333333
Mid Range	MR =	41
Quartiles		Quartiles:
Q1 --> 5
Q2 --> 17
Q3 --> 32.5
Interquartile Range	IQR =	27.5

hwVB0eKUehxy:
12
45
3
5
9
3
19
22
11
107
15
35
18
29
43
9
7
12
26
17
38
33

Minimum	min =	3
Maximum	max =	107
Range	range =	104
Size	n =	22
Sum	sum =	518
Mean	x¯¯¯ =	23.5454545455
Median	x˜ =	17.5
Mode	mode =	12, 3, 9
Standard Deviation	s =	22.6226335731
Variance	s2 =	511.783549784
Mid Range	MR =	55
Quartiles		Quartiles:
Q1 --> 9
Q2 --> 17.5
Q3 --> 33
Interquartile Range	IQR =	24

vtc5qYP2r8Ut:
40
37
6
38
3
37
47
54
37
10
17
12
24
4

Minimum	min =	3
Maximum	max =	54
Range	range =	51
Size	n =	14
Sum	sum =	366
Mean	x¯¯¯ =	26.1428571429
Median	x˜ =	30.5
Mode	mode =	37
Standard Deviation	s =	17.2709500111
Variance	s2 =	298.285714286
Mid Range	MR =	28.5
Quartiles		Quartiles:
Q1 --> 10
Q2 --> 30.5
Q3 --> 38
Interquartile Range	IQR =	28

+ exp. anova
+ 2nd parsed_res data
+ initial # -> parsed/clean # -> duped (domains) # -> cluster count -> subcluster count

Show example of subcluster layering process
Show media example (leave built variants in appendix?)

ONE-WAY ANOVA VARIANCE CALCULATIONS:
F-statistic value = 0.08421
P-value = 0.91936

Summary of Data						
	Treatments					
	1	2	3	4	5	Total
N	21	22	14			57
∑X	490	518	366			1374
Mean	23.3333	23.5455	26.1429			24.105
∑X2	21668	22944	13446			58058
Std.Dev.	22.6215	22.6226	17.271			21.1024

Result Details				
Source	SS	df	MS	
Between-treatments	77.5329	2	38.7665	F = 0.08421
Within-treatments	24859.8355	54	460.3673	
Total	24937.3684	56		
The f-ratio value is 0.08421. The p-value is .919361. The result is not significant at p < .10.

Heatmaps were installed but due to technical errors did not record behavior. This is a common avenue of identifying/tracking behavior (cite something here)


potential avenues:
working heatmaps
feature density / topographic images / contour maps
develop some quantitative metric for determing success/effectiveness of a layout 

tables:
number of initial sites, then parsed, then cluster_data
results (anova)
clusters



## Discussion and Conclusion

## Appendix

## References


[1-bibtex]@misc{antoniou_2015, title={Marketplace}, url={https://aws.amazon.com/marketplace/pp/B07QK2XWNV?qid=1555346599089&sr=0-1&ref_=srh_res_product_title}, journal={Amazon}, publisher={Scb Distributors}, author={Antoniou, Laura}, year={2015}}




[2-bibtex]@article{article,
author = {Farabet, Clement and Couprie, Camille and Najman, Laurent and Lecun, Yann},
year = {2013},
month = {08},
pages = {1915-1929},
title = {Learning Hierarchical Features for Scene Labeling},
volume = {35},
journal = {IEEE transactions on pattern analysis and machine intelligence},
doi = {10.1109/TPAMI.2012.231}
}


[3-bibtex]@article{article,
author = {Frederick, Dede},
year = {2015},
month = {02},
pages = {pp. 87-95},
title = {The Effects of Parallax Scrolling on User Experience in Web Design},
volume = {Volume 10},
journal = {Journal of Usability Studies}
}

[4-bibtex]@INPROCEEDINGS{4293575,
author={J. {Ferreira} and J. {Noble} and R. {Biddle}},
booktitle={Agile 2007 (AGILE 2007)},
title={Agile Development Iterations and UI Design},
year={2007},
volume={},
number={},
pages={50-58},
keywords={software engineering;user interfaces;agile development iteration;user interaction design;automated code testing;Software prototyping;Iterative methods;User interfaces;Software performance;Prototypes;Automatic testing;Software testing;Software quality;Process design;Usability},
doi={10.1109/AGILE.2007.8},
ISSN={null},
month={Aug},}

[5-bibtex]@article{10.1016/j.jvlc.2017.08.004,
author = {Desolda, Giuseppe and Ardito, Carmelo and Costabile, Maria Francesca and Matera, Maristella},
title = {End-User Composition of Interactive Applications through Actionable UI Components},
year = {2017},
issue_date = {October 2017},
publisher = {Academic Press, Inc.},
address = {USA},
volume = {42},
number = {C},
issn = {1045-926X},
url = {https://doi.org/10.1016/j.jvlc.2017.08.004},
doi = {10.1016/j.jvlc.2017.08.004},
journal = {J. Vis. Lang. Comput.},
month = oct,
pages = {46–59},
numpages = {14},
keywords = {Web service composition, Mashup model, Utilization study}
}
  


[6-bibtex]@INPROCEEDINGS{7780459,
author={K. {He} and X. {Zhang} and S. {Ren} and J. {Sun}},
booktitle={2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
title={Deep Residual Learning for Image Recognition},
year={2016},
volume={},
number={},
pages={770-778},
keywords={image classification;learning (artificial intelligence);neural nets;object detection;COCO segmentation;ImageNet localization;ILSVRC & COCO 2015 competitions;deep residual nets;COCO object detection dataset;visual recognition tasks;CIFAR-10;ILSVRC 2015 classification task;ImageNet test set;VGG nets;residual nets;ImageNet dataset;residual function learning;deeper neural network training;image recognition;deep residual learning;Training;Degradation;Complexity theory;Image recognition;Neural networks;Visualization;Image segmentation},
doi={10.1109/CVPR.2016.90},
ISSN={1063-6919},
month={June},}

[7-bibtex]@inproceedings{10.1145/3206025.3206039,
author = {Li, Hongzhi and Ellis, Joseph G. and Zhang, Lei and Chang, Shih-Fu},
title = {PatternNet: Visual Pattern Mining with Deep Neural Network},
year = {2018},
isbn = {9781450350464},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3206025.3206039},
doi = {10.1145/3206025.3206039},
booktitle = {Proceedings of the 2018 ACM on International Conference on Multimedia Retrieval},
pages = {291–299},
numpages = {9},
keywords = {image classification, convolutional neural network, visual pattern mining, object proposal},
location = {Yokohama, Japan},
series = {ICMR '18}
}
  

[8-bibtex]@article{article,
author = {Jevremovic, Aleksandar and Adamović, Saša and Veinović, Mladen},
year = {2014},
month = {02},
pages = {23-23},
title = {Mousetracking Visitors to Evaluate Efficacy of Web Site Design},
volume = {00},
journal = {Serbian Journal of Electrical Engineering},
doi = {10.2298/SJEE131223023J}
}

[9-bibtex]@article{doi:10.1080/07370024.2011.646927,
author = { Talya   Porat  and  Noam   Tractinsky },
title = {It's a Pleasure Buying Here: The Effects of Web-Store Design on Consumers' Emotions and Attitudes},
journal = {Human–Computer Interaction},
volume = {27},
number = {3},
pages = {235-276},
year  = {2012},
publisher = {Taylor & Francis},
doi = {10.1080/07370024.2011.646927},

URL = { https://www.tandfonline.com/doi/abs/10.1080/07370024.2011.646927},
eprint = { 
        https://www.tandfonline.com/doi/pdf/10.1080/07370024.2011.646927
    
}

}

[10-bibtex]@article{article,
author = {Veral, Roberto and Macías, José},
year = {2018},
month = {09},
pages = {},
title = {Supporting User-Perceived Usability Benchmarking Through a Developed Quantitative Metric},
volume = {122},
journal = {International Journal of Human-Computer Studies},
doi = {10.1016/j.ijhcs.2018.09.012}
}

Peer Assessment of Webpage Design: Behavioral Sequential Analysis Based on Eye Tracking Evidence 


[11-bibtex]@article{10.1145/2688203,
author = {Silva, Hugo Pl\'{a}cido Da and Fairclough, Stephen and Holzinger, Andreas and Jacob, Robert and Tan, Desney},
title = {Introduction to the Special Issue on Physiological Computing for Human-Computer Interaction},
year = {2015},
issue_date = {January 2015},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {21},
number = {6},
issn = {1073-0516},
url = {https://doi.org/10.1145/2688203},
doi = {10.1145/2688203},
journal = {ACM Trans. Comput.-Hum. Interact.},
month = jan,
articleno = {Article 29},
numpages = {4}
}
  



[12-bibtex]@article{Sermanet2013OverFeatIR,
  title={OverFeat: Integrated Recognition, Localization and Detection using Convolutional Networks},
  author={Pierre Sermanet and David Eigen and Xiang Zhang and Micha{\"e}l Mathieu and Rob Fergus and Yann LeCun},
  journal={CoRR},
  year={2013},
  volume={abs/1312.6229}
}


[13-bibtex]
@article{doi:10.1080/10447318.2018.1554319,
author = {Supavich (Fone) Pengnate and Rathindra Sarathy and JinKyu Lee},
title = {The Engagement of Website Initial Aesthetic Impressions: An Experimental Investigation},
journal = {International Journal of Human–Computer Interaction},
volume = {35},
number = {16},
pages = {1517-1531},
year  = {2019},
publisher = {Taylor & Francis},
doi = {10.1080/10447318.2018.1554319},

URL = { 
        https://doi.org/10.1080/10447318.2018.1554319
    
},
eprint = { 
        https://doi.org/10.1080/10447318.2018.1554319
    
}

}


[14-bibtex]@INPROCEEDINGS{7298935,
author={O. {Vinyals} and A. {Toshev} and S. {Bengio} and D. {Erhan}},
booktitle={2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
title={Show and tell: A neural image caption generator},
year={2015},
volume={},
number={},
pages={3156-3164},
keywords={computer vision;learning (artificial intelligence);natural language processing;recurrent neural nets;neural image caption generator;image content description;artificial intelligence;computer vision;natural language processing;generative model;deep recurrent architecture;machine translation;natural sentence generation;language fluency;learning;BLEU-1 score;Pascal dataset;Flickr30k;SBU;COCO dataset;Logic gates;Measurement;Training;Visualization;Recurrent neural networks;Google},
doi={10.1109/CVPR.2015.7298935},
ISSN={1063-6919},
month={June},}


[15-bibtex]
@inproceedings{Wang2017OnTO,
  title={On the Origin of Deep Learning On the Origin of Deep Learning},
  author={Haohan Wang and Bhiksha Raj},
  year={2017}
}

Style: IEEE
Word Count: 1204