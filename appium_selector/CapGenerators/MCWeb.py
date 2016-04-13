from hotdog.Config import GetConfig

from appium_selector.CapGenerators.Caps import Caps


class MCWeb(Caps):

    def __init__(self, environment):
        self.mcNode = []
        self.options = {}
        self.caps = {}
        self.env = environment

    def displayString(self):
        device = self.env.find('deviceName').text
        browser = self.env.find('browserName').text
        return "MobileCenter -- %s -- %s " % (device, browser)

    def desiredCaps(self, mustard=True):
        self.options['provider'] = 'mcWeb'
        self.options['manufacturer'] = self.env.find('platformName').text
        self.options['model'] = self.env.find('browserName').text
        self.options['osv'] = self.env.find('version').text
        self.options['mustard'] = mustard
        self.options['deviceName'] = self.displayString()

        self.caps['platformName'] = self.env.find('platformName').text
        self.caps['browserName'] = self.env.find('browserName').text
        self.caps['deviceName'] = self.env.find('deviceName').text
        self.caps['userName'] = 'admin@default.com'
        self.caps['password'] = 'password'

        return {'desiredCaps': self.caps, 'options': self.options}
