# -*- coding: utf-8 -*-
import sys

from PyQt4.QtGui import QAction, QIcon, QFileDialog

import resources_rc

from PyQt4 import QtCore, QtGui, Qt, QtDeclarative


class I_will_be_form(QtDeclarative.QDeclarativeView):
    def __init__(self, qml_source, parent=None):
        QtDeclarative.QDeclarativeView.__init__(self, parent)

        # Убираем рамку окна
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        self.setSource(QtCore.QUrl(qml_source))

        self.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
        self.setGeometry(100, 100, 400, 240)

        self.signal_func_Qml()
        self.signalThis()
        self.slot()
        self.prop()

    def signal_func_Qml(self):
        print "Qml's signal"
        root = self.rootObject()
        print "root: ", root
        root.wantquit.connect(self.close)
        # root.updateMessage('From root') #(3)
        self.rootContext().setContextProperty("mainwindow", self)

    def signalThis(self):
        print "Signal of PyQt"

    def slot(self):
        print "Property"

    def prop(self):
        print "Slot "

    @QtCore.pyqtProperty(unicode)
    def selectFile(self):
        filename = QFileDialog.getOpenFileName(self, "Choose file")
        print filename
        print type(filename)
        return filename


class Plugin():

    def __init__(self, iface):
        self.iface = iface
        self.__name = "QMLPlugin"

    def initGui(self):
        self.action = QAction(
            QIcon(":/plugins/qmlplugin/icons/info.png"),
            "QMLStart",
            self.iface.mainWindow()
        )

        self.iface.addPluginToMenu(self.__name, self.action)
        self.iface.addToolBarIcon(self.action)

        self.action.triggered.connect(self.run)

    def unload(self):
        self.iface.removePluginMenu(self.__name, self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        # QgsMessageLog.logMessage(
        #     "Run about",
        #     self.__name,
        #     QgsMessageLog.INFO
        # )

        # self.iface.messageBar().pushMessage(
        #     self.__name,
        #     "Run about",
        #     self.iface.messageBar().WARNING,
        #     2
        # )
        Iwbf = I_will_be_form('qrc:/plugins/qmlplugin/main.qml', self.iface.mainWindow())
        Iwbf.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    Iwbf = I_will_be_form('main.qml')
    Iwbf.show()
    sys.exit(app.exec_())
