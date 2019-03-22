
import asyncio
from aiohttp import web
from aiohttp_session import get_session, setup, session_middleware
import aiohttp_cors

from context.ApplicationContext import ApplicationContext
from context.Context import Context
from session.Session import Session
from logger.Logger import Logger
from base.Config import Config
from apps.todo.TodoRoutes import TodoRoutes

from aiohttp_session import setup
import base64
from cryptography import fernet
from aiohttp_session.cookie_storage import EncryptedCookieStorage


@asyncio.coroutine
def route_handleTodo(request):
    mongoConfig = Config().getConfiguration('todo')
    host = mongoConfig['mongo.hostname']
    port = mongoConfig['mongo.port']
    session = Session('usr', 'pwd', host, port)
    conn = Context().mongo_connection(session)
    Logger().info('Request acquired {0}'.format(request), __name__)
    return web.Response(text='Done')

if __name__ == '__main__':

    appCtxt = ApplicationContext()
    Config().loadConfiguration("mongo.conf")

    tr = TodoRoutes()
    app = web.Application()

    fernetKey = fernet.Fernet.generate_key()
    secretKey = base64.urlsafe_b64decode(fernetKey)
    setup(app, EncryptedCookieStorage(secretKey))

    app.router.add_get('/find', tr.findTodo, name='find')
    app.router.add_post('/insert', tr.insertTodo, name='insert')
    app.router.add_post('/update', tr.updateTodo, name='update')
    app.router.add_get('/list', tr.listTodos, name='list')
    app.router.add_delete('/delete', tr.deleteTodo, name='delete')
    app.router.add_post('/login', tr.login, name='login')

    cors = aiohttp_cors.setup(app, defaults=
    {
        "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
            )
    })

    for route in list(app.router.routes()):
        cors.add(route)

    web.run_app(app)
