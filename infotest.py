# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 12:11:47 2018

@author: john3
"""

import requests
import bs4 as bs

resp=requests.get("http://www.rttnews.com/CorpInfo/ClinicalTrialCalendar.aspx")
soup=bs.BeautifulSoup(resp.text, "lxml")
print(soup)