import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication

class PromptText(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))  # 这个静态方法设置了用于提示框的字体。
        # 这里使用10px大小的SansSerif字体。
        self.setToolTip('This is a <b>QWidget</b> widget')  # 调用setTooltip()方法创建提示框。
        # 可以在提示框中使用富文本格式。
        btn = QPushButton('Button', self)  # 创建按钮
        btn.setToolTip('This is a <b>QPushButton</b> widget')  # 设置按钮提示框
        btn.resize(btn.sizeHint())  # 改变按钮大小
        btn.move(300, 100)  # 移动按钮位置
        self.setGeometry(300, 100, 600, 600)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PromptText()
    sys.exit(app.exec_())