import pandas as pd
from openpyxl.workbook import workbook
import matplotlib.pyplot as plt

russ2000 = pd.read_csv("/Users/Kigen/Documents/r/RUSS.csv")

print (russ2000) #print first 4 and last 4 rows
print (russ2000.columns) #print column names

print (russ2000.iloc[4])
print (russ2000.iloc[2:5])
print (russ2000['Close'])

print (russ2000[russ2000['Close'] > 700])
print (russ2000.loc[russ2000['Close']>700])

print (russ2000[(russ2000['Date'] >= '2019-01-01') & (russ2000['Close'] >= 1355.92)])

russ2000['Indicator'] = russ2000['Close'].apply(lambda x: 0 if x < 700 else 1 if x < 1500 else 2)

print (russ2000['Indicator'])

russ2000['TimesTwo'] = False

russ2000.loc[russ2000['Close'] < 1000, 'TimesTwo'] = True

print (russ2000['TimesTwo'])

aggData = russ2000.groupby(['Indicator']).mean().sort_values('TimesTwo')

print (aggData)
