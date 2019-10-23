# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:02:39 2019

@author: Mathu
"""

from helper import scrap
import pandas as pd
url="https://liko.in/districts/tiruchirappalli"
s =scrap(url)

def FetchBlocks():
    '''
    Function to invoke the scrap.getBlock method 
    which returns the dataframe 
    '''
    return s.getBlocks()
def read_data(file):
    df_district = pd.read_excel(file, sheet_name="district")
    df_block = pd.read_excel(file, sheet_name="block")
    df_url = pd.read_excel(file, sheet_name="url")
    

if __name__ == '__main__':
    read_data(".\schoolist.xlsx")
    #df_blocks=FetchBlocks()
    
    
    