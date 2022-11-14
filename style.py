from PyQt5 import QtCore, QtGui, QtWidgets

from components.Clock.Clock import Clock


# Шаблон MainWindow
class Ui_MainWindow(object):
    # Инициализировать стиль
    def setupUi(self, MainWindow):
        # Создать окно с размерами 1058x902px
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 902)
        MainWindow.setStyleSheet("")
        # Создать центральный виджет
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: #E9E9E9;")
        self.centralwidget.setObjectName("centralwidget")
        # Создать часы с размерами 400x400px и положением (560, 240)
        self.clock_widget = Clock(self.centralwidget)
        self.clock_widget.setGeometry(QtCore.QRect(560, 240, 400, 400))
        self.clock_widget.setObjectName("clock_widget")
        # Создать контейнер для будильников с размерами 350x680px и положением (110, 140)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 140, 350, 680))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        # Создать вертикальный слой с размерами 351x681px и положением (0, 0)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 351, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        # Создать кнопку сброса
        self.reset_btn = QtWidgets.QPushButton(MainWindow)
        self.reset_btn.setGeometry(QtCore.QRect(720, 730, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.reset_btn.setFont(font)
        self.reset_btn.setObjectName("btn_ok")
        # Вертикальная направляющая внутри контейнера
        self.alarms_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.alarms_layout.setContentsMargins(0, 0, 0, 0)
        self.alarms_layout.setSpacing(20)
        self.alarms_layout.setObjectName("alarms_layout")
        # Создать  с размерами 80x40px и положением (720, 180)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(720, 180, 80, 40))
        # Установить шрифт размером 20px
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        # Установить значение +-12
        self.spinBox.setMinimum(-12)
        self.spinBox.setMaximum(12)
        self.spinBox.setObjectName("spinBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Переименование стилей
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Будильник"))
        self.reset_btn.setText(_translate("MainWindow", "сброс"))
