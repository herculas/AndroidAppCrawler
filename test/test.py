import bs4
import urllib.request
import config.config as config
from collections import deque

queue = deque()
visited = set()

root_url = config.TARGET_CONFIG['tencent']
queue.append(root_url)

while queue:
    this_url = queue.popleft()
    visited.add(this_url)
    this_content = urllib.request.urlopen(this_url)

    if 'html' not in this_content.getheader('Content-Type'):
        continue
    try:
        this_content_html = this_content.read().decode('utf-8')
    except:
        continue

    print(this_content_html)
