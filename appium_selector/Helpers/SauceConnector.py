import os
import xml.etree.ElementTree as ET
from appium_selector.CapGenerators.SauceMobile import SauceMobile
from appium_selector.CapGenerators.SauceWeb import SauceWeb
from appium_selector.CapGenerators.SauceMobileWeb import SauceMobileWeb
from appium_selector.Helpers.Config import GetConfig


class SauceConnector(object):

    webNodes = []
    mobileNodes = []
    mobileWebNodes = []

    def __init__(self):

        #Open Device Config File
        projectFolder = GetConfig("ProjectFolder")
        devicePath = projectFolder + "/Sauce.xml"
        if os.path.exists(devicePath):

            #Find Device
            root = ET.parse(devicePath).getroot()
            webNodes = root.findall(".//node[platform='web']")
            for node in webNodes:
                self.webNodes.append(SauceWeb(node))

            mobileNodes = root.findall(".//node[platform='mobile']")
            for node in mobileNodes:
                self.mobileNodes.append(SauceMobile(node))

            mobileWebNodes = root.findall(".//node[platform='mobileWeb']")
            for node in mobileWebNodes:
                self.mobileWebNodes.append(SauceMobileWeb(node))