'''
    In this lab, we will build a histogram from scratch. You many not use numpy for this lab.
    Given an array of numbers, a, and number of bins, b, construct an array mapping if value
    of a to the correct bin.
    Hint: To get the bin width, you can do ((max-min) + 1) / b
'''

import argparse

a = [5, 6, 5, 11, 15, 19, 4]
b = 3

numBins = b
min = min(a)
max = max(a)

intervalSize = (max - min) / numBins
outputList = []
intervalMin = min
intervalMax = intervalMin + intervalSize

for i in range(1, numBins + 1):
    lastBin = False
    if i == numBins:
        lastBin = True
    numMatches = 0
    for num in a:
        if num >= intervalMin and num < intervalMax:
            numMatches += 1
        elif num >= intervalMin and num <= intervalMax and lastBin:
            numMatches += 1
    outputList.append(numMatches)
    intervalMin = intervalMax
    intervalMax += intervalSize

print(outputList)