# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:03:38 2018

@author: john3
"""

import json
import re
import bs4 as bs
import requests
import pandas as pd
import numpy as np

coupleofurlpieces=[]
resp=requests.get("http://investsnips.com/publicly-traded-micro-cap-pharmaceutical-companies/")
soup=bs.BeautifulSoup(resp.text, "lxml")
scriptag=soup.find_all("script")[5].string

douche=scriptag[133:2948]
dx=json.loads(douche)
print(dx)
dx=pd.DataFrame.from_dict(dx["Micro Cap Pharmaceuticals"])
print(dx)
#dx.to_csv("microtest.csv", mode="w", header="True")
