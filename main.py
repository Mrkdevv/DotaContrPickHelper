import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLineEdit
import sqlite3

connection = sqlite3.connect('dota.db')
cursor = connection.cursor()

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

        label_font = QFont("Arial", 20)
        label_font.setBold(True)
        font.setItalic(True)

        self.label = QLabel(self)
        self.label.setGeometry(-10, 60, 300, 200)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(label_font)

    def on_enter(self):
        text = self.input.text().capitalize()

        cursor.execute("SELECT id from HEROES WHERE name = ?", (text,))
        hero = cursor.fetchone()

        if hero:
            hero_id = hero[0]
            cursor.execute("SELECT first, second, third from Counterpicks WHERE hero_id = ?", (hero_id,))
            counterpicks = cursor.fetchone()
            self.label.setText(f"1) {counterpicks[0]}\n 2) {counterpicks[1]}\n 3) {counterpicks[2]}\n")


        else:
            print("Hero not found")


app = QApplication(sys.argv)

window = main_window_to_write_hero()
window.show()

app.exec()

