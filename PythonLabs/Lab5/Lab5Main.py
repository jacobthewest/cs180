import argparse
import string

print("USAGE EXAMPLE: python Lab5Main.py --string Aliens Exist!")
parser = argparse.ArgumentParser()
parser.add_argument('--string', '--arg', nargs='+', type=str)
args = parser.parse_args()
input = args.string

stringFromInput = input[0]
if len(input) > 1:
    stringFromInput += ' '

for i in range(1, len(input)):
    stringFromInput += input[i]

    if i != len(input) - 1:
        stringFromInput += ' '

print(stringFromInput[::-1])