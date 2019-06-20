import sys
from PyQt5 import QtGui, QtCore, QtWidgets

# ЦВЕТА ПОЛЕЙ
sss_vivod = ("background-color: #456173; color: #f2f2f0; font: 14pt 'Courier New'")


# ГРАФИКА
class RulesWindow(QtWidgets.QWidget):  # Класс Window  наследует класс QWidget
    def __init__(self, parent=None):  # Создаёт конструктор класса, parent - ссылка на родительский эл-т
        #QtWidgets.QWidget.__init__(self, parent)
        super().__init__(parent, QtCore.Qt.Window)
        self.resize(500, 400)
        self.vbox = QtWidgets.QVBoxLayout()
        #         # ---
        self.pole_vivod = QtWidgets.QTextEdit('')
        self.pole_vivod.setStyleSheet(sss_vivod)
        self.vbox.addWidget(self.pole_vivod)
        # ---
        self.setLayout(self.vbox)
        # ---
        RulesWindow.on_start(self)

    # ЛОГИКА

    def on_start(self):
        i = '<h1>Правила игры</h1><p>Игрок должен соединить как можно больше элементов одинакового цвета в одну строку или линию. Строка или линия длиной от трёх элементов одинакового цвета автоматически уничтожается</p>'
        self.pole_vivod.append(str(i))
        self.pole_vivod.moveCursor(QtGui.QTextCursor.Start)