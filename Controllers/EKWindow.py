from PyQt5.Qt import QSystemTrayIcon, QIcon, QAction, QDialog, QMenu, qApp, QFileDialog
from PyQt5.QtGui import QPixmap
from view import dialog_ui
from database import DatabaseManager
from EkEngine import Engine

import win32api
import win32con


class EKWindow(QDialog, dialog_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.engine = Engine("tables/Tamil-bamini.txt.in")
        self.minimize_action = QAction("Minimize", self)
        self.maximize_action = QAction("Maximize", self)
        self.settings_action = QAction("Settings", self)
        self.about_action = QAction("About", self)
        self.quit_action = QAction("Quit", self)
        self.tray_icon_menu = QMenu(self)
        self.tray_icon = QSystemTrayIcon(self)
        self.setupUi(self)
        self.icon = QIcon(QPixmap(":icon/off_logo"))
        self.construct_tray_icon()
        self.signal_connectors()
        self.database = DatabaseManager()
        self.shortcut_key = self.database.get_shortcut_key()
        self.populate_modifier_cbox()
        if self.database.get_current_state() == "True":
            self.engine.conv_state = False
        else:
            self.engine.conv_state = True
        self.icon_activated(QSystemTrayIcon.Trigger)
        self.file_path_tview.setEnabled(False)

    def construct_tray_icon(self):
        self.tray_icon.setIcon(self.icon)
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
        self.browse_button.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        self.file_path_tview.setText(QFileDialog.getOpenFileName(file_dialog,
                                                                 str("Open Image"),
                                                                 "",
                                                                 str("Scim Tables (*.in *.txt)"))[0])

    def show_about(self):
        pass

    def quit(self):
        self.engine.un_hook()
        win32api.PostThreadMessage(win32api.GetCurrentThreadId(), win32con.WM_QUIT, 0, 0)
        self.exit(0)

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
        self.register_shortcut_listener()

    def register_shortcut_listener(self):
        self.engine.event_queue.remove_all()
        if self.shortcut_key.parent.name == "NONE":
            self.engine.event_queue.register_event(
                [
                    [self.shortcut_key.name],
                    self.icon_activated,
                    QSystemTrayIcon.Trigger
                ]
            )
        elif self.shortcut_key.parent.name == "CTRL":
            self.engine.event_queue.register_event(
                [
                    ['Lcontrol', self.shortcut_key.name],
                    self.icon_activated,
                    QSystemTrayIcon.Trigger
                ]
            )
            self.engine.event_queue.register_event(
                [
                    ['Rcontrol', self.shortcut_key.name],
                    self.icon_activated,
                    QSystemTrayIcon.Trigger
                ]
            )
        elif self.shortcut_key.parent.name == "ALT":
            self.engine.event_queue.register_event(
                [
                    ['LMenu', self.shortcut_key.name],
                    self.icon_activated,
                    QSystemTrayIcon.Trigger
                ]
            )
            self.engine.event_queue.register_event(
                [
                    ['RMenu', self.shortcut_key.name],
                    self.icon_activated,
                    QSystemTrayIcon.Trigger
                ]
            )
        return True

    def change_status(self):
        self.engine.conv_state = not self.engine.conv_state
        self.database.set_current_state(self.engine.conv_state)
        if self.engine.conv_state:
            self.show_on_status()
        else:
            self.show_off_status()

    def icon_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            pass
        elif reason == QSystemTrayIcon.Trigger:
            self.change_status()
        elif reason == QSystemTrayIcon.MiddleClick:
            pass
        else:
            pass

    def show_on_status(self):
        self.icon = QIcon(QPixmap(":icon/on_logo"))
        self.change_icons()

    def show_off_status(self):
        self.icon = QIcon(QPixmap(":icon/off_logo"))
        self.change_icons()

    def change_icons(self):
        self.tray_icon.setIcon(self.icon)
        self.setWindowIcon(self.icon)
        # TODO : Need to implement this method with current keyboard name
        self.tray_icon.setToolTip("Keyboard Name")
        self.show_tray_message()

    def show_tray_message(self):
        if self.engine.conv_state:
            message = "Ekalappai is Switched ON"
        else:
            message = "Ekalappai is Switched OFF"
        self.tray_icon.showMessage(
            qApp.applicationName() + " " + qApp.applicationVersion(),
            message,
            QSystemTrayIcon.MessageIcon(0),
            100
        )
