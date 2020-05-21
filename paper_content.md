# Textual content for research paper

- [Textual content for research paper](#textual-content-for-research-paper)
  - [Details](#details)
    - [Title: Identification and Measurement of Hierarchical Layout Patterns on User Experience](#title-identification-and-measurement-of-hierarchical-layout-patterns-on-user-experience)
    - [Author: Roman Sorin](#author-roman-sorin)
    - [Email: roman@romansorin.com](#email-romanromansorincom)
    - [Affiliation: Mentor High School](#affiliation-mentor-high-school)
  - [Introduction](#introduction)
  - [Methods](#methods)
    - [Participants](#participants)
    - [Procedure](#procedure)
    - [Design](#design)
  - [Results](#results)
    - [Content analysis results](#content-analysis-results)
    - [Experimental Results](#experimental-results)
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

## Methods

 A two-fold approach was selected to gather data regarding layouts. The first approach was an analysis of {NUMBER} sites that were pulled from the Amazon Alexa API for Top Sites. These sites were then parsed and filtered to identify possible network connectivity issues and dead sites. The remaining sites were then screenshotted, and sites that had the same domain but different subdomains were compared using an image similarity algorithm provided by an API, and then filtered out if they were within a threshold of {THRESHOLD}. The remaining sites were then fed into a KMeans algorithm which created four clusters. Within each cluster, KMeans was ran again to find {NUMBER} subclusters to make identification of patterns/layout density easier. Images within each subcluster were then overlayed and each subcluster was manually analyzed to identify common components/layouts. These components were then merged together and re-analyzed for error/logical layout. In the end, THREE variants were identified by density and object placement, and comparitive template layouts were created for the experimental portion of the experiment.

The experimental portion of study consisted of randomly assigning the participant to one of three variants built out from the identified layouts. Participants were instructed to navigate throughout the layout and figure out how to "sign up" or "get started" with the presented product. When beginning the experiment, a document ID was assigned and their session start was recorded. They were redirected to the assigned variant and navigated; when they finished, the time they ended was recorded in the document. The session length was then calculated for data analysis.

Heatmaps were installed but due to technical errors did not record behavior. This is a common avenue of identifying/tracking behavior (cite something here)


### Participants

Approximately fifty to one hundred individuals age 18+ participated in the experimental portion of this study. Approximately 5000 sites were collected from the Amazon Web Services Alexa API and used in feature extraction/KMeans algorithm (clustering).

### Procedure

The current research was done through analysis of Alexa API responses and experimental application of the KMeans clustering. The intended participants included software engineers, data scientists, and UI/UX researchers. By using industry professionals as participants, I aimed to reduce friction that may occur due to inexperience of navigation and task completion, further skewing any results without significant real-world application. These participants are assumed to have experience navigating around interfaces and understanding how to complete the task asked of them. All participants interacted with the layouts through the site built to host this research (https://research.romansorin.com), and tracking/identification by cookies was implemented. Participant emails were also collected at the beginning of the experiment. Cookies contained the id of a randomly chosen variant layout and the individual's user ID assigned on initial project sign-up. Participants were asked to complete a task, which was reaching registration/purchase endpoint, as quickly as possible by navigating through their presented layout.

### Design

The study included both a quantitative and qualitative analysis of user behavior and layouts, respectively. In the first stage of the study (content analysis), queries to the Alexa API were saved, parsed, and sites were extracted from the responses. These sites were then screenshotted and fed into a KMeans model for clustering and identification of commonalities across layouts. These commonalities identified by the algorithm were then analyzed manually, and several layout variants were created to represent the few most common layouts. These layout variants would be shown at random (in A/B variant style) to participants. In the experimental facet of the study, user interaction with the layout was measured through various UX metrics, recorded sessions, analytics, and heatmaps.


## Results

Ideas for data analysis:
- Scatter plots of variants and session times (variant by color, Y axis is session length)
- correlation between session time and variant; abstract the reasoning out for whyu this could be (i.e., one variant has clearly presented information CTA over another)
- regression analysis


Implications:

Limitations:

Directions for research:


### Content analysis results

### Experimental Results

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