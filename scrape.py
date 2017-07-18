# -*- coding: utf-8 -*-
"""
Scrape ASX prices
"""

import pandas as pd
def scrape(url=None, date=None):
    
    if not date:
        date = '7-2018-2017'
    
    expiry = ['Jul 2017', 'Aug 2017', 'Sep 2017', 'Oct 2017', 'Nov 2017', 'Dec 2017',
              'Jan 2018', 'Feb 2018', 'Mar 2018']
    previous_settlement = [151, 116.5, 85.25, 78, 83.45, 69.8, 80.05, 80.05, 80.05]
    
    data = pd.DataFrame(previous_settlement, index=expiry)
    data.columns = ['price']
    return data
