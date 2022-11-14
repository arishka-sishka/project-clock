import sqlite3
from datetime import datetime, timedelta

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow

import style
from components.Alarm.Alarm import Alarm


#
class App(QMainWindow, style.Ui_MainWindow):
    # Инициализация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #
        self.alarms = [Alarm(self.centralwidget), Alarm(self.centralwidget),
                       Alarm(self.centralwidget), Alarm(self.centralwidget),
                       Alarm(self.centralwidget)]
        #
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        for count, data in enumerate(cur.execute("select * from alarms").fetchall()):
            alarm_id, title, time, state, sound = data
            time = datetime.strptime(time, "%H:%M:%S").time()
            self.alarms[count].set_data(alarm_id, "Проверка" if title else "", time, bool(state),
                                        sound if sound else "base.mp3")
        con.close()
        for alarm in self.alarms:
            self.alarms_layout.addWidget(alarm)
        self.spinBox.valueChanged.connect(self.on_change)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_time)
        self.timer.start(500)

    #
    def on_change(self):
        self.clock_widget.offset = timedelta(hours=self.spinBox.value())

    #
    def on_time(self):
        time = datetime.utcnow() + timedelta(hours=self.spinBox.value())
        self.clock_widget.time = time
        self.clock_widget.update()
        for alarm in self.alarms:
            alarm.check_alarm(time)
