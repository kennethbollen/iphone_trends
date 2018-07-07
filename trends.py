#python3

import pandas as pd
import matplotlib as plt

#APPROACH 1
'''
#make the index of the dataframe into datetime for time series analysis
df_samsung = pd.read_csv('/Users/DELL/Documents/GitHub/iphone_trends/iphone_trends.csv', skiprows=2)
df_iphone.index = df_iphone['Week']
del(df_iphone['Week'])
df_iphone.index = pd.to_datetime[df_iphone.index]
df_samsung = df_samsung.rename(columns='iphone: (Worldwide)': 'iphone_searches')

df_samsung = pd.read_csv('/Users/DELL/Documents/GitHub/iphone_trends/samsung_trends.csv', skiprows=2)
df_samsung.index = df_samsung['Week']
del(df_samsung['Week'])
df_samsung.index = pd.to_datetime[df_samsung.index]
df_samsung = df_samsung.rename(columns='samsung galaxy: (Worldwide)': 'samsung_searches')

#merge the iphone and samsung datasets
df_smart = df_iphone.join(df_samsung, how='inner')

#line plot graph for eda
df_smart.plot(title='smart phone google searches', grid=True)'''

#APPROACH 2

#read csv for iphone searches
df = pd.read_csv('/Users/DELL/Documents/GitHub/iphone_trends/iphone_trends.csv', skiprows=2)
#read csv for apple stock history
df_stock = pd.read_csv('/Users/DELL/Documents/GitHub/iphone_trends/aapl_stock.csv')

#reindex dataframe to be date
df.index = pd.to_datetime(df['Week'], format='%d/%m/%Y')
del(df['Week'])

df_stock.index = pd.to_datetime(df_stock['Date'], format='%d/%m/%Y')
#stock data is daily and search data is weekly, need to resample data to be consistent
df_stock.resample('W').sum()
#focus is only trading volume, remove rest of information
df_stock = df_stock['Volume']

# Convert the stock index and iphone search index into sets
set_stock_dates = set(df_stock.index)
set_iphone_dates = set(df_iphone.index)

#which dates don't match?
print(set_iphone_date - set_stock_date)

#merge stock volume and search volume data
df_comp = df.join(df_stock, how='inner')












