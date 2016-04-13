import os
from appium_selector.FilePath import get_full_path
import unittest
import threading
import builtins

os.environ['PROJECTFOLDER'] = get_full_path('')

from appium_selector.DeviceSelector import DeviceSelector


os.environ['AddMustard'] = 'True'


builtins.threadlocal = threading.local()

def run_all_test(device=None):
    builtins.threadlocal.config = device
    loader = unittest.TestLoader()

    tests = loader.discover('./Tests', pattern='*Tests.py')
    runner = unittest.TextTestRunner()
    runner.run(tests)

threads =[]
devices = DeviceSelector(True, platform='').getDevice()
for device in devices:
    #t = threading.Thread(target=run_all_test, args=[device])
    #threads.append(t)
    print(str(device))
    #t.start()

print(len(devices))