import sqlite3
from datetime import datetime, timedelta, time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow

import style
from components.Alarm.Alarm import Alarm


# Приложение
class App(QMainWindow, style.Ui_MainWindow):
    # Инициализация
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Создание будильников
        self.alarms = [Alarm(self.centralwidget), Alarm(self.centralwidget),
                       Alarm(self.centralwidget), Alarm(self.centralwidget),
                       Alarm(self.centralwidget)]
        # Заполнение их из базы
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        for count, data in enumerate(cur.execute("select * from alarms").fetchall()):
            alarm_id, title, alarm_time, state, sound = data
            alarm_time = datetime.strptime(alarm_time, "%H:%M:%S").time()
            self.alarms[count].set_data(alarm_id, title if title else "", alarm_time, bool(state),
                                        sound if sound else "base.mp3")
        con.close()
        # Добавление будильников в контейнер
        for alarm in self.alarms:
            self.alarms_layout.addWidget(alarm)
        # Подключение функций к событиям
        self.spinBox.valueChanged.connect(self.on_change)
        self.reset_btn.clicked.connect(self.reset)
        # Запуск таймера обновления
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.on_time)
        self.timer.start(500)

    # Передача значения из QSpinBox в часы
    def on_change(self) -> None:
        self.clock_widget.offset = timedelta(hours=self.spinBox.value())

    # Обновление часов
    def on_time(self) -> None:
        # Время часов (UTC + смещение)
        clock_time = datetime.utcnow() + timedelta(hours=self.spinBox.value())
        self.clock_widget.time = clock_time
        # Обновление часов
        self.clock_widget.update()
        # Проверка будильников
        for alarm in self.alarms:
            alarm.check_alarm(clock_time)

    # Сбросить все данные
    def reset(self) -> None:
        self.spinBox.setValue(0)
        for alarm in self.alarms:
            alarm.set_data(alarm.id, "", time.fromisoformat("00:00:00"), False, sound="")
            alarm.update_database()
