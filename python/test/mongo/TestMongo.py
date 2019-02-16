import unittest
from base.Singleton import Singleton
from context.Context import Context
from session.Session import Session
from logger.Logger import Logger
import asyncio

@asyncio.coroutine
def insert(collection, documents):
    result = yield from collection.insert_one(documents)
    Logger().info('results {0}'.format(result), __name__)

class TestMongo(unittest.TestCase):
    def test_MongoInsert(self):
        s = Session('user', 'pwd', 'localhost', 23000)
        assert s.username == 'user'

        c = Context()
        client = c.mongo_connection(s)
        client.drop_database('test_db')
        db = client['test_db']
        collection = db['test_collection']

        loop = asyncio.get_event_loop()
        loop.run_until_complete(insert(collection, {'test': 1230}))

    def test_logging(self):
        Logger().info('Testing logging', __name__)
        

if __name__ == '__main__':

    unittest.main()
    sys.exit(0)