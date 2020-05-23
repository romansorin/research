# Textual content for research paper

- [Textual content for research paper](#textual-content-for-research-paper)
  - [Details](#details)
    - [Title: Identification and Measurement of Hierarchical Layout Patterns on User Experience](#title-identification-and-measurement-of-hierarchical-layout-patterns-on-user-experience)
    - [Author: Roman Sorin](#author-roman-sorin)
    - [Email: roman@romansorin.com](#email-romanromansorincom)
  - [Introduction](#introduction)
  - [Method](#method)
    - [Participants](#participants)
    - [Design](#design)
    - [Analytical Procedure](#analytical-procedure)
    - [Experimental Procedure](#experimental-procedure)
  - [Results](#results)
    - [Clustering](#clustering)
    - [Implementation](#implementation)
  - [Discussion and conclusions](#discussion-and-conclusions)
    - [Limitations:](#limitations)
    - [future work:](#future-work)
  - [Appendix](#appendix)
  - [References](#references)

## Details

### Title: Identification and Measurement of Hierarchical Layout Patterns on User Experience

### Author: Roman Sorin

### Email: roman@romansorin.com


NOTES:
- REMOVE THINGS ABOUT HCI
- REMOVE THINGS ABOUT CNN
- REMOVE THINGS ABOUT I18N
- REMOVE THINGS ABOUT DRY, SOLID (?)
- REPLACE CNN WITH KMEANS AND OTHER RELEVANT INFO
- GENERALLY CURTAIL INTRODUCTION TO BE MORE RELEVANT TO THE ACTUAL EXPERIMENT AND ANALYSIS PERFORMED


## Introduction

\section{Introduction}User experience (UX) has continually developed in the field of software engineering and is seen as being highly integral to the success and usability of an application \cite{10.1016/j.jvlc.2017.08.004}. Alongside concepts such as accessibility and presence of I18n in interfaces, perceived user experiences—notable traits such as design, animation, and usability—are one of the most important aspects to consider in the development and analysis of interactions \cite{benchmarking}. Seen both within and beyond software, reputable products and services are known to utilize effective user experience in creating a product that attracts and retains consumers, subsequently expanding the product influence. User experience drives both offline and online interactions that result in psychological and economic impact on consumers and businesses. User experience is a broad and highly expansive field that can take the form of layouts; colors; fonts; copy; animations; and more granular aspects of design and interaction, making UX highly complex to assess and properly execute. In this study, the impact which hierarchical layout structure and design patterns have will be of focus to approach user experience in web interfaces from a bottom-up approach and architectural stance, addressing the fundamental integration of components in the presentational layer.

From one perspective, user experience is derived from the physiological interaction between user and system \cite{10.1145/2688203}. As interfaces and applications are developed further to suit the needs of consumers and developers alike, there exists a significant need to address the psychological implications of human-computer interaction (HCI) in a more focused and detailed pursuit. Conversely, this continual development of products and experiences creates a significant amount of both practical and technical applications for user experience to manifest itself within, providing for new theses and findings. Within the previous decades, several studies have explored the importance of user experience on this success of products and applications \cite{doi:10.1080/07370024.2011.646927, mousetracking, parallax} in various facets. A common pattern that exists in much of the current research on user experience regards the aesthetics and appearance of a website with consideration of both higher and lower-level abstraction. When analyzing judgment and response by users, aesthetic and appearance is a large determinant in utilization and rates of recurrence \cite{10.1145/3206025.3206039}. In the domain of product and application development, the quality of the experience is extremely vital in progressive rates of user retention, user satisfaction, revenues from sales and advertising, and other analytical measures that are used to determine the relative success of a product or application. Of the serious need for appealing and usable interfaces are businesses that rely on online traffic for customers, and identification and use of these interfaces may provide an advantage over the competition; increasing revenue and attraction by customers to the respective site \cite{10.1145/3206025.3206039}. Consequently, definitive data on optimal layouts by use cases can serve as being beneficial to businesses in both financial and social capital. Moreover, synonymous with the DRY and SOLID principles used in software engineering,designers may look to these data to optimize their processes and focus on more granular parts of the system; and developers can be more oriented towards releasing minimum viable products (MVPs) with confidence and reasoning for utilizing a given layout.

Correspondingly, machine learning (ML) and deep learning algorithms have undergone significant developments and continue to advance in their rates of application \cite{Wang2017OnTO}. The use of deep learning in machine learning has allowed for solving more complex artificial intelligence tasks, including object and pattern recognition \cite{7780459}, a concept that will be fundamental in the findings within this paper \cite{Wang2017OnTO}. More specifically, applications of machine learning such as convolutional neural networks (CNNs) \cite{Sermanet2013OverFeatIR}, pattern recognition, and image classification establish opportunities for automated image caption and description generation \cite{7298935}, labeling of features and objects \cite{hierarchical}, and identifying common patterns within a set of images \cite{doi:10.1080/10447318.2018.1554319}. In this context, hierarchical features describe the components found within a layout, and a layout may thus be referred to as layout hierarchy.

A major limitation of UX and its applicability is the granularity found within even the foundational layouts, ignoring any higher-level or specific abstractions. Layouts are recursive and cascading, consisting of components which contain a great degree of subjectivity, development, and iterative processes. These iterative processes take a significant amount of time to implement and analyze, relating to the engineering debt that occurs within design and development \cite{4293575}. Considering the complexity of an interface composed of several different components (all of which are recursive and componentized themselves), the difficulty in achieving an optimal layout in terms of UX is quite evident. As such, the fluidity of design is likely a reason behind the lack of data and definition of layouts, despite patterns in layouts being common and each being utilized in thousands of cases. Even as UX expands as a field and significant area of focus within software engineering, research is relatively limited and restricted to case studies and internal data at best, suggesting a need for a method for identifying these data.

While the fields of software engineering and machine learning have been individually addressed and developed, there has yet to be studies that consider the integration of machine learning with the user experience facet in software engineering. Moreover, there are no definite data on how layout hierarchies affect UX metrics. The capability for pattern recognition and hierarchical analysis using machine learning is of high importance concerning layouts and user experience, as models may present possible solutions for identifying patterns within layouts using models and generating labels that may be implemented to identify these desired metrics. Consequently, two research questions are presented:

\renewcommand{\labelitemi}{$\textendash$}
\begin{itemize}
    \item (1) How does layout hierarchy impact user experience metrics, and what metrics are associated with what hierarchical features?
    \item (2) How can hierarchical features best be implemented to optimize the overall user experience and address a greater range of provided metrics?
\end{itemize}


In data sets which contain a large number of samples, such as a set of the highest indexed sites on the web (minimum 10,000+ indices), manual identification of both common and more intricate patterns are incredibly difficult to find and waste resources. In contrast, statistical methods and the use of trained algorithmic models will have higher rates of success in identifying patterns that may otherwise not be seen. Thus, there is a chance that integrating algorithmic models into site analysis to identify patterns may more significantly benefit the field of software engineering. Because of the aforementioned limitations of manual analysis, layouts and structures which are deemed to be efficient and successful are strictly subjective and reported on an "at-will" basis; this information may come from individual analyses or findings by user experience researchers within case studies or companies. Thus, this paper proposes an approach to find objective data through the collection of existing sites from Alexa Top Sites \cite{antoniou_2015}, then programmatically collect screenshots of every site, which will then be fed into a model to identify patterns in layouts. By itself, these data will be of little value to the purpose of this paper and therefore requires implementation and an experimental investigation to identify what metrics are associated in practice rather than strict ranking. Thus, this paper seeks to identify the most common layout hierarchies and patterns seen in the highest-indexing sites and measure which UX metrics can be best associated with a given layout or features.

## Method

### Participants

The study involved 57 individuals who voluntarily participated in the experimental portion of layout analysis. Individuals were age 18 and older, with all participants being from the United States. All participants were expected to have familiarity and experience with navigating layouts and websites, and several individuals had several years of work experience in software engineering and computer science fields. No compensation or reimbursement was provided for involvement in the study. All participants successfully completed the experiment. Participants were recruited through direct and indirect advertisement/sharing of the study. Participation was limited to devices with a minimum screen width of 1024px or a large breakpoint, as only desktop-based layout interfaces were presented. After the experiment, participants were thanked and then provided with an email for further inquiries.


### Design

A paired analytical and experimental approach was taken to identify common layouts and their potential association to user behavior. The analytical procedure utilized scripts and applications \cite{sorin_2020} built specifically for this study to query various APIs [aws, image sim], collect screenshots of sites, and manipulate/process screenshots for use in K-Means clustering and image overlaying. These K-Means clusters were then assessed and analyzed to identify potential commonalities in layouts. Experimentally, a site dedicated to the experiment was built [research-rs] to track user interaction with the presented interfaces. In order to track user behavior, different analytics tools to identify demographics (location, estimated age), in addition to heatmaps and recordings were installed on the site (Google Analytics [ga] and Hotjar [hotjar], respectively). As the participants worked through the experiment, the timestamps of their session start and session end were collected and set in a unique document provided by Google's Firebase [firestore].

### Analytical Procedure

Analysis began by querying the AWS Alexa Top Sites API [aws] for an initial count of 1002 sites. The Top Sites API provides the highest ranking sites by region, and the region chosen was "global" for this experiment. The API responses were then parsed and tested to identify if there were any sites that were no longer active, not working (such as a status code of 500), or could not be connected to. Each of the sites were queried for status, and if they existed, an RGB screenshot of the page at the domain was taken. Due to lazy loading, infinite scroll, and asynchronous calls, screenshot height was limited to 30000 pixels. The driver then scrolled from each max scroll height every five seconds up until the screenshot maximium height, which upon reaching max height the driver jumped to the 0th pixel and rescrolled in increments of 200 pixels every 0.5 seconds and took a full page screenshot. This secondary scroll pass ensured that content would have loaded by the time the screenshot was taken. Pages that were not active were ignored by the driver, and the function moved to the next site. After all RGB screenshots were taken, a secondary image processing step was taken: conversion of all RGB sites to greyscale using opencv [cv2] to eliminate the influence of color on clustering and image similarity. Many sites were found to have a presence of subdomains or TLDs due to regional or content differences, however these could not be automatically eliminated due to the fact that different subdomains could serve different purposes — a subdomain may map to a dashboard, another may handle support channels, etc. Instead, sites with the same root domain (ignoring both the subdomain and TLDs) were compared using an image similarity API provided by OpenAI [image sim]. The greyscale versions of these same root domains but differing subdomains or TLDs were compared to each other; if the site similarity surpassed the arbitrary threshold of fifteen, the higher ranking site/screenshot was kept, and the comparison image was removed from the dataset. However, before image comparisons were done, every greyscale screenshot was cropped to some found height. Filtered domains were sorted using insertion sort to identify base domain and duplicates. Width of the site remained constant due to all screenshots being taken on a single device (width of 2560px), though heights were dependent on the site. Screenshots were iterated over and a flag variable was created to identify the shortest/smallest height dimension to be used for cropping. In order to circumvent any technical glitches, a minimum height of 1440px was set. Images below this minimum height were removed. After ensuring that all screenshots can be considered "unique" content, these images were then fed into a Keras vgg16 pretrained model [keras] to perform K-Means clustering algorithm with k=4 clusters selected. Due to some clusters containing several hundred images, an image overlaying function was run inside of each cluster to generate subclusters of maximum 50 images each. Subclusters were displayed as a PNG, where the denser parts of the image (greyscale, overlay weighted 50/50) represented the commonalities of objects/features in layouts. These features were then manually extracted and represented in a mockup. After each cluster's subclusters had mockups generated, mockups were analyzed and some features were detracted from the mockup due to overlapping features/clarity of the layout. After mockups From four clusters, three common layouts could be realistically created and identified, and mockups were then converted into web components with TailwindUI provided components [tailwindui]. Each layout was then built out into a web app and a random string identifier was created for each variant. Session length was collected and inserted into Firebase Cloud Store [fb].
Subdomain and root domain were split with a hyphen delimiter. Subdomain and TLD were analyzed separately.

### Experimental Procedure

The experiment was conducted on a website [research.rs] built to host the experiment and information related to the experiment. Upon viewing on the homepage, users were presented with a message describing the entire study in brief, directions for participation, and information on what data is collected and how it will be used. Consent was provided as users had to manually input their email and press "begin". Upon pressing begin, the participant was randomly assigned to one of three aforementioned layout variants, and they could not assign themselves to another interface. Participants were instructed to navigate and read through the information and structure of the interface as they typically would with a real-world product, and then attempt to register or purchase the presented product or service. After they pressed the relevant buttons/links to begin registration, they were then redirected to the final screen confirming that their participation in the experiment was finished.

## Results

This section presents the results of both portions of the study, including the numbers of sites throughout processing stages, number of K clusters and N sites within each cluster, and the observed behaviors of users based on session lengths. Overall, it was shown that there was little variance of the session lengths of all three layouts as they compare to each other, and that layout did not affect a user's ability to complete the task as it relates to time.

### Clustering

Following collection of data from the AWS Alexa Top Sites API [aws], the datasets were run through the image processing and filtering stages. To simulate the importance of this processing stage as is relates to use of data, Fig. 1 shows the number of sites used in the analytical portion of the experiment as it relates to each stage. In stage 0, which is initial data collection and parsing of the API, 1002 sites were returned and added to a table within the study application. Stage 1 concerns the removal of dead and inactive sites as the Selenium webdriver went through and collected screenshots of each site, and removed sites that did not have a status code within the 200 range, resulting in 975 sites being left for processing. Stage 2 concerns the comparison of same root domain sites using the image similarity API and an arbitrarily set threshold, eliminating subdomains and geographical TLDs with content that too closely resembled that of the higher ranking root domain. In addition to similarity processing, reshaping of the resulting screenshots led to those which did not exceed the minimum height of 1440px to be thrown out as well, reducing the sample size to 908 sites as screenshots. These remaining screenshots were deemed unique enough to be clustered using the K-means algorithm, and fit the minimum array length (delve into what is required/why of an image, why it has to fit some height/width), and were used in the following clustering.

% Please add the following required packages to your document preamble:
% \usepackage{booktabs}
\begin{table}[]
\begin{tabular}{@{}ll@{}}
Stage & n    \\
0     & 1002 \\
1     & 975  \\
2     & 908 
\end{tabular}
\end{table}

<!-- TODO: WHERE TO PUT this -->
<!-- Following the clustering of the remaining 908 images using the Keras VGG16 pretrained model for K-means algorithm -->

Due to a lack of appropriately typed data to apply either the elbow method [some source here on what it is] or gap method [some source here on what it is] to identify the optimal number of K clusters used in K-means, an abitrary but reasonable value of 4 was selected, outputting four groups of clustered (similar) images. A K value of 4 was most reasonable for simplicity and ease of evaluation. Table 2 illustrates the number of images per cluster after running the K-means model, where cluster 0 had n = 242 images; cluster 1 had n = 125 images; cluster 2 had n = 111 images; and cluster 3 had n = 385 images. In an effort to ease the manual analysis of cluster results, such as cluster 3's n = 385, a function iterated over the cluster results and generated a weighted image for every 50 images (subclusters). Images within a subcluster were blended using the OpenCV addWeighted() function, which utilizes the following formula, where both \alpha and \beta represent the intended weight of source images f_0(x) and f_1(x), and \gamma = 0 implicitly:

\[dst = \alpha f_0(x) + \beta f_1(x) + \gamma\]

Table 2 also illustrates the number of subclusters per cluster, with cluster 0 having 5; cluster 1 having 3; cluster 2 having 3; and cluster 3 having 8. Figure 2 shows an example subcluster from a given cluster to better illustrate the intention and output of the weighted images, and its improvement on clarity for analysis.

% Please add the following required packages to your document preamble:
% \usepackage{booktabs}
\begin{table}[]
\begin{tabular}{@{}lll@{}}
Cluster & n   & Subclusters \\
0       & 242 & 5           \\
1       & 125 & 3           \\
2       & 111 & 3           \\
3       & 385 & 8          
\end{tabular}
\end{table}

Within subclusters, common features could be identified based on image / pixel density (i.e., the darker portions of an image or where object are clearly overlapping) to generate one common layout per cluster. Due to a lack of obvious variance between two of the four layouts created, the number of layouts were reduced from 4 to 3 to better represent differences in layout and hierarchical elements for experimental implementation. Figures 3 to 5 show the layouts that were implemented in the experimental portion of the study.

### Implementation

Though heatmaps and other tracking tools were installed on the experimental site, a technical error led to failure to collect that data and thus only led to session data length being collected. Table 3 shows a total of 57 data points, with session length elapsed associated with variants. Two potential outliers were identified: a value of 80 for variant 0 and a value of 107 for variant 1. These two outliers do not have clear explanations, as factors such as internet connection and someone's understanding of the task could not be assessed/tracked/considered with this implementation.

% Please add the following required packages to your document preamble:
% \usepackage{booktabs}
\begin{table}[]
\begin{tabular}{@{}llll@{}}
Variant & 0       & 1        & 2      \\
        & \multicolumn{3}{l}{Seconds} \\
        & 7       & 12       & 40     \\
        & 5       & 45       & 37     \\
        & 3       & 3        & 6      \\
        & 60      & 5        & 38     \\
        & 59      & 9        & 3      \\
        & 24      & 3        & 37     \\
        & 5       & 19       & 47     \\
        & 55      & 22       & 54     \\
        & 30      & 11       & 37     \\
        & 24      & 107      & 10     \\
        & 80      & 15       & 17     \\
        & 5       & 35       & 12     \\
        & 3       & 18       & 24     \\
        & 2       & 29       & 4      \\
        & 35      & 43       &        \\
        & 28      & 9        &        \\
        & 15      & 7        &        \\
        & 9       & 12       &        \\
        & 6       & 26       &        \\
        & 18      & 17       &        \\
        & 17      & 38       &        \\
        &         & 33       &       
\end{tabular}
\end{table}

Table 5 shows all 57 data points split across three respective variants, with values representing seconds. Descriptive statistics for each variant are shown to understand how basic values compare across each variant

% Please add the following required packages to your document preamble:
% \usepackage{booktabs}
\begin{table}[]
\begin{tabular}{@{}llll@{}}
       & V(0)  & V(1)  & V(2)  \\
n      & 21    & 22    & 14    \\
Mean   & 23.33 & 23.55 & 26.14 \\
Min    & 2     & 3     & 3     \\
Max    & 80    & 107   & 54    \\
SD     & 22.62 & 22.62 & 17.27 \\
Median & 17    & 17.5  & 30.5
\end{tabular}
\end{table}

Using a one-way ANOVA statistical test, analysis of the session length associated with three variants showed that the compared interface variances generally were found to be statistically insignificant at p < .10. Table 3 shows descriptive statistics associated with each variant, while table 4 shows information relevant to the ANOVA test. The means of the three treatment groups (interfaces) were found to have a p-value of 0.919361, and an f-ratio value of 0.08421. While the means were relatively similar across treatment groups (T_1 = 23.33, T_2 = 23.55, T_3 = 26.14), the potential effect of the extreme values is unclear unless the test is reran without the outliers.

% Please add the following required packages to your document preamble:
% \usepackage{booktabs}
\begin{table}[]
\begin{tabular}{@{}lllll@{}}
                      & \multicolumn{3}{l}{Treatments} &       \\
                      & 1        & 2        & 3        & Total \\
N                     & 21       & 22       & 14       & 57    \\
∑X                    & 490      & 518      & 366      & 1374  \\
Mean                  & 23.33    & 23.55    & 26.14    & 24.11 \\
∑X\textasciicircum{}2 & 21668    & 22944    & 13446    & 58058 \\
SD                    & 22.62    & 22.62    & 17.27    & 21.10
\end{tabular}
\end{table}

\begin{table}[]
\begin{tabular}{@{}lllll@{}}
Source             & SS       & df & MS     &             \\ \midrule
Between-treatments & 77.53    & 2  & 38.77  & F = 0.08421 \\
Within-treatments  & 24859.84 & 54 & 460.37 &             \\ \midrule
Total              & 24937.37 & 56 &        &            
\end{tabular}
\end{table}


Rerunning the one-way ANOVA test without the identified outliers still leads to a statistically insignificant p value (p = 0.485862), but leads to a large difference between the p and f values. The means of the non-outlier treatments were found to have an f-ratio value of 0.73194 and a p-value of 0.485862.

% Please add the following required packages to your document preamble:
% \usepackage{booktabs}
\begin{table}[]
\begin{tabular}{@{}lllll@{}}
                      & \multicolumn{3}{l}{Treatments} &       \\
                      & 1        & 2        & 3        & Total \\
N                     & 20       & 21       & 14       & 55    \\
∑X                    & 410      & 411      & 366      & 1187  \\
Mean                  & 20.50    & 19.57    & 26.14    & 21.58 \\
∑X\textasciicircum{}2 & 15268    & 11495    & 13446    & 40209 \\
SD                    & 19.00    & 13.14    & 17.27    & 16.44
\end{tabular}
\end{table}

% Please add the following required packages to your document preamble:
% \usepackage{booktabs}
\begin{table}[]
\begin{tabular}{@{}lllll@{}}
Source             & SS       & df & MS     &             \\
Between-treatments & 399.52    & 2  & 199.76  & F = 0.73194 \\
Within-treatments  & 14191.86 & 52 & 272.92 &             \\
Total              & 14591.38 & 54 &        &            
\end{tabular}
\end{table}

Though the resulting session lengths were found to be statistically insignificant, observing graph 1 of session lengths without outliers leads to interesting findings. Variant 1 is clearly seen to have more consistently spaced data points with a lower maximum, whereas both variant 0 and variant 2 had clusters on both the minimum and maximum ends of the graph, exceeding that of variant 1. Relative to variant 1, variants 0 and 2 took longer for several individuals in both cases. However, this pattern cannot be clearly explained due to various potential factors and without further analysis or data manipulation. Referencing figures 3 through 5, variant 1 had less "call-to-action" points and required a further scroll distance to reach the target, whereas variants 0 and 2 both had immediately presented "call-to-action" and additional targets. Without additional measurements and further research, it is unclear whether this is due to friction of the input field on variant 2, color schemes throughout each variant, or the choice of copy in each button/section. A larger sample size and other associated data could be used to identify if these factors had any influence on user behavior. Further analysis of measure of travel/scroll distance and placement of objects could potentially explain the variance.



## Discussion and conclusions
This paper proposes a potential approach to identifying common layouts, features, etc. in a given domain (e.g., ecommerce, business, healthcare, media) and optimization/analysis of the effectiveness of layouts. A statistically insignificant result does not necessarily mean that the layouts perform equally well. For web interfaces, many confounding variables may be present that impact the length and ease of a user's inquiry. This proposed model could best be applied on a legitimate product/site with more development to analyze how it performs in real world scenarios, and how other factors may influence ease. This paper focused simply on static layouts and the technology used to create the layouts is specifically built for static site generation, leading to already preloaded assets/page content, which may generally reduce time spent. On sites that use asynchronous calls, animation, or real content, these may confound and create a longer lifetime session or cause delay in network requests which also increase session length.
Additionally, though there is statistical insignificance, this tool can be used to validate custom layouts / designer ideas against tried and true layouts generated from top sites to determine the effectiveness of the layout and the hierarchy of components. Though not evident without abstraction, hierarchy may have been influential in the results of this study, and present itself at a greater scale with a higher sample size or different application of this proposal. The "how" and "where" representation of different components and hierarchical features in each variant likely held an influence on the distribution of data, but more research is required to make the exact factors known.

As mentioned before, variant 1 is of particular interest. Despite having a reduced number of successful targets to click and more scroll distance required to complete the task, leading to more time elapsed, data was more consistent and did not broach the upper ends of the distribution like variants 0 and 2 did. This display of results is unexpected: variant 0 had a large section about a fourth into the interface that allowed users to get started with the product automatically, and variant 2 had a direct call-to-action within the initial viewport. Despite variants 0 and 2 being technically more accessible and intuitively quicker to get started with, more participants were seen to have trouble with these variants — either figuring out how to use them, or turned away by the format and display of information.

### Limitations:
As with any study, this study suffers from several limitations that may have negatively influenced results. Beginning with analysis (stage 0), it is possible that too global of a site data collection was specified; the globally highest-indexing sites were returned, and not those specific to a given region. Due to cultural differences and availability of engineering, research, and design, different regions have different opinions on design and different standards on how information should be best presented. Future research and retrials of this proposed model should specify a given region, such as the U.S. or Canada. In addition to selecting too large of a ranking range, this initial study was clearly too broad in terms of categories. While the AWS Alexa Top Sites API does not provide data based on category of site (such as ecommerce, media, news, etc.), a potential solution could be to cross-analyze/join APIs and identify the category based on a single URL. By specifying region and category, businesses, engineers, designers, and researchers can better understand how to present information to their target audience by demographic and focus.

A single K-Means clustering in stage 2 may not have been a sufficient or best possible approach to identifying commonalities in images. While some basic image processing and filtering was applied, there are likely other ways to process images for the K-means algorithm to better cluster, such as applying hidden layers using a CNN, or potentially training another K-Means model. It may be a better approach to instead focus on individual parts of hierarchy within a layout and cluster those, rather than doing full pages: such as the hero, headers, footers, etc. These cluster data can then be combined to identify the "best" layout by working incrementally. Furthermore, common features or objects can be difficult to detect even in subclusters of 50 overlayed images. Considering how limited this dataset was and the general manual time required to be invested, it would be impractical — or even impossible — to run manual analysis of overlayed images on a dataset of 500,000 sites. It is unclear how this paper's approach of "subclustering" was or wasn't useful in identifying common features within a cluster, and if it could have been avoided entirely if another model was used alongside the Keras VGG16. For the purpose of clarity and logic in these interfaces, manual analysis likely led to a degree of bias in design and elements, especially since elements had to be recreated from the clusters/subclusters (no elements or copy could be directly copied), which means that the researcher's design tendencies may have affected user experience positively or negatively.

Experimentally, the choice of participant demographic and previous exposure to interfaces may have been counterintuituve. While mostly software engineers and web designers were prompted to participate in the study so as to reduce potential confusion in the required task, this study may have overestimated the degree to which the layout or directions would be considered to be confusing. As such, these individuals are already trained to quickly and effectively navigate through layouts and interfaces, which is non-representative of the actual market or target population. However, this also reinforces the need for live implementation of this study's proposed model in real-world applications, and how it can potentially yield descriptive results when put into effect in these environments.

Generally, this study's methods suffered due to a lack of pre-existing research to fill in gaps of inquiry and approaches. In several areas, from data collection to image processing to experimentation, this study creates potential methods and procedures for use by the software engineering community in varying aspects. Replication of this study with more time and larger datasets, as well as addressing the aforementioned limitations of querying category and demographic could very potentially yield results that benefit the software engineering and design community as a whole.

### future work:
There are several avenues of improvement and future inquiry in both analytical and experimental contexts. It is highly likely that relying strictly on a KMeans algorithm and manual analysis of clusters led to misrepresentation of what the most common layouts really are, or that they could have been considerably more detailed than they were in this study. With that in mind, inclusion of other machine learning based methods and models — such as feature and object detection — in addition to more developed clustering models may allow for better understanding what common features or components exist in layouts, and how they work together to build hierarchically effective layouts. In addition to simply clustering and using image overlays, the presence of features could potentially be represented by "density", which would require a quantitative and empirical metric of its own. This density could describe features on an interface, which could lead to the creation of contour maps to illustrate where components are commonly placed as another abstracted measure of layout effectiveness. Pairing this proposed model with both proven and widely utilized eye and mouse tracking could be incredibly fruitful, and would allow this model to be ran several more times on a greater scale, providing more data to analyze and generate potential correlations from. With these increased trials, some quantitative metric could potentially be created to determine and predict the success or effectiveness of a layout depending on where objects are located, and of what type. Doing this allow would allow for designers and engineers to understand what exactly leads to one layout being more effective than another, and may potentially produce gains for businesses who would like to most quickly optimize the time it takes for a user to get started with their product, or to read over the presented information as quickly as possible. Doing this research would allow businesses to focus less on constant A/B variant testing of their own, and instead to explain their decisions through a quantitative metric and spend more time developing their product instead of optimizing landing page interfaces.

Overall, it's imperative that more research in this field is done and that this study is replicated due to its potential applicability to real-world products and its benefits to the software engineering community. It is also important to recognize that within this context, both qualitative abstract analysis and quantitative statistical testing is required to identify the effectiveness of a layout, and to identify potential factors that may lead to optimization. Informally, both are applied in isolated case studies throughout the community, but there is yet to be an abundance of research that blends both to improve the quality of interfaces with widely available models and procedures.


<!--!  NOTE FOR MYSELF -->

**
variant 0 = 8nqXhdl3JD8u

variant 1 = hwVB0eKUehxy

variant 2 = vtc5qYP2r8Ut
**










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
  .



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

@misc{sorin_2020, title={romansorin/research-screenshot}, url={https://github.com/romansorin/research-screenshot}, journal={GitHub}, author={Sorin, Roman M}, year={2020}, month={May}}

@misc{hotjar, title={Website Heatmaps & Behavior Analytics Tools}, url={https://www.hotjar.com/}, journal={Hotjar}}

@misc{sorin, title={Home}, url={https://research.romansorin.com/}, journal={Home | rs Research}, author={Sorin, Roman M}}

@misc{google_firebase, url={https://firebase.google.com/}, journal={Google}, publisher={Google}}

@misc{google_analytics, title={Google Analytics}, url={https://analytics.google.com/analytics/web/}, journal={Google}, publisher={Google}}
Style: IEEE
Word Count: 1204