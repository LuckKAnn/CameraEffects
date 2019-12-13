# -*- coding: utf-8 -*-
'''
多窗口反复切换，只用PyQt5实现
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton


class FirstUi(QMainWindow):
    def __init__(self):
        super(FirstUi, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 200)
        self.setWindowTitle('First Ui')
        self.btn = QPushButton('jump', self)
        self.btn.setGeometry(50, 100, 100, 50)
        self.btn.clicked.connect(self.slot_btn_function)

    def slot_btn_function(self):
        self.hide()
        self.s = SecondUi()
        self.s.show()


class SecondUi(QWidget):
    def __init__(self):
        super(SecondUi, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 350)
        self.setWindowTitle('Second Ui')
        self.btn = QPushButton('jump', self)
        self.btn.setGeometry(150, 150, 100, 50)
        self.btn.clicked.connect(self.slot_btn_function)

    def slot_btn_function(self):
        self.hide()
        self.f = FirstUi()
        self.f.show()


def main():
    app = QApplication(sys.argv)
    w = FirstUi()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()