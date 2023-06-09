### Pharmacovigilance
<p align="center">
  <img src="./pv-main/images/Pharmacovigilance-Market.jpg" alt="Pharmacovigilance Image">
</p>

**Vishu Andavilli**

#### Executive Summary
This project aims to enhance pharmacovigilance through Natural Language Processing (NLP) techniques for improved identification and understanding of adverse drug events (ADEs). By analyzing 5,000 annotated pharmacovigilance events from medical case reports, the project aims to enhance ADE categorization and knowledge, leveraging NLP for more efficient analysis and deeper insights.

#### Rationale
Pharmacovigilance plays a crucial role in monitoring medication safety, protecting patients from harm, ensuring regulatory compliance, and improving overall healthcare quality.

#### Research Question
This project focuses on improving the detection and understanding of adverse drug events (ADEs) to enable more effective risk management strategies, early interventions, and enhanced patient safety. Additionally, it aims to streamline pharmacovigilance processes and regulatory reporting, contributing to the development of safer medications. By leveraging advanced NLP techniques, the project seeks to enhance ADE detection, classification, and understanding, providing valuable data-driven insights for pharmacovigilance.

#### Data Sources
- [PHEE: A Dataset for Pharmacovigilance Event Extraction from Text](https://zenodo.org/record/7689970#.ZF1X3-zMLnQ)
- #### BioWordVec Model

The BioWordVec model is a pre-trained word embedding model specifically designed for biomedical natural language processing tasks. It was trained on a large corpus of biomedical literature, including PubMed and MIMIC-III datasets. 
You can download the BioWordVec model file from the [official FTP server](https://ftp.ncbi.nlm.nih.gov/pub/lu/Suppl/BioSentVec/BioWordVec_PubMed_MIMICIII_d200.vec.bin).

#### Pharmacovigilance NLP Analysis

The project follows the CRISP-DM Methodology for Pharmacovigilance NLP Analysis:

1. **Business Understanding**: Initially, the project aimed to understand the business objectives by distinguishing between Adverse Events (AEs) and Potential Therapeutic Events (PTEs) to comprehensively analyze medication effects. Research questions, goals, and success criteria were defined.

2. **Data Understanding**: Relevant data sources, including medical case reports, electronic health records, and social media, were gathered and explored. Data quality, completeness, and availability for AE and PTE identification were assessed. Insights into the data structure, characteristics, and patterns were obtained through exploration techniques.

3. **Data Preparation**: NLP techniques were used to preprocess the data. Text cleaning, tokenization, and normalization were performed to standardize the textual data. Named entity recognition and classification models identified AE and PTE mentions. Semantic analysis extracted relevant features and attributes.

4. **Modeling**: NLP algorithms and techniques were employed to develop AE and PTE detection and classification models. Supervised learning approaches using annotated data trained and validated the models. Accurate identification and categorization of AEs and PTEs allowed for comprehensive medication effect analysis.

5. **Evaluation**: Performance and effectiveness of the developed models for AE and PTE identification were assessed using precision, recall, and F1-score metrics. Iterative evaluation refined the models and algorithms, enhancing their performance and reliability.

6. **Deployment**: (*Outside the scope of the capstone project*)
Deployment of the evaluated models for practical use in pharmacovigilance processes is the next step.

7. **Monitoring**: (*Outside the scope of the capstone project*)
Ongoing monitoring and evaluation of the deployed models ensure their effectiveness and alignment with changing data and business requirements. Potential issues are identified, and necessary adjustments are made.

By following the CRISP-DM Methodology, the project leveraged NLP techniques to distinguish between AEs and PTEs, providing valuable insights for pharmacovigilance analysis and improving medication safety.

#### Results
*Part - 1 EDA Report*

1. **Distribution Analysis - Adverse Events, Therapeutic Events, and Dual-Impact Drugs:**
This analysis examines the occurrence of adverse events and potential therapeutic events related to specific drugs, providing insights into the balance between desired therapeutic effects and undesired adverse effects.

2. **Unveiling Hidden Signals - Utilizing the 'analyze_rare_words' Function for In-depth Pharmacovigilance Analysis and Adverse Drug Reaction Detection:**
By leveraging the 'analyze_rare_words' function, this analysis uncovers rare signals in pharmacovigilance data, shedding light on diverse adverse drug events, different therapies involved, and rare or unusual reactions.

3. **Class Imbalance - A Visual Examination of Adverse Drug Events (ADEs) and Potential Therapeutic Events (PTEs):**
This analysis focuses on the significant class imbalance between adverse drug events (ADEs) and potential therapeutic events (PTEs), highlighting the implications for sentiment analysis and the need for a comprehensive understanding of both adverse and therapeutic effects.

4. **KDE Plots:**
KDE plots are used to visualize sentiment distribution, text characteristics (character count, word count, sentence count), and linguistic patterns. These plots offer valuable insights into the prevalence of negative sentiments and the variability of text length.

5. **Unveiling Insights by Leveraging Data Analysis for Actionable Pharmacovigilance Intelligence:**
This analysis aims to extract actionable insights from pharmacovigilance data by analyzing sentiment distribution, emphasizing the importance of negative mention detection, and exploring the potential for positive sentiments in understanding treatment outcomes and favorable patient responses.

6. **Extracted n-grams:**
By extracting n-grams from the data, this analysis identifies significant patterns of words associated with positive and negative sentiments, shedding light on health conditions, drug effects, and the occurrence of adverse events. These insights aid in understanding sentiment analysis and adverse drug reaction detection.

7. **Parts of speech analysis:**
This analysis examines the usage of adjectives, adverbs, nouns, and verbs in pharmacovigilance reports, revealing patterns in language expression related to adverse events and drug effects. It provides valuable insights into the linguistic characteristics of pharmacovigilance data.

8. **Calculating Lexical Diversity:**
By calculating the lexical diversity of ADE and PTE sentiments, this analysis explores the variation in word usage within each sentiment category. It provides insights into the richness and diversity of language used to describe adverse events and potential therapeutic effects.

*Part - 2 Model Generation*

1. **Multinomial Naive Bayes model:** Multinomial Naive Bayes is a variant of the classic Naive Bayes model, which has been widely used for text classification problems. The model was trained to classify text into either potential therapeutic effects (PTE) or adverse drug events (ADE).

2. **Performance before rebalancing:** Before we addressed the class imbalance issue, the model was heavily biased towards the ADE class, which was the majority. This resulted in high overall accuracy (~91%) due to the model's excellent performance at identifying ADE instances. However, the model struggled to identify PTE instances, thus it was not performing as well.

3. **Performance after rebalancing:** Using SMOTE to balance the dataset resulted in a decrease in the overall accuracy (~62%),but the model's ability to identify PTE instances improved significantly.

4. **The trade-off:** The trade-off made in balancing the classes was intended to ensure that the model could identify both PTE and ADE instances effectively. Though the overall accuracy dropped, it's important to remember that the objective in this scenario is not just to achieve high accuracy, but also to effectively identify both PTE and ADE instances.

5. **Metrics comparison:** While precision remained consistent (~92%), other metrics like recall, F1 score and the ROC AUC score were adversely impacted after rebalancing. This indicated that the model was not performing as well in terms of balancing the identification of PTE and ADE instances.

In conclusion: Although the rebalanced model's performance may seem to be lower, it's important to understand that it was optimized for the real-world use case – pharmacovigilance, where identifying both PTE and ADE instances accurately is critical. If we only focus on high accuracy, we risk missing important PTE instances, which could lead to less informed healthcare decisions.

*Part - 3 Next Steps with PharmacoVigilance dataset*

1. **By leveraging Cosine Similarity**, we were able to measure the similarity between different pieces of text, enabling the identification of patterns and associations within the pharmacovigilance dataset. This technique helped in identifying related instances and establishing connections between drugs and their potential effects.

2. **The utilization of XGBoost**, a powerful machine learning algorithm, improved the classification accuracy and performance of the model. It effectively learned from the data to distinguish between PTE and ADE instances, enabling more accurate predictions and identification of drug-related effects.

3. **The CNN analysis** yielded a precision of 0.91, recall of 1.00, F1 score of 0.95, and AUC-ROC score of 0.63, indicating accurate identification of positive cases (PTE), a good balance between precision and recall, and effective discrimination between positive and negative cases (PTE and ADE).This analysis using CNN ensures accurate identification of positive cases, minimizing false positives, enhancing patient safety, and supporting evidence-based decision-making in pharmacovigilance while effectively allocating resources.

#### Improvements
Future enhancements include:
1. Refining multi-event subset detection.
2. Integrating contextual information such as patient demographics and medical history.

These improvements will contribute to a more accurate and comprehensive analysis of ADEs and PTEs in pharmacovigilance.

#### Recommendation

Based on the analysis conducted and considering the real-world scenario where patient safety is of utmost importance, it is recommended to use a combination of techniques for optimal results. The following approach can be taken:

1. **Data Preparation:** Ensure that relevant data has been collected, addressing the class imbalance issue to improve model performance.

2. **Advanced Technique:** Utilize a more sophisticated technique such as Convolutional Neural Network (CNN) to analyze the pharmacovigilance dataset. CNN has shown promising results in accurately identifying positive cases (PTE) and effectively discriminating between positive and negative cases (PTE and ADE).

3. **Ensemble Learning:** Consider employing ensemble learning techniques, such as combining multiple models like XGBoost and Multinomial Naive Bayes, to leverage the strengths of each algorithm and improve overall performance.

4. **Regular Model Evaluation:** Continuously evaluate the model's performance using appropriate metrics such as precision, recall, F1 score, and AUC-ROC. This ensures that the model maintains a balance between accuracy, precision, and recall, allowing for effective identification of potential therapeutic effects and adverse drug events.

5. **Iterative Improvement:** Regularly update and refine the model based on new data and emerging patterns. This iterative process helps in continuously improving the model's performance and keeping up with evolving pharmacovigilance requirements.

In summary, in a real-world scenario where patient safety is paramount, it is recommended to employ advanced techniques such as CNN and ensemble learning, while ensuring continuous evaluation and improvement of the model. This comprehensive approach aims to accurately identify potential therapeutic effects and adverse drug events, ultimately supporting informed healthcare decisions and prioritizing patient safety.

#### Outline of the Project

1. [Exploratory Data Analysis (EDA)](https://github.com/vandavilli/My-AIML-Portfolio/blob/main/Capstone/pv-main/pv_eda.ipynb)
   - In-depth analysis of the PharmacoVigilance dataset.

2. [Sentiment Analysis Model](https://github.com/vandavilli/My-AIML-Portfolio/blob/main/Capstone/pv-main/pv_model.ipynb)
   - Sentiment analysis model to analyze sentiments in the dataset.

3. Additional Analysis
   - Using Cosine Similarity & XGBoost (https://github.com/vandavilli/My-AIML-Portfolio/blob/main/Capstone/pv-main/pv_cosine_similarity.ipynb) 
   - CNN (https://github.com/vandavilli/My-AIML-Portfolio/blob/main/Capstone/pv-main/pv_cnn.ipynb)

4. [Click here for Presentation (in PDF)](https://github.com/vandavilli/My-AIML-Portfolio/blob/main/Capstone/presentation/PharmacoVigilance-Final.pdf)
   - Presentation deck for stakeholders.

#### Contact and Further Information

For any inquiries or further information, please feel free to contact:

- Vishu Andavilli
- Email: vishu.andavilli@gmail.com
- [LinkedIn](https://www.linkedin.com/in/vandavilli/)
