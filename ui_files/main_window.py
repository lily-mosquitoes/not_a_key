# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1088, 714)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.coupletLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coupletLabel.sizePolicy().hasHeightForWidth())
        self.coupletLabel.setSizePolicy(sizePolicy)
        self.coupletLabel.setMinimumSize(QtCore.QSize(30, 20))
        self.coupletLabel.setObjectName("coupletLabel")
        self.verticalLayout.addWidget(self.coupletLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButtonZero = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonZero.setMinimumSize(QtCore.QSize(10, 10))
        self.radioButtonZero.setChecked(True)
        self.radioButtonZero.setObjectName("radioButtonZero")
        self.horizontalLayout_3.addWidget(self.radioButtonZero)
        self.zeroTextLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroTextLabel.sizePolicy().hasHeightForWidth())
        self.zeroTextLabel.setSizePolicy(sizePolicy)
        self.zeroTextLabel.setMinimumSize(QtCore.QSize(20, 30))
        self.zeroTextLabel.setSizeIncrement(QtCore.QSize(0, 0))
        self.zeroTextLabel.setWordWrap(True)
        self.zeroTextLabel.setObjectName("zeroTextLabel")
        self.horizontalLayout_3.addWidget(self.zeroTextLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.zeroPicBackButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroPicBackButton.sizePolicy().hasHeightForWidth())
        self.zeroPicBackButton.setSizePolicy(sizePolicy)
        self.zeroPicBackButton.setMinimumSize(QtCore.QSize(20, 60))
        self.zeroPicBackButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.zeroPicBackButton.setObjectName("zeroPicBackButton")
        self.horizontalLayout_5.addWidget(self.zeroPicBackButton)
        self.zeroPicLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroPicLabel.sizePolicy().hasHeightForWidth())
        self.zeroPicLabel.setSizePolicy(sizePolicy)
        self.zeroPicLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.zeroPicLabel.setObjectName("zeroPicLabel")
        self.horizontalLayout_5.addWidget(self.zeroPicLabel)
        self.zeroPicForwdButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zeroPicForwdButton.sizePolicy().hasHeightForWidth())
        self.zeroPicForwdButton.setSizePolicy(sizePolicy)
        self.zeroPicForwdButton.setMinimumSize(QtCore.QSize(20, 60))
        self.zeroPicForwdButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.zeroPicForwdButton.setObjectName("zeroPicForwdButton")
        self.horizontalLayout_5.addWidget(self.zeroPicForwdButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButtonOne = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButtonOne.setMinimumSize(QtCore.QSize(10, 10))
        self.radioButtonOne.setObjectName("radioButtonOne")
        self.horizontalLayout_2.addWidget(self.radioButtonOne)
        self.oneTextLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oneTextLabel.sizePolicy().hasHeightForWidth())
        self.oneTextLabel.setSizePolicy(sizePolicy)
        self.oneTextLabel.setMinimumSize(QtCore.QSize(20, 30))
        self.oneTextLabel.setWordWrap(True)
        self.oneTextLabel.setObjectName("oneTextLabel")
        self.horizontalLayout_2.addWidget(self.oneTextLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.onePicBackButton = QtWidgets.QPushButton(self.centralwidget)
        self.onePicBackButton.setMinimumSize(QtCore.QSize(20, 60))
        self.onePicBackButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.onePicBackButton.setObjectName("onePicBackButton")
        self.horizontalLayout_6.addWidget(self.onePicBackButton)
        self.onePicLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.onePicLabel.sizePolicy().hasHeightForWidth())
        self.onePicLabel.setSizePolicy(sizePolicy)
        self.onePicLabel.setObjectName("onePicLabel")
        self.horizontalLayout_6.addWidget(self.onePicLabel)
        self.onePicForwdButton = QtWidgets.QPushButton(self.centralwidget)
        self.onePicForwdButton.setMinimumSize(QtCore.QSize(20, 60))
        self.onePicForwdButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.onePicForwdButton.setObjectName("onePicForwdButton")
        self.horizontalLayout_6.addWidget(self.onePicForwdButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setEnabled(False)
        self.backButton.setMinimumSize(QtCore.QSize(10, 70))
        self.backButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.backButton.setBaseSize(QtCore.QSize(0, 0))
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_4.addWidget(self.backButton)
        self.chooseButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chooseButton.sizePolicy().hasHeightForWidth())
        self.chooseButton.setSizePolicy(sizePolicy)
        self.chooseButton.setMinimumSize(QtCore.QSize(20, 70))
        self.chooseButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.chooseButton.setBaseSize(QtCore.QSize(0, 0))
        self.chooseButton.setObjectName("chooseButton")
        self.horizontalLayout_4.addWidget(self.chooseButton)
        self.skipButton = QtWidgets.QPushButton(self.centralwidget)
        self.skipButton.setEnabled(False)
        self.skipButton.setMinimumSize(QtCore.QSize(10, 70))
        self.skipButton.setObjectName("skipButton")
        self.horizontalLayout_4.addWidget(self.skipButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.locationHeaderLabel = QtWidgets.QLabel(self.centralwidget)
        self.locationHeaderLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.locationHeaderLabel.setObjectName("locationHeaderLabel")
        self.verticalLayout_2.addWidget(self.locationHeaderLabel)
        self.locationTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.locationTextLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.locationTextLabel.setObjectName("locationTextLabel")
        self.verticalLayout_2.addWidget(self.locationTextLabel)
        self.sortHeaderLabel = QtWidgets.QLabel(self.centralwidget)
        self.sortHeaderLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sortHeaderLabel.setObjectName("sortHeaderLabel")
        self.verticalLayout_2.addWidget(self.sortHeaderLabel)
        self.sortTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.sortTextLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sortTextLabel.setObjectName("sortTextLabel")
        self.verticalLayout_2.addWidget(self.sortTextLabel)
        self.sortTextLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.sortTextLabel2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sortTextLabel2.setObjectName("sortTextLabel2")
        self.verticalLayout_2.addWidget(self.sortTextLabel2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.possibleLabel = QtWidgets.QLabel(self.centralwidget)
        self.possibleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.possibleLabel.setObjectName("possibleLabel")
        self.verticalLayout_2.addWidget(self.possibleLabel)
        self.possibleList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.possibleList.sizePolicy().hasHeightForWidth())
        self.possibleList.setSizePolicy(sizePolicy)
        self.possibleList.setMinimumSize(QtCore.QSize(400, 0))
        self.possibleList.setObjectName("possibleList")
        self.verticalLayout_2.addWidget(self.possibleList)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.mistakenLabel = QtWidgets.QLabel(self.centralwidget)
        self.mistakenLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mistakenLabel.setObjectName("mistakenLabel")
        self.verticalLayout_2.addWidget(self.mistakenLabel)
        self.mistakenList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mistakenList.sizePolicy().hasHeightForWidth())
        self.mistakenList.setSizePolicy(sizePolicy)
        self.mistakenList.setMinimumSize(QtCore.QSize(400, 0))
        self.mistakenList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mistakenList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mistakenList.setResizeMode(QtWidgets.QListView.Fixed)
        self.mistakenList.setObjectName("mistakenList")
        self.verticalLayout_2.addWidget(self.mistakenList)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.impossibleLabel = QtWidgets.QLabel(self.centralwidget)
        self.impossibleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.impossibleLabel.setObjectName("impossibleLabel")
        self.verticalLayout_2.addWidget(self.impossibleLabel)
        self.impossibleList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.impossibleList.sizePolicy().hasHeightForWidth())
        self.impossibleList.setSizePolicy(sizePolicy)
        self.impossibleList.setMinimumSize(QtCore.QSize(400, 0))
        self.impossibleList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.impossibleList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.impossibleList.setObjectName("impossibleList")
        self.verticalLayout_2.addWidget(self.impossibleList)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1088, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuActions = QtWidgets.QMenu(self.menuBar)
        self.menuActions.setObjectName("menuActions")
        MainWindow.setMenuBar(self.menuBar)
        self.actionLaunchFilterWindow = QtWidgets.QAction(MainWindow)
        self.actionLaunchFilterWindow.setObjectName("actionLaunchFilterWindow")
        self.menuActions.addAction(self.actionLaunchFilterWindow)
        self.menuBar.addAction(self.menuActions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Not a Key"))
        self.coupletLabel.setText(_translate("MainWindow", "TextLabel"))
        self.radioButtonZero.setText(_translate("MainWindow", "0."))
        self.zeroTextLabel.setText(_translate("MainWindow", "TextLabel"))
        self.zeroPicBackButton.setText(_translate("MainWindow", "<<"))
        self.zeroPicLabel.setText(_translate("MainWindow", "TextLabel"))
        self.zeroPicForwdButton.setText(_translate("MainWindow", ">>"))
        self.radioButtonOne.setText(_translate("MainWindow", "1."))
        self.oneTextLabel.setText(_translate("MainWindow", "TextLabel"))
        self.onePicBackButton.setText(_translate("MainWindow", "<<"))
        self.onePicLabel.setText(_translate("MainWindow", "TextLabel"))
        self.onePicForwdButton.setText(_translate("MainWindow", ">>"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.chooseButton.setText(_translate("MainWindow", "Choose"))
        self.skipButton.setText(_translate("MainWindow", "Skip"))
        self.locationHeaderLabel.setText(_translate("MainWindow", "Chosen location:"))
        self.locationTextLabel.setText(_translate("MainWindow", "TextLabel"))
        self.sortHeaderLabel.setText(_translate("MainWindow", "Sorting by:"))
        self.sortTextLabel.setText(_translate("MainWindow", "TextLabel"))
        self.sortTextLabel2.setText(_translate("MainWindow", "TextLabel"))
        self.possibleLabel.setText(_translate("MainWindow", "Possible species:"))
        self.mistakenLabel.setText(_translate("MainWindow", "Possible, if mistaken:"))
        self.impossibleLabel.setText(_translate("MainWindow", "Impossible species:"))
        self.menuActions.setTitle(_translate("MainWindow", "Actions"))
        self.actionLaunchFilterWindow.setText(_translate("MainWindow", "Launch Filter Window"))

