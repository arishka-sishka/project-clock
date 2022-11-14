from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QDialog, QWidget

from components.AlarmDialog.style import Ui_Dialog


# Диалоговое окно будильника
class Dialog(QDialog, Ui_Dialog):
    # Инициализация
    def __init__(self, title: str, time: str, filename: str, parent: QWidget = None):
        self.parent = parent
        super().__init__()
        self.setupUi(self, title, time)
        # Закрытие при нажатии ОК
        self.btnOk.clicked.connect(self.close)
        # Воспроизведение звука из файла
        self.sound = QMediaPlayer()
        self.sound.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
        self.sound.play()
