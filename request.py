import requests

access_key = '336a82f42c718236a4ef1487e85dd5ef9f2854ec'
headers = {'Authorization': f'Bearer {access_key}'}
url = 'https://api.timepad.ru/v1/events.json'
params = {'category_ids': '457'}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    events = response.json()
    print(events)
else:
    print(f"Request failed with status code: {response.status_code}")
