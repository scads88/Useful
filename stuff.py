# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 23:32:23 2018

@author: john3

"""
import sys
sys.path.append(r"C:\Users\john3\Anaconda3\Lib\site-packages\financial_fundamentals")
import pandas as pd
import financial_fundamentals as ff

date_range = pd.date_range('2012-1-1', '2013-12-31')
required_data = pd.DataFrame(columns=['MSFT', 'GOOG', 'YHOO', 'IBM'], index=date_range)

eps = ff.accounting_metrics.earnings_per_share(required_data)
print (eps)