from bs4 import BeautifulSoup
from urllib import request
from urllib import parse
import config.config as conf
from repository.database import database_settings
import pprint


def get_soup_object(url, domain_core):
    response = request.urlopen(url)
    html_content = response.read().decode('utf-8')
    soup_object = BeautifulSoup(html_content, features="html.parser")

    # get all the links
    for item in soup_object.find_all('a'):
        ref = item.get('href')
        abs_ref = parse.urljoin(url, ref)

        # determine if this is an inter-domain link
        if domain_core in abs_ref:
            print(abs_ref)


def get_application_info(soup_object, collection_name):
    name_tag = soup_object.find(class_='det-name-int')
    size_tag = soup_object.find(class_='det-size')
    download_tag = soup_object.find(class_='det-down-btn')
    version_tag = soup_object.find(class_='det-othinfo-data')
    publish_tag = soup_object.find(id='J_ApkPublishTime')

    collection = database_settings(collection_name)
    app_info = {'app_name': name_tag.string,
                'app_size': size_tag.string,
                'apk_name': download_tag.get('apk'),
                'apk_url': download_tag.get('data-apkurl'),
                'apk_version': version_tag.string,
                'apk_publish_time': publish_tag.get('data-apkpublishtime')
                }

    if collection.count_documents({'apk_name': download_tag.get('apk')}) == 0:
        collection.insert_one(app_info)


response = request.urlopen('https://android.myapp.com/myapp/detail.htm?apkName=ctrip.android.view')
html_content = response.read().decode('utf-8')
soup_object = BeautifulSoup(html_content, features="html.parser")
get_application_info(soup_object, 'tencent')
