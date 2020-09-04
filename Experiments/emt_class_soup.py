import requests
from bs4 import BeautifulSoup
import csv


prms = {"pgm_id":"62", "end_dayrng_id":"365"}
res = requests.get('https://njems.njlincs.net/jsp/rlm/catalog.jsp', verify=False, params=prms)
soup = BeautifulSoup(res.text, "html.parser")

courses = soup.find_all(class="htmGHOT-row")

print(res.text)

