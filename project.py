from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 550)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 400, 400, 100))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 200, 300, 50))

        font = QtGui.QFont()
        font.setPointSize(30)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)

        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Время с компа"))
        self.pushButton.setText(_translate("MainWindow", "ОСТАНОВИТЬ ТАЙМЕР"))
        self.label.setText(_translate("MainWindow", "00:00:00:000"))


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.setText("ЗАПУСТИТЬ ТАЙМЕР")
        self.pushButton.clicked.connect(self.click_button)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(100)  # +
        self.timer.timeout.connect(self.displayTime)

    def click_button(self):
        if self.pushButton.text() == "ЗАПУСТИТЬ ТАЙМЕР":
            self.timer.start()
            self.pushButton.setText("ОСТАНОВИТЬ ТАЙМЕР")
        else:
            self.timer.stop()
            self.pushButton.setText("ЗАПУСТИТЬ ТАЙМЕР")

    def displayTime(self):
        #        self.label.setText(QtCore.QDateTime.currentDateTime().toString())
        self.label.setText(QtCore.QDateTime.currentDateTime().toString('hh:mm:ss:zzz'))  # +++
        self.label.adjustSize()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()
