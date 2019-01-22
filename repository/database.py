import pymongo
import config.config as conf


def database_settings(collection_name):
    client = pymongo.MongoClient(conf.DATABASE['host'], conf.DATABASE['port'])
    database = client[conf.DATABASE['database']]
    collection = database[collection_name]
    return collection
