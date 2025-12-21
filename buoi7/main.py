import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.load_ui(r"/home/jammy/code/python/MindX-PTA/buoi7/ui/login.ui", self)
        self.registerButton.clicked.connect(self.register)
        self.loginButton.clicked.connect(self.isLoginValid)
        self.messageBox = QMessageBox()

    def isLoginValid(self):
        inputUsername = self.usernameInput().text()
        inputPassword = self.passwordInput().text()
        if inputUsername == "admin" and inputPassword == "admin":
            main.show()
            self.close()

    def register(self):
        pass