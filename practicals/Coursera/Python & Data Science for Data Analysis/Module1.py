#this uses russell 2000 and s&p 500 instead of facebook and microsoft

import pandas as pd

#import data

russ2000 = pd.read_csv('/Users/Kigen/Documents/r/RUSS.csv')
sp500 = pd.read_csv('/Users/Kigen/Documents/r/GSPC.csv')

#check types of data and print first and last few lines of data
print (type(russ2000), type(sp500))
print(russ2000.shape, sp500.shape) #notice how russ has one extra row

#by looking at the head and tail, we can find the extra row
print (russ2000.head(), russ2000.tail()) 
#print (sp500.head(), sp500.tail())

#display summary statistics
russSummary = russ2000.describe()
#spSummary = sp500.describe()

print russSummary, spSummary
#can also display russ2000.describe()

#slicing the dataframe
russ2000[3:5] #display specific rows
russ2000.iloc[3:5, 3:5] #display or extract specific rows and columns

russClose = russ2000.iloc[0:2551 , 5] #slice by location/position
spClose = sp500.iloc[0:2551, 5]

#we can also slice by name of the variable
print (russ2000.loc[: , 'Close']) #extracts close data

print (spClose[1:365].plot())
print (spClose[366:730].plot())
print (spClose[731:1100].plot())
print (spClose[1101:].plot())
