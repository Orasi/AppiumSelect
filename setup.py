from distutils.core import setup
setup(
  name = 'appium_selector',
  packages = ['appium_selector'], # this must be the same as the name above
  version = '0.3.2',
  description = 'Creates a Tcl/Tk window to read connected Appium devices from Selenium Grid and display them for selection',
  author = 'Matt Watson',
  author_email = 'Watson.Mattc@gmail.com',
  url = 'https://github.com/Mattwhooo/appium_selector.git', # use the URL to the github repo
  download_url = 'https://github.com/Mattwhooo/appium_selector/tarball/0.3.1', # I'll explain this in a second
  keywords = ['appium', 'selenium', 'testing'], # arbitrary keywords
  classifiers=[],
  install_requires=['beautifulsoup4', 'requests']
)