# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:57:41 2018

@author: john3
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bs4 as bs
import pickle
import collections
import datetime
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
import datetime as dt
import requests


df=pd.DataFrame.from_csv("douche1.csv", encoding = "ISO-8859-1")
biotickers=df["1"][5:7] # calls the column for tickers generated


class CompanyEvaluation:
    pass
    #can use class variables instead of hardcoding into methods

    def __init__(self):
        pass
    
    
    def infotrigger1(self):
        pass


    def roundTime(dt=None, roundTo=60): #From Thierry Husson 2012
        if dt == None : dt = datetime.datetime.now()
        seconds = (dt.replace(tzinfo=None) - dt.min).seconds
        rounding = (seconds+roundTo/2) // roundTo * roundTo
        return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)
       #print (roundTime(datetime.datetime(2012,12,31,23,44,59,1234),roundTo=15*60))


    def stockchart(self):
        #relates to what the actual prices are doing relative to self and others
        AVkey="E82V6HPLXDMUN5TM"
        totaltickers=[str(ticker) for ticker in biotickers]
        #totaltickers=["AAPL", "FB"]
        ts=TimeSeries(key=AVkey, output_format='pandas')
        start=dt.datetime.today()-dt.timedelta(days=100)
        #print(roundTime(start))
        end=dt.datetime.today()
        tickerdic={}
        #will be useful to have plt tutorial to address axes, labeling, legends again
        #combined chart, individual chart, multiple timescales, (daily/weekly/monthly)
        #incorporate something in to account for value error
        #incorporate the filter for whether or not generate stock data
        #incorporate aspects to plot by days
        for ticker in totaltickers: 
            data, meta_data=ts.get_daily_adjusted(ticker)
            tickerdic[ticker]=data
            #data2, meta_data2=ts.get_intraday(ticker)
            #plt.legend(meta_data["2. Symbol"])
            #tickerdic[ticker]["5. adjusted close"].plot(label=ticker)
            plt.xlabel("100 Day Moving Average")
            plt.ylabel("Stock Price ($)")
            plt.axis([start, end, 0, 200])
            #print(meta_data["2. Symbol"])
            plt.legend(loc="upper right")
            #print(data.head())
        #print(len(tickerdic["DGX"]))
        #print(tickerdic)
        plt.title("Testgraph of tickers")
        plt.show()
        #return tickerdic["AKAO"]
        print (tickerdic["AKAO"]["3. low"]["2018-07-03"])
        #return "cheese"
        

print(CompanyEvaluation().stockchart())