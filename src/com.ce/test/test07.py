import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication


# ##***箱布局***## #
class BoxLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # 创建了一个水平箱布局，并且增加了一个拉伸因子和两个按钮。拉伸因子在两个按钮之前增加了一个可伸缩空间。
        # 这会将按钮推到窗口的右边。
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 为了创建必要的布局，把水平布局放置在垂直布局内。拉伸因子将把包含两个按钮的水平箱布局推到窗口的底边。
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BoxLayout()
    sys.exit(app.exec_())