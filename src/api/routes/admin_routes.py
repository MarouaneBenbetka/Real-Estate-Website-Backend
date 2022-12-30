from api import app
from bs4 import BeautifulSoup
import requests

@app.get('/fetch')
def fetch():
    response = requests.get("http://www.annonce-algerie.com/upload/flux/rss_1.xml",verify=False)
    items = BeautifulSoup(response.content,"xml").find_all("item")
    for item in items:
        response = requests.get(item.find("link").get_text(), verify=False)
        table = len(BeautifulSoup(response.content,"html.parser").find_all('table',class_="da_rub_cadre"))
        print(table)

    return "hi"