import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        checkbox = QCheckBox('Show title', self)  # QCheckBox('텍스트라벨', 부모위젯)
        checkbox.move(20, 20)
        checkbox.toggle()  # 체크박스의 기본값은 off 상태이기 때문에 on 상태로 나타내기 위해
        checkbox.stateChanged.connect(self.changeTitle)
        # 체크박스의 상태가 바뀔 때 발생하는 시그널을 changeTitle 메소드에 연결

        self.setWindowTitle('')
        self.setGeometry(500, 500, 400, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
