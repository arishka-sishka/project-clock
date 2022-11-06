from PyQt5 import QtCore, QtGui, QtWidgets

from components.Clock.Clock import Clock


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 902)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: #E9E9E9;")
        self.centralwidget.setObjectName("centralwidget")
        self.clock_widget = Clock(self.centralwidget)
        self.clock_widget.setGeometry(QtCore.QRect(560, 240, 400, 400))
        self.clock_widget.setObjectName("clock_widget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(110, 140, 350, 680))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 351, 681))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.alarms_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.alarms_layout.setContentsMargins(0, 0, 0, 0)
        self.alarms_layout.setSpacing(20)
        self.alarms_layout.setObjectName("alarms_layout")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(720, 180, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMaximum(12)
        self.spinBox.setObjectName("spinBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
