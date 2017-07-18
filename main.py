# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:04:48 2017

@author: LWu
"""

import pandas as pd
from scrape import scrape
import matplotlib.pyplot as plt


monthly_data = scrape('monthly')
#quarterly_data = scrape('quarterly')

#monthly_data.plot('Expiry', 'Previous Settlement')
#quarterly_data.plot('Expiry', 'Previous Settlement')

fig, ax = plt.subplots()
ax.plot_date(monthly_data['Expiry'], monthly_data['Previous Settlement'])