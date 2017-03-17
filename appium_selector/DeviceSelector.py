from tkinter import *
import sys
import os
from tkinter.ttk import Notebook
import re
from appium_selector.Helpers.Config import GetConfig
from appium_selector.Helpers.GridConnector import GridConnector
from appium_selector.Helpers.LocalConnector import LocalConnector
from appium_selector.Helpers.SauceConnector import SauceConnector
from appium_selector.Helpers.MCConnector import MCConnector

class DeviceSelector:

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    devices = None

    local = LocalConnector()
    grid = GridConnector()
    sauce = SauceConnector()
    mc = MCConnector()

    def __init__(self, parallel=False, platform='mobile'):
        self.parallel = parallel
        self.platform = platform


    def start(self):
        parallel = self.parallel
        platform = self.platform

        # Create Window
        self.root = Tk()
        win = self.root
        self.note = Notebook(self.root)

        # Set Window Properties
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
        mobileData = []
        mobileNodes = self.grid.mobileNodes
        for node in mobileNodes:
            mobileData.append(node)
            self.listboxMobile.insert(END, node.displayString())

        sauceNodes = self.sauce.mobileNodes
        for node in sauceNodes:
            mobileData.append(node)
            self.listboxMobile.insert(END, node.displayString())

        mcNodes = self.mc.mobileNodes
        for node in mcNodes:
            mobileData.append(node)
            self.listboxMobile.insert(END, node.displayString())

        self.mobileData = mobileData

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
        webData = []
        webDisplay =[]

        localNodes = self.local.webNodes
        for node in localNodes:
            webData.append(node)
            self.listboxDesktop.insert(END, node.displayString())

        webNodes = self.grid.webNodes
        for node in webNodes:
            ds = node.displayString()
            if ds not in webDisplay:
                webDisplay.append(ds)
                webData.append(node)
                self.listboxDesktop.insert(END, ds)

        sauceNodes = self.sauce.webNodes
        for node in sauceNodes:
            webData.append(node)
            self.listboxDesktop.insert(END, node.displayString())

        sauceNodes = self.sauce.mobileWebNodes
        for node in sauceNodes:
            webData.append(node)
            self.listboxDesktop.insert(END, node.displayString())

        mcNodes = self.mc.webNodes
        for node in mcNodes:
            webData.append(node)
            self.listboxDesktop.insert(END, node.displayString())

        self.webData = webData

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
            self.note.add(desktopFrame, text='Web')
        else:
            self.note.add(desktopFrame, text='Web')
            self.note.add(mobileFrame, text='Mobile')
        self.note.pack(fill=BOTH, expand=1)

        # allow double clicking in listbox to select a browser
        self.listboxMobile.bind('<Double-1>', lambda x: self._saveDevices())
        self.listboxDesktop.bind('<Double-1>', lambda x: self._saveDevicesDesktop())

    def _toggleMustard(self):
        self.mustard = not self.mustard

    def getDevice(self, filter=None, mustard=True):
        if filter:
            #webNodes = self.grid.webNodes
            #mobileNodes = self.grid.mobileNodes
            if self.platform:
                if self.platform == 'desktop':
                    nodes = self.grid.webNodes + self.sauce.webNodes + self.sauce.mobileWebNodes
                elif self.platform == 'mobile':
                    nodes = self.grid.mobileNodes + self.sauce.mobileNodes
                else:
                    nodes = self.grid.webNodes + self.grid.mobileNodes + self.sauce.webNodes + self.sauce.mobileWebNodes
            output=[]
            for node in nodes:
                if re.search(filter, node.displayString()):
                    dc = node.desiredCaps(mustard=mustard)
                    output.append(dc)
            return output
        else:
            self.start()
            # for osx bring selector window to the front
            if sys.platform.lower() == 'darwin':  # Mac OS
                self.root.lift()
                self.root.attributes('-topmost', True)
            self.root.mainloop()
            self.root.destroy()
            output = []
            for x in range(len(self.devices)):
                dc = self.devices[x].desiredCaps(mustard=self.mustard)
                if dc not in output:
                    output.append(dc)
            return output

    def _saveDevicesDesktop(self):

        selected = self.listboxDesktop.curselection()

        output = []
        for selection in selected:
            output.append(self.webData[int(selection)])

        self.frame.quit()
        self.devices = output

    def _saveDevices(self):

        selected = self.listboxMobile.curselection()

        output = []
        for selection in selected:
            output.append(self.mobileData[int(selection)])

        self.frame.quit()
        self.devices = output
