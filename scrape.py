# -*- coding: utf-8 -*-
"""
Scrape ASX prices
"""

import datetime as dt
#import dateutil as du
import pandas as pd


def scrape(period=None, date=None):
    
    filename = period + '_' + date + '.xlsx'
    df = pd.read_excel(filename, sheetname='Sheet1')
    df = df[['Expiry', 'Previous Settlement']]
    
    if period == 'quarterly':
        df['Expiry'] = df['Expiry'] - dt.timedelta(days=45)
    return df

if __name__ == '__main__':
    raise Exception('Don\'t run this file')