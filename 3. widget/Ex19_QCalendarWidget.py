import sys

from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)  # 달력에 그리드 표시
        cal.clicked[QDate].connect(self.showDate)  # 날짜를 클릭한 이벤트

        self.label = QLabel(self)
        date = cal.selectedDate()  # 선택된 날짜 정보
        self.label.setText(date.toString(Qt.DefaultLocaleLongDate))
        self.label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.setWindowTitle('')
        self.setGeometry(500, 500, 400, 200)
        self.show()

    def showDate(self, date):
        self.label.setText(date.toString(Qt.DefaultLocaleLongDate))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
