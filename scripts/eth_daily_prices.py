import requests

url = "https://api.g.alchemy.com/prices/v1/docs-demo/tokens/historical"

payload = {
    "symbol": "ETH",
    "startTime": 1704067200,
    "endTime": "2024-01-31T23:59:59Z",
    "interval": "1d"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)