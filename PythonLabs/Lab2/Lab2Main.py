import json
import string
import argparse

print('USAGE EXAMPLE: python Lab2Main.py --string "This is a string"')
parser = argparse.ArgumentParser()
parser.add_argument('--string', '--arg', nargs='*', type=str, required=True)
args = parser.parse_args()

def remove_punctuation(text):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    inputString = text.translate(table)
    return inputString

# Remove punctuation from the string
inputString = args.string
inputString = [remove_punctuation(i) for i in inputString]
inputString = [x for x in inputString if x] # removes empty strings

# Lowercase the string
inputString = [x.lower() for x in inputString]

wordDict = {}
for word in inputString:
    try:
        wordDict[word] += 1
    except:
        wordDict[word] = 1

output_dict = {}

with open('word-counts.json', 'w', encoding='utf-8') as f:
    json.dump(wordDict, f, ensure_ascii=False, indent=4)