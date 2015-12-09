from appium_selector.CapGenerators.Caps import Caps


class SauceWeb(Caps):

    def __init__(self, environment):
        self.sauceNode = []
        self.options = {}
        self.caps = {}
        self.env = environment

    def displayString(self):
        platform = self.env.find('platformName').text
        browser = self.env.find('browserName').text
        version = self.env.find('version').text
        return "Sauce -- %s -- %s -- %s" % (platform, browser, version)

    def desiredCaps(self, mustard=True):
        self.options['provider'] = 'sauceWeb'
        self.options['manufacturer'] = self.env.find('platformName').text
        self.options['model'] = self.env.find('browserName').text
        self.options['osv'] = self.env.find('version').text
        self.options['mustard'] = mustard
        self.options['deviceName'] = self.displayString()

        self.caps['platform'] = self.env.find('platformName').text
        self.caps['browserName'] = self.env.find('browserName').text
        self.caps['version'] = self.env.find('version').text
        self.caps['udid'] = "%s-%s-%s" % (self.env.find('platformName').text.replace('.',''), self.env.find('browserName').text.replace('.',''), self.env.find('version').text.replace('.',''))
        return {'desiredCaps': self.caps, 'options': self.options}
