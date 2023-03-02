import requests

link = "http://info.cern.ch/"
r = requests.get(link)
print(r.status_code)

html = r.text.replace("home of the first website", "casa de la primera página web").replace("Browse the first website", "Navegar la primera página").replace("Browse the first website using the line-mode browser simulator", "Navegar la primera página web usando...")

print(html)
