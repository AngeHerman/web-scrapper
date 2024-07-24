from requests import get
from scrapy import Selector
from utils.utils import *

def nycbikes_parser():
    url = "https://s3.amazonaws.com/tripdata/index.html"
    source = get_response(url)
    if source:
        selector = Selector(text=source)
        links = selector.css("table.table-striped tr td > a")
        # print("Taille "+str(len(titles)))
        found = 0

        for link in links:
            href = link.attrib['href']
            text = link.css("::text").get().strip()
            if text and href and text != "index.html" :
                print(f"Texte: {text}, URL: {href}")
                found += 1
        if found == 0:
            print("Error, the amazon aws page must have changed.")
            