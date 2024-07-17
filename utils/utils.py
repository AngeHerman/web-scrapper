from requests import get
from scrapy import Selector

def get_source_code(url):
    response = get(url)
    source = None
    if response.status_code == 200:
        source = response.text
    return source