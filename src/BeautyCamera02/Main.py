import sys

from PyQt5.QtWidgets import QApplication
from ImageMain import ImageMain
from  LogInMain import  LoginInMain


# 主运行窗口
from VideoMain import VideoMain

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow =ImageMain()
    mainWindow.show()
    sys.exit(app.exec_())
