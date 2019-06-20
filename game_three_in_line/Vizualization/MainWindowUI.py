from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QGridLayout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 540)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.resize(500, 500)
        self.gameFieldTableView = QtWidgets.QTableView(self.centralwidget)
        self.gameFieldTableView.setStyleSheet("QTableView {\n"
                                              "  background-color: silver;\n"
                                              "}")
        self.gameFieldTableView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameFieldTableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.gameFieldTableView.setObjectName("gameFieldTableView")
        self.gameFieldTableView.horizontalHeader().setVisible(False)
        self.gameFieldTableView.horizontalHeader().setDefaultSectionSize(30)
        self.gameFieldTableView.verticalHeader().setVisible(False)
        self.gameFieldTableView.resize(500, 500)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))