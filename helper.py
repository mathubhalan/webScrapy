# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:16:47 2019

@author: Mathu
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
class scrap:
    '''
    class holds all function calls
    '''
    def __init__(self, url):
        '''
        initlize the class scrap 
        '''
        self.url = url
        self.headers = requests.utils.default_headers()
        self.headers.update({ 'User-Agent': 'Mozilla/5.0 \
                             (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

    def getBlocks(self):
        '''
        method to get the block from the page
        Input : self. url
        gets the block and urls of the block in a list
        output: Returns the block and associated url as dataframe
        '''
        
        req = requests.get(self.url, self.headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        ul = soup.find('ul', {'class':'double li'})
        #print(table)
        a_href = ul.find_all('a')
        #print(a_href)
        link = []
        block = []
        for a in a_href:
            link.append(a.get('href'))
            block.append(a.text)
        block = [w.replace("Schools in ",'') for w in block]
        block_df = pd.DataFrame(list(zip(block,link)),
                                columns=['Block','URL'])
        return block_df
    
    def getTable(self, df): 
        cols = ['school','href','village','pin_code','cluster','block','district']
        df_school = pd.DataFrame(columns=cols)
        for index,row in df.head(n=5).iterrows():
            req = requests.get(row['URL'], self.headers)
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
        return df_school
        

