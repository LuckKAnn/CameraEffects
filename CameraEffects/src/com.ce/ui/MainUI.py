import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication


class MenuBar(object):
    def __init__(self,QMainWindow):
        super().__init__()
        self.QMainWindow = QMainWindow
        self.initUI()
        self.fileMenu()
        self.functionMenu()
        self.inforMenu()


    def fileMenu(self,QMainWindow):
        # 保存
        saveAction =QAction(QIcon('panda.ico'), '&保存', self)
        saveAction.setShortcut('Ctrl+S')
        # 另存为
        saveAsAction = QAction(QIcon('panda.ico'), '&另存为', self)

        exitAction = QAction(QIcon('panda.ico'), '&退出', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)
        fileMenu.addAction(exitAction)
        self.show()

    def functionMenu(self,QMainWindow):
        changeFaceAction = QAction(QIcon('panda.ico'), '&AI换脸', self)
        imageAction = QAction(QIcon('panda.ico'), '&图片处理', self)
        videoAction = QAction(QIcon('panda.ico'), '&视频处理', self)


        self.statusBar()
        menubar = self.menuBar()
        funcMenu = menubar.addMenu('&功能')
        funcMenu.addAction(changeFaceAction)
        funcMenu .addAction(imageAction)
        funcMenu.addAction(videoAction)
        self.show()

    def inforMenu(self,QMainWindow):
        exitAction = QAction(QIcon('panda.ico'), '&联系我们', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        updateAction =  QAction(QIcon('panda.ico'), '&检查更新', self)
        updateAction.setStatusTip("检测是否有新的跟新")

        self.statusBar()
        menubar = self.menuBar()
        helpMenu = menubar.addMenu('&帮助')
        helpMenu.addAction(exitAction)
        helpMenu.addAction(updateAction)
        self.show()


    def initUI(self):
        '显示窗口'
        # sys.argv参数是一个来自命令行的参数列表。
        # self = QWidget()  # Qwidget组件是PyQt5中所有用户界面类的基础类。我们给QWidget提供了默认的构造方法。
        # 默认构造方法没有父类。没有父类的widget组件将被作为窗口使用。
        # 默认构造方法没有父类。没有父类的widget组件将被作为窗口使用。

        self.resize(500, 500)  # resize()方法调整了widget组件的大小。它现在是500px宽，500px高。
        self.move(500, 100)  # move()方法移动widget组件到一个位置，这个位置是屏幕上x=500,y=200的坐标。
        self.setWindowTitle('人脸特效')  # 设置了窗口的标题。这个标题显示在标题栏中。
        self.setWindowIcon(QIcon('panda.ico'))
        self.show()  # show()方法在屏幕上显示出widget。一个widget对象在这里第一次被在内存中创建，并且之后在屏幕上显示。


class MainBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = QMainWindow()
    meanuBar = MenuBar()
    sys.exit(app.exec_())