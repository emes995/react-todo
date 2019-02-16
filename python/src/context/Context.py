#
# $Id$
#

import motor.motor_asyncio as ma
import logging.config
from base.Singleton import Singleton
import os

from session.Session import Session

class Context(object):

    class MongoConnection(metaclass=Singleton):
        def __init__(self, session):
            self._mongo_session = session
            self._client = None

        def _connect(self):
            if self._client == None:
                if self._mongo_session.useAuth:
                    self._client = ma.AsyncIOMotorClient(self._mongo_session.host, self._mongo_session.port,
                                                        username=self._mongo_session.username,
                                                        password=self._mongo_session.password)
                else:
                    self._client = ma.AsyncIOMotorClient(self._mongo_session.host, self._mongo_session.port)

            return self._client

        @property
        def connection(self):
            return self._connect()

    def __init__(self):
        pass

    def mongo_connection(self, credentials):
        return Context.MongoConnection(credentials).connection
