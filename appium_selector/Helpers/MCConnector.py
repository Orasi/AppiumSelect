import os
import xml.etree.ElementTree as ET

from appium_selector.CapGenerators.MCMobile import MCMobile
from appium_selector.CapGenerators.MCWeb import MCWeb
from appium_selector.Helpers.Config import GetConfig


class MCConnector(object):

    webNodes = []
    mobileNodes = []

    def __init__(self):

        #Open Device Config File
        projectFolder = GetConfig("ProjectFolder")
        devicePath = projectFolder + "/MobileCenter.xml"
        if os.path.exists(devicePath):

            #Find Device
            root = ET.parse(devicePath).getroot()
            webNodes = root.findall(".//node[platform='web']")
            for node in webNodes:
                self.webNodes.append(MCWeb(node))

            mobileNodes = root.findall(".//node[platform='mobile']")
            for node in mobileNodes:
                self.mobileNodes.append(MCMobile(node))
