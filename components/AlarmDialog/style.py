from PyQt5 import QtCore, QtGui, QtWidgets


# Стиль диалогового окна
class Ui_Dialog(object):
    # Инициализировать стиль
    def setupUi(self, Dialog, title, time):
        # Создать окно с размерами 370x188px
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 188)
        # Создать заголовок с размерами 371x41px и положением (0, 0)
        self.label_header = QtWidgets.QLabel(Dialog)
        self.label_header.setGeometry(QtCore.QRect(0, 0, 371, 41))
        # Установить шрифт размером 15px
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
        # Создать кнопку с размерами 101x31px и положением (260, 150)
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(260, 150, 101, 31))
        # Установить шрифт размером 16px
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnOk.setFont(font)
        self.btnOk.setObjectName("btnOk")
        # Создать строку информации о будильнике с размерами 371x41px и положением (0, 40)
        self.label_signature_alarm = QtWidgets.QLabel(Dialog)
        self.label_signature_alarm.setGeometry(QtCore.QRect(0, 40, 371, 41))
        # Установить шрифт размером 12px
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_signature_alarm.setFont(font)
        self.label_signature_alarm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_signature_alarm.setObjectName("label_signature_alarm")
        # Создать строку отображения времени с размерами 371x61px и положением (0, 80)
        self.label_time = QtWidgets.QLabel(Dialog)
        self.label_time.setGeometry(QtCore.QRect(0, 80, 371, 61))
        # Установить шрифт размером 20px
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")

        self.retranslateUi(Dialog, title, time)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # Переименование стилей
    def retranslateUi(self, Dialog, title, time):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_header.setText(_translate("Dialog", "Будильник"))
        self.btnOk.setText(_translate("Dialog", "ок"))
        self.label_signature_alarm.setText(_translate("Dialog", title))
        self.label_time.setText(_translate("Dialog", time))
