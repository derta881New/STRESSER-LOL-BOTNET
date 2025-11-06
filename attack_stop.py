import requests

url = "YOUR_ATTACK_STOP_ENDPOINT"
headers = {
    "Authorization": "Bearer YOUR_API_TOKEN"
}
data = {
    "host": "example.com",
    "method": "stop"  # or "stopall"
}

response = requests.post(url, headers=headers, data=data)
print(response.json())
