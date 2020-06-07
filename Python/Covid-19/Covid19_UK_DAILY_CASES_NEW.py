# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:38:04 2020

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
Data_N_Cases_GBR = Data_new_cases[Data_new_cases['location']=='United Kingdom']
#Data_N_Cases_GBR.head()
Data_N_Cases_GBR = Data_N_Cases_GBR.reset_index(drop=True)
"""
The following was me testing that all dates are unique and that all new cases
 are reported as being positive numbers, for some reason 2020-05-21 i.e. the
 21st of may 2020 reports negative 525 cases, no idea why, I followed it up 
 at https://www.mims.co.uk/live-updates-coronavirus-covid-19-uk/infections-and-infestations/article/1673649
 and I can find no reason and it doesn't seem to be an error.
"""
"""
Data_N_Cases_GBR
uniques = []
for i in Data_N_Cases_GBR['date'].unique():
    uniques.append(i)
len(uniques)
for i in Data_N_Cases_GBR['new_cases']:
    if i <= 0:
        print(i)
"""

# This code actually creates a graph of the new daily cases for Covid-19 in
# the United Kingdom, I know the ticks didn't need to be done manually.
Data_N_Cases_GBR = Data_N_Cases_GBR[['date','new_cases']]

#Data_N_Cases_GBR.loc[Data_N_Cases_GBR['new_cases'] == -525]

fig= plt.figure(figsize=(60,30))

axes= fig.add_axes([0.1,0.1,0.8,0.8])

x= Data_N_Cases_GBR['date']

y= Data_N_Cases_GBR['new_cases']
plt.xticks(rotation=90)
plt.title("New daily Covid-19 Cases, 28th of May, United Kingdom", fontsize = 40)
plt.xlabel("Dates", fontsize = 40)
plt.ylabel("New cases", fontsize= 40)
axes.tick_params(axis="y", labelsize=20)
axes.plot(x,y)
plt.yticks([-525,0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500])
plt.savefig("DailyCasesUnitedKingdom.jpg")
plt.show()