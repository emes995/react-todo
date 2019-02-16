#
# $Id$
#

import unittest
from base.Singleton import Singleton
from session.Session import Session
from context.Context import Context

class TestBase(unittest.TestCase):

    def test_Singleton(self):
        class MySingleton(metaclass=Singleton):
            def __init__(self):
                print('me')

        ms = MySingleton()
        assert ms == Singleton._instances.pop(MySingleton)

if __name__ == '__main__':

    unittest.main()

