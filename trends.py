#python3

import pandas as pd
import matplotlib as plt

#make the index of the dataframe into datetime for time series analysis
df_iphone = pd.read_csv('/Users/DELL/Google Drive/Data Analysis/Python/iphone_trends.csv', skiprows=2)
df_iphone.index = df_iphone['Week']
df_iphone.index = pd.to_datetime[df_iphone.index]

#line plot graph for eda
df_iphone.plot()
plot.show()





