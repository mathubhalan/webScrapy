# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:09:09 2019
To do 
>>> Fetch the block & URL in a DF
>>> Browse block, navigate and fetch the table. 
>>> Check pagination, if yes iter each page and follow step 2
>>> once a bloc is completed follow step 2,3
@author: Mathu
"""
import requests
from bs4 import BeautifulSoup
# Set headers  
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})



url = "https://liko.in/districts/tiruchirappalli"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
'''
lst=soup.find_all("table").get("a")
print(lst)
'''

#table = soup.find('table', {'class': 'table_1'})
ul = soup.find('ul', {'class':'double li'})
#print(table)
a_href = ul.find_all('a')
print(a_href)
link=[]
block = []
#block=[]
for a in a_href:
    link.append(a.get('href'))
    block.append(a.text)

block = [w.replace("Schools in ",'') for w in block]

s = "Schools in Trichy"
a = s.replace("Schools in ",'')
print (a)

print(df_blocks['URL'])

'''
rows = table.findAll('tr')
for tr in rows:
    cols = tr.findAll('td')
    if len(cols) >= 4 and "2013" in cols[3].text:
        link = cols[1].find('a').get('href')
        print link
'''