# pip install requests types-requests bs4
# python -m http.server 3333

import requests

url = 'http://192.168.0.125:3333'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)
