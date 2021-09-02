import argparse

print("USAGE EXAMPLE: python Lab4Main.py --array 1 2 3 4")
parser = argparse.ArgumentParser()
parser.add_argument('--array', '--arg', nargs='+', type=float)
args = parser.parse_args()

input = args.array

lowestNumber = 1000000000000000000000000000
highestNumber = -1000000000000000000000000000
runningSum = 0

# Calculate the mean
for num in input:
    runningSum += num

mean = runningSum / len(input)

# Calculate empirical variance
runningSum = 0
for num in input:
    temp = (num - mean)**2
    runningSum += temp

empiricalVariance = runningSum / len(input)

print('mean = ' + str(mean))
print('var = ' + str(empiricalVariance))
