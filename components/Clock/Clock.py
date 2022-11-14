import datetime

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPen, QFont, QPaintEvent
from PyQt5.QtWidgets import QWidget


# Часы
class Clock(QWidget):
    # Инициализация
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent)
        # Разница времени от UTC
        self.offset = datetime.timedelta(hours=0)
        self.init_ui()
        # UTC время
        self.time = datetime.datetime.utcnow()

    # Инициализирует стиль
    def init_ui(self) -> None:
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Часики')

    # Событие отрисовки часов
    def paintEvent(self, event: QPaintEvent) -> None:
        # Текущее время часов
        time = datetime.datetime.utcnow() + self.offset
        qp = QPainter()
        # Нарисовать циферблат
        self.draw_dial(qp, QColor(0, 0, 0))
        # Нарисовать секундную стелку
        self.draw_second(qp, time.second, QColor(240, 0, 0))
        # Нарисовать минутную стрелку
        self.draw_minute(qp, time.minute, QColor(0, 200, 0))
        # Нарисовать часовую стрелку
        self.draw_hour(qp, time.hour, QColor(0, 0, 230))

    # Отрисовка циферблата
    def draw_dial(self, qp: QPainter, color: QColor) -> None:
        qp.begin(self)
        # Переместить кооринаты (0, 0) кисти в точку центра
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

    # Отрисовка секундной стрелки
    def draw_second(self, qp: QPainter, seconds: int, color: QColor) -> None:
        qp.begin(self)
        # Переместить кооринаты (0, 0) кисти в точку центра
        qp.translate(self.width() / 2, self.height() / 2)
        # Установить цвет кисти
        qp.setBrush(color)
        # Повернуть стрелку в соответствии с временем (1 секунда = 6 градусов)
        qp.rotate(6 * seconds)
        # Нарисовать стрелку
        qp.drawConvexPolygon(QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -90)
        ]))
        qp.end()

    # Отрисовка минутной стрелки
    def draw_minute(self, qp: QPainter, minutes: int, color: QColor) -> None:
        qp.begin(self)
        # Переместить кооринаты (0, 0) кисти в точку центра
        qp.translate(self.width() / 2, self.height() / 2)
        # Установить цвет кисти
        qp.setBrush(color)
        # Повернуть стрелку в соответствии с временем (1 минута = 6 градусов)
        qp.rotate(6 * minutes)
        # Нарисовать стрелку
        qp.drawConvexPolygon(QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -70)
        ]))
        qp.end()

    # Отрисовка часовой стрелки
    def draw_hour(self, qp: QPainter, hours: int, color: QColor) -> None:
        qp.begin(self)
        # Переместить кооринаты (0, 0) кисти в точку центра
        qp.translate(self.width() / 2, self.height() / 2)
        # Установить цвет кисти
        qp.setBrush(color)
        # Повернуть стрелку в соответствии с временем (1 час = 30 градусов)
        qp.rotate(30 * hours)
        # Нарисовать стрелку
        qp.drawConvexPolygon(QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -50)
        ]))
        qp.end()
