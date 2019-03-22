import unittest
import asyncio
import aiohttp
import json

@asyncio.coroutine
def fetch_page(session, url):
    with aiohttp.Timeout(10):
        #response = yield from session.post(url, data=json.dumps({'user': 'first.lastname@email.com', 'pwd': 'XXX123XXX'}),
        #                                   headers={'content-type': 'application/json'})
        loginURL = '{0}?user={1}&pwd={2}'.format(url, 'first.lastname@email.com', 'XXX123XXX')
        print(loginURL)
        response = yield from session.post(loginURL)
        print(response)
        assert response.status == 200
        resp = yield from response.read()
        return resp

class TestClient(unittest.TestCase):

    def test_client_post(self):
        loop = asyncio.get_event_loop()
        with aiohttp.ClientSession(loop=loop) as session:
            content = loop.run_until_complete(fetch_page(session, 'http://localhost:8080/login'))
            print(content)
        loop.close()

if __name__ == '__main__':
    unittest.main()
