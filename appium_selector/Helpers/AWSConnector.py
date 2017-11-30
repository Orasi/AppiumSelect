import os
import xml.etree.ElementTree as ET
from appium_selector.CapGenerators.AWSWeb import AWSWeb
from appium_selector.CapGenerators.AWSMobileWeb import AWSMobileWeb
from appium_selector.Helpers.Config import GetConfig


class AWSConnector(object):

    webNodes = []
    mobileNodes = []
    mobileWebNodes = []

    def __init__(self):

        #Open Device Config File
        projectFolder = GetConfig("ProjectFolder")
        devicePath = projectFolder + "/AWS.xml"
        if os.path.exists(devicePath):

            #Find Device
            root = ET.parse(devicePath).getroot()
            webNodes = root.findall(".//node[platform='web']")
            for node in webNodes:
                self.webNodes.append(AWSWeb(node))

            mobileWebNodes = root.findall(".//node[platform='mobileWeb']")
            for node in mobileWebNodes:
                self.mobileWebNodes.append(AWSMobileWeb(node))