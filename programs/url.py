import json
import requests

count = 0

num = int(input("pages: "))
url = f"https://urlhaus-api.abuse.ch/v1/urls/recent/limit/{num}"

data = requests.get(url).json()
    
for count in range(num):
    print(data['urls'][count]["url"])
    count = count + 1