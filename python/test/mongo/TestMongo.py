import unittest
from base.Singleton import Singleton
from context.Context import Context
from session.Session import Session
from logger.Logger import Logger
import asyncio

async def insert(collection, documents):
    result = await collection.insert_one(documents)
    Logger().info('results {0}'.format(result), __name__)

class TestMongo(unittest.TestCase):
    def test_MongoInsert(self):
        s = Session('test.user@email.com', 'XXX123XXX', 'localhost', 23000, True)
        assert s.username == 'test.user@email.com'

        c = Context()
        client = c.mongo_connection(s, authSource='test_db')
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