import sys
from random import randint
from UI import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.show()
        self.pushButton.clicked.connect(self.paintcircle)
        self.should_paint_circle = False

    def paintEvent(self, event):
        size = self.size()
        if self.should_paint_circle:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.black, 1, Qt.SolidLine))
            painter.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
            for i in range(5):
                w = h = randint(10, 200)
                x = randint(1, size.width() - w)
                y = randint(1, size.height() - w)
                painter.drawEllipse(x, y, w, h)

    def paintcircle(self):
        self.should_paint_circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.setFixedSize(680, 520)
    ex.show()
    sys.exit(app.exec_())