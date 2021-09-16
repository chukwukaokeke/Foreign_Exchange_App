import json
import os
from dotenv import load_dotenv

import requests
from prettytable import PrettyTable

load_dotenv()
API_KEY = os.getenv("API_KEY")

url = "https://currency-converter13.p.rapidapi.com/convert"

base = input(str("what currency do you have? "))
amount = input(str("How much " + base + " do you have? "))
convert = input(str("what currency do you want to convert to? "))

headers = {
    'x-rapidapi-host': "currency-converter13.p.rapidapi.com",
    'x-rapidapi-key': API_KEY
}

querystring = {"from": base, "to": convert, "amount": amount}

query = requests.request("GET", url, headers=headers, params=querystring)
response = query.text
json_object = json.loads(response)  # covert json object to dictionary

converted = json_object["amount"]

table = PrettyTable()
table.field_names = ["Amount", "From", "To", "Converted"]
table.add_row([amount, base, convert, converted])


print(table)
