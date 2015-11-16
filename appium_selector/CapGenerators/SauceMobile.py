from appium_selector.CapGenerators.Caps import Caps


class SauceMobile(Caps):

    sauceNode = []
    options = {}
    caps = {}

    def __init__(self, environment):
        self.env = environment

    def displayString(self):
        platform = self.env.find('platformName').text
        browser = self.env.find('browserName').text
        version = self.env.find('version').text
        return "Sauce -- %s -- %s -- %s" % (platform, browser, version)

    def desiredCaps(self):
        self.options['provider'] = 'sauceWeb'
        self.options['manufacturer'] = self.env.find('platformName').text
        self.options['model'] = self.env.find('browserName').text
        self.options['osv'] = self.env.find('version').text

        self.caps['platformName'] = self.env.find('platformName').text
        self.caps['browserName'] = self.env.find('browserName').text
        self.caps['version'] = self.env.find('version').text
        return {'desiredCaps': self.caps, 'options': self.options}