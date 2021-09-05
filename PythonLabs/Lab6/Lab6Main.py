import argparse

print("USAGE EXAMPLE: python Lab6Main.py --x 10")
parser = argparse.ArgumentParser()
parser.add_argument('--x', '--arg', nargs=1, type=int)
args = parser.parse_args()

input = args.x

# All negative numbers are never palindromes
if input[0] < 0:
    print('false')
    exit(0)

# All single digits are palindromes
if input[0] >= 0 and input[0] < 10:
    print('true')
    exit(0)

# Convert to string and see if it reads forwards and backwards the same with a stack
intAsString = str(input[0])
stack = []
for char in intAsString: # Construct the stack
    stack.append(char)

frontIndex = 0
backIndex = len(stack) - 1
while frontIndex <= backIndex:
    if stack[frontIndex] != stack[backIndex]:
        print('false')
        exit(0)
    else:
        frontIndex += 1
        backIndex -= 1
print('true')
