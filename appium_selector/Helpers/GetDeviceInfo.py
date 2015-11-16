import os
import xml.etree.ElementTree as ET

from appium_selector.Helpers.Config import GetConfig


def getDeviceInfo(udid, platform):

    #Open Device Config File
    projectFolder = GetConfig("ProjectFolder")
    devicePath = projectFolder + "/Devices.xml"
    if not os.path.exists(devicePath):
        open(devicePath, 'w').close()

    #Find Device
    root = ET.parse(devicePath).getroot()
    deviceNode = root.findall(".//device[udid='" + udid + "']")

    try:
        device = {}
        device['udid'] = udid
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