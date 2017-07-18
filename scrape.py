# -*- coding: utf-8 -*-
"""
Scrape ASX prices
"""

import datetime as dt
#import dateutil as du
import pandas as pd


def scrape(period=None):
    
    if period == 'monthly':
        filename = 'monthly_7-18-2017.xlsx'
    if period == 'quarterly':
        filename = 'quarterly_7-18-2017.xlsx'
        
    df = pd.read_excel(filename, sheetname='Sheet1', converters={'Expiry': str})
#    df['Expiry'] = pd.to_datetime(df['Expiry'], format='%Y-%d-%m %H:%M:%S')
    return df

if __name__ == '__main__':
    raise Exception('Don\'t run this file')