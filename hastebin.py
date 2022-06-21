import requests
import pyperclip
import json

BASE_URL = "https://www.toptal.com/developers/hastebin"

data = pyperclip.paste()

response = requests.post(f'{BASE_URL}/documents', data=data)

if response.status_code == 200:
    key = json.loads(response.text)['key']
    pyperclip.copy(f'{BASE_URL}/{key}')
    exit(0)
else:
    pyperclip.copy(f'hastebin response code: {response.status_code}')
    exit(1)
