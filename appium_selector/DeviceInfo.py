import os
import xml.etree.ElementTree as ET
import requests
from appium_selector.Config import GetConfig
from bs4 import BeautifulSoup

class DeviceInfo:

    def __init__(self):
        tree = self.loadDeviceXML()
        self.root = tree.getroot()

    def loadDeviceXML(self):
        if 'APPIUMDEVICES' in os.environ:
            devicePath = os.environ.get('APPIUMDEVICES')
        else:
            raise EnvironmentError('No APPIUMDEVICES environment variable set.  Can not find Devices.xml')

        if not os.path.exists(devicePath):
            open(devicePath, 'w').close()

        return ET.parse(devicePath)

    def getDevice(self, info):

        udid = info[0]
        platform = info[1]

        deviceNode = self.root.findall(".//device[udid='" + udid + "']")
        try:
            device = {}
            device['udid'] = deviceNode[0].find('udid').text
            device['platform'] = platform
            device['name'] = deviceNode[0].find('deviceName').text
            device['manufacturer'] = deviceNode[0].find('manufacturer').text
            device['model'] = deviceNode[0].find('model').text
            device['osv'] = deviceNode[0].find('osv').text
            return device
        except:
            device = {}
            device['udid'] = udid
            device['platform'] = platform
            device['name'] = 'unknown'
            device['manufacturer'] = 'unknown'
            device['model'] = 'unknown'
            device['osv'] = 'unknown'
            return device


    def gridDevices(self):
        try:
            page = requests.get(GetConfig('GRID_URL') + '/grid/console')
            soup = BeautifulSoup(page.text, 'html.parser')
            output = []
            for id in soup.select('a[title*=platform]'):
                if id.attrs['title'].find("MAC") > 0:
                    output.append([id.text, 'iOS'])
                else:
                    output.append([id.text, "Android"])
        except:
            output = []
        return output
