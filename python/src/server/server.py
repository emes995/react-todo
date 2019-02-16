import asyncio
import asyncio
from aiohttp import web

from context.ApplicationContext import ApplicationContext
from context.Context import Context
from session.Session import Session

@asyncio.coroutine
def route_handleTodo(request):
    session = Session('usr', 'pwd', 'localhost', 23000)
    conn = Context().mongo_connection(session)
    return web.Response(text='Done')

def route_hello(request):
    return web.Response(text='Hello World')

if __name__ == '__main__':

    appCtxt = ApplicationContext()

    app = web.Application()
    app.router.add_get('/', route_handleTodo)
    web.run_app(app)
