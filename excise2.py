import requests
r = requests.get('https://api.github.com/pingao2019', auth=('user', 'pass'))
r.status_code

r.headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
r.text
'{"type":"User"...'
r.json()
{'disk_usage': 368627, 'private_gists': 484, ...}