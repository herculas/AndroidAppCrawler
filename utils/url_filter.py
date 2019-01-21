from urllib import parse

def is_relative_url(this_url):
    return True

def url_parser(this_url, relative_url):
    absolute_url = parse.urljoin(this_url, relative_url)
    return absolute_url

def is_in_same_domain(root_domain, this_url, new_url):
    if is_relative_url(new_url):
        return True
    elif not is_relative_url(new_url):

