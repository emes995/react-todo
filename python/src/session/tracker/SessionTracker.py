#
# $Id$
#

from base.Singleton import Singleton

class SessionTracker(metaclass=Singleton):

    def __init__():
        self._sessions = {}

    def getSessionFor(sessionId:int)