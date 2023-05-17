# Pharmacovigilance Sentiment Analysis Task List

## 1. Exploratory Data Analysis (EDA)
- Clean and preprocess the dataset:
  - Remove any rows with missing or irrelevant drug or adverse event information.
- Visualize the distribution of sentiment labels:
  - Create a bar plot to show the count of each sentiment label for Adverse_event and Potential_therapeutic_event separately.
- Explore the relationship between variables:
  - Analyze the co-occurrence of specific drug names and adverse events within the Adverse_event and Potential_therapeutic_event topics to identify potential patterns or associations.
- Analyze statistical properties of the dataset:
  - Calculate the average number of adverse events and potential therapeutic events per drug to understand the frequency of reported events.

## 2. Feature Extraction
- Choose a feature extraction technique:
  - Select BioWordVec word embeddings as the feature extraction method.
- Implement the selected technique to transform text data:
  - Load the BioWordVec model using the `KeyedVectors.load_word2vec_format()` function from the gensim library.
- Generate feature vectors for each document:
  - For each document, calculate the average word embedding vector based on the BioWordVec word embeddings for the drug and adverse event text fields within the Adverse_event and Potential_therapeutic_event topics.
- Concatenate the average word embedding vectors with other relevant features:
  - If desired, you can combine the average word embedding vectors with other extracted features (such as TF-IDF vectors or statistical properties) to create a comprehensive feature representation for each document.

## 3. Ensemble Techniques using LDA & Naive Bayes
- Apply Latent Dirichlet Allocation (LDA) to extract topics from text data:
  - Use the drug and adverse event text fields within the Adverse_event and Potential_therapeutic_event topics to extract topics related to specific drug effects or potential therapeutic events mentioned in the dataset.
- Train a Naive Bayes classifier using the extracted features and sentiment labels:
  - Fit a Naive Bayes classifier on the extracted features (LDA topics) and sentiment labels specific to Adverse_event and Potential_therapeutic_event to predict sentiment based on the identified topics within each topic separately.

## 4. Scoring & Measuring Performance
- Split the dataset into training and testing sets:
  - Divide the dataset into training and testing subsets for Adverse_event and Potential_therapeutic_event separately, ensuring an equal distribution of sentiment labels in both sets.
- Train the ensemble model on the training set:
  - Fit the ensemble model (LDA + Naive Bayes) on the training data for Adverse_event and Potential_therapeutic_event separately to learn the relationship between topics and sentiment labels specific to pharmacovigilance.
- Evaluate the model's performance using metrics such as accuracy, precision, recall, F1-score, and AUC-ROC:
  - Calculate these metrics on the testing data for Adverse_event and Potential_therapeutic_event separately to assess the model's ability to predict sentiment accurately in pharmacovigilance scenarios within each topic.
- Analyze the confusion matrix to gain insights into predicted sentiment labels:
  - Visualize the confusion matrix separately for Adverse_event and Potential_therapeutic_event to identify any specific sentiment classes that are challenging to classify correctly in the pharmacovigilance domain within each topic.

## 5. Testing with Sample Data
- Prepare a small sample dataset representing a subset of the full data:
  - Randomly select a small subset of pharmacovigilance reports, ensuring it covers various drug-adverse event and drug-potential therapeutic event combinations within each topic.
- Preprocess and transform the sample data:
  - Apply the same preprocessing and feature extraction techniques used for the full dataset on the sample pharmacovigilance reports.
- Train and evaluate the ensemble model on the sample data to ensure it performs as expected.
- Verify that the sentiment predictions align with the expected sentiments for the sample data.
- Make any necessary adjustments or refinements to the model based on the performance and insights gained from the sample data testing.
