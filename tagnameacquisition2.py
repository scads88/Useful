# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:21:28 2018

@author: john3

testing out the name and length of identifiers
"""

import requests
import bs4
from bs4 import BeautifulSoup
import sys
import pandas as pd

#have a spot for a global ticker or tickers variable up top

_CIK_URI = 'http://www.sec.gov/cgi-bin/browse-edgar' \
           '?action=getcompany&CIK={s}&count=10&output=xml'


def get_cik(symbol):
    """
    Retrieves the CIK identifier of a given security from the SEC based on that
    security's market symbol (i.e. "stock ticker").
    :param symbol: Unique trading symbol (e.g. 'NVDA')
    :return: A corresponding CIK identifier (e.g. '1045810')
    """

    response = requests.get(_CIK_URI.format(s=symbol))
    page_data = bs4.BeautifulSoup(response.text, "html.parser")
    cik = page_data.companyinfo.cik.string
    return cik

ciknumber=get_cik("AZN")
print (ciknumber)
#get_cik("WMT")=ciknumber

#print(ciknumber)
###################################################
# Access page
cik = ciknumber
#cik = '0000051143'
type = '10-K'
dateb = '20180101'

# Obtain HTML for search page
base_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type={}&dateb={}"
edgar_resp = requests.get(base_url.format(cik, type, dateb))
edgar_str = edgar_resp.text

# Find the document link
doc_link = ''
soup = BeautifulSoup(edgar_str, 'html.parser')
table_tag = soup.find('table', class_='tableFile2')
rows = table_tag.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 3:
        if '2017' in cells[3].text:
            doc_link = 'https://www.sec.gov' + cells[1].a['href']

# Exit if document link couldn't be found
if doc_link == '':
    print("Couldn't find the document link")
    sys.exit()

# Obtain HTML for document page
doc_resp = requests.get(doc_link)
doc_str = doc_resp.text

# Find the XBRL link
xbrl_link = ''
soup = BeautifulSoup(doc_str, 'html.parser')
table_tag = soup.find('table', class_='tableFile', summary='Data Files')
rows = table_tag.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 3:
        if 'INS' in cells[3].text:
            xbrl_link = 'https://www.sec.gov' + cells[2].a['href']

# Obtain XBRL text from document
xbrl_resp = requests.get(xbrl_link)
xbrl_str = xbrl_resp.text

# Find and print stockholder's equity
soup = BeautifulSoup(xbrl_str, 'lxml')

tag_list = soup.find_all()
testset=set()
for tag in tag_list:
    testset.add(tag.name)
    #print (tag.name)
    if tag.name == 'us-gaap:depreciation':
        pass#print("depreciation: " + tag.text)
print (testset)
print(len(testset))
uniqueTICKERdic={}

#df1=pd.DataFrame(testset)
#print(df1)