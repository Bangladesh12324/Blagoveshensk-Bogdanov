import sys
import random
from PyQt6 import QtWidgets, QtGui, uic


class CircleWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []  # Список для хранения окружностей
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)  # Загрузка UI из файла

        # Подключаем кнопку к методу
        self.button.clicked.connect(self.draw_circle)

        self.setGeometry(100, 100, 800, 600)
        self.show()

    def draw_circle(self):
        # Случайный диаметр окружности
        diameter = random.randint(20, 100)
        radius = diameter // 2
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        # Добавляем окружность в список
        self.circles.append((x, y, diameter))
        self.update()  # Обновляем виджет для перерисовки

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setBrush(QtGui.QColor(255, 255, 0))  # Жёлтый цвет

        # Рисуем все окружности
        for (x, y, diameter) in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = CircleWindow()
    sys.exit(app.exec())
