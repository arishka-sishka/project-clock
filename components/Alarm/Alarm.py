import datetime
import sqlite3

from PyQt5.QtWidgets import QWidget, QFileDialog

from components.Alarm.style import Ui_Form
from components.AlarmDialog.Dialog import Dialog


# Виджет будильника
class Alarm(QWidget, Ui_Form):
    # Инициализация
    def __init__(self, parent: QWidget):
        self.sound = None
        self.id = None
        super().__init__(parent=parent)
        self.setupUi(self)
        # Стили
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
        # Назначение действий на события
        self.lineEdit.textChanged.connect(self.update_database)
        self.timeEdit.timeChanged.connect(self.update_database)
        self.checkBox.stateChanged.connect(self.update_database)
        self.soundBtn.clicked.connect(self.change_sound)

    # Срабатывание будильника
    def check_alarm(self, time: datetime.datetime) -> None:
        # Получение времени будильника в формате date.time
        alarm_time = self.timeEdit.time().toPyTime()
        # Сравнение времени часов с временем данного будильника
        if alarm_time.second == time.second and alarm_time.minute == time.minute \
                and alarm_time.hour == time.hour and self.checkBox.isChecked():
            # Создание и отображение диалогового окна
            dialog = Dialog(self.lineEdit.text(), self.timeEdit.time().toPyTime().strftime("%H:%M"), self.sound)
            dialog.exec()

    # Установить данные будильника
    def set_data(self, alarm_id: int, title: str, time: datetime.time, state: bool,
                 sound: str = "components/sound/base.mp3") -> None:
        self.sound = sound
        self.id = alarm_id
        self.lineEdit.setText(title)
        self.timeEdit.setTime(time)
        self.checkBox.setCheckState(state)
        self.update_database()

    # Обновить данные в бд в соответсвии с данными будильника
    def update_database(self) -> None:
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        cur.execute("""update alarms set title = ?, time = ?, state = ?, sound = ? where id = ?""",
                    (self.lineEdit.text(), self.timeEdit.time().toPyTime().strftime("%H:%M:%S"),
                     self.checkBox.isChecked(), self.sound, self.id))
        con.commit()
        con.close()

    # Изменение звука будильника
    def change_sound(self) -> None:
        self.sound = QFileDialog.getOpenFileName(self, "Выбрать звук", '', filter="*.mp3")[0]
        self.update_database()
