#
# $Id$
#

import uuid

class Session(object):

    def __init__(self, username, password, host, port, useAuth=False):
        self._username = username
        self._password = password
        self._hostname = host
        self._port = port
        self._isActive = False
        self._uuid = uuid.uuid4()
        self._useAuthentication = useAuth

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def host(self):
        return self._hostname

    @property
    def port(self):
        return self._port

    @property
    def isActive(self):
        return self._isActive

    @isActive.setter
    def isActive(self, status):
        self._isActive = status

    @property
    def id(self):
        return self._uuid

    @property
    def useAuth(self):
        return self._useAuthentication

    @useAuth.setter
    def useAuth(self, value):
        self._useAuthentication = value

    def __str__(self):
        return '{0}@{1}:{2}@xxxxxx IsActive={3} ID={4}'.format(self.host(), self.port(),
                                                               self.username(), self.isActive(),
                                                               self.id())
