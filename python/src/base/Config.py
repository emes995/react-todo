#
# $Id$
#

from base.Singleton import Singleton
from logger.Logger import Logger
import json
import os

class Config(metaclass=Singleton):

    def __init__(self):
        self._configurations = {}

    def _readConfiguration(self, fileLocation):
        jsonStr = ''
        with open(fileLocation, 'r') as config:
            jsonStr = config.read()
        
        return jsonStr

    def loadConfiguration(self, configFile, pathAbs=False):
        fileLocation = os.path.join(os.path.dirname(__file__), '..', '..', 'resources', 'config', configFile) if not pathAbs else configFile
        jsonStr = self._readConfiguration(fileLocation)
        Logger().info('Loading configuration file: {0}'.format(fileLocation), __name__)

        try:
            configEntries = json.loads(jsonStr)
            self._configurations.update(configEntries)
        except Exception as e:
            Logger().error(str(e), __name__)
            Logger().error('Unable to parse json string: {0}'.format(jsonStr), __name__)

    def getConfiguration(self, configEntry, defaultValue=None):

        if configEntry in self._configurations:
            return self._configurations[configEntry]

        if defaultValue == None:
            raise KeyError('Configuration entry does not exist: {0}'.format(configEntry), __name__)

        return defaultValue
    
    def configurationExists(self, configEntry):
        return configEntry in self._configurations
