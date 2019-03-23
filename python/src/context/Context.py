#
# $Id$
#

import motor.motor_asyncio as ma
import logging.config
from base.Singleton import Singleton
import os

from session.Session import Session

class Context(object):

    class MongoConnection():
        def __init__(self, session):
            self._mongo_session = session
            self._client = None

        def connect(self, **kwargs):
            if self._client == None:
                if self._mongo_session.useAuth:
                    self._client = ma.AsyncIOMotorClient(self._mongo_session.host, self._mongo_session.port,
                                                        username=self._mongo_session.username,
                                                        password=self._mongo_session.password,
                                                        **kwargs)
                else:
                    self._client = ma.AsyncIOMotorClient(self._mongo_session.host, self._mongo_session.port)

            return self._client

    def __init__(self):
        pass

    def mongo_connection(self, credentials, **kwargs):
        return Context.MongoConnection(credentials).connect(**kwargs)
