from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt6 import uic
import sys 

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"/home/jammy/code/python/MindX-PTA/buoi8/hoang/login.ui", self)
        self.registerButton.clicked.connect(self.show_register)
        self.loginButton.clicked.connect(self.check_login)
        self.msg_box = QMessageBox()

    def check_login(self):
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        if email == "1" and password == "1":
            main.show()
            self.close()
        else:
            self.msg_box.setText("Vui lòng nhập kiểm tra lại thông tin đăng nhập")
            self.msg_box.setIcon(QMessageBox.Icon.Warning)
            self.msg_box.exec()
        
    def show_register(self):
        register.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"/home/jammy/code/python/MindX-PTA/buoi8/hoang/register.ui", self)
        self.btnLogin.clicked.connect(self.show_login)
        self.msg_box = QMessageBox()

    def show_login(self):
        login.show()
        self.close()

class Main(QMainWindow):
    def __init__(self) :
        super().__init__()
        uic.loadUi(r"/home/jammy/code/python/MindX-PTA/buoi8/hoang/main.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    register = Register()
    main = Main()
    app.exec()
