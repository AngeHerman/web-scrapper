from requests import get
from scrapy import Selector
from utils.utils import *

def starwars_parser():
    url = "https://fr.wikipedia.org/wiki/Star_Wars"
    source = get_source_code(url)
    if source:
        selector = Selector(text=source)
        titles = selector.css("div.vector-toc ul > li")
        for title in titles:
            level = title.css("span.vector-toc-numb::text").extract_first()
            name = title.css("span.vector-toc-numb + span::text").extract_first()
            if level and name:
                print(level + " " + name)
            else:
                print("Error, the wikipedia page must have changed.")