# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:29:05 2018

@author: john3
"""

import bs4 as bs
import requests

resp=requests.get("https://web.archive.org/web/20171004154237/http://www.marketwatch.com:80/investing/stock/nke/profile")
soup=bs.BeautifulSoup(resp.text, "lxml")
print(soup)