__author__ = 'Raj'

import os
import shutil
import time
import sys

from PyQt5.Qt import QSystemTrayIcon, qApp, QSettings, QGroupBox, QLabel, \
    QComboBox, QIcon, QHBoxLayout, QCheckBox, QAction, QDialog, QMenu, QVBoxLayout
from PyQt5.QtCore import qWarning
from PyQt5.QtGui import QPixmap

from resources import ekalappai_rc
from view import dialog_ui


class EKWindow(QDialog, dialog_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.minimize_action = QAction("Minimize", self)
        self.maximize_action = QAction("Maximize", self)
        self.settings_action = QAction("Settings", self)
        self.about_action = QAction("About", self)
        self.quit_action = QAction("Quit", self)
        self.tray_icon_menu = QMenu(self)
        self.tray_icon = QSystemTrayIcon(self)
        self.setupUi(self)
        self.construct_tray_icon()
        self.signal_connectors()

    def construct_tray_icon(self):
        self.tray_icon.setIcon(QIcon(QPixmap(":icon/logo")))
        self.tray_icon_menu.addAction(self.settings_action)
        self.tray_icon_menu.addSeparator()
        self.tray_icon_menu.addAction(self.about_action)
        self.tray_icon_menu.addSeparator()
        self.tray_icon_menu.addAction(self.quit_action)
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        self.tray_icon.show()

    def signal_connectors(self):
        self.settings_action.triggered.connect(self.show_setting)
        self.about_action.triggered.connect(self.show_about)
        self.quit_action.triggered.connect(self.quit)
        self.add_new_button.clicked.connect(self.change_dialog_index)
        self.back_button.clicked.connect(self.change_dialog_index)

    def show_about(self):
        pass

    def quit(self):
        self.engine.un_hook()
        exit(0)

    def show_setting(self):
        self.stacked_widget.setCurrentIndex(0)
        self.showNormal()

    def change_dialog_index(self):
        current_index = self.stacked_widget.currentIndex()
        if current_index == 0:
            self.stacked_widget.setCurrentIndex(1)
        else:
            self.stacked_widget.setCurrentIndex(0)
