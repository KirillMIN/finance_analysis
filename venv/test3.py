from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.money = QLineEdit()
        self.category = QLineEdit()

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(QLabel('money'), 1, 0)
        layout.addWidget(self.money, 1, 1)
        value_sum = self.money.text()
        layout.addWidget(QLabel('category'), 10, 0)
        layout.addWidget(self.category, 1, 1)
        value_category = self.money.text()


        # def get_sum()



if __name__ == '__main__':
    app = QApplication([])

    mw = Window()
    mw.show()
    app.exec()