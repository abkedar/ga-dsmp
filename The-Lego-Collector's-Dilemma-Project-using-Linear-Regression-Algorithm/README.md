### Project Overview

 This dataset contains information on lego sets scraped from lego.com. Each observation is a different lego set with various features like how many pieces in the set, rating for the set, number of reviews per set etc. The aim was to build a linear regression model to predict the price of a set.


### Learnings from the project

 This concept that I aaplied in this proejct are Train-test split, Correlation between the features, Linear Regression, MSE, R^2.


### Approach taken to solve the problem

 This datasets has both type of data that is numerical and categorical features. But since I want to predict the price of the lego. I need only numerical data, so I separate the usefull data. Next the data which I separate in that is there any correlation between two features, if yes then that too we have take into consideration. Though the data  data was small, the most interesting part was to find correlation between columns. This approach was applied after the spliting the data into train set and test set. Then applly the LinearRegression algorithm.  


### Challenges faced

 The challenge I have that what criteria should i decide that what should be the value of the correlation between the column. This was a bit of try it not work, then try another thershold level. Thus after predicting the value, it turn out that majority value of predicted were close to  close the the tru value. But still the other point are still need to take into consideration.


