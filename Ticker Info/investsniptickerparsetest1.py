# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 23:59:12 2018

@author: john3
"""


import requests
import bs4 as bs

resp=requests.get("http://investsnips.com/publicly-traded-micro-cap-pharmaceutical-companies/")
soup=bs.BeautifulSoup(resp.text, "lxml")
scriptag=soup.find_all("script")[5]#.string
moretag=scriptag.find("container_id")
print(moretag)

