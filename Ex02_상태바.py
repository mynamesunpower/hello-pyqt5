import sys

from PyQt5.QtCore import QDate, Qt, QTime, QDateTime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget, QLabel, QVBoxLayout


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        # 프로그램 종료 action 만들기
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)


        # 하단 상태 바 만들기
        # 현재 날짜와 시간
        datetime = QDateTime.currentDateTime()
        self.statusBar().showMessage(datetime.toString(Qt.DefaultLocaleLongDate))

        # 메뉴 바 만들기
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        # 툴바 만들기
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        # 창의 속성 변경
        self.setWindowTitle('StatusBar')
        self.resize(500, 500)
        self.center()
        self.show()

    # 창을 화면 중심으로 이동하기
    def center(self):
        qr = self.frameGeometry()  # 창의 위치와 크기 정보를 얻는다.
        cp = QDesktopWidget().availableGeometry().center()  # 모니터 화면의 가운데 위치를 파악
        qr.moveCenter(cp)  # 창의 직사각형 위치를 화면 중심의 위치로 이동
        self.move(qr.topLeft())  # 현재 창을, qr의 위치로 이동시킨다.

    def make_label(self):
        label_red = QLabel('Red')
        label_green = QLabel('Green')
        label_blue = QLabel('Blue')

        label_red.setStyleSheet("color: red;"
                                "border-style: solid;"
                                "border-width: 2px;")

        vbox = QVBoxLayout()
        vbox.addWidget(label_red)
        vbox.addWidget(label_green)
        vbox.addWidget(label_blue)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())