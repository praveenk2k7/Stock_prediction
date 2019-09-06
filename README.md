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
 
 
# Regression models to predict the price


**Linear Regression**

Simple linear regression is useful for finding relationship between two continuous variables. One is predictor or independent variable and other is response or dependent variable. It looks for statistical relationship but not deterministic relationship. Relationship between two variables is said to be deterministic if one variable can be accurately expressed by the other.




  



