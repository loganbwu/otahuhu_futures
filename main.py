# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:04:48 2017

@author: LWu
"""

import pandas as pd
from scrape import scrape
import matplotlib.pyplot as plt
import numpy as np


def interpolate_dates(dates):
    interpolated_dates = []
    for i in range(len(dates)-1):
        for j in range(4):
            delta = dates[i+1] - dates[i]
            interpolated_dates.append(dates[i] + delta*j/4)
    return interpolated_dates

monthly_data = scrape('monthly')
quarterly_data = scrape('quarterly')
interpolated_quarterly_dates = interpolate_dates(quarterly_data['Expiry'])
interpolated_quarterly_data = pd.DataFrame({'Expiry': interpolated_quarterly_dates}, index = range(len(interpolated_quarterly_dates)))
interpolated_quarterly_data = interpolated_quarterly_data.append(quarterly_data)
interpolated_quarterly_data = interpolated_quarterly_data.sort_values('Expiry')
interpolated_quarterly_data = interpolated_quarterly_data.interpolate(method='linear')
print(interpolated_quarterly_data)

#monthly_data.plot('Expiry', 'Previous Settlement')
#quarterly_data.plot('Expiry', 'Previous Settlement')

fig, ax = plt.subplots()
ax.plot_date(monthly_data['Expiry'], monthly_data['Previous Settlement'], '-')
ax.plot_date(quarterly_data['Expiry'], quarterly_data['Previous Settlement'], '-')
ax.plot_date(interpolated_quarterly_data['Expiry'], interpolated_quarterly_data['Previous Settlement'], '-')
ax.legend(['Monthly', 'Quarterly', 'Interpolated'])