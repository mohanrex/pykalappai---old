__author__ = "Manikk, Vijay, Mohan"
__copyright__ = "Copyright (c) 2015 http://thamizha.com/"
__credits__ = ["Manikk, Vijay, Mohan"]
__license__ = "GNU/GPL v3 or (at your option) any later version."
__version__ = "4.0.0"
__maintainer__ = "http://thamizha.com/"
__email__ = ""
__status__ = "Development"

import os
import shutil
import time
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import QSharedMemory, QSplashScreen, \
    QSystemTrayIcon, qApp, QSettings, QGroupBox, QLabel, \
    QComboBox, QIcon, QHBoxLayout, QCheckBox, QAction, QDialog, QMenu, QVBoxLayout
from PyQt5.QtCore import qWarning
from PyQt5.QtGui import QPixmap

from resources import ekalappai_rc
from EkEngine import Engine
from view import dialog_ui


class EkWindow(QDialog, dialog_ui.Ui_Dialog):

    def __init__(self):
        super(EkWindow, self).__init__()
        self.minimizeAction = QAction("Minimize", self)
        self.maximizeAction = QAction("Maximize", self)
        self.settingsAction = QAction("Settings", self)
        self.aboutAction = QAction("About", self)
        self.quitAction = QAction("Quit", self)
        self.trayIconMenu = QMenu(self)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon(QPixmap(":icon/logo")))
        self.trayIconMenu.addAction(self.settingsAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.aboutAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("eKalappai")
    app.setApplicationVersion("4.0.0")
    shared = QSharedMemory("59698760-43bb-44d9-8121-181ecbb70e4d")

    if not shared.create(512, QSharedMemory.ReadWrite):
        qWarning("Cannot start more than one instance of eKalappai any time.")
        exit(0)
    splashImage = QPixmap(':intro/splash_screen')
    splashScreen = QSplashScreen(splashImage)
    splashScreen.show()
    time.sleep(2)
    splashScreen.hide()
    QApplication.setQuitOnLastWindowClosed(False)
    ekWindow = EkWindow()
    sys.exit(app.exec_())
