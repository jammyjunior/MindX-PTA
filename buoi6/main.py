from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic
import sys

class Login(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"/home/jammy/code/python/MindX-PTA/buoi6/ui/login.ui", self)

class Register(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"/home/jammy/code/python/MindX-PTA/buoi6/ui/login.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    register = Login()
    register.show()
    app.exec()