# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:02:39 2019

@author: Mathu
"""

from helper import scrap

url="https://liko.in/districts/tiruchirappalli"
s =scrap(url)

def FetchBlocks():
    '''
    Function to invoke the scrap.getBlock method 
    which returns the dataframe 
    '''
    return s.getBlocks()


if __name__ == '__main__':
    df_blocks=FetchBlocks()