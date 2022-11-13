import sys
import datetime
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPen, QFont
from PyQt5.QtWidgets import QWidget, QApplication


class Clock(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.offset = datetime.timedelta(hours=0)
        self.initUI()
        self.time = datetime.datetime.utcnow()

    def initUI(self):
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Часики')

    def paintEvent(self, event):
        time = datetime.datetime.utcnow() + self.offset
        qp = QPainter()
        self.draw_cifer(qp, QColor(0, 0, 0))
        self.draw_second(qp, time.second, QColor(240, 0, 0))
        self.draw_minute(qp, time.minute, QColor(0, 200, 0))
        self.draw_hour(qp, time.hour, QColor(0, 0, 230))

    def draw_cifer(self, qp, color):
        qp.begin(self)
        qp.translate(self.width() / 2, self.height() / 2)
        qp.setPen(QPen(color, 2))
        qp.setFont(QFont("Helvetica", pointSize=20))
        qp.drawText(QPoint(-12, -120), "𝟙𝟚")
        qp.drawText(QPoint(120, 6), "𝟛")
        qp.drawText(QPoint(-134, 6), "𝟡")
        qp.drawText(QPoint(-6, 140), "𝟞")

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
    ex = Clock(None)
    ex.show()
    sys.exit(app.exec())
