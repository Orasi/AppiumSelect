import os
import re
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup

from appium_selector.Config import GetConfig


class DeviceInfo:

    def __init__(self, platform='mobile'):
        self.platform = platform
        tree = self.loadDeviceXML()
        self.root = tree.getroot()

    def loadDeviceXML(self):
        projectFolder = GetConfig("ProjectFolder")
        devicePath = projectFolder + "/Devices.xml"
        if not os.path.exists(devicePath):
            open(devicePath, 'w').close()
        return ET.parse(devicePath)

    def getDevice(self, info):

        if '<|>' in info[1] or 'Desktop' in info[1]:
            return self.getDesktopDevice(info)
        else:
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

    def getDesktopDevice(self, info):
        env = info[1].split('<|>')
        device = {}
        device['udid']= info[1]
        device['platform'] = 'Desktop'
        device['name'] = info[1]
        device['manufacturer'] = env[2]
        device['model'] = env[0]
        device['osv'] = env[1]
        return device

    def sauceDevices(self):
        pass

    def gridDevices(self):
        output = []
        try:

            page = requests.get(GetConfig('GRID_URL') + '/grid/console')
            soup = BeautifulSoup(page.text, 'html.parser')
            if self.platform == 'mobile':
                output += self.mobileGridDevices(soup)
            elif self.platform == 'desktop':
              output += self.desktopGridDevices(soup)

        except:
            output = []
        return output

    def mobileGridDevices(self, soup):
        output = []
        for id in soup.select('a[title*=platform]'):
            if id.attrs['title'].find("MAC") > 0:
                output.append([id.text, 'iOS'])
            else:
                output.append([id.text, "Android"])
        return output

    def desktopGridDevices(self, soup):
        output = []
        for id in soup.select('img[title*=WebDriver]'):
            browser = re.search('browserName=.*?[}|,]', id['title']).group().split('=')[1].replace(',','')
            platform = re.search('platform=.*?[}|,]', id['title']).group().split('=')[1].replace('}','').replace(',','')
            browserVersion = re.search('version=.*?[}|,]', id['title']).group().split('=')[1].replace('}','').replace(',','')
            if not [id.text, browser + '<|>' + browserVersion + '<|>' + platform] in output:
                output.append([id.text, browser + '<|>' + browserVersion + '<|>' + platform])
        return output