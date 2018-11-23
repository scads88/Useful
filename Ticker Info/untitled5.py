# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 00:00:08 2018

@author: john3
"""

import bs4 as bs
import pandas as pd
import os
import requests

#global variables

rec=requests.get("http://investsnips.com/complete-list-of-biotechnology-companies-listed-on-u-s-exchanges/") #request call
soup=bs.BeautifulSoup(rec.text, "lxml") #souping it up
littlesoup=soup.find_all("div", class_="et_pb_text_inner")[4:6] #finding a subset of soup we want to focus on
finalsouplist=[i.find_all("a", href=True) for i in littlesoup]# finding the exact piece of the soup we care about



nameNtickerlist=[] #list to hold the names of the companies and tickers
hreflist=[] #list of the hrefs
bselementtaglist=finalsouplist[0] #gotta take a subset
for bselementtag in bselementtaglist:
    hreflist.append(bselementtag["href"])
    nameNtickerlist.append(bselementtag.get_text().replace(")", "").split(" ("))
for num in range(len(hreflist)):
    x=(hreflist[num])
    nameNtickerlist[num].extend([x])
nameNtickerNhreflist={"Biotech":nameNtickerlist}
df1=pd.DataFrame.from_dict(nameNtickerNhreflist["Biotech"])
print(df1)
#df1.to_csv("allbiotech.csv", mode="w", header="True")