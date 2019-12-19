from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtGui import QPen, QPainter, QColor
from PyQt5.QtCore import Qt
from random import randint
import sys
from PyQt5 import uic


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)

        self.btn = QPushButton('click', self)
        self.btn.resize(100, 30)
        self.btn.move(200, 450)

        self.btn.clicked.connect(self.run)
        self.flag = False

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.qp)
            self.qp.end()

    def draw(self, qp):
        pen = QPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)), 3)
        self.qp.setPen(pen)
        x = randint(100, 400)
        y = randint(100, 400)
        r = randint(0, 100)
        self.qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Interface()
    ex.show()
    sys.exit(app.exec_())
