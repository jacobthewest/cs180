import argparse

print("USAGE EXAMPLE: python Lab4Main.py --array 1 2 3 4")
parser = argparse.ArgumentParser()
parser.add_argument('--array', '--arg', nargs='+', type=float)
args = parser.parse_args()

input = args.array

lowestNumber = 1000000000000000000000000000
highestNumber = -1000000000000000000000000000
runningSum = 0

for num in input:
    pass

