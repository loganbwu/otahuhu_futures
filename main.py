# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:04:48 2017

@author: LWu
"""

import datetime as dt
import dateutil as du

import pandas as pd
from scrape import scrape

date_list=[dt.date.today()+ du.relativedelta.relativedelta(months = x) for x in range(24)]
month_list=[dt.date.strftime(x,'%b %Y') for x in date_list]

prices = pd.DataFrame(index=month_list)

today_data = scrape('today')

prices['today'] = today_data
prices.plot()