# Super Simple Todo List
# Ziling Zhao <zilingzhao@gmail.com>

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript

from nowdothis import NowDoThis

class NowDoThisMoid(plasmascript.Applet):
    def __init__(self, parent, args=None):
        plasmascript.Applet.__init__(self, parent)

    def init(self):
        self.setHasConfigurationInterface(True)
        self.setAspectRatioMode(Plasma.Square)

        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)

        self.layout = QGraphicsLinearLayout(Qt.Horizontal, self.applet)
        label = Plasma.Label(self.applet)
        label.setText("DoThisNow")
        self.layout.addItem(label)
        self.setLayout(self.layout)
        self.resize(125,125)

        self.settings = {}
        gc = self.config()

        self.settings["editor"] = gc.readEntry("editor", "/usr/bin/kwrite")

        self.ndt = NowDoThis(self.settings["editor"])


def CreateApplet(parent):
    return NowDoThisMoid(parent)
