#
# $Id$
#

import asyncio

class ToDoEntry:

    def __init__(self, user, id, title):
        self._entry{
            '_id': id,
            'user': user,
            'title': title
        }

    @property
    def entry(self):
        return self.entry

    @entry.setter
    def entry(self, entry):
        self._entry = entry

    async def findTodo(self, user, title, userContext):
        mongoConn = userContext.mongo_connection()
        todo = await mongoConn['todo'].find({'user': user,'title': title})
        print(todo)