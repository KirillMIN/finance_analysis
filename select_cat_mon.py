# Внесение денег и категорий в базу данных
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import  QRegExp
import shelve
import matplotlib.pyplot as pl
from time import sleep



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # надпись категория
        """
        self.label = QtWidgets.QLabel("<center>Привет, мир!</center>")
        self.label.setGeometry(QtCore.QRect(40, 40, 181, 41))
        """
        # надпись деньги
        """
        self.label = QtWidgets.QLabel("<center>Привет, мир!</center>")
        self.label.setGeometry(QtCore.QRect(40, 40, 181, 41))
        """
        # надпись денег потрачено
        self.sum_m = QtWidgets.QLabel(self.centralwidget)
        self.sum_m.setGeometry(QtCore.QRect(300, 50, 500, 500))
        self.sum_m.setObjectName("lineEdit")
        # график
        self.grap = QtWidgets.QLabel(self.centralwidget)
        self.grap.setGeometry(QtCore.QRect(300, 200, 500, 500))
        self.grap.setObjectName("grap")
        # внести  категорию
        category_range = "[a-zA-Zа-яА-ЯёЁ]{,100}"  # Часть регулярного выржение
        # Само регулярное выражение
        reg_ex = QRegExp("^" + category_range + "$")
        self.category = QtWidgets.QLineEdit(self.centralwidget)
        self.category.setGeometry(QtCore.QRect(40, 40, 181, 41))
        self.category.setObjectName("category")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.category)
        self.category.setValidator(input_validator)
        # кнопка внести
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 110, 121, 41))
        self.pushButton.setObjectName("pushButton")
        # внести деньги
        money_range = "\d{,10}"  # Часть регулярного выржение
        # Само регулярное выражение
        reg_ex = QRegExp("^" + money_range + "\\." + money_range + "$")
        self.money = QtWidgets.QLineEdit(self.centralwidget)
        self.money.setGeometry(QtCore.QRect(40, 100, 181, 31))
        self.money.setObjectName("money")
        input_validator = QtGui.QRegExpValidator(reg_ex, self.money)
        self.money.setValidator(input_validator)
        # внести меню
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        # внести статус меню
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # создание нажимания на кнопки
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.data_values)
        self.pushButton.clicked.connect(self.print_data_values)
        self.pushButton.clicked.connect(self.sum_data_money)
        self.pushButton.clicked.connect(self.category.clear)
        self.pushButton.clicked.connect(self.money.clear)
        self.pushButton.clicked.connect(self.sum_m.show)
        self.pushButton.clicked.connect(self.get_graph)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # появление ui

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Insert"))
    """
    def data_values(self):
        money_value = float(self.money.text())
        category_value = self.category.text()
        if category_value not in mini_data_structure.keys():
            mini_data_structure.update({category_value: money_value})
        else:
            mini_data_structure[category_value] += money_value
        for keys, values in mini_data_structure.items():
            print(keys, values)
    """

    # текущий счет
    # внесение данных
    def data_values(self):
        money_value = float(self.money.text())
        category_value = self.category.text()
        with shelve.open("data_base") as data:
            if category_value not in data:
                data[category_value] = money_value
            else:
                data[category_value] += money_value

    def sum_data_money(self):
        result = 0
        with shelve.open("data_base") as data:
            for keys, state in data.items():
                if state == max(data.values()):
                    max_category = keys
                result += state
            self.sum_m.setText(f'Денег потрачено: {str(result)}, максимальная категория:{max_category}')

    @staticmethod
    def print_data_values():
        with shelve.open("data_base") as data:
            for state in data.items():
                print(state)



    @staticmethod
    def clear_data_values():
        with shelve.open("data_base") as data:
            for state in data.items():
                del state

    # график потраченных денег
    def get_graph(self):
        with shelve.open("data_base") as data:
            pl.bar(data.keys(), data.values())
        self.grap.setText(pl.show())




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())