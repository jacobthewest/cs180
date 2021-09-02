### Prepare Data For The Lab ###

import requests

costs_csv = requests.get("https://raw.githubusercontent.com/wingated/cs180_labs/main/costs.csv").text
supplements_csv = requests.get("https://raw.githubusercontent.com/wingated/cs180_labs/main/supplements.csv").text
print('stop')