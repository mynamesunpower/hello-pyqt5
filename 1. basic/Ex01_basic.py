import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QPushButton, QToolTip, QApplication


# 필요한 모듈 불러온다.

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # self 는 MyApp 객체

        # 상태 바 만들기


        # 메인 프레임에 툴팁
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('this is a <b>QWidget</b> widget')

        close_btn = QPushButton('Quit', self)
        close_btn.setToolTip('This is a <b>QPushButton</b> widget')
        close_btn.move(50, 50)
        close_btn.resize(close_btn.sizeHint())  # 버튼을 적절한 크기로 설정하기
        close_btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('web.png'))
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())