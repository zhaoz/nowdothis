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
        self.setAspectRatioMode(Plasma.IgnoreAspectRatio)

        self.theme = Plasma.Svg(self)
        self.theme.setImagePath("widgets/background")
        self.setBackgroundHints(Plasma.Applet.DefaultBackground)

        self.settings = {}
        gc = self.config()
        self.settings["editor"] = gc.readEntry("editor", "/usr/bin/kate")
        self.ndt = NowDoThis(self.settings["editor"])

        self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)
        self.setLayout(self.layout)

        self.task = Plasma.Label(self.applet)
        self.task.setText(self.ndt.curTask() or "No Tasks")
        self.layout.addItem(self.task)

        done = Plasma.PushButton(self.applet)
        done.setText("Done")
        self.layout.addItem(done)
        self.connect(done, SIGNAL("clicked()"), self.finishTask)

        edit = Plasma.PushButton(self.applet)
        edit.setText("Edit")
        self.layout.addItem(edit)
        self.connect(edit, SIGNAL("clicked()"), self.edit)

        self.resize(125,125)


    def updateTaskText(self):
        self.task.setText(self.ndt.curTask() or "No Tasks")
        self.task.update()

    def edit(self):
        self.ndt.edit()
        self.updateTaskText()

    def finishTask(self):
        if self.ndt.finishTask():
            self.ndt.save()
            self.updateTaskText()

def CreateApplet(parent):
    return NowDoThisMoid(parent)
