import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('First Label', self)  # QLabel('라벨 텍스트', 부모 위젯)
        label1.setAlignment(Qt.AlignCenter)  # 라벨의 배치 설정; Qt.AlignCenter (수평, 수직 가운데 정렬)

        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignVCenter)  # Qt.AlignVCenter (수직 가운데 정렬)

        font1 = label1.font()
        font1.setPointSize(20)  # 폰트의 크기 결정; 기본값 (13)

        font2 = label2.font()
        font2.setFamily('Times New Roman')  # 폰트 종류 결정
        font2.setBold(True)  # 폰트를 진하게 설정

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('')
        self.setGeometry(500, 500, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
