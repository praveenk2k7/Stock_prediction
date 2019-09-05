# Stock_prediction
Predict stock prices using different Deep learning and ML models

# Overview
This is the project on predicting the stock prices using various Machine Learning and Deep Learning models ranging from simple linear models to reinforcement learning. The task also includes analyzing stocks using python. The project is based on basic python and ML libraries along with historical data of AAPL downloaded form yahoo finance. The link is provided below

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

# Task 1: 3 different regression models to predict the price

  



