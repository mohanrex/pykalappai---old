# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(404, 300)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stacked_widget = QtWidgets.QStackedWidget(Dialog)
        self.stacked_widget.setObjectName("stacked_widget")
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setObjectName("settings_page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.settings_page)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.settings_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.keyboard_cbox = QtWidgets.QComboBox(self.groupBox)
        self.keyboard_cbox.setObjectName("keyboard_cbox")
        self.horizontalLayout_3.addWidget(self.keyboard_cbox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.add_new_button = QtWidgets.QPushButton(self.groupBox)
        self.add_new_button.setMinimumSize(QtCore.QSize(0, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/add_file_icon"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/icon/add_file_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_new_button.setIcon(icon)
        self.add_new_button.setObjectName("add_new_button")
        self.horizontalLayout_3.addWidget(self.add_new_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem2 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.settings_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.modifier_cbox = QtWidgets.QComboBox(self.groupBox_2)
        self.modifier_cbox.setObjectName("modifier_cbox")
        self.horizontalLayout.addWidget(self.modifier_cbox)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.shortcut_key_cbox = QtWidgets.QComboBox(self.groupBox_2)
        self.shortcut_key_cbox.setObjectName("shortcut_key_cbox")
        self.horizontalLayout.addWidget(self.shortcut_key_cbox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem4 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.settings_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_windows_check = QtWidgets.QCheckBox(self.groupBox_3)
        self.start_windows_check.setObjectName("start_windows_check")
        self.horizontalLayout_2.addWidget(self.start_windows_check)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.stacked_widget.addWidget(self.settings_page)
        self.keyboard_add_page = QtWidgets.QWidget()
        self.keyboard_add_page.setObjectName("keyboard_add_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.keyboard_add_page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.keyboard_add_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.file_path_tview = QtWidgets.QLineEdit(self.groupBox_4)
        self.file_path_tview.setStyleSheet("background-color : #F6F6F6;")
        self.file_path_tview.setReadOnly(True)
        self.file_path_tview.setObjectName("file_path_tview")
        self.gridLayout.addWidget(self.file_path_tview, 0, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 1)
        self.back_button = QtWidgets.QPushButton(self.groupBox_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/settings_icon"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.back_button.setIcon(icon1)
        self.back_button.setObjectName("back_button")
        self.gridLayout.addWidget(self.back_button, 2, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 5, 1, 1)
        self.browse_button = QtWidgets.QPushButton(self.groupBox_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/browse_icon"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.browse_button.setIcon(icon2)
        self.browse_button.setObjectName("browse_button")
        self.gridLayout.addWidget(self.browse_button, 0, 4, 1, 1)
        self.clear_button = QtWidgets.QPushButton(self.groupBox_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/clear_icon"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.clear_button.setIcon(icon3)
        self.clear_button.setObjectName("clear_button")
        self.gridLayout.addWidget(self.clear_button, 2, 2, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.groupBox_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/add_file_icon"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.add_button.setIcon(icon4)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 2, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 0, 0, 1, 1)
        self.error_msg = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.error_msg.setFont(font)
        self.error_msg.setText("")
        self.error_msg.setObjectName("error_msg")
        self.gridLayout.addWidget(self.error_msg, 1, 2, 1, 2)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.keyboard_add_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.keyboard_table = QtWidgets.QTableWidget(self.groupBox_5)
        self.keyboard_table.setObjectName("keyboard_table")
        self.keyboard_table.setColumnCount(0)
        self.keyboard_table.setRowCount(0)
        self.horizontalLayout_4.addWidget(self.keyboard_table)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.stacked_widget.addWidget(self.keyboard_add_page)
        self.verticalLayout_3.addWidget(self.stacked_widget)

        self.retranslateUi(Dialog)
        self.stacked_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Keyboards"))
        self.label.setText(_translate("Dialog", "Keyboard :"))
        self.add_new_button.setText(_translate("Dialog", "Add New"))
        self.groupBox_2.setTitle(_translate("Dialog", "Shortcut Settings"))
        self.label_2.setText(_translate("Dialog", "Modifier Key"))
        self.label_3.setText(_translate("Dialog", "Shortcut Key"))
        self.groupBox_3.setTitle(_translate("Dialog", "Other Settings"))
        self.start_windows_check.setText(_translate("Dialog", "Start eKalappai whenever Windows starts"))
        self.groupBox_4.setTitle(_translate("Dialog", "Add Keyboard"))
        self.file_path_tview.setPlaceholderText(_translate("Dialog", "Your Scim file path"))
        self.label_5.setText(_translate("Dialog", "Scim Table Path"))
        self.back_button.setText(_translate("Dialog", "Go Back"))
        self.browse_button.setText(_translate("Dialog", "Browse"))
        self.clear_button.setText(_translate("Dialog", "Clear"))
        self.add_button.setText(_translate("Dialog", "Add"))
        self.groupBox_5.setTitle(_translate("Dialog", "Remove Keyboards"))
