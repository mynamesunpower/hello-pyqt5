import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setAcceptRichText(True)
        self.label2 = QLabel('The number of words is 0')

        self.te.textChanged.connect(self.text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.te)
        vbox.addWidget(self.label2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('')
        self.setGeometry(500, 500, 400, 200)
        self.show()

    def text_changed(self):
        text = self.te.toPlainText()
        self.label2.setText('The number of words is ' + str(len(text.split())))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
