from hotdog.Config import GetConfig

from appium_selector.CapGenerators.Caps import Caps

class AWSMobileWeb(Caps):

    def __init__(self, environment):
        self.awsNode = []
        self.options = {}
        self.caps = {}
        self.env = environment

    def displayString(self):
        browser = self.env.find('browserName').text
        version = self.env.find('version').text
        screen_size = self.env.find('screenSize').text
        return "AWS Mobile -- Linux -- %s -- %s -- %s" % (browser, version, screen_size)

    def desiredCaps(self, mustard=True):
        self.options['provider'] = 'awsMobileWeb'
        self.options['model'] = self.env.find('browserName').text
        self.options['osv'] = self.env.find('version').text
        self.options['mustard'] = mustard
        self.options['deviceName'] = self.displayString()

        self.caps['browserName'] = self.env.find('browserName').text
        self.caps['version'] = self.env.find('version').text
        self.caps['chromeOptions'] = {}
        return {'desiredCaps': self.caps, 'options': self.options}