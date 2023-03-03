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
... some text goes here

## Evaluation
... some text goes here

## Deployment
... some text goes here

## Recommendations
... some text goes here
