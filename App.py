import sqlite3
import sys
from datetime import datetime, timedelta

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

from components.Alarm.Alarm import Alarm
import style


class App(QMainWindow, style.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.alarms = [Alarm(self.centralwidget), Alarm(self.centralwidget),
                       Alarm(self.centralwidget), Alarm(self.centralwidget),
                       Alarm(self.centralwidget)]
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        for count, data in enumerate(cur.execute("select * from alarms").fetchall()):
            id, title, time, state, sound = data
            time = datetime.strptime(time, "%H:%M:%S").time()
            self.alarms[count].setData(id, "Проверка" if title else "", time, bool(state),
                                       sound if sound else "base.mp3")
        con.close()
        for alarm in self.alarms:
            self.alarms_layout.addWidget(alarm)
        self.spinBox.valueChanged.connect(self.onChange)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.onTime)
        self.timer.start(500)

    def onChange(self):
        self.clock_widget.offset = timedelta(hours=self.spinBox.value())

    def onTime(self):
        time = datetime.utcnow() + timedelta(hours=self.spinBox.value())
        self.clock_widget.time = time
        self.clock_widget.update()
        for alarm in self.alarms:
            alarm.check_alarm(time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
