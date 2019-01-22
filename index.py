from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import config.config as conf


def get_soup_object(url, domain_core):
    response = request.urlopen(url)
    html_content = response.read().decode('utf-8')
    soup_object = BeautifulSoup(html_content, features="html.parser")
    for item in soup_object.find_all('a'):
        ref = item.get('href')
        abs_ref = parse.urljoin(url, ref)
        if domain_core in abs_ref:
            print(abs_ref)
