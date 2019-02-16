#
# $Id$
#

import logging.config
from base.Singleton import Singleton
import motor.motor_asyncio
import os

class ApplicationContext(metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        self._setupLogging()

    def _setupLogging(self):
        logConfig = os.path.join('/', 'home', 'developer001', 'projects', 'react', 'todo', 'python', 'resources', 'config', 'logging.conf')
        if not os.path.exists(logConfig):
            raise FileNotFoundError('logger config file {0} not found'.format(logConfig), __name__)
        logging.config.fileConfig(logConfig)

