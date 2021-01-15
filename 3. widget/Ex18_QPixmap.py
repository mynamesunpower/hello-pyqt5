import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # QPixmap 객체 생성 QPixmap('파일명')
        pixmap = QPixmap('../imgs/landscape.png')
        
        label_img = QLabel()
        # setPixmap(픽스맵) 을 이용해 라벨에 표시될 이미지로 설정
        label_img.setPixmap(pixmap)

        # 사이즈 표시하기
        label_size = QLabel('Width: ' + str(pixmap.width()) + ', Height: ' + str(pixmap.height()))
        label_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(label_img)
        vbox.addWidget(label_size)
        self.setLayout(vbox)

        self.setWindowTitle('')
        self.setGeometry(500, 500, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
