# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 16:41:02 2020

@author: Yusef Quinlan
"""
# Source of data from the csv is https://www.kaggle.com/tamber/steam-video-games/data
# to this csv the columns 'ID','Game Name', 'Behaviour', 'Value' and 'Numeric,
# Have been added.

# Imports

import csv
import pandas as pd

# Read the csv and seperate it into Behaviours, and also grab the game names
regcsv= pd.read_excel('steam-200k.xlsm')
regcsv2 = regcsv[regcsv['Behaviour'] == 	'purchase']
regcsv3 = regcsv[regcsv['Behaviour'] == 'play']
games = regcsv['Game Name'].unique()

# Make countlists and a percentage list
puCountList = []
plCountList = []
playpercent = []

"""
 Fill the countlists
 First of all puCountList refers to the count of purchases for a game name
 and plCountList refers to the amount of people who purchased a game that 
 also played that game.
"""
for i in games:
    puCountList.append(len(regcsv2[regcsv2['Game Name']==i]))
    plCountList.append(len(regcsv3[regcsv3['Game Name']==i]))

"""
    Getting the percentage of players who played a game they have purchased
    for every game in the 'games' list and placing those percentages into a 
    list.
"""    
for i in range(5155):
    playpercent.append( (plCountList[i] / puCountList[i]) * 100)

"""
    Converting everything to a string so it can be appended to a csv file,
    replacing the commas in games names so they don't make weird csv entries
"""
puCountList = [str(i) for i in puCountList]
plCountList = [str(i) for i in plCountList]
playpercent = [str(i) for i in playpercent]
games = [str(i) for i in games]
games2 = [i.replace(',',' ') for i in games]

"""
 Appending the amount of people who purchased a game, and the amount of people
 who played a game along with the name of that game, and the percentage ratio
 of purchases to plays, to a csv. So every game shows its purchase count, 
 its play count and play/purchase ratio. This creates a csv if it doesn't exist,
 but will append to a csv of the same name if it does exist.'
"""
for i in range(-1,5155):
    with open('Game Percentage.csv', "a") as csv_file:
        if i == -1:
            csv_file.write('Game Name,PurchasedCount,PlayedCount,Percentage who played \n')
        else:
            string1 = games2[i] + ',' + puCountList[i] + ','+ plCountList[i] + ',' + playpercent[i] +'\n'
            csv_file.write(string1)

"""
    Making several DataFrames, one of the newly made csv, one that is the csv
    but order by gameplay plap/purchase ratio in descending order
    and the final one ordered by the amount of purchases per game title in 
    ascending order.
"""
gameData = pd.read_csv('Game Percentage.csv')
gameDataPlayed = gameData.sort_values(by=['Percentage who played '], ascending=False)
gameDataPurchased = gameData.sort_values(by=['PurchasedCount'], ascending=False)

# Printing out the top 20 most purchased games.
x = 1
for i in gameDataPurchased.iloc[:20]['Game Name']:
    if x == 1:
        print(i + " is the most purchased game") 
        x+=1
    elif x == 2:
        print(i + " is the 2nd most purchased game")
        x+=1
    elif x == 3:
        print(i + " is the 3rd most purchased game")
        x+=1
    else:
        print(i + " is the " + str(x) + "th most purchased game")
        x+=1
            
    
       