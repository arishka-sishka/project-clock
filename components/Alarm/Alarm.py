import sys
from PyQt5.QtWidgets import QWidget, QApplication

from components.Alarm.style import Ui_Form


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

    def on_alarm(self):
        self.label_signature_alarm
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Alarm(None)
    ex.show()
    sys.exit(app.exec())
