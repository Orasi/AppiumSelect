from appium_selector.CapGenerators.Caps import Caps


class SauceMobile(Caps):

    def __init__(self, environment):
        self.env = environment
        self.sauceNode = []
        self.options = {}
        self.caps = {}

    def displayString(self):
        platform = self.env.find('platformName').text
        browser = self.env.find('deviceName').text
        version = self.env.find('platformVersion').text
        return "Sauce -- %s -- %s -- %s" % (platform, browser, version)

    def desiredCaps(self, mustard=True):
        self.options['provider'] = 'sauceMobile'
        self.options['manufacturer'] = self.env.find('platformName').text
        self.options['model'] = self.env.find('deviceName').text
        self.options['osv'] = self.env.find('platformVersion').text
        self.options['mustard'] = mustard
        self.options['deviceName'] = self.displayString()

        self.caps['deviceName'] = self.env.find('deviceName').text
        self.caps['deviceOrientation'] = self.env.find('deviceOrientation').text
        self.caps['browserName'] = ''
        self.caps['platformVersion'] = self.env.find('platformVersion').text
        self.caps['platformName'] = self.env.find('platformName').text


        return {'desiredCaps': self.caps, 'options': self.options}
