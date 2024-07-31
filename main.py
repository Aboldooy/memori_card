'''
Головний файл програми. Він запускає її, показує вікна
'''

from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

from app import app
from main_window import window_main


window = QWidget()
window_layout = QVBoxLayout()

window_layout.addWidget(window_main)

window.setLayout(window_layout)
window.show()
app.exec()