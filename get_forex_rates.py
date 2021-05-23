#! /bin/python3

import csv
import requests
import os

# Downloads the Banque de France forex rates and transforms them to align with 
# revolut-stocks format. 

url = "http://webstat.banque-france.fr/fr/downloadFile.do?id=5385698&exportType=csv"

with open("forex_rates.csv", 'wb') as forex_file:
    r = requests.get(url, allow_redirects=True)
    forex_file.write(r.content)

with open("forex_rates.csv", "r") as forex_file:
    csv_reader = csv.reader(forex_file, delimiter=";")
    for row in csv_reader:
        value = row[38]
        if value == '-':
            continue
        date = row[0]
        try:
            formatted_date = date.replace("/", ".")
            formatted_value = 1/float(value.replace(",", "."))
            print(f"\"{formatted_date}\" : \"{formatted_value}\",")
        except ValueError:
            continue

os.remove("forex_rates.csv")