import sqlite3
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog

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
        self.lineEdit.textChanged.connect(self.updateDatabase)
        self.timeEdit.timeChanged.connect(self.updateDatabase)
        self.checkBox.stateChanged.connect(self.updateDatabase)
        self.soundBtn.clicked.connect(self.changeSound)

    def check_alarm(self, time):
        alarm_time = self.timeEdit.time().toPyTime()
        if alarm_time.second == time.second and alarm_time.minute == time.minute and alarm_time.hour == time.hour and self.checkBox.isChecked():
            dialog = Dialog(self.lineEdit.text(), self.timeEdit.time().toPyTime().strftime("%H:%M"), self.sound)
            dialog.exec()

    def setData(self, id, title, time, state, sound="components/sound/base.mp3"):
        self.sound = sound
        self.id = id
        self.lineEdit.setText(title)
        self.timeEdit.setTime(time)
        self.checkBox.setCheckState(state)
        self.updateDatabase()

    def updateDatabase(self):
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        cur.execute("""update alarms set title = ?, time = ?, state = ?, sound = ? where id = ?""",
                    (self.lineEdit.text(), self.timeEdit.time().toPyTime().strftime("%H:%M:%S"),
                     self.checkBox.isChecked(), self.sound, self.id))
        con.commit()
        con.close()

    def changeSound(self):
        self.sound = QFileDialog.getOpenFileName(self, "Выбрать звук", '', filter="*.mp3")[0]
        self.updateDatabase()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alarm(None)
    ex.show()
    sys.exit(app.exec())
