import urllib.request
import config.config as config
import bs4

response = urllib.request.urlopen(config.TARGET_CONFIG['tencent'])
html = response.read().decode('utf-8')
soup = bs4.BeautifulSoup(html, features="html.parser")
result = soup.select('a[href]')

for item in result:
    print(item)
