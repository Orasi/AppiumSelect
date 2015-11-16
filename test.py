import os

from appium_selector.FilePath import get_full_path

os.environ['PROJECTFOLDER'] = get_full_path('')
from appium_selector.DeviceSelector import DeviceSelector
from selenium import webdriver




select = DeviceSelector(False, platform='desktop')
test = select.getDevice()
print(test)
driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=test[0]['desiredCaps'])

driver.implicitly_wait(10)
driver.get("http://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("Sauce Labs")
elem.submit()
print(driver.title)

# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.
driver.quit()