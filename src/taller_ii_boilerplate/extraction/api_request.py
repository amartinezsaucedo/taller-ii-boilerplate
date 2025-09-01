import requests

response = requests.get('https://dummyjson.com/products')

if response.status_code == 200:
    data = response.json()
else:
    print('Error:', response.status_code)

