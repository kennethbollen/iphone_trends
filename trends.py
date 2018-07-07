#python3

import pandas as pd
import matplotlib as plt

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
df_iphone.plot()
plot.show()





