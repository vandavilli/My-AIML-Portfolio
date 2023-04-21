### Overview
The main objective of the application is to study & analyze the various classifiers like Logistic Regression, SVM, KNN, Decision Tree to choose the best model to analyze the dataset. The dataset used for this analysis is a Bank dataset which captures responses from a telemarketing campaign targetting customers with a high-yield term deposit. Please find below link to a jupyter notebook containing the necessary technical analysis of the dataset. 

https://github.com/vandavilli/BH-PCMLAI/blob/main/Application-5/prompt_III_va.ipynb

I have tried to use open source packages from YellowBrick to visualize classification reports, use of open source packages like missingno to view missing values in the dataset, pandas profiling packages to view the pandas dataset & produce HTML reports & many other useful open source libraries. The attempt is to demonstrate how these packages can be used for EDA, model development & analysis with a couple of lines of code.

### Data Analysis
The first stage of any modelling is data analysis. I used pandas profiler to generate EDA report ( full report embedded in the note book ). Eg. shown below

<img src='img/1.png'>
<br>
<img src='img/2.png'>

The advantage of using pandas profiler is with a few lines of code, a significant amount of analytical data gets generated for easy consumption & distribution. Less code implies more attention towards analysis & presentation of data to the stake holders.

### Understanding the Task
A well-trained ML model's objective is to predict accurately if the customer accepts an attractive long-term deposit application during a direct marketing campaign call. The main idea here is that a effective campaign reduces the marketing cost by X% and acquires Y% of the prospects. The dataset has various attributes ( personal & socio-economic indicators ) which when fed into a well trained model, can help drive better predictions to acquire prospects thereby driving costs down.

### Training, Testing & Baseline Model
Before presenting the data to machine learning modeling, it went through encoding, transformations & the class imbalance which would have signalled more "No" was eliminated using the standard techniques like dropping features & data that had little impact on the outcome, use LabelEncoders on categorical featurs & SMOTE to handle class imbalance. The next step was to use sklearn's train_test_split to create a training & test datasets.

### Model Comparisons
A baseline model is one in which we can always guess the most frequently occurring class. Without using any ML, i did a quick check for the score using the most frequently occuring class. This score came out to be 88.74%. 

The problem required me to use LogisticRegression as a baseline model & the test accuracy score was 86.3% ( close enough !!! )
<br>
<img src='img/3.png'>

#### Summary of all the classification results ( defaults with no hyperparameter tuning )
<br>
<img src='img/4.png'>



### Conclusion & Future Steps
