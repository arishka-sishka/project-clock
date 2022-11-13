from PyQt5 import QtCore, QtGui, QtWidgets

# Шаблон установки будильника
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 120)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 350, 120))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.soundBtn = QtWidgets.QPushButton(self.frame)
        self.soundBtn.setGeometry(QtCore.QRect(295, 20, 30, 30))
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame)
        self.timeEdit.setGeometry(QtCore.QRect(20, 70, 210, 30))
        self.timeEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.timeEdit.setObjectName("timeEdit")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(240, 70, 100, 30))
        self.checkBox.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setText(_translate("Form", "(для записей)"))
        self.timeEdit.setDisplayFormat(_translate("Form", "hh:mm"))
        self.checkBox.setText(_translate("Form", "вкл/выкл"))
