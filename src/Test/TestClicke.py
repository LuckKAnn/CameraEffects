#这是继承QGraphicsScene的自定义类
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtWidgets

from skimage.viewer.utils import FigureCanvas
import matplotlib as plt

from ImgUi import Ui_MainWindow


class CARscene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(CARscene, self).__init__(parent)

    def mousePressEvent(self, QMouseEvent):
        #这行代码是期望显示坐标，奈何永远都是[0.0, 0.0]
        print([QMouseEvent.pos().x(), QMouseEvent.pos().y()])

    #这是主窗口的类，继承自QtDesigner设计的界面

class CDataMingQtUi(QtWidgets.QMainWindow, Ui_MainWindow):
        def __init__(self):
            super(CDataMingQtUi, self).__init__()
            self.setupUi(self)

            #CARgraphview 是一个QGraphicView的实例
            self.figure = plt.figure()
            self.canvas = FigureCanvas(self.figure)
            self.graph_sence = CARscene()
            self.graph_sence.addWidget(self.canvas)
            self.CARgraphview.setScene(self.graph_sence)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
