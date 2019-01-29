import time
from repository.database import database_settings


def get_application_info(soup_object):
    """
    information filter customized for Tencent Application Market

    :param soup_object: a HTML page element object resolved by beautiful soup
    :return: if not information page return NoneType else do not return anything
    """

    if soup_object is None:
        return

    name_tag = soup_object.find(class_='det-name-int')
    size_tag = soup_object.find(class_='det-size')
    download_tag = soup_object.find(class_='det-down-btn')
    version_tag = soup_object.find(class_='det-othinfo-data')
    publish_tag = soup_object.find(id='J_ApkPublishTime')

    if name_tag is None or \
       size_tag is None or \
       download_tag is None or \
       version_tag is None or \
       publish_tag is None:
        return

    collection = database_settings('tencent')
    app_info = {
        'app_name': name_tag.string,
        'app_size': size_tag.string,
        'apk_name': download_tag.get('apk'),
        'apk_url': download_tag.get('data-apkurl'),
        'apk_version': version_tag.string,
        'apk_publish_time': publish_tag.get('data-apkpublishtime'),
        'insert_time': time.time()
    }

    if collection.count_documents({'apk_name': download_tag.get('apk')}) == 0:
        collection.insert_one(app_info)
