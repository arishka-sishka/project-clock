import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from components.Alarm import Alarm
import style


class App(QMainWindow, style.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.alarms_layout.addWidget(Alarm.Alarm(self.centralwidget))
        self.alarms_layout.addWidget(Alarm.Alarm(self.centralwidget))
        self.alarms_layout.addWidget(Alarm.Alarm(self.centralwidget))
        self.alarms_layout.addWidget(Alarm.Alarm(self.centralwidget))
        self.alarms_layout.addWidget(Alarm.Alarm(self.centralwidget))
        self.spinBox.valueChanged.connect(self.onChange)

    def onChange(self):
        self.clock_widget.set_offset(self.spinBox.value())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
