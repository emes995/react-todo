import unittest
import asyncio
import aiohttp
import json

async def fetch_page(url, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        #response = yield from session.post(url, data=json.dumps({'user': 'first.lastname@email.com', 'pwd': 'XXX123XXX'}),
        #                                   headers={'content-type': 'application/json'})
        loginURL = '{0}?user={1}&pwd={2}'.format(url, 'first.lastname@email.com', 'XXX123XXX')
        print(loginURL)
        response = await session.post(loginURL)
        print(response)
        assert response.status == 200
        resp = await response.read()
        return resp

class TestClient(unittest.TestCase):

    def test_client_post(self):
        loop = asyncio.get_event_loop()
        content = loop.run_until_complete(fetch_page('http://localhost:8080/login', loop))
        print(content)
        loop.close()

if __name__ == '__main__':
    unittest.main()
