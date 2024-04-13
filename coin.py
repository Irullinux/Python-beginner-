import requests

url = "https://pro-api.coingecko.com/api/v3/ping"

headers = {"x-cg-pro-api-key": "CG-HM8kjh4bEozJ1ru2wrKp44Np"}

response = requests.get(url, headers=headers)

print(response.text)
