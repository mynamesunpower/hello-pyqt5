import sys

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        color = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.frame = QFrame(self)
        self.frame.setStyleSheet('QWidget { background-color: %s }' % color.name())
        self.frame.setGeometry(130, 35, 100, 100)

        self.setWindowTitle('')
        self.setGeometry(500, 500, 400, 200)
        self.show()

    def showDialog(self):
        color = QColorDialog.getColor()

        # 색상을 선택하고 'OK'를 누르면 isValid()가 True, 'Cancel'이면 False 반환.
        if color.isValid():
            self.frame.setStyleSheet('QWidget { background-color: %s }' % color.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
