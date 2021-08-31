import json
import string
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text', type=str, help='The text to parse.')
args = parser.parse_args()

# Remove punctuation from the string
table = str.maketrans(dict.fromkeys(string.punctuation))
inputString = args.text.translate(table)

# Lowercase the string
inputString = inputString.lower()

# Break up the string into a list
wordList = inputString.split()

wordDict = {}
for word in wordList:
    try:
        wordDict[word] += 1
    except:
        wordDict[word] = 1

with open('word-counts.json', 'w', encoding='utf-8') as f:
    json.dump(wordDict, f, ensure_ascii=False, indent=4)