import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = QLabel('Option1', self)
        self.label.move(50, 150)

        combobox = QComboBox(self)
        combobox.addItem('Option1')
        combobox.addItem('Option2')
        combobox.addItem('Option3')
        combobox.addItem('Option4')
        combobox.move(50, 50)

        combobox.activated[str].connect(self.onActivated)

        self.setWindowTitle('')
        self.setGeometry(500, 500, 400, 200)
        self.show()

    def onActivated(self, text):
        self.label.setText(text)
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
