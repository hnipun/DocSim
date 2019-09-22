from pymongo.errors import PyMongoError
from pymongo import MongoClient
from product_recommandation.utilities import Config
from product_recommandation.utilities import Logger
from product_recommandation.exceptions import DatabaseException
from product_recommandation.utilities import get_secret


class Database:
    _instance = None
    database_error_msg = 'database error occurred'

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        try:
            if Config().Database().read('ENABLE_AWS_SERVER'):
                secret = get_secret('database/scraper_db')
                server = Config().Database().read('AWS_SERVER').format(secret['username'], secret['password'])
            else:
                server = Config().Database().read('LOCAL_SERVER')

            client = MongoClient(server)
            self.db = client[Config().Database().read('DB_NAME')]
        except PyMongoError as e:
            Logger().critical(e)
            raise DatabaseException(e)

    # ......................Read from MongoDB...........................#

