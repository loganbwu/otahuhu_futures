# -*- coding: utf-8 -*-
"""
Scrape ASX prices
"""

import datetime as dt
#import dateutil as du
import pandas as pd


def scrape(period=None, date=None):
    """
    period  : 'monthly' or 'quarterly'
    date    : format %m-%d-%Y
    """
    
    filename = period + '_' + date + '.xlsx'
    df = pd.read_excel(filename, sheetname='Sheet1')
    df = df.set_index('Expiry', drop=True)
    df = df['Previous Settlement']
    df.name = period + '_' + date
    
    if period == 'quarterly':
        df['Expiry'] = df['Expiry'] - dt.timedelta(days=45)
    return df
    df['Expiry'] = pd.DatetimeIndex(df['Expiry']).round('D')

if __name__ == '__main__':
    raise Exception('Don\'t run this file')