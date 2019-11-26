import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication


class MenuBar(QWidget):
    def __init__(self):
        super().__init__()

        self.fileMenu()
        self.functionMenu()
        self.inforMenu()
        # self.MainBord()
        self.initUI()

    def fileMenu(self):
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

    def functionMenu(self):
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

    def inforMenu(self):
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
        title = QLabel('用户名')
        author = QLabel('密码')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)  # 创建了一个网格布局并且设置了组件之间的间距。

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        logUpButton = QPushButton("注册")

        logInButton = QPushButton("登录")
        grid.addWidget(logUpButton, 3, 0)
        grid.addWidget(logInButton, 3, 1)
        self.setLayout(grid)
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('人脸特效')
        self.setWindowIcon(QIcon('panda.ico'))
        self.show()



    # def MainBord(self):




if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = QMainWindow()
    meanuBar = MenuBar()
    sys.exit(app.exec_())