import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 188)
        self.label_header = QtWidgets.QLabel(Dialog)
        self.label_header.setGeometry(QtCore.QRect(0, 0, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_header.setFont(font)
        self.label_header.setMouseTracking(False)
        self.label_header.setTabletTracking(False)
        self.label_header.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_header.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_header.setTextFormat(QtCore.Qt.AutoText)
        self.label_header.setScaledContents(False)
        self.label_header.setAlignment(QtCore.Qt.AlignCenter)
        self.label_header.setWordWrap(False)
        self.label_header.setIndent(-1)
        self.label_header.setOpenExternalLinks(True)
        self.label_header.setObjectName("label_header")
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(260, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")

        self.label_signature = QtWidgets.QLabel(Dialog)
        self.label_signature.setGeometry(QtCore.QRect(0, 40, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_signature.setFont(font)
        self.label_signature.setAlignment(QtCore.Qt.AlignCenter)
        self.label_signature.setObjectName("label_signature")
        self.label_time = QtWidgets.QLabel(Dialog)
        self.label_time.setGeometry(QtCore.QRect(0, 80, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")

        self.setStyleSheet("""
                        QDialog{
                            background: white;
                        }
                        Qbtn_ok{
                            border-radius: 6px;
                            background: white;
                        }
                        Qlabel_signature{
                            border-radius: 6px;
                        }   
                        """)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_header.setText(_translate("Dialog", "Будильник"))
        self.btn_ok.setText(_translate("Dialog", "ок"))
        self.label_signature.setText(_translate("Dialog", "TextLabel"))
        self.label_time.setText(_translate("Dialog", "00:00"))


