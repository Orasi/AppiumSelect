from appium_selector.CapGenerators.Caps import Caps, propertyFromString


class LocalWeb(Caps):

    options = {}
    caps = {}

    def __init__(self, browser):
        self.browser = browser

    def displayString(self):
        return "Local %s" % self.browser

    def desiredCaps(self):
        self.options['provider'] = 'local-' + self.browser
        self.options['manufacturer'] = 'local'
        self.options['model'] = 'local'
        self.options['osv'] = 'Local'
        self.options['mustard'] = False

        self.caps['platformName'] = 'Local'
        self.caps['browserName'] = 'Local'
        self.caps['version'] = 'Local'
        self.caps['deviceName'] = 'Local'

        return {'desiredCaps': self.caps, 'options': self.options}
