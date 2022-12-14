# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converterui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(329, 378)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(329, 378))
        MainWindow.setMaximumSize(QtCore.QSize(329, 378))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 303))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chooseFileButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.horizontalLayout.addWidget(self.chooseFileButton)
        self.chooseFileEditText = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.chooseFileEditText.setReadOnly(True)
        self.chooseFileEditText.setObjectName("chooseFileEditText")
        self.horizontalLayout.addWidget(self.chooseFileEditText)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_4.addWidget(self.saveButton)
        self.fileSavePathEditText = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.fileSavePathEditText.setReadOnly(True)
        self.fileSavePathEditText.setObjectName("fileSavePathEditText")
        self.horizontalLayout_4.addWidget(self.fileSavePathEditText)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.fpsSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.fpsSpinBox.setMinimum(1)
        self.fpsSpinBox.setProperty("value", 5)
        self.fpsSpinBox.setObjectName("fpsSpinBox")
        self.horizontalLayout_2.addWidget(self.fpsSpinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.setStretch(2, 7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.convertButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.convertButton.setObjectName("convertButton")
        self.verticalLayout.addWidget(self.convertButton)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.numberOfFilesLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.numberOfFilesLabel.setObjectName("numberOfFilesLabel")
        self.horizontalLayout_3.addWidget(self.numberOfFilesLabel)
        self.label2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label2.setObjectName("label2")
        self.horizontalLayout_3.addWidget(self.label2)
        self.progressLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.progressLabel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.progressLabel.setObjectName("progressLabel")
        self.horizontalLayout_3.addWidget(self.progressLabel)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 5)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 329, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video to GIF"))
        self.chooseFileButton.setText(_translate("MainWindow", "Choose A File"))
        self.chooseFileEditText.setPlaceholderText(_translate("MainWindow", "File path"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.fileSavePathEditText.setPlaceholderText(_translate("MainWindow", "File save path"))
        self.label_2.setText(_translate("MainWindow", "FPS:"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))
        self.label.setText(_translate("MainWindow", "Current:"))
        self.numberOfFilesLabel.setText(_translate("MainWindow", "(0/0)"))
        self.label2.setText(_translate("MainWindow", "Progress:"))
        self.progressLabel.setText(_translate("MainWindow", "0%"))
