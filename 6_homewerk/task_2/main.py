import requests

res = requests.get('https://api.openbrewerydb.org/breweries')
print(res.json()[0])
print(res.text)
print(res.headers)