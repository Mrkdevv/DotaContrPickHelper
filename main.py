import sys

from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLineEdit


class main_window_to_write_hero(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HeroChoose")
        self.setWindowIcon(QIcon("logo.jpg"))
        self.setFixedSize(300, 300)
        self.setStyleSheet("background-color:white;") #change in the future

        # --

        self.input = QLineEdit(self)
        self.input.setFixedSize(300,50)
        self.input.setPlaceholderText("Enter hero name")
        self.input.setStyleSheet("background-color:black;")
        self.input.returnPressed.connect(self.on_enter)

        #--

        font = QFont("Arial", 18)
        font.setBold(True)
        font.setItalic(True)
        self.input.setFont(font)
        self.input.setStyleSheet("background-color: black; color: white;")

    def on_enter(self):
        text = self.input.text().capitalize()
        return text


app = QApplication(sys.argv)

window = main_window_to_write_hero()
window.show()

app.exec()

