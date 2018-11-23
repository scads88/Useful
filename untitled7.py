
import json
import re
import bs4 as bs
import requests

coupleofurlpieces=[]
resp=requests.get("http://investsnips.com/publicly-traded-micro-cap-pharmaceutical-companies/")
soup=bs.BeautifulSoup(resp.text, "lxml")
scriptag=soup.find_all("script")[5].string

douche=scriptag[133:2948]
#print(douche)
dx=json.loads(douche)
print(dx)
#print(dx["Micro Cap Pharmaceuticals"][1])



