from hotdog.Config import GetConfig

from appium_selector.CapGenerators.Caps import Caps

class SauceMobileWeb(Caps):

    def __init__(self, environment):
        self.sauceNode = []
        self.options = {}
        self.caps = {}
        self.env = environment

    def displayString(self):
        platform = self.env.find('platformName').text
        browser = self.env.find('browserName').text
        version = self.env.find('version').text
        mobile_name = self.env.find('mobileEmulation').text
        return "Sauce Mobile -- %s -- %s -- %s -- %s" % (platform, browser, version, mobile_name)

    def desiredCaps(self, mustard=True):
        self.options['provider'] = 'sauceMobileWeb'
        self.options['manufacturer'] = self.env.find('platformName').text
        self.options['model'] = self.env.find('browserName').text
        self.options['osv'] = self.env.find('version').text
        self.options['mustard'] = mustard
        self.options['deviceName'] = self.displayString()
        self.options['mobileEmulation'] = True

        try:
            self.caps['parentTunnel'] = GetConfig('SAUCE_PARENT_TUNNEL')
        except:
            pass
        self.caps['platform'] = self.env.find('platformName').text
        self.caps['browserName'] = self.env.find('browserName').text
        self.caps['version'] = self.env.find('version').text
        self.caps['udid'] = "%s-%s-%s" % (self.env.find('platformName').text.replace('.',''), self.env.find('browserName').text.replace('.',''), self.env.find('version').text.replace('.',''))
        self.caps['chromeOptions'] = {}
        self.caps['chromeOptions']['mobileEmulation'] = {}
        self.caps['chromeOptions']['mobileEmulation']['deviceName'] = self.env.find('mobileEmulation').text
        return {'desiredCaps': self.caps, 'options': self.options}