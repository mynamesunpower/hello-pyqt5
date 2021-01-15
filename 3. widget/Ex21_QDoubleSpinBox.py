import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label1 = QLabel('QDoubleSpinBox')
        self.doublespinbox = QDoubleSpinBox()
        self.doublespinbox.setRange(0, 100)
        self.doublespinbox.setSingleStep(0.5)
        self.doublespinbox.setPrefix('$ ')  # 접두어 // setSuffix()는 접미어
        self.doublespinbox.setDecimals(1)  # 소수점 자릿수 정해주기

        self.label2 = QLabel('$ 0.0')

        self.doublespinbox.valueChanged.connect(self.value_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.doublespinbox)
        vbox.addWidget(self.label2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('')
        self.setGeometry(500, 500, 400, 200)
        self.show()

    def value_changed(self):
        self.label2.setText('$ ' + str(self.doublespinbox.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
