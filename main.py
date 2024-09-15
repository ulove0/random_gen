from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from random import randint


app = QApplication([])
win = QWidget()

win.setWindowTitle("Моя програма")

win.resize(800,600)

text_1 = QLabel("Переможець:")
text_number = QLabel("?")

button = QPushButton("Згенерувати")

main_line = QVBoxLayout()

main_line.addWidget(text_1, alignment=Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(text_number, alignment=Qt.AlignmentFlag.AlignCenter)
main_line.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

win.setLayout(main_line)


def click():
    rand_number = randint(1,100)
    text_number.setText(str(rand_number))

button.clicked.connect(click)


win.show()
app.exec()