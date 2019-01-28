import importlib
import time
from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import config.config as conf


url_queue = []
visited_url = set()


def get_soup_object(url, domain_core):
    """
    get the beautiful soup object corresponding to the given url
    :param url: the specific url which to be resolved
    :param domain_core: the core oof the domain which is used to determine if this page is inter-domain page
    :return: if exception occurs return NoneType else return the beautiful soup object
    """

    print('read url: ', url)
    try:
        response = request.urlopen(url)
    except:
        return
    html_content = response.read().decode('utf-8')
    soup_object = BeautifulSoup(html_content, features="html.parser")
    # get all the links
    for item in soup_object.find_all('a'):
        ref = item.get('href')
        abs_ref = parse.urljoin(url, ref)

        # determine if this is an inter-domain link
        if domain_core in abs_ref:
            if abs_ref not in visited_url:
                url_queue.append(abs_ref)
    return soup_object


def crawler(domain):
    """
    the main driver of the crawler which control the loop of crawling
    :param domain: the domain selector which is used to specify the target market site
    """
    domain_object = conf.TARGET[domain]
    base_url = domain_object['url']
    base_core = domain_object['core']
    url_queue.append(base_url)
    while url_queue:
        this_url = url_queue.pop()
        if this_url not in visited_url:
            soup = get_soup_object(this_url, base_core)
            visited_url.add(this_url)
            get_application_info = importlib.import_module('utils.' + domain).get_application_info
            get_application_info(soup)
            time.sleep(3)


def main():
    crawler('tencent')


if __name__ == '__main__':
    main()
