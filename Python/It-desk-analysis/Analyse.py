# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:41:07 2020

@author: User
"""

import pandas as pd
Data = pd.read_excel("ItRecord.xlsx")
Data['Number']
Data['ServiceCategory']

#Data['ServiceCategory']['Incident']
#Data[['ServiceCategory' == 'Incident']]


#The following gets the percentage of solved Incident requests.

Data2 = Data['ServiceCategory'] == 'Incident'
Data3 = Data[Data2]
Data4 = Data3[Data3['Action']=="Raised"]
Data5 = Data3[Data3['Action']=="Resolved"]
SumRaised = Data4["Number"].sum()
SumResolved = Data5["Number"].sum()
PercentageSolvedIncidents = SumResolved/SumRaised * 100

#The following gets the percentage of solved Major Incident Requests.
Data2 = Data['ServiceCategory'] == 'Major Incident'
Data3 = Data[Data2]
Data4 = Data3[Data3['Action']=="Raised"]
Data5 = Data3[Data3['Action']=="Resolved"]
SumRaised = Data4["Number"].sum()
SumResolved = Data5["Number"].sum()
PercentageSolvedMajor = SumResolved/SumRaised * 100

#The following gets the percentage of solved Service Requests
Data2 = Data['ServiceCategory'] == 'Service Request'
Data3 = Data[Data2]
Data4 = Data3[Data3['Action']=="Raised"]
Data5 = Data3[Data3['Action']=="Resolved"]
SumRaised = Data4["Number"].sum()
SumResolved = Data5["Number"].sum()
PercentageSolvedService = SumResolved/SumRaised * 100

#Print the percentages
print("The percentage of Regular Incidents resolved is: " + str(PercentageSolvedIncidents) + "\n")
print("The percentage of Major Incidents resolved is: " + str(PercentageSolvedMajor) + "\n")
print("The percentage of Service requests resolved is: " + str(PercentageSolvedService) + "\n")