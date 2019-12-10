import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication


# ##***应用图标***## #
class AppIcon(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)  # 窗口在屏幕上显示，并设置了它的尺寸。resize()和remove()合而为一的方法。
        # 前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。
        self.setWindowTitle('Icon')  # 创建一个窗口标题
        self.setWindowIcon(QIcon('panda.ico'))  # 创建一个QIcon对象并接收一个我们要显示的图片路径作为参数。
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppIcon()
    sys.exit(app.exec_())