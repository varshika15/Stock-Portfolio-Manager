#import relevant modules
import pandas as pd
import numpy as np
from pandas_datareader import data
from math import sqrt
import matplotlib.pyplot as plt
 
 
#download data into DataFrame and create moving averages columns
sp500 = data.DataReader('MSFT', 'yahoo',start='1/1/2000',end='1/2/2018')
sp500['42d'] = np.round(sp500['Close'].rolling(window=42).mean(),2)
sp500['252d'] = np.round(sp500['Close'].rolling(window=252).mean(),2)
 
#create column with moving average spread differential
sp500['42-252'] = sp500['42d'] - sp500['252d']
 
#set desired number of points as threshold for spread difference and create column containing strategy 'Stance'
X = 50
sp500['Stance'] = np.where(sp500['42-252'] > X, 1, 0)
sp500['Stance'] = np.where(sp500['42-252'] < X, -1, sp500['Stance'])
sp500['Stance'].value_counts()
 
#create columns containing daily market log returns and strategy daily log returns
sp500['Market Returns'] = np.log(sp500['Close'] / sp500['Close'].shift(1))
sp500['Strategy'] = sp500['Market Returns'] * sp500['Stance'].shift(1)
 
#set strategy starting equity to 1 (i.e. 100%) and generate equity curve
sp500['Strategy Equity'] = sp500['Strategy'].cumsum() + 1
 
#show chart of equity curve
sp500['Strategy Equity'].plot()