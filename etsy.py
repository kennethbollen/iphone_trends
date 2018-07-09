import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.stattools import adfuller
from math import sqrt

#convert the dataframe index into datetime for time series analysis
etsy.index = etsy['Date']
etsy.index = pd.to_datetime(etsy.index)
del(etsy['Date'])

#create a dataframe with just the closing stock price, which is the focus of the analysis
returns = pd.DataFrame(etsy['Adj Close'])

#change the returns from daily to weekly
returns = returns.resample('W').mean()
returns = returns.dropna()

#calculate the autocorrelation of the weekly returns of ETSY
autocorrelation = returns['Adj Close'].autocorr()
print('The autocorrelation of eekly ETSY returns is %4.2f' %(autocorrelation))
n = len(returns)
conf = 1.96/sqrt(n)
print('The approximate confidence interval is +/- %4.2f' %(conf))
plot_acf(returns, alpha=0.05, lags=20)

#do the etsy prices follow a random walk - augmented dickey fuller test
#with the adf test the null hypothesis is that the etsy stock price follows a random walk
#if p-value is below 0.05 we reject the null that etsy stock prices follows a random walk
results = adfuller(etsy['Adj Close'])
print(results)
print('The p-value of the test on prices is: ' + str(results[1]))




