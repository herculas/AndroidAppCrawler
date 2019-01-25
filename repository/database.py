import pymongo
import config.config as conf


def database_settings(collection_name):
    """
    establish connection with MongoDB database
    and choose proper collection based on domain
    :param collection_name: the proper collection name based on the domain
    :return: the collection object for further CURD operation
    """

    client = pymongo.MongoClient(conf.DATABASE['host'], conf.DATABASE['port'])
    database = client[conf.DATABASE['database']]
    collection = database[collection_name]
    return collection
