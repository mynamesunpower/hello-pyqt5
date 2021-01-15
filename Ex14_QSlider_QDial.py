import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)  # QSlider(Qt.방향, 부모 위젯)
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)  # 값의 범위를 0에서 50까지로 설정
        self.slider.setSingleStep(2)  # 조절 가능한 최소 단위를 설정

        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)

        btn = QPushButton('Default', self)
        btn.move(35, 160)

        # 슬라이더와 다이얼의 값이 발생하는 시그널을 각각
        # 다이얼과 슬라이더의 값을 조절해주는 메소드에 연결함으로써
        # 두 위젯의 값이 언제나 일치하도록 해 줍니다
        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle('')
        self.setGeometry(500, 500, 400, 200)
        self.show()

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
