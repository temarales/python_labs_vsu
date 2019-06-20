import os

from Vizualization.MainWindowUI import Ui_MainWindow
from Game.Game import *
from Game.Color import *
from Vizualization.SettingsWindow import *
from Vizualization.RulesWindow import *
from Game.Point import *

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5 import QtSvg
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._game = Game(4, 10)
        #self.old_x = -1
        #self.old_y = -1
        self.old_point = Point(-1,-1)
        self.settings_window = None
        self.rules_window = None
        self.color_count = None

        self.setMinimumSize(QSize(700, 600))  # Устанавливаем размеры
        self.setWindowTitle("Игра несколько в ряд")  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет
        self._colorDictionary = {Color.NONE_COLOR:QtGui.QColor(192, 192, 192), Color.BLUE:QtGui.QColor(106, 92, 205), Color.GREEN:QtGui.QColor(34, 139, 34), Color.RED:QtGui.QColor(139, 0, 0), Color.YELLOW:QtGui.QColor(255, 255, 0), Color.PINK:QtGui.QColor(238, 130, 238)}

        self.grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(self.grid_layout)  # Устанавливаем данное размещение в центральный виджет

        self.buttonSettings = QtWidgets.QPushButton('Settings', self)
        self.buttonSettings.clicked.connect(self.open_settings_window)
        self.buttonSettings.move(550, 100)

        self.buttonRules = QtWidgets.QPushButton("Rules", self)
        self.buttonRules.clicked.connect(self.open_rules_window)
        self.buttonRules.move(550, 300)

        self._table = QTableWidget(self)  # Создаём таблицу
        self._table.setColumnCount(self._game.size)
        self._table.setRowCount(self._game.size)

        self.refresh_table()

        # делаем ресайз колонок по содержимому
        self._table.resizeColumnsToContents()
        self.grid_layout.addWidget(self._table, 0, 0)
        self._table.cellClicked.connect(self.row_column_clicked)

    def open_settings_window(self):
        if not self.settings_window:
            self.settings_window = SettingsWindow(self, self.paste_text)
        self.settings_window.show()

    def open_rules_window(self):
        if not self.rules_window:
            self.rules_window = RulesWindow(self)
        self.rules_window.show()

    def paste_text(self, value):
        self.color_count = int(value)
        self.start_new_game(self.color_count, 10)

    def row_column_clicked(self):
        new_point = Point(self._table.currentRow(), self._table.currentColumn())
        if self.old_point.getX == -1:
            self.old_point = new_point
        else:
            self._game.change_positions(new_point.getX, new_point.getY, self.old_point.getX, self.old_point.getY)
            self.old_point.setX(-1)
            self.old_point.setY(-1)
            self.refresh_table()
            self.clear_table()
            self.refresh_table()

    def start_new_game(self, color_count, size):
        self._game = Game(color_count, size)
        self.repaint()

    def refresh_table(self):
        for i in range(self._game.size):
            for j in range(self._game.size):
                self._table.setItem(i, j, QtWidgets.QTableWidgetItem())
                self._table.item(i, j).setBackground(self._colorDictionary[self._game.field.array[i][j].color])

    def clear_table(self):
        k = 0
        while (not k == self._game.size * 2):
            k = 0
            for i in range(self._game.size):
                column_begin, column_end = self._game.field.check_horizontal(i)
                if not column_end == -1:
                    self._game.field.delete_line(i, column_begin, i, column_end)
                    self.repaint()
                    time.sleep(.750)
                    self._game.field.move_elements(i, column_begin, i, column_end)
                    self.repaint()
                    time.sleep(.750)
                    self._game.field.fill_emptinesses()
                    self.repaint()
                    time.sleep(.750)
                else:
                    k += 1
            for i in range(self._game.size):
                row_begin, row_end = self._game.field.check_vertical(i)
                if not row_end == -1:
                    self._game.field.delete_line(row_begin, i, row_end, i)
                    self.repaint()
                    time.sleep(.750)
                    self._game.field.move_elements(row_begin, i, row_end, i)
                    self.repaint()
                    time.sleep(.750)
                    self._game.field.fill_emptinesses()
                    self.repaint()
                    time.sleep(.750)
                else:
                    k += 1
        time.sleep(.750)

    def paintEvent(self, event):
        k = 0
        self.refresh_table()