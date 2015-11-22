from PyQt5.Qt import QSystemTrayIcon, QIcon, QAction, QDialog, QMenu
from PyQt5.QtGui import QPixmap
from view import dialog_ui
from database import DatabaseManager


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
        self.database = DatabaseManager()
        self.shortcut_key = self.database.get_shortcut_key()
        self.populate_modifier_cbox()

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
        self.modifier_cbox.currentIndexChanged.connect(self.populate_shortcut_key)
        self.shortcut_key_cbox.currentIndexChanged.connect(self.save_shortcut_key)

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

    def populate_modifier_cbox(self):
        self.modifier_cbox.blockSignals(True)
        modifiers = self.database.get_keys()
        for modifier in modifiers:
            self.modifier_cbox.addItem(modifier.name, modifier.id)
            if modifier.id == self.shortcut_key.parent.id:
                self.modifier_cbox.setCurrentText(modifier.name)
        self.populate_shortcut_key()
        self.modifier_cbox.blockSignals(False)

    def populate_shortcut_key(self):
        self.shortcut_key_cbox.blockSignals(True)
        self.shortcut_key_cbox.clear()
        keys = self.database.get_keys(self.modifier_cbox.currentData())
        for key in keys:
            self.shortcut_key_cbox.addItem(key.name, key.id)
            if key.id == self.shortcut_key.id:
                self.shortcut_key_cbox.setCurrentText(key.name)
        self.shortcut_key_cbox.blockSignals(False)
        self.save_shortcut_key()

    def save_shortcut_key(self):
        self.database.set_shortcut_key(self.shortcut_key_cbox.currentData())
        self.shortcut_key = self.database.get_shortcut_key()
