The python file contained in this folder, uses data in the steam-200k.xlsm file
sourced from https://www.kaggle.com/tamber/steam-video-games/data.

The file reads the data into a dataframe and makes a csv file that contains the unique
game names found in the original file, along with the amount of ID's i.e. unique accounts
that purchased each unique game, the amount of ID's that played each game, and the ratio
of total plays per game title divided by the total purchases per game title. This data
was not in the original xlsm file and was made via DataFrame manipulation using pandas.
In addition the python file prints out the top 20 most purchased games, a DataFrame was
made that would have allowed the user to print the top 20 games with the highest play/purchase
ratios, however as a considerable percentage of games had a ratio of 100% i.e. 100 percent of people who
purchased the game also played the game, this DataFrame was not used in a print loop as there are far more
than 20 games with a 100% ratio.