import os
from bs4 import BeautifulSoup

def GetConfig(configName):
    if 'PROJECTFOLDER' in os.environ:
        configPath = os.environ.get('PROJECTFOLDER')
        if configPath[-1] == '/':
            configPath = configPath[:-1]
    else:
        raise EnvironmentError('No PROJECTFOLDER environment variable set.  Can not find Config.xml')

    if configName.lower() == 'projectfolder':
        return configPath

    if os.path.exists(configPath):
        config = open(configPath + '/Config.xml', 'r')
    else:
        config = open(configPath + '/Config.xml', 'w')

    soup = BeautifulSoup(config, 'xml')
    node = soup.find(configName)

    if node==None:
        raise ValueError("Could not find value in Config.XML for [%s]" % configName)
    return node.text
