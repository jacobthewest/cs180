### Getting Started ###

import requests
cereal_csv = requests.get("https://raw.githubusercontent.com/porterjenkins/cs180-intro-data-science/master/data/cereal.csv").text

# Example Code
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

PROTEIN_INDEX = 4
FAT_INDEX = 5
CARB_INDEX = 8

#############################---Exercise 1 Start---###################################
'''
  Carbs, fats and proteins are the three primary macro nutrients. Create a figure plotting the 
  distribution of each of these macro nutrients together (ie, three distributions on a single plot). 
  Make sure to provide a legend.
'''

cereal_data = cereal_csv.splitlines()
cereal_data = [i.split(',') for i in cereal_data]

for row in cereal_data[1:]:
    for i in range(len(row)):
        if i >= 3:
            row[i] = float(row[i])

carbs = []
fats = []
proteins = []

for row in cereal_data[1:]:
  carbs.append(row[CARB_INDEX])
  fats.append(row[FAT_INDEX])
  proteins.append(row[PROTEIN_INDEX])

columns = [carbs, fats, proteins]

fig, ax = plt.subplots()
ax.boxplot(columns)

fig.set_figwidth(10)
fig.set_figheight(5)

plt.suptitle('')
plt.title('Macronutrient Distribution of Cereals')
plt.xlabel('Grams')
#plt.xticks(np.arange(3), ['', 'Carbs', 'Fats', 'Proteins'])  # Set text labels.
plt.ylabel('Hour of the day')
#plt.yticks(np.arange(0, 25, 2))
plt.grid(linewidth=.5)
plt.show()


######################################################################################