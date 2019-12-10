import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox,QTextEdit,QLabel,
    QPushButton, QApplication,QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,QGridLayout,
    QLineEdit,QSlider)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import Qt


# ##***文本审阅***## #
class TextReview(QWidget):
    def __init__(self,parent=None):
        # super().__init__()
        super(TextReview, self).__init__(parent)
        self.initUI()

    def initUI(self):

        title = QLabel('程度(大->小):')
        author = QLabel('目标脸:')
        # review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        reviewEdit2= QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)  # 创建了一个网格布局并且设置了组件之间的间距。

        # grid.addWidget(title, 1, 0)
        grid.addWidget(reviewEdit, 1, 0,5,2)
        choicImgButton = QPushButton("选择视频")
        videoCatchButton = QPushButton("打开摄像头")
        grid.addWidget(choicImgButton, 8, 0)
        grid.addWidget(videoCatchButton, 8,1)

        Button1 = QPushButton("磨皮")
        Button2 = QPushButton("美白")
        Button3 = QPushButton("祛痘除斑")
        Button4 = QPushButton("添加贴纸")
        Button5 = QPushButton("人脸检测")
        self.splider = QSlider(Qt.Horizontal)
        # self.splider.valueChanged.connect(self.valChange)
        self.splider.setMinimum(20)  # 最小值
        self.splider.setMaximum(60)  # 最大值
        self.splider.setSingleStep(2)  # 步长
        self.splider.setTickPosition(QSlider.TicksBelow)  # 设置刻度位置，在下方
        self.splider.setTickInterval(5)  # 设置刻度间隔
        grid.addWidget(self.splider,7,1,1,2)
        grid.addWidget(title,7,0)
        grid.addWidget(Button1, 1,2 )
        grid.addWidget(Button2, 2, 2)
        grid.addWidget(Button3, 3,2)
        grid.addWidget(Button4, 4, 2)
        grid.addWidget(Button5, 5, 2)
        # logInButton  = QPushButton("登录")
        # grid.addWidget( authorEdit, 1, 3,3,0)
        # grid.addWidget(videoCatchButton, 3, 1)
        # grid.addWidget(reviewEdit, 3, 1, 1, 1)  # 如果我们向网格布局中增加一个组件，我们可以提供组件的跨行
        # 和跨列参数。在这个例子中，我们让reviewEdit组件跨了5行。

        self.setLayout(grid)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('人脸特效')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextReview()
    sys.exit(app.exec_())