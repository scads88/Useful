# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 23:29:59 2018

@author: john3
"""

import bs4 as bs
import pandas as pd
import os
import requests

#global variables

rec=requests.get("http://investsnips.com/list-of-publicly-traded-pharmaceutical-companies/")
soup=bs.BeautifulSoup(rec.text, "lxml")
littlesoup=soup.find_all("div", class_="et_pb_text_inner")[7:9]
#print(littlesoup)
finalsouplist=[i.find_all("a", href=True) for i in littlesoup]

nameNtickerlist=[]
hreflist=[]
bselementtaglist=finalsouplist[0]
for bselementtag in bselementtaglist:
    hreflist.append(bselementtag["href"])
    nameNtickerlist.append(bselementtag.get_text().replace(")", "").split(" ("))
for num in range(len(hreflist)):
    x=(hreflist[num])
    nameNtickerlist[num].extend([x])
nameNtickerNhreflist={"Pharma":nameNtickerlist}
df1=pd.DataFrame.from_dict(nameNtickerNhreflist["Pharma"])
print(df1)
df1.to_csv("pharma1of2.csv", mode="w", header="True")