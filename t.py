import requests

url = 'http://127.0.0.1:8000'

myobj = {
    'name': 'hhh',
    'lastname': 'jjij',
    'valu1': '22',
    'valu2': '33',
    }

x = requests.get(url , myobj)