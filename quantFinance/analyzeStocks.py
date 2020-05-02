"""
Created on Tue Apr 28 13:49:25 2020

@author: Kigen
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests
from requests_html import HTMLSession

#First chunk of this code was copied from Andrew Treadways' GitHub:
#https://github.com/atreadw1492/yahoo_fin/blob/master/yahoo_fin/stock_info.py
   
base_url = "https://query1.finance.yahoo.com/v8/finance/chart/"

def build_url(ticker, start_date = None, end_date = None, interval = "1d"):
    
    if end_date is None:  
        end_seconds = int(pd.Timestamp("now").timestamp())
        
    else:
        end_seconds = int(pd.Timestamp(end_date).timestamp())
        
    if start_date is None:
        start_seconds = 7223400    
        
    else:
        start_seconds = int(pd.Timestamp(start_date).timestamp())
    
    site = base_url + ticker
    
    #"{}/v8/finance/chart/{}".format(self._base_url, self.ticker)
    
    params = {"period1": start_seconds, "period2": end_seconds,
              "interval": interval.lower(), "events": "div,splits"}
    
    
    return site, params


def force_float(elt):
    
    try:
        return float(elt)
    except:
        return elt
    


def get_data(ticker, start_date = None, end_date = None, index_as_date = True,
             interval = "1d"):
    '''Downloads historical stock price data into a pandas data frame.  Interval
       must be "1d", "1wk", or "1mo" for daily, weekly, or monthly data.
    
       @param: ticker
       @param: start_date = None
       @param: end_date = None
       @param: index_as_date = True
       @param: interval = "1d"
    '''
    
    if interval not in ("1d", "1wk", "1mo"):
        raise AssertionError("interval must be of of '1d', '1wk', or '1mo'")
    
    # build and connect to URL
    site, params = build_url(ticker, start_date, end_date, interval)
    resp = requests.get(site, params = params)
    
    
    if not resp.ok:
        raise AssertionError(resp.json())
        
    
    # get JSON response
    data = resp.json()
    
    # get open / high / low / close data
    frame = pd.DataFrame(data["chart"]["result"][0]["indicators"]["quote"][0])

    # add in adjclose
    frame["adjclose"] = data["chart"]["result"][0]["indicators"]["adjclose"][0]["adjclose"]
    
    # get the date info
    temp_time = data["chart"]["result"][0]["timestamp"]
    
    
    frame.index = pd.to_datetime(temp_time, unit = "s")
    frame.index = frame.index.map(lambda dt: dt.floor("d"))
    
    
    frame = frame[["open", "high", "low", "close", "adjclose", "volume"]]
        
    frame['ticker'] = ticker.upper()
    
    if not index_as_date:  
        frame = frame.reset_index()
        frame.rename(columns = {"index": "date"}, inplace = True)
        
    return frame

#read in stock data
market = ["S&P 500", "DJIA", "Small Cap", "Apple", "Microsoft", "Large Cap"]

sp = get_data('^GSPC').tail(90)
dow = get_data('^DJI').tail(90)
sml = get_data('^SML').tail(90)
aapl = get_data('AAPL').tail(90)
msft = get_data('MSFT').tail(90)
ndx = get_data('^NDX').tail(90)

combinedMarket = sp.join(dow, how = 'inner', rsuffix = '_dow').join(sml, how = 'inner', rsuffix = '_sml')
combinedMarket = combinedMarket.join(aapl, how = 'inner', rsuffix = '_aapl').join(msft, how = 'inner', rsuffix = '_msft')
combinedMarket = combinedMarket.join(ndx, how = 'inner', rsuffix = '_ndx')

plotData = combinedMarket[['adjclose', 'adjclose_dow', 'adjclose_sml', 'adjclose_aapl', 'adjclose_msft', 'adjclose_ndx']]

plt.figure(figsize=(20,10))

xlab = range(90)

for n, stock in enumerate(plotData):
    plt.subplot(2, 3, n + 1)
    plt.plot(xlab, plotData[stock])
    plt.title(market[n])


curiousList = ['COWN', 'CPG', 'VNOM', 'KOS', 'HLX']

#function to visualize a list of stocks using volume, adjusted close, open, high, etc.
#default period is 90 days and default field called is adjusted close

def plot_stockList(stockList, period = 90, label = 'adjclose'):
    
    userInput = int(input("Want to use your own input? 1 for Yes, 0 for No: ")) 
    print (userInput)
    
    if (userInput == 1):
        
        stocks = []
        n = int(input("Enter number of stocks to analyze: "))
        print("You will enter ", n, " stock tickers")

        for i in range(n):
            ticker = str(input("Enter Tickers for Stocks: "))
            stocks.append(ticker)

        print ("You entered the following stocks: ", stocks)
        
    else:
        
        stocks = curiousList

    par = len(stocks)
    
    field = label
    stockData = pd.DataFrame(get_data("^GSPC")[field]).tail(period)

    for stock in range(par):
        data = pd.DataFrame(get_data(stocks[stock])[field]).tail(period)
        stockData = stockData.join(data, how = 'inner', rsuffix = stocks[stock])

    stockData = stockData.drop(columns = [field])
    
    xlab = range(period)

    plt.figure(figsize=(20,10))

    for n, stock in enumerate(stockData):
        plt.subplot(round(par/2), par-round(par/2), n + 1)
        plt.suptitle("Now plotting: " + field + " over the last " + str(period) + " days", size = 16)
        plt.plot(xlab, stockData[stock])
        plt.title(stocks[n])
        
    print ("Reached End Successfully")

   
#technical indicators
#the function below takes in a list of stocks (could be one) and returns OBV results and plots showing OBV 

def OnBalanceVolume (stocks, period):
    
    #initialize dataframes and other parameters
    stockData = pd.DataFrame(get_data("^GSPC")[['adjclose', 'volume']]).tail(period)
    OBV_Data = pd.DataFrame()
    par = len(stocks)
    
    #get price and volume data   
    for stock in range(par):
        data = pd.DataFrame(get_data(stocks[stock])[['adjclose', 'volume']]).tail(period)
        stockData = stockData.join(data, how = 'inner', rsuffix = stocks[stock])

    stockData = stockData.drop(columns = ['adjclose', 'volume'])

    for stock in range(par):
        stockData['priceChange_'+stocks[stock]] = stockData['adjclose'+stocks[stock]].pct_change().fillna(0)
        stockData['volDirection_'+stocks[stock]] = (abs(stockData['priceChange_'+stocks[stock]])/stockData['priceChange_'+stocks[stock]])*stockData['volume'+stocks[stock]]
        OBV_Data['OBV_'+stocks[stock]] = stockData['volDirection_'+stocks[stock]].cumsum().fillna(0)
    
    plotOBV = plt.figure(figsize=(20,10))

    for n, stock in enumerate(OBV_Data):
        plt.subplot(round(par/2), par-round(par/2), n + 1)
        plt.suptitle("Now plotting OBV over the last " + str(period) + " days", size = 16)
        plt.plot(xlab, OBV_Data[stock])
        plt.title(stocks[n])
    
    print ("OBV Reached End Successfully")
    #plotOBV.show()
    
    return (stockData, OBV_Data, plotOBV)

plot_stockList(curiousList, 360, 'adjclose')
plot_stockList(curiousList, 90, 'adjclose') #plot adjusted close over 90 days
plot_stockList(curiousList, 90, 'volume') #plot trade volume over 90 days
OnBalanceVolume(stocks = curiousList, period = 90) #assess on balance volume over the last 90 days

