import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
from functools import partial
import keyword
import pyautogui
import time

"""def copyToclipboard(text):
    QGuiApplication.clipboard().setText(text)


class WorkerTheread(QThread):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def work(self):
        print("Working...")
    
    def run(self):
        print("Stared")
        self.timer = QThread()
        self.timer.timeout.connect(self.work)
        self.timer.start(100)"""


class MyWindow(QFrame):
    def __init__(self, title=None, icon=None):
        QFrame.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowState)
        self.setStyleSheet(
            '''padding: 0 0 0 0;
            border-spacing: 0px 0px;
            margin: 0px;'''
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QSizePolicy.Minimum,
            QSizePolicy.Maximum)
        self.setMaximumSize(1, 1)
        self.setSizePolicy(sizePolicy)

        self.res = QLabel('Screen:')
        self.res.setAlignment(Qt.AlignCenter)

        self.timeEdit = QLabel()
        frontSize = self.timeEdit.font().pointSize()
        fontFamily = self.timeEdit.font().family()
        self.timeEdit.setFont(QFont(fontFamily, 14, QFont.Bold))

        exitButton = QPushButton("Exit")
        exitButton.clicked.connect(self.exitEvent)

        verticalLayout = QVBoxLayout(self)
        verticalLayout.setContentsMargins(10, 10, 10, 10)
        verticalLayout.setSpacing(5)
        # verticalLayout.addWidget(self.res)
        verticalLayout.addWidget(self.timeEdit)
        verticalLayout.addWidget(exitButton)
        self.setLayout(verticalLayout)

        sizePolicy = QtWidgets.QSizePolicy(
            QSizePolicy.Minimum,
            QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.timeEdit.setSizePolicy(sizePolicy)
        self.timeEdit.setAlignment(Qt.AlignCenter)

