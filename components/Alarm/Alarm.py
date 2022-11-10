import sys
from PyQt5.QtWidgets import QWidget, QApplication

from components.Alarm.style import Ui_Form
from components.AlarmDialog.Dialog import Dialog


class Alarm(QWidget, Ui_Form):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.setStyleSheet("""
        QFrame{
            background: white;
            border-radius: 8px;
        }
        QCheckBox{
            background: white;
        }
        QLineEdit{
            border-radius: 8px;
        }   
        """)

    def check_alarm(self, time):
        alarm_time = self.timeEdit.time().toPyTime()
        if alarm_time.second == time.second and alarm_time.minute == time.minute and alarm_time.hour == time.hour and self.checkBox.isChecked():
            dialog = Dialog(self.lineEdit.text(), self.timeEdit.time().toPyTime().strftime("%H:%M"), "components/sound/base.mp3")
            dialog.exec()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alarm(None)
    ex.show()
    sys.exit(app.exec())
