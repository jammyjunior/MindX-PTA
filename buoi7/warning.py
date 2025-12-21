import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)
msg_box = QMessageBox()
msg_box.setWindowTitle("404 Not Found!")
msg_box.setIcon(QMessageBox.Icon.Warning)
msg_box.setText("Can't connect to the world")
msg_box.setStyleSheet("background-color: white; color: red")
sys.exit(msg_box.exec())