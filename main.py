import sys
import datetime
from PyQt5.QtCore import QPoint, QTimer
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPen, QStaticText, QFont
from PyQt5.QtWidgets import QWidget, QApplication


class Clock(QWidget):
    def __init__(self, offset):
        super().__init__()
        self.offset = datetime.timedelta(hours=offset)
        self.initUI()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def set_offset(self, offset):
        self.offset = datetime.timedelta(hours=offset)

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Рисование')

    def paintEvent(self, event):
        time = datetime.datetime.utcnow() + self.offset
        qp = QPainter()
        self.draw_cifer(qp, QColor(0, 0, 0))
        self.draw_second(qp, time.second, QColor(255, 0, 0))
        self.draw_minute(qp, time.minute, QColor(0, 255, 0))
        self.draw_hour(qp, time.hour, QColor(0, 0, 255))


    def draw_cifer(self, qp, color):
        qp.begin(self)
        qp.translate(self.width() / 2, self.height() / 2)
        qp.setPen(QPen(color, 3))
        qp.setFont(QFont("Helvetica", pointSize=20))
        qp.drawText(QPoint(-12, -120), "12")
        qp.drawText(QPoint(120, 6), "3")
        qp.drawText(QPoint(-134, 6), "9")
        qp.drawText(QPoint(-6, 140), "6")


        for i in range(12):
            qp.drawLine(QPoint(0, -100), QPoint(0, -110))
            qp.rotate(30)
        qp.end()

    def draw_second(self, qp, seconds, color):
        qp.begin(self)
        qp.translate(self.width() / 2, self.height() / 2)
        qp.setBrush(color)
        qp.rotate(6 * seconds)
        qp.drawConvexPolygon(QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -90)
        ]))
        qp.end()

    def draw_minute(self, qp, minutes, color):
        qp.begin(self)
        qp.translate(self.width() / 2, self.height() / 2)
        qp.setBrush(color)
        qp.rotate(6 * minutes)
        qp.drawConvexPolygon(QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -70)
        ]))
        qp.end()

    def draw_hour(self, qp, hours, color):
        qp.begin(self)
        qp.translate(self.width() / 2, self.height() / 2)
        qp.setBrush(color)
        qp.rotate(30 * hours)
        qp.drawConvexPolygon(QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -50)
        ]))
        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Clock(3)
    ex.show()
    sys.exit(app.exec())
