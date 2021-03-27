import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'LSTAT':5, 'RM':200})

print(r.json())