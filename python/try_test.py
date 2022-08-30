import requests

try:
    r = requests.get("https://www.onramp.io/")
    print(r.status_code)
except requests.exceptions.ConnectionError:
    print("could not connect to server")