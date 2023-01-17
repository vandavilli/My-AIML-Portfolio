# Practical Application Assignment 5.1 (Module 5, UC Berkeley AI/ML Professional Certification)
The practical application I have used to study the dataset helps develop insights into the following question “Will a customer accept the coupon?”. I have developed this notebook for 2 coupon types & the various acceptance numbers help develop insights into the customer & coupon acceptance rates. 

# Brief Description of the Dataset
The data used for the data analysis assignment comes from the UCI Machine Learning repository and was collected via a survey on Amazon Mechanical Turk. The survey describes different driving scenarios, including the destination, current time, weather, passenger, etc., and then asks people whether they will accept the coupon if they are the driver. Answers given that the users will drive there “right away” or “later before the coupon expires” are labeled as “Y = 1”, and answers “no, I do not want the coupon” are labeled as “Y = 0”. There are five different types of coupons—less expensive restaurants (under $20), coffee houses, carry out and take away, bars, and more expensive restaurants ($20–$50).

In order to study and present some of the data analysis and cleaning techniques, I have used 2 different coupon types - Bar, Carry out & Take away. The meta data & its description is available inside the notebook. 

# Codes for Visualization and Analysis
The notebook can be found at this location: https://github.com/vandavilli/BH-PCMLAI/blob/main/prompt.ipynb

# Summary
After studying the acceptance rates for **Bar Coupons**, here are some of my findings:
- Bar Coupons have an average acceptance rate of 41% which is neither too low or too high. 
- Some of the factors that drive a better acceptance rates include
  1. Age of the drivers likely to be over 30.
  2. Drivers who ride with no kids
- Occupation or Marital Status don't seem to have any significant impact on coupon acceptance.

After studying the acceptance rates for **CarryOut & Takeaway Coupons**, here are some of my findings:
- CarryOut coupons have a higher acceptance rate ( 73% ) as compared to Bar Coupons
- Some of the factors that drive a better acceptance rates include
  1. Drivers have taken a carry out atleast once in a month
  2. Drivers who drive alone with no passengers
  3. Drivers who typically drive to work & back home.
- Based on the demographic analysis, single male (30.9%) & a married female (30.1) driver seem to have a higher probablity of accepting a carryout coupon.

# Recommendations and Next Steps
Based on the above coupon analysis, it is evident that Carry Coupons have a better acceptance rate over Bar Coupons. Hence, my recommendation would be target CarryOut & Takeaway Coupons. The target drivers would be the ones who drive ==alone==, typically to work & back home and are either single males or married females. 
