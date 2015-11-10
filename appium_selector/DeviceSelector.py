from tkinter import *
import sys
import os
from tkinter.ttk import Notebook

from appium_selector.DeviceInfo import DeviceInfo
from appium_selector.Config import GetConfig


class DeviceSelector:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    devices = None

    def __init__(self, parallel=False, platform='mobile'):
        # Create Window
        self.root = Tk()
        win = self.root
        self.note = Notebook(self.root)

        # Set Window Properties
        if sys.platform.lower() == 'windows' or sys.platform.lower() == 'win32':
            win.iconbitmap(default=os.path.join(self.BASE_DIR, 'runner.ico'))
        win.wm_title("Test Runner")
        win.minsize(width=500, height=500)

        # Create Listbox
        scrollbar = Scrollbar(win)
        scrollbar.pack(side=RIGHT, fill=Y)

        #Add Mustard Checkbox and Instructions Label
        frame = Frame(win)


        self.mustard = GetConfig('SKIP_MUSTARD').lower() == 'false'
        c = Checkbutton(frame, text="Add Mustard?", command=self._toggleMustard)
        if self.mustard:
            c.select()
        c.pack(side=RIGHT)

        mobileFrame = Frame(win)
        if parallel:
            label = Label(frame, text="Please Select one or more devices to run")
            label.pack(side=LEFT)
            self.listboxMobile = Listbox(mobileFrame, selectmode=EXTENDED)
        else:
            label = Label(frame, text="Please Select one device to run")
            label.pack(side=LEFT)
            self.listboxMobile = Listbox(mobileFrame, selectmode=SINGLE)
        frame.pack(fill=X)


        self.listboxMobile.pack(fill=BOTH, expand=1)

        # Attach Scrollbar to Listbox
        self.listboxMobile.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listboxMobile.yview)

        # Generate Listbox Data
        info = DeviceInfo(platform='mobile')
        for deviceId in info.gridDevices():
            device = info.getDevice(deviceId)
            self.listboxMobile.insert(END,
                                device['platform'] + ' -- ' + device['udid'] + ' -- ' + device['name'] if device['name'] != 'unknown'
                                else device['platform'] + ' -- ' + device['udid'] + ' -- Unknown Device,  Please add to details to Devices.xml')
        self.listboxMobile.insert(END, 'SauceLabs')
        self.listboxMobile.insert(END, 'Local Device')




        desktopFrame = Frame(win)
        if parallel:
            self.listboxDesktop = Listbox(desktopFrame, selectmode=EXTENDED)
        else:
            self.listboxDesktop = Listbox(desktopFrame, selectmode=SINGLE)
        frame.pack(fill=X)


        self.listboxDesktop.pack(fill=BOTH, expand=1)

        # Attach Scrollbar to Listbox
        self.listboxDesktop.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listboxDesktop.yview)

        # Generate Listbox Data
        info = DeviceInfo(platform='desktop')
        for deviceId in info.gridDevices():
            device = info.getDevice(deviceId)
            if device['platform'] == 'Desktop':
                self.listboxDesktop.insert(END,
                                device['platform'] + ' -- '  + device['name'].replace('<|>', " -- "))
            else:
                self.listboxDesktop.insert(END,
                                device['platform'] + ' -- ' + device['udid'] + ' -- ' + device['name'] if device['name'] != 'unknown'
                                else device['platform'] + ' -- ' + device['udid'] + ' -- Unknown Device,  Please add to details to Devices.xml')
        self.listboxDesktop.insert(END, 'Local Chrome')
        self.listboxDesktop.insert(END, 'Local Firefox')
        self.listboxDesktop.insert(END, 'Local IE')

        self.frame = Frame(win)
        self.frame.pack(fill=X)


        # Create Buttons
        Button(mobileFrame, text="Cancel", fg="red", command=self.frame.quit, width=50, height=5).pack(side=RIGHT, fill=Y)
        Button(mobileFrame, text="Run Test", fg="green", command=self._saveDevices, width=50).pack(side=LEFT, fill=Y)

        # Create Buttons
        Button(desktopFrame, text="Cancel", fg="red", command=self.frame.quit, width=50, height=5).pack(side=RIGHT, fill=Y)
        Button(desktopFrame, text="Run Test", fg="green", command=self._saveDevicesDesktop, width=50).pack(side=LEFT, fill=Y)

        if platform.lower() == 'mobile':
            self.note.add(mobileFrame, text='Mobile')
            self.note.add(desktopFrame, text='Desktop')
        else:
            self.note.add(desktopFrame, text='Desktop')
            self.note.add(mobileFrame, text='Mobile')
        self.note.pack(fill=BOTH, expand=1)





    def _toggleMustard(self):
        self.mustard = not self.mustard

    def getDevice(self):
        self.root.mainloop()
        self.root.destroy()
        return self.devices

    def _saveDevicesDesktop(self):
        info = DeviceInfo()
        devices = self.listboxDesktop.curselection()

        output = []
        for device in devices:
            deviceString = self.listboxDesktop.get(device)
            if deviceString in ['Local Chrome', 'Local Firefox', 'Local IE']:
                output.append(self._createLocalDesiredCaps(deviceString))
            else:
                d = deviceString.split(' -- ')
                deviceInfo = info.getDevice(['', d[1] + '<|>' + d[2] + '<|>' + d[3]])
                output.append(self._createDesiredCapabilites(deviceInfo))


        self.frame.quit()
        self.devices = output

    def _saveDevices(self):
        info = DeviceInfo()
        devices = self.listboxMobile.curselection()

        output = []
        for device in devices:
            deviceString = self.listboxMobile.get(device)
            deviceInfo = info.getDevice([deviceString.split(' -- ')[1], deviceString.split(' -- ')[0]] )
            output.append(self._createDesiredCapabilites(deviceInfo))

        self.frame.quit()
        self.devices = output

    def _createLocalDesiredCaps(self, device):
        options = {}
        caps = {}
        options['provider'] = device
        options['manufacturer'] = device
        options['model'] = device
        options['osv'] = device
        options['mustard'] = False
        caps['udid'] = device
        caps['platformName'] = device
        caps['browserName'] = device
        caps['deviceName'] = device
        return {'desiredCaps': caps, 'options': options}
    def _createDesiredCapabilites(self, device):
        caps = {}
        options = {}
        if device['udid'] == 'SauceLabs':
            options['provider'] = 'saucelabs'
            options['mustard'] = self.mustard

            caps['browserName'] = ""
            caps['appiumVersion'] = "1.4.11"
            caps['deviceName'] = "Android Emulator"
            caps['deviceOrientation'] = "portrait"
            caps['platformVersion'] = "5.0"
            caps['platformName'] = "Android"
        elif device['udid'] == 'Local Device':
            caps['browserName'] = "Local Device"
            options['provider'] = 'local'
            options['mustard'] = self.mustard

            options['manufacturer'] = '1234'
            options['model'] = '123'
            options['osv'] = '12345'

            caps['udid'] = '877cfdb7ad60d5b78d8aa02c9e90b0e929891c91'
            caps['platformName'] = "iOS"
            #caps['browserName'] = device['udid']
            #caps['appActivity'] = '.SignInActivity'
            #caps['appWaitActivity'] = '.SignInActivity'
            caps['deviceName'] = "Android Emulator"
            #caps['platformName'] = "Android"
        elif device['platform'] == 'Desktop':
            options['provider'] = 'localDesktop'
            options['manufacturer'] = device['manufacturer']
            options['model'] = device['model']
            options['osv'] = device['osv']
            options['mustard'] = self.mustard
            caps['udid'] = device['udid']
            caps['platformName'] = device['manufacturer']
            caps['browserName'] = device['model']
            caps['deviceName'] = device['udid']
        else:
            options['provider'] = 'grid'
            options['manufacturer'] = device['manufacturer']
            options['model'] = device['model']
            options['osv'] = device['osv']
            options['mustard'] = self.mustard

            if device['platform'] == 'Android':
                caps['appActivity'] = '.SignInActivity'
                caps['appWaitActivity'] = '.SignInActivity'

            caps['platformName'] = device['platform']
            caps['deviceName'] = device['name']
            caps['udid'] = device['udid']
            caps['browserName'] = device['udid']

        if device['platform'] == 'Android':
            caps['app'] = GetConfig('ANDROID_APP_URL')
        elif device['platform'].upper() == 'IOS':
            caps['app'] = GetConfig('IOS_APP_URL')

        return {'desiredCaps': caps, 'options': options}
