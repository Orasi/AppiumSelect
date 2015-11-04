import os
from bs4 import BeautifulSoup

def GetConfig(configName):
    if 'APPIUMCONFIG' in os.environ:
        configPath = os.environ.get('APPIUMCONFIG')
    else:
        raise EnvironmentError('No APPIUMCONFIG environment variable set.  Can not find Config.xml')

    if os.path.exists(configPath):
        config = open(configPath, 'r')
    else:
        config = open(configPath, 'w')

    soup = BeautifulSoup(config, 'xml')
    node = soup.find(configName)

    if node==None:
        raise ValueError("Could not find value in Config.XML for [%s]" % configName)
    return node.text
