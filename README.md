# Stock_prediction
Predict stock prices using different Deep learning and ML models

# Overview
This is the project on predicting the stock prices using various Machine Learning and Deep Learning models. The project also includes analyzing stocks using python. The project is based on basic python and ML libraries along with historical data of AAPL downloaded form yahoo finance. The link is provided below

https://finance.yahoo.com/quote/AAPL/history?p=AAPL

# Data Analysis

![image](https://user-images.githubusercontent.com/44360746/64338966-81ad0000-d015-11e9-813d-25f8f9a31fbb.png)

The dataframe contains six different features, 

open which remarks the starting price of the stock at the opening of the day. Similarly, Close represents the close price of the stock at the end of the day. Low and High are the lowest point and the highest point respectively on the particular day. The adjusted closing price is the amended closing price with factors in anything that might affect the stock price after the market closes.

**Exploring Rolling Mean:** 

Rolling Mean/Moving Average smooths out the price, cut down the noise and reveals the trend of the stock price. It smooths out by creating a constantly updated average price.

![image](https://user-images.githubusercontent.com/44360746/64339806-60e5aa00-d017-11e9-9ba9-d55579272901.png)

The moving average curve showcase the increasing or decreasing trend of stocks price.

**Determining risk and return:**

The return of the stock is found by the fraction of price at time t to the price at time shifted back by 1 minus 1. 
Expected return is the mean or expected value of the probability distribution of investment returns. 

![image](https://user-images.githubusercontent.com/44360746/64340202-2defe600-d018-11e9-97d1-03957907fc63.png)

The plot shows there is a deop at 2013 adn the ideal stock return is based on return as high or stable.

# Feature Engineering

It is important to clean the data before using them in the model. In our dataset, we predict the adjusted close value using the features. 

    Drop missing value
    Separate one percent of data to forecast
    Separate the label, we want to predict the AdjClose
    Scale the independent variable X so that every variable has same distribution
    Finally We want to find Data Series of late X and early X (train) for model generation and evaluation
    Separate label and identify it as y
    Separation of training and testing of model by cross validation train test split
 
 ![Features](https://user-images.githubusercontent.com/44360746/64469383-9eefe480-d163-11e9-8633-8588f6400ae5.png)
 

# Regression models to predict the price

**Results**

**Confidence score: **

R-squared is a statistical measure of how close the data are to the fitted regression line. It is also known as the coefficient of determination, or the coefficient of multiple determination for multiple regression.The definition of R-squared is fairly straight-forward; it is the percentage of the response variable variation that is explained by a linear model.

R-squared = Explained variation / Total variation

**MSE**
Mean Squared error: squared differences between the estimated value and the actual value.

***Linear Regression***



Mean Squared Error=119.7
Confidence score = 72.5%

***Adding ridge regression to Linear classifier***

![Ridge regression](https://user-images.githubusercontent.com/44360746/64469564-ed52b280-d166-11e9-83f6-560a81ecee94.png)

As the tunable paramert lambda increases, the MSE increases. So the model performs better with no regularization.

***Quadratic Regression with ridge regularizer***

MSE: 118.9
Confidence Score = 72.9%

***cubic features with ridge regularizer***

MSE: 118.9
Confidence Score = 72.9%


**Forecast using Linear Regression prediction**

![Forecast](https://user-images.githubusercontent.com/44360746/64469612-8bdf1380-d167-11e9-914f-a1ec106f99ee.png)







  



