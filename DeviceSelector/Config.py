from bs4 import BeautifulSoup
from DeviceSelector.FilePath import get_full_path

def GetConfig(configName):
    config = open(get_full_path('Config.xml'), 'r')
    soup = BeautifulSoup(config, 'xml')
    node = soup.find(configName)

    if node==None:
        raise ValueError("Could not find value in Config.XML for [%s]" % configName)
    return node.text
