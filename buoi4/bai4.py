# class animals:
#     def __init__(self, name, age, typeAnimal, enviroment):
#         self.name = name
#         self.age = age
#         self.typeAnimal = typeAnimal
#         self.enviroment = enviroment

#     def info(self):
#         return f"""
#         Ten: {self.name}
#         Tuoi: {self.age}
#         Loai: {self.typeAnimal}
#         Song o: {self.liveIn}
#         """

#     def changeEnviroment(self, newEnviroment):
#         self.enviroment = newEnviroment

# Duck = animals("Donald", 5, "duck", "water")
# Duck.changeEnviroment("H20")
# print(Duck.info)


from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Click me")

button = QPushButton("Click me!", parent=window)
button.setGeometry(500, 500, 100, 30)
label = QLabel("Hello World! This is my first program!", parent=window)

window.show()
app.exec()