# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:12:49 2020

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
Data_new_cases = Data2[['date','location','total_cases']]
Data_N_Cases_PERU = Data_new_cases[Data_new_cases['location']=='Peru']
#Data_N_Cases_GBR.head()
Data_N_Cases_PERU = Data_N_Cases_PERU.reset_index(drop=True)

#Making sure the dates are all unique.
Data_N_Cases_PERU
uniques = []
for i in Data_N_Cases_PERU['date'].unique():
    uniques.append(i)
len(uniques)
#ytick = [ i*25000 for i in range(12)]
# This code actually creates a graph of the new daily cases for Covid-19 in
# Peru
Data_N_Cases_PERU = Data_N_Cases_PERU[['date','total_cases']]

fig= plt.figure(figsize=(60,30))
ytick = [ i*10000 for i in range(15)]
axes= fig.add_axes([0.1,0.1,0.8,0.8])

x= Data_N_Cases_PERU['date']

y= Data_N_Cases_PERU['total_cases']
plt.xticks(rotation=90)
plt.title("Casos acumulados de Covid-19, 28 de Mayo, Peru", fontsize = 40)
plt.xlabel("Fechas", fontsize = 40)
plt.ylabel("Casos en total", fontsize= 40)
axes.tick_params(axis="y", labelsize=25)
axes.plot(x,y)
plt.yticks(ytick)
plt.savefig("TotalCasesPeru.jpg")
plt.show()