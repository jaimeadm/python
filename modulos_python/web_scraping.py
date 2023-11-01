# pip install requests types-requests bs4
# python -m http.server 3333
import requests
import re
from bs4 import BeautifulSoup

url = 'http://192.168.0.125:3333'
response = requests.get(url)
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

# if parsed_html is not None:
#     print(parsed_html.title.text)


top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
# print(top_jobs_heading)


if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
