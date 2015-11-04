from distutils.core import setup
setup(
  name = 'AppiumSelector',
  packages = ['AppiumSelector'], # this must be the same as the name above
  version = '0.1',
  description = 'Creates a TKL window to read connected Appium devices from Selenium Grid and display them for selection',
  author = 'Matt Watson',
  author_email = 'Watson.Mattc@gmail.com',
  url = 'https://github.com/Mattwhooo/AppiumSelector.git', # use the URL to the github repo
  download_url = 'https://github.com/Mattwhooo/AppiumSelector/tarball/0.1', # I'll explain this in a second
  keywords = ['appium', 'selenium', 'testing'], # arbitrary keywords
  classifiers=[]
)