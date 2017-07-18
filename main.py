# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:04:48 2017

@author: Logan Wu
"""

import pandas as pd
from scrape import scrape
import matplotlib.pyplot as plt

yesterday = '7-18-2017'
today = '7-19-2017'

def interpolate_dates(dates, n=3):
    """
    n       : number of sub-intervals i.e. 3 months per quarter
    """
    
    interp_dates = []
    for i in range(len(dates)-1):
        for j in range(1,n):
            delta = dates[i+1] - dates[i]
            interp_dates.append(dates[i] + delta*j/n)
    return interp_dates

def interpolate_data(df, n, key='Expiry', method='cubic'):
    """
    df      : data frame to be interpolated
    n       : number of sub-intervals i.e. 3 months per quarter
    key     : axis to interpolate over
    method  : interpolation type
    """
    
    interp_dates = interpolate_dates(df[key], 3)
    interp_data = pd.DataFrame({key: interp_dates}, index = range(len(interp_dates)))
    interp_data = interp_data.append(df)
    interp_data = interp_data.sort_values(key)
    interp_data = interp_data.reset_index(drop=True)
    interp_data.interpolate(method, inplace=True)
    return interp_data
    

def main():
    monthly_data_yesterday = scrape('monthly', today)
    print(monthly_data_yesterday.reset_index())
#    quarterly_data_today = scrape('quarterly', today)
#    interpolated_quarterly_data_today = interpolate_data(quarterly_data_today, 3)
#    
#    monthly_data_yesterday = scrape('monthly', yesterday)
#    quarterly_data_yesterday = scrape('quarterly', yesterday)
#    interpolated_quarterly_data_yesterday = interpolate_data(quarterly_data_yesterday, 3)
    
#    delta = interpolated_quarterly_data_today['Previous Settlement'] - interpolated_quarterly_data_yesterday['Previous Settlement']
    
    fig, axarr = plt.subplots(2, sharex=True)
    axarr[0].plot_date(monthly_data_yesterday.reset_index()['Expiry'], monthly_data_yesterday[0], 'x-')
#    axarr[0].plot_date(quarterly_data_yesterday['Expiry'], quarterly_data_yesterday['Previous Settlement'], 'x-')
#    axarr[0].plot_date(interpolated_quarterly_data_yesterday['Expiry'], interpolated_quarterly_data_yesterday['Previous Settlement'], '-')
    axarr[0].legend(['Monthly', 'Quarterly', 'Interpolated quarterly'])
    axarr[0].set_title('Expected Otahuhu Base Price')
    
#    axarr[1].plot_date(monthly_data_yesterday['Expiry'], delta, 'x-')
#    axarr[1].plot_date(monthly_data_today['Expiry'], monthly_data_today['Previous Settlement'], 'x-')
#    axarr[1].plot_date(quarterly_data_today['Expiry'], quarterly_data_today['Previous Settlement'], 'x-')
#    axarr[1].plot_date(interpolated_quarterly_data_today['Expiry'], interpolated_quarterly_data_today['Previous Settlement'], '-')
#    axarr[1].legend(['Monthly', 'Quarterly', 'Interpolated quarterly'])
#    axarr[1].set_title('Expected Otahuhu Base Price')
#    fig.autofmt_xdate()
    
if __name__ == '__main__':
    main()