# Practical Application Assignment 5.1 (Module 5, UC Berkeley AI/ML Professional Certification)
The practical application I have used to study the dataset helps develop insights into the following question “Will a customer accept the coupon?”. I have developed this notebook for 2 coupon types & the various acceptance numbers help develop insights into the customer & coupon acceptance rates. 

# Brief Description of the Dataset
The data used for the data analysis assignment comes from the UCI Machine Learning repository and was collected via a survey on Amazon Mechanical Turk. The survey describes different driving scenarios, including the destination, current time, weather, passenger, etc., and then asks people whether they will accept the coupon if they are the driver. Answers given that the users will drive there “right away” or “later before the coupon expires” are labeled as “Y = 1”, and answers “no, I do not want the coupon” are labeled as “Y = 0”. There are five different types of coupons—less expensive restaurants (under $20), coffee houses, carry out and take away, bars, and more expensive restaurants ($20–$50).

In order to study and present some of the data analysis and cleaning techniques, I have used 2 different coupon types - Bar, Carry out & Take away. The meta data & its description is available inside the notebook. 

# Codes for Visualization and Analysis
The notebook can be found at this location: https://github.com/vandavilli/BH-PCMLAI/blob/main/prompt.ipynb

# Summary
After studying the acceptance rates for Bar and CarryOut Coupons, here are some of my findings
- Bar Coupons have an average acceptance rate of 41% which is neither too low or too high. 
- Some of the factors that drive a better acceptance rates include
  1. Age of the drivers likely to be over 30.
  2. Drivers who ride with no kids
- Occupation or Marital Status don't seem to have any significant impact on coupon acceptance.


73.55 % of the customers accepted the carryout coupon.
47.78 % of the customers took a carryout more than 4 times in a month.
52.22 % of all other customers who do a carryout.
28.52 % of the customers took a carryout more than 4 times in a month & drove alone
29.55 % of the customers took a carryout less than 4 times in a month & drove alone
28.35 % of the customers accepted a carryon coupon while driving to work before noon.
29.26 % of the customers accepted a carryon coupon while driving to home in the evening.

Drivers most likely to accept a carry out coupon
- have taken a carry out atleast once in a month
- drivers who drive alone with no passengers
- are the ones who typically drive to work & back home.

# Recommendations and Next Steps




56.84 % of the customers accepted the coupon
41.0 % of the customers accepted the bar coupon.
81.5 % of the customers accepted the coupon and went to a bar 3 or fewer times a month.
18.5 % of the customers accepted the coupon and went to a bar more than 3 times in a month.
35.31 % of customers, who accepted the coupon, were over 25 and went to the bar more than once
64.69 % of customers, who accepted the coupon, were less than 25 years of age and never went to a bar
2.06 % of customers, who accepted the coupon, went to a bar more than once & had occupations other than farming, fishing or forestry & also had passengers that were not a kid
47.52 % of customers who go to bars more than once, who have no kids and were not widowed
30.11 % of customers who go to bars more than once, and are under the age of 30
18.86 % of customers who go to cheap restaurants more than 4 times a month and have income less than 50k

Drivers most likely to accept a bar coupon
- have been atleast once to a bar.
- have no kid passangers.
- are over the age of 30.
