# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:09:09 2019
To do 
>>> Fetch the block & URL in a DF
>>> Browse block, navigate and fetch the table. 
>>> Check pagination, if yes iter each page and follow step 2
>>> once a bloc is completed follow step 2,3

1. set the page url as df_url[1], 
2. get the table values and append the data in dict
3. check for pagination if yes change the page url
4. follow step 2
5. once pagination completed move to next block
6. follow step 1-5

@author: Mathu
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
# Set headers  
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})


domain = "https://liko.in"
url = domain +"/blocks/andhanallur-block?page=2"

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
pag = soup.find('ul', {'class':'pagination'}).findChildren()[2]

#if next_li_element is None
print(pag.text, pag.find('a').get('href'))



#url = "https://liko.in/blocks/andhanallur-block"
#req = requests.get(url, headers)
#soup = BeautifulSoup(req.content, 'html.parser')
#table = soup.find('table')
#print(table)
#table = soup.find('table', {'class': 'table_1'})

#get the td & tr
'''
{'school':'',
 'href': '',
 'village':'',
 'cluster':'',
 'pin_code':''
 }
'''

def getTable(url): 
    site_url= url
    req = requests.get(site_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    #school = []
    cols = ['school','href','village','pin_code','cluster','block','district']
    df_table = pd.DataFrame(columns=cols)
    #df_table.fillna(0)
    for row in soup.select('tbody tr'):   
        
        school_dct = {}
        data = row.find_all('td')
        school_dct['school'] = data[0].find('a').text
        school_dct['href'] = data[0].find('a').get('href')
        school_dct['village']=data[1].text
        school_dct['cluster']=data[2].text
        school_dct['pin_code']=data[3].text
        school_dct['from_page_url']=site_url
        school_dct['block']=block
        school_dct['district']=dist
        df_table=df_table.append(school_dct, ignore_index=True)
    print(df_table)
    return df_table


df_district = pd.read_excel(".\schoolist.xlsx", sheet_name="district")
df_block = pd.read_excel(".\schoolist.xlsx", sheet_name="block")
df_url = pd.read_excel(".\schoolist.xlsx", sheet_name="url")
cols = ['school','href','village','pin_code','cluster','block','district']
df_school = pd.DataFrame(columns=cols)
for index,row in df_url.head(n=5).iterrows():
    req = requests.get(row['URL'], headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    for r in soup.select('tbody tr'):
        school_dct = {}
        data = r.find_all('td')
        school_dct['school'] = data[0].find('a').text
        school_dct['href'] = data[0].find('a').get('href')
        school_dct['village']=data[1].text
        school_dct['cluster']=data[2].text
        school_dct['pin_code']=data[3].text
        school_dct['from_page_url']=row['URL']
        school_dct['block']=row['Block']
        school_dct['district']=row['District']
        df_school=df_school.append(school_dct, ignore_index=True)


    
    
df_school = 


df_1 =df_1.append(getTable("https://liko.in/blocks/andhanallur-block"), ignore_index=True)
data1 =pd.DataFrame(lst1)


data.append(lst)

print(data.head())



    #school_dct['school'] = 
   
    
    #ow_text = [x.text for x in row.find_all('td')]
    #print(', '.join(row_text))  # You can save or print this string however you want.

'''
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
'''
rows = table.findAll('tr')
for tr in rows:
    cols = tr.findAll('td')
    if len(cols) >= 4 and "2013" in cols[3].text:
        link = cols[1].find('a').get('href')
        print link
'''