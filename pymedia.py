from PyQt6.QtWidgets import  QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSlider

import sys
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Media Player")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('play.png'))

        self.show()

def init_ui(self):


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

