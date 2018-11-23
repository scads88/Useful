# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:05:22 2018

@author: john3
"""

import bs4 as bs
import pandas as pd
import os
import requests

#global variables



rec=requests.get("http://investsnips.com/complete-list-of-biotechnology-companies-listed-on-u-s-exchanges/")
soup=bs.BeautifulSoup(rec.text, "lxml")
littlesoup=soup.find_all("div", class_="et_pb_text_inner")[4:6]
moreshit=[i.find_all("a", href=True) for i in littlesoup]
print(moreshit[1])
adme=[]
dick=[]
jont=moreshit[0:1][:len(moreshit)]
for i in jont:
    dick.append(i["href"])
    adme.append(i.get_text().replace(")", "").split(" ("))
#print(dick)

for i in range(len(dick)):
    x=(dick[i])
    adme[i].extend([x])
#print(adme)

somedic={"Biotech":adme}
#print(somedic)
df=pd.DataFrame.from_dict(somedic["Biotech"])
#print(df)

#cockdic={adme[1]:}
#dfx=pd.DataFrame.from_dict(cockdic)
#print(dfx)

#df.to_csv("allbiotech.csv", mode="w", header="True")