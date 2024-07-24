from requests import get
from requests_html import HTMLSession

def get_source_code(url):
    response = get(url)
    source = None
    if response.status_code == 200:
        source = response.text
    return source

# For pages that are loaded with javascript
def get_response(url):
    session = HTMLSession()
    response = session.get(url)

    # Render for javascript
    response.html.render(timeout=30, sleep = 3)
    rendered_html = response.html.html
    return rendered_html