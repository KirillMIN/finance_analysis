from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.new_btn_text = QtWidgets.QLabel(self)
        self.setWindowTitle("financial")  # заголовок приложения
        self.setGeometry(200, 200, 800, 800)  # рамки приложения
        self.main_text = QtWidgets.QPlainTextEdit(self)
        self.main_text.setGeometry(50, 50, 300, 100)
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setGeometry(200, 200, 100, 50)
        self.btn.setText('insert')
        self.btn.setFixedWidth(300)
        self.btn.clicked.connect(self.btn_changer)

    def btn_changer(self):
        self.new_btn_text.setText("insert money")




def application(): # основная функция для запуска приложения
    app = QApplication(sys.argv)  # создание приложения
    window = Window() # создание окна приложения
    window.show()  # показ окна
    sys.exit(app.exec())  # корректный выход из приложения
"""
    window.setWindowTitle("financial") # заголовок приложения
    window.setGeometry(200, 200, 800, 800) # рамки приложения
    main_text = QtWidgets.QPlainTextEdit(window)
    main_text.setGeometry(50, 50, 300,100)
    btn = QtWidgets.QPushButton(window)
    btn.setGeometry(200, 200, 100,50)
    btn.setText('insert')
    btn.setFixedWidth(300)
    btn.clicked.connect(btn_changer)
    window.show() # показ окна
    sys.exit(app.exec()) # корректный выход из приложения
"""
if __name__ == "__main__":
    application()
