import requests
url = "https://www.google.com"
res = requests.get(url)

print(f"Your request to {url} returned status code {res.status_code}")