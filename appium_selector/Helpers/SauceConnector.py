import os
import xml.etree.ElementTree as ET
from appium_selector.CapGenerators.SauceMobile import SauceMobile
from appium_selector.CapGenerators.SauceWeb import SauceWeb
from appium_selector.Helpers.Config import GetConfig


class SauceConnector(object):

    webNodes = []
    mobileNodes = []

    def __init__(self):

        #Open Device Config File
        projectFolder = GetConfig("ProjectFolder")
        devicePath = projectFolder + "/Sauce.xml"
        if not os.path.exists(devicePath):
            open(devicePath, 'w').close()

        #Find Device
        root = ET.parse(devicePath).getroot()
        webNodes = root.findall(".//node[platform='web']")
        for node in webNodes:
            self.webNodes.append(SauceWeb(node))

        mobileNodes = root.findall(".//node[platform='mobile']")
        for node in mobileNodes:
            self.mobileNodes.append(SauceMobile(node))