# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 14:41:33 2018

@author: john3
"""

import os
import pandas as pd
import json
import requests
import bs4 as bs


coupleofurlpieces=[]
resp=requests.get("http://investsnips.com/publicly-traded-micro-cap-pharmaceutical-companies/")
soup=bs.BeautifulSoup(resp.text, "lxml")
scriptag=soup.find_all("script")[5].string

douche=scriptag[133:2948]
dx=json.loads(douche)
print(dx)
dx=pd.DataFrame.from_dict(dx["Micro Cap Pharmaceuticals"])
print(dx)

    
dx.to_csv("microtest.csv", mode="w", header="True")