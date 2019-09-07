import pandas as pd
import datetime
#import pandas_datareader.data as web
from pandas import Series, DataFrame
import math
import numpy as np
import sklearn.preprocessing as preprocessing
import operator
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2017, 1, 11)

#df = web.DataReader("AAPL", 'yahoo', start, end)
#df.tail()
df=pd.read_csv('AAPL.csv')
dfreg=df.loc[:,['Adj Close','Volume']]
dfreg['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
dfreg['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0
dfreg.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
dfreg = df.loc[:,['Adj Close','Volume']]
dfreg['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
dfreg['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0

dfreg.fillna(value=-99999, inplace=True)# We want to separate 1 percent of the data to forecast
forecast_out = int(math.ceil(0.01 * len(dfreg)))# Separating the label here, we want to predict the AdjClose
forecast_col = 'Adj Close'
dfreg['label'] = dfreg[forecast_col].shift(-forecast_out)
X = np.array(dfreg.drop(['label'], 1))# Scale the X so that everyone can have the same distribution for linear regression
X = preprocessing.scale(X)# Finally We want to find Data Series of late X and early X (train) for model generation and evaluation
X_lately = X[-forecast_out:]
X = X[:-forecast_out]# Separate label and identify it as y
y = np.array(dfreg['label'])
y = y[:-forecast_out]

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33, random_state=42)

# Linear regression
clfreg = LinearRegression(n_jobs=-1)
clfreg.fit(X_train, y_train)# Quadratic Regression 2
clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
clfpoly2.fit(X_train, y_train)

# Quadratic Regression 3
clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
clfpoly3.fit(X_train, y_train)

Results={'Linear regression':clfreg.score(X_test, y_test),'Quadratic regression':clfpoly2.score(X_test, y_test),'cubic regression':clfpoly3.score(X_test, y_test),}
print("Models Tested: ")
print(list(Results.keys()))
print("Best Performing model: ")
print("{} with confidence score of {}".format(max(Results.items(), key=operator.itemgetter(1))[0],Results[max(Results.items(), key=operator.itemgetter(1))[0]]))

