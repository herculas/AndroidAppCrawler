import time
from repository.database import database_settings


def get_application_info(soup_object):
    """
    information filter customized for 360 Application Market

    :param soup_object: a HTML page element object resolved by beautiful soup
    :return: if not information page return NoneType else do not return anything

    360 SUCKS!
    The HTML of their page SUCKS!
    360 frontend programmer SUCKS!
    """

    if soup_object is None:
        return

    name = soup_object.find(id='app-name').contents[0].string
    size = soup_object.find(class_='pf').contents[7].string
    download_info_href = soup_object.find(class_='js-downLog').get('href')
    download_info = download_info_href[download_info_href.find('&url') + 5:]
    apk_official_name = download_info[download_info.rfind('/') + 1: download_info.rfind('_')]
    version = soup_object.find(class_='base-info').find('table').contents[1].contents[3].contents[1].contents[1]
    publish_time = soup_object.find(class_='base-info').find('table').contents[1].contents[1].contents[3].contents[1]

    if name is None or \
       size is None or \
       download_info is None or \
       version is None or \
       publish_time is None:
        return

    collection = database_settings('360')
    app_info = {
        'app_name': name,
        'app_size': size,
        'apk_name': apk_official_name,
        'apk_url': download_info,
        'apk_version': version,
        'apk_publish_time': publish_time,
        'insert_time': time.time()
    }

    print(app_info)
    if collection.count_documents({'apk_name': apk_official_name}) == 0:
        collection.insert_one(app_info)
