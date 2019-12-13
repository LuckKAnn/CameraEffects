# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class one(QMainWindow):
    sig_1 = pyqtSignal()

    def __init__(self):
        super(one, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300, 200)
        self.setWindowTitle('1')
        self.btn_1 = QPushButton(self)
        self.btn_1.setText('Emit')
        self.btn_1.setGeometry(100, 80, 100, 40)
        self.btn_1.clicked.connect(self.slot_btn_1)
        self.sig_1.connect(self.sig_1_slot)

    def slot_btn_1(self):
        self.sig_1.emit()

    def sig_1_slot(self):
        self.t = two()
        self.t.show()


class two(QMainWindow):

    def __init__(self):
        super(two, self).__init__()
        self.resize(500, 100)
        self.setWindowTitle('two')


def ui_main():
    app = QApplication(sys.argv)
    w = one()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    ui_main()
