# What Drives the Price of a Car?
The goal of the application was to use the techniques learned thus far to develop a model based on a scaled-down version (~450K records) of a Kaggle dataset (with 3 million records). The linear regression model designed would help identify features that make a used car more attractive. Using the recommendations provided below would help dealerships fine-tune their used-car inventory.

My jupyter notebook link @ https://github.com/vandavilli/BH-PCMLAI/edit/main/Application-2/README.md.

# CRISP-DM Framework

## Business Understanding
The primary business objective of a  used-car dealership is to ensure quick rotation of the vehicles; hence, the focus is to identify features that help them to do so. It becomes essential to pick a dataset with high variability ( rich set of "appropriate" features ) to provide such recommendations. For this analysis, I have attempted to model a linear regression model to help bring out the 5 most essential features that make used cars saleable. 

## Data Understanding
The dataset used for my analysis is a subset of a more extensive database of used cars. For practical purposes, I have used about 450,000 records containing 18 features. The dataset had a lot of categorical data & integer values. Description of the dataset gave me a the following insights ...
1. The top manufacturer was 'Ford'
2. The top model was 'f-150'
3. Most of the cars in the dataset had transmission type listed as 'automatic'
4. '4wd' had close to ~275k records
5. The most number of cars in the inventory were 'white'

Some insights that i could gather using box plots hinted at
1. 4wd were pricy
2. automatics had a wide price range and availability
3. There were more full-size vehicles

_Additional insights embedded as part of the boxplots in my note book ( with comments)_

## Data Preperation
On the surface, we can ignore some features like id & VIN, which don't add any material impact to the price of the vehicle. For the same reason, I decided to drop state & region. The rest of the features are all categorical (nominal/labeled). Some features like condition & size have scaling characteristics and are hence classified as nominal. One of the significant challenges in this dataset is a large number of missing values. I also found quite a few outliers in the dataset. The critical takeaway after this stage in the analysis was the decision to 
1. remove NaN's. 
   - year ( 0.28% of NaN's)
   - manufacturer ( 4% of NaN's)
   - model ( 1.2% of NaN's)
   - odometer (1.03% of NaN's)
   - fuel (0.70% of NaN's)
   - title_status (1.93% of NaN's)

2. Handle Outliers.
   - price, odometer & year had significant outliers and hence decided to use filter out data that were outside the 0.25 & 0.75 boundries. 

_Additional Observations / Reasonings_
I decided to drop fuel & title_status instead of replacing them using simple imputers because these data types can change the classification of the vehicle. E.g., a diesel truck cant is re-classified into any other frequently occurring fuel type like gas or electricity. The feature title_status also has a reputation score tied to the dealership & hence decided to not tamper with the missing value. 

Another observation was filtering out rows with "only parts" listed in the parts_only feature. With all the data cleaning tasks completed, the data lost was close to 10%, which was an acceptable loss & would not have impacted the accuracy of my prediction.

## Modeling
The first step in my supervised learning model was to develop a series of linear regression models, starting with the simplest and gradually zeroing in on techniques to help narrow down my list of features that would help predict a used car. As part of my model evaluation, I kept computing the RMSE values on the test dataset at every stage. The idea here was to pick a Linear Regression technique that produced the least MSE score & then decide on the features that created such a score. Those are my recommendations to the dealership. To proceed with the linear regression modeling, the data had to be first encoded & I chose a JamesStien encoder to encode the categorical data & a standard scaler to scale the data before presenting it to the linear regression model using a Sklearn pipeline object. 

Below are the Linear Regression techniques along with the train & test MSE scores:

| LR Type     | TRAIN MSE | Test MSE     |
| :---        |    :----:   |          ---: |
| Simple LR ( all features )      | 69658567.49       | 75504875.81   |
| Ridge Regression ( best alpha eq 10 )   | 69658567.63        | 75504662.48      |
| LASSO    | 69658578.85        | 75505613.41      |
| SFS ( LR )   | 70350171.77        | 76482069.99      |

All the above models listed similar features & the key takeaway was the negative correlation of price to odometer & transmission, which was logical. Condition also showed up as a negative but i decided to drop this feature because of the nature of the used-car business and also having the year feature pretty much helped bring out its relationship with condition ( newer cars will be closer to 2022 ) 

LASSO regression returned all the features ( with varying coeffients ) & also had a better score. The top 6 features for LASSO coorelated with SFS.
LASSO top 6 features:
_model, odometer, year, transmission, type, drive_

Sequential Feature Selector returned the following as the best features:
_year, model, odometer, transmission, drive & type_

### Exploring higher order polyomials with the identifed features

Degree 2 polynomial with the top 6 features identified produced the following results:

| LR Type     | TRAIN MSE | Test MSE     |
| :---        |    :----:   |          ---: |
| **LR ( degree =2 )**   | 66300546.84        | 72068495.72      |
| Ridge ( degree =2 )    | 66300547.22        | 72068615.15      |
| LASSO ( degree =2 )    | 68705604.07        | 74851193.62     |

_Observations:_
1. alpha changed from 10 to 0.001 - simple ridge regression vs ridge with degree 2 polynomial & the test MSE is getting better ( though not by a large margin )
2. LASSO produced coeficient values that provided certain additional insights 
   - year, odometer, drive, & type had negative correlation
   - model & transmission have positive correlation

## Evaluation
... some text goes here

## Deployment
... some text goes here

## Recommendations
... some text goes here
