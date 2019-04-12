#
# $Id$
#

import asyncio
from session.Session import Session
from base.Config import Config
from context.Context import Context
from pymongo import ReturnDocument
from pymongo.errors import OperationFailure
from bson import ObjectId
from aiohttp.web import json_response
from aiohttp_session import get_session, session_middleware
from logger.Logger import Logger

class TodoRoutes:

    def __init__(self):
        self._sessions = {}

    def getMongoConnection(self, request):
        todoConfig = Config().getConfiguration('todo')
        session = Session(request.query['user'],
                          request.query['pwd'],
                          todoConfig['mongo.hostname'],
                          todoConfig['mongo.port'],
                          True
        )
        mongoConn = Context().mongo_connection(session, authSource=todoConfig['mongo.database'])
        mongoDb = mongoConn[todoConfig['mongo.database']]

        return mongoDb

    async def findTodo(self, request):
        mongoDb = self.getMongoConnection(request)
        todos = await mongoDb['todo'].find_one({'user': request.query['user'],
                                                     'title': request.query['title']})
        print(todos)

    async def insertTodo(self, request):
        mongoDb = self.getMongoConnection(request)
        todos = await mongoDb['todo'].insert_one({'user': request.query['user'],
                                                       'title': request.query['title'],
                                                       'completed': False})
        return json_response({'user': request.query['user'], 'id': str(todos.inserted_id), 'title': request.query['title']})

    async def updateTodo(self, request):
        mongoDb = self.getMongoConnection(request)
        todo = await mongoDb['todo'].find_one_and_update(
            {
                '_id': ObjectId(request.query['id'])
            },
            {
                '$set': {
                    'completed': True if request.query['completed'].lower() == 'true' else False
                }
            },
            return_document=ReturnDocument.AFTER
        )
        return json_response({'user': todo['user'], 'id': str(todo['_id']), 'title': todo['title'], 'completed': todo['completed']})

    def generateError(self, errorMessage):
        return {
            'status': 'ERROR',
            'message': errorMessage
        }

    async def listTodos(self, request):
        await self.login(request)
        mongoDb = self.getMongoConnection(request)
        cursor = mongoDb['todo'].find({'user': request.query['user']})
        responseList = []
        try:
            for doc in await cursor.to_list(length=50):
                responseList.append(
                    {
                        'id': str(doc['_id']),
                        'user': doc['user'],
                        'title': doc['title'],
                        'completed': doc['completed']
                    }
                )
        except Exception as e:
            Logger.error(e.message, __name__)
            responseList.append(self.generateError(e.message))
            
        return json_response(responseList)

    async def deleteTodo(self, request):
        mongoDb = self.getMongoConnection(request)
        result = await mongoDb['todo'].delete_one(
            {
                '_id': ObjectId(request.query['id'])
            }
        )

        if result.deleted_count == 1:
            return json_response({'id': request.query['id']})

        return json_response({'message': 'Item with id {0} not deleted'.format(request.query['id'])})

    async def login(self, request):
        session = await get_session(request)
        lastVisit = session['last_visit'] if 'last_visit' in session else None
        mongoDb = self.getMongoConnection(request)
        print(mongoDb)
        try:
            rslt = await mongoDb['todo'].find_one({})
        except OperationFailure as e:
            Logger().error('Unable to login for user: {0}'.format(request.query['user']), __name__)
            return json_response({'message': 'Unable to login',
                                  'status': 'LOGIN_ERROR'
                                 })
        print(rslt)
        return json_response({'message': request.query['user'],
                              'status': 'LOGIN_SUCCESSFUL',
                              'last_visit': lastVisit
                             })
