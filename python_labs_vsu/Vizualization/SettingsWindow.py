import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *


class SettingsWindow(QtWidgets.QWidget):
    def __init__(self, parent=None, callback=None):
        # Передаём ссылку на родительский элемент и чтобы виджет
        # отображался как самостоятельное окно указываем тип окна
        super().__init__(parent, QtCore.Qt.Window)
        self.build()
        self.callbackFunction = callback


    def build(self):
        layout = QGridLayout()
        self.setLayout(layout)
        self.listwidget = QListWidget()
        self.listwidget.insertItem(0, "Три цвета")
        self.listwidget.insertItem(1, "Четыре цвета")
        self.listwidget.insertItem(2, "Пять цветов")
        self.listwidget.clicked.connect(self.list_clicked)
        layout.addWidget(self.listwidget)
        self.mainLayout = QtWidgets.QVBoxLayout()

    def list_clicked(self, qmodelindex):
        item = self.listwidget.currentIndex().row() + 3
        if self.callbackFunction:
            self.callbackFunction(item)