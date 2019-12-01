import requests
import pyperclip
import json

data = pyperclip.paste()

response = requests.post('https://hastebin.com/documents', data=data)

if response.status_code == 200:
    key = json.loads(response.text)['key']
    pyperclip.copy('https://hastebin.com/{}'.format(key))
    exit(0)
else:
    pyperclip.copy('hastebin response code: {}'.format(response.status_code))
    exit(1)
