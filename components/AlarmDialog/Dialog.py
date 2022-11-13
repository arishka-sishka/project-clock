import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QDialog
from components.AlarmDialog.style import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, title, time, filename, parent=None):
        self.parent = parent
        super().__init__()
        self.setupUi(self, title, time)
        self.btn_ok.clicked.connect(self.close)
        self.sound = QMediaPlayer()
        self.sound.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        self.sound.play()


# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     window = Dialog("Мой хуй - катапульта", "13:00", "dfghj")
#     window.show()
#
#     sys.exit(app.exec_())
