from appium_selector.CapGenerators.LocalWeb import LocalWeb
from appium_selector.Helpers.Config import GetConfig


class LocalConnector(object):

    localWeb = ['ie', 'chrome', 'firefox', 'safari', 'firefox:marionette']
    webNodes = []

    def __init__(self):

        for browser in self.localWeb:
            self.webNodes.append(LocalWeb(browser))
