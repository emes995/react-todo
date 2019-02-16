#
# $Id#
#

from base.Singleton import Singleton
import logging

class Logger(metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        self._logger = logging.getLogger('todo')

    def _formatMessage(self, message, source):
        return '{1} : {0}'.format(message, source)

    def info(self, message, source='not_avalable'):
        self._logger.info(self._formatMessage(message, source))

    def debug(self, message, source='not_avalable'):
        self._logger.debug(self._formatMessage(message, source))

    def warn(self, message, source='not_avalable'):
        self._logger.warn(self._formatMessage(message, source))

    def error(self, message, source='not_avalable'):
        self._logger.error(self._formatMessage(message, source))
