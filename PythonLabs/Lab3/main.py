'''
    Write a function cube(n: Int): Int that takes the first n cubes (i.e. [1^3, 2^3, ..., n^3]),
    keeps the ones where the first digit is even (e.g., 3^3 = 27) and adds those up and returns that answer.
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text', type=int, help='Input n')
args = parser.parse_args()
input = int(args.text)

def cube(n):
    totalToReturn = 0
    for i in range(1, n+1):
        result = pow(i,3) # i^3 is how pow works
        resultAsString = str(result)

        firstChar = resultAsString[0]
        firstCharAsInt = int(firstChar)

        if firstCharAsInt % 2 == 0: # if the first thing is even
            totalToReturn += result
    return totalToReturn

print(cube(input))