from hotdog.Config import GetConfig

from appium_selector.CapGenerators.Caps import Caps


class AWSWeb(Caps):

    def __init__(self, environment):
        self.awsNode = []
        self.options = {}
        self.caps = {}
        self.env = environment

    def displayString(self):
        browser = self.env.find('browserName').text
        version = self.env.find('version').text
        return "AWS Web -- Linux -- %s -- %s" % (browser, version)

    def desiredCaps(self, mustard=True):
        self.options['provider'] = 'awsWeb'
        self.options['model'] = self.env.find('browserName').text
        self.options['osv'] = self.env.find('version').text
        self.options['mustard'] = mustard
        self.options['deviceName'] = self.displayString()

        self.caps['browserName'] = self.env.find('browserName').text
        self.caps['version'] = self.env.find('version').text

        return {'desiredCaps': self.caps, 'options': self.options}
