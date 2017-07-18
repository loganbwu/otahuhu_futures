# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:04:48 2017

@author: Logan Wu
"""

import pandas as pd
from scrape import scrape
import matplotlib.pyplot as plt


def interpolate_dates(dates, n=3):
    interp_dates = []
    for i in range(len(dates)-1):
        for j in range(1,n+1):
            delta = dates[i+1] - dates[i]
            interp_dates.append(dates[i] + delta*j/4)
    return interp_dates

def interpolate_data(df, n, key='Expiry', method='cubic'):
    interp_dates = interpolate_dates(df[key], 3)
    interp_data = pd.DataFrame({key: interp_dates}, index = range(len(interp_dates)))
    interp_data = interp_data.append(df)
    interp_data = interp_data.sort_values(key)
    interp_data = interp_data.reset_index(drop=True)
    interp_data.interpolate(method, inplace=True)
    return interp_data
    

date = '7-18-2017'

monthly_data = scrape('monthly', date)
quarterly_data = scrape('quarterly', date)

interpolated_quarterly_data = interpolate_data(quarterly_data, 3)

fig, ax = plt.subplots()
ax.plot_date(monthly_data['Expiry'], monthly_data['Previous Settlement'], 'x-')
ax.plot_date(quarterly_data['Expiry'], quarterly_data['Previous Settlement'], 'x-')
ax.plot_date(interpolated_quarterly_data['Expiry'], interpolated_quarterly_data['Previous Settlement'], '-')
ax.legend(['Monthly', 'Quarterly', 'Interpolated quarterly'])
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
plt.title('Expected Otahuhu Base Price')