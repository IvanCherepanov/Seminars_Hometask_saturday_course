import requests

try:
    a = requests.get("http://localhost:5000/")
except:
    pass
print(a.status_code)