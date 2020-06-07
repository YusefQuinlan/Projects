# -*- coding: utf-8 -*-
"""
Created on Fri May 29 09:43:09 2020

@author: User
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
"""
 
The following attempts to get the daily new cases for all location, based on
data taken from 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
"""

der = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
Data = pd.DataFrame(der)
#der2 = pd.read_csv("owid-covid-data.csv")
#Data2 = pd.DataFrame(der2)



# Get all locations and for each one makes a graph.
for i in Data_new_cases['location'].unique():
    Data_new_cases = Data[['date','location','new_cases']] 
    Data_new_cases = Data_new_cases[Data_new_cases['location']==i]

    Date = str(Data_new_cases.date.max())
    Data_new_cases = Data_new_cases.reset_index(drop=True)
    """
    The following was me testing  that all new cases
     are reported as being positive numbers, 
     any negative anomalies will not be metioned specifically in a graph,
     but the graph will mention that they are present if they are.
    """
    Negative = ""
    for n in Data_new_cases['new_cases']:
        if n < 0:
            Negative = ",  There are negative anomalies present."
    
    
    # This code actually creates a graph of the new daily cases for Covid-19 in
    # the selected location
    Data_new_cases = Data_new_cases[['date','new_cases']]
    
    
    fig= plt.figure(figsize=(60,30))
    
    axes= fig.add_axes([0.1,0.1,0.8,0.8])
    
    x= Data_new_cases['date']
    
    y= Data_new_cases['new_cases']
    plt.xticks(rotation=90)
    plt.title("New daily Covid-19 Cases, date, Location".replace("date",Date).replace("Location",i) + Negative, fontsize = 40)
    plt.xlabel("Dates", fontsize = 40)
    plt.ylabel("New cases", fontsize= 40)
    axes.tick_params(axis="y", labelsize=20)
    axes.plot(x,y)
    #plt.yticks()
    plt.savefig("location Daily Covid19 Cases.jpg".replace("location", i))
    plt.show()