import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import datetime
import numpy as np
#import json
function="TIME_SERIES_DAILY_ADJUSTED"
api_key="E82V6HPLXDMUN5TM"
ticker="MSFT"
#api_key=open("alpha.txt", "r").read()
data=requests.get("https://www.alphavantage.co/query?function={}&symbol={}&apikey={}".format(function, ticker, api_key))
data=data.json()
data=data["Time Series (Daily)"]
df=pd.DataFrame(columns=["date", "open", "high", "low", "close", "adjusted close", "volume", "dividend amount", "split"])
for d,p in data.items():
    date=datetime.datetime.strptime(d, "%Y-%m-%d")
    data_row=[date, float(p["1. open"]), float(p["2. high"]), float(p["3. low"]), float(p["4. close"]), float(p["5. adjusted close"]), float(p["6. volume"]), float(p["7. dividend amount"]), float(p["8. split coefficient"])]
    df.loc[-1,:]=data_row
    df.index=df.index+1
data=df.sort_values("date")
data['close']=data['close'].astype(float)
data['day']=np.round(data['close'])#.rolling(window=5).mean(),2)
data[['day','close']].plot()
plt.show()



"""

df=pd.DataFrame(data)
df=df.T
print(df)
#df["5. adjusted close"].plot()
#plt.show()
"""
