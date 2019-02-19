from urllib import parse
import time

from repository.database import database_settings


def get_application_info(soup_object):
    """
    information filter customized for Mi Application Market

    :param soup_object: a HTML page element object resolved by beautiful soup
    :return: if not information page return NoneType else do not return anything
    """

    if soup_object is None:
        return

    name = soup_object.find(class_='intro-titles').contents[1].string
    size = soup_object.find(class_='details').contents[0].contents[1].string
    download_info_relative = soup_object.find(class_='app-info-down').contents[0].get('href')
    download_info = parse.urljoin('http://app.mi.com', download_info_relative)
    apk_official_name = soup_object.find(class_='details').contents[0].contents[7].string
    version = soup_object.find(class_='details').contents[0].contents[3].string
    publish_time = soup_object.find(class_='details').contents[0].contents[5].string

    if name is None or \
       size is None or \
       download_info is None or \
       apk_official_name is None or \
       version is None or \
       publish_time is None:
        return

    collection = database_settings('mi')

    app_info = {
        'app_name': name,
        'app_size': size,
        'apk_name': apk_official_name,
        'apk_url': download_info,
        'apk_version': version,
        'apk_publish_time': publish_time,
        'insert_time': time.time()
    }

    if collection.count_documents({'apk_name': apk_official_name}) == 0:
        collection.insert_one(app_info)
