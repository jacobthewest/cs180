import requests
import csv
import os

#############################---Exercise 1 Start---####################################

dta = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
headers = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'class']

def write_csv(dta, headers):

    data = dta.split('\n')

    with open('exercise1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for row in data:
            floatList = row.split(',')
            writer.writerow(floatList)
            #writer.writerow(row)

write_csv(dta, headers)

######################################################################################