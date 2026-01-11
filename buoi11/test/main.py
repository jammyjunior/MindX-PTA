from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt6 import uic
import webbrowser
import sys 

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"/home/jammy/code/python/MindX-PTA/buoi11/ui/login.ui", self)
        self.registerSwitch.clicked.connect(self.showRegister)
        self.loginButton.clicked.connect(self.checkLogin)
        self.msg_box = QMessageBox()

    def checkLogin(self):
        usernameInput = self.usernameInput.text()
        passwordInput = self.passwordInput.text()
        robotCheck = self.robotBox.isChecked()
        if not robotCheck:
            self.msg_box.setText("Error! Please confirm you are not a robot!")
            self.msg_box.setIcon(QMessageBox.Icon.Warning)
            self.msg_box.exec()
        elif usernameInput != "admin" or passwordInput != "admin":
            self.msg_box.setText("Error! Wrong username or password!")
            self.msg_box.setIcon(QMessageBox.Icon.Warning)
            self.msg_box.exec()
        else:
            main.show()
            self.close()
    def showRegister(self):
        register.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"/home/jammy/code/python/MindX-PTA/buoi11/ui/register.ui", self)
        self.loginSwitch.clicked.connect(self.show_login)
        self.registerButton.clicked.connect(self.checkRegister)
        self.msg_box = QMessageBox()

    def checkRegister(self):
        usernameInput = self.usernameInput.text()
        passwordInput = self.passwordInput.text()
        robotCheck = self.robotBox.isChecked()
        agreeCheck = self.agreeBox.isChecked()
        
        if usernameInput == "" or passwordInput == "":
            self.msg_box.setText("Username or password must not be empty!")
            self.msg_box.setIcon(QMessageBox.Icon.Warning)
            self.msg_box.exec()
        elif not robotCheck or not agreeCheck:
            self.msg_box.setText("Check the box please!")
            self.msg_box.setIcon(QMessageBox.Icon.Warning)
            self.msg_box.exec()
        else:
            login.show()
            self.close()


    def show_login(self):
        login.show()
        self.close()

class Main(QMainWindow):
    def __init__(self) :
        super().__init__()
        uic.loadUi(r"/home/jammy/code/python/MindX-PTA/buoi11/ui/main.ui", self)
        self.imagineSpotify.clicked.connect(self.imagineSpotify)
        self.imagineYoutube.clicked.connect(self.imagineYoutube)
        self.coldplaySpotify.clicked.connect(self.coldplaySpotify)
        self.coldplayYoutube.clicked.connect(self.coldplayYoutube)
        self.glassSpotify.clicked.connect(self.glassSpotify)
        self.glassYoutube.clicked.connect(self.glassYoutube)


    def imagineSpotify(self):
        webbrowser.open("https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q")

    def imagineYoutube(self):
        webbrowser.open("https://www.youtube.com/channel/UCT9zcQNlyht7fRlcjmflRSA")

    def coldplaySpotify(self):
        webbrowser.open("https://www.youtube.com/channel/UCT9zcQNlyht7fRlcjmflRSA")

    def coldplayYoutube(self):
        webbrowser.open("https://www.youtube.com/channel/UCT9zcQNlyht7fRlcjmflRSA")

    def glassSpotify(self):
        webbrowser.open("https://www.youtube.com/channel/UCT9zcQNlyht7fRlcjmflRSA")

    def glassYoutube(self):
        webbrowser.open("https://www.youtube.com/channel/UCT9zcQNlyht7fRlcjmflRSA")

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    register = Register()
    main = Main()
    app.exec()



def greet(name):
    print("hello", name)

alex = greet("alex")
