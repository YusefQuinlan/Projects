# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:33:45 2020

@author: Yusef Quinlan
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
"""
 the commented out read_csv and DataFrame(der) is commented out in case the site
 is unavailable, the data is taken from the csv up to the 28th of May
 17:41 -6 gmt.
"""

#der = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
#Data = pd.DataFrame(der)
der2 = pd.read_csv("owid-covid-data.csv")
Data2 = pd.DataFrame(der2)
#print(Data.head())
print(Data2.head())
#Data['location']
#Data['date']
Data_new_cases = Data2[['date','location','new_cases']]
Data_N_Cases_Chile = Data_new_cases[Data_new_cases['location']=='Chile']
#Data_N_Cases_GBR.head()
Data_N_Cases_Chile = Data_N_Cases_Chile.reset_index(drop=True)
"""
The following was me testing that all dates are unique and that all new cases
 are reported as being positive numbers.
"""
"""
Data_N_Cases_Chile
uniques = []
for i in Data_N_Cases_Chile['date'].unique():
    uniques.append(i)
len(uniques)
len(Data_N_Cases_Chile)
for i in Data_N_Cases_Chile['new_cases']:
    if i <= 0:
        print(i)
"""

# This code actually creates a graph of the new daily cases for Covid-19 in
# Chile.
Data_N_Cases_Chile = Data_N_Cases_Chile[['date','new_cases']]



fig= plt.figure(figsize=(60,30))

axes= fig.add_axes([0.1,0.1,0.8,0.8])
ytick = [ i*500 for i in range(12)]
x= Data_N_Cases_Chile['date']

y= Data_N_Cases_Chile['new_cases']
plt.xticks(rotation=90)
plt.title("Nuevos Casos Diarios de Covid-19, 28 de Mayo, Chile", fontsize = 40)
plt.xlabel("Fechas", fontsize = 40)
plt.ylabel("Nuevos Casos", fontsize= 40)
axes.tick_params(axis="y", labelsize=20)
axes.plot(x,y)
plt.yticks(ytick)
plt.savefig("DailyCasesChile.jpg")
plt.show()