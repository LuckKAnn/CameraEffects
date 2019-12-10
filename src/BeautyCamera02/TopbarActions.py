import AiMain
import VideoMain
import ImageMain


def slot_btn_changToAi(self):
    self.signal_ChangeAI.emit()


def slot_btn_changToImg(self):
    self.signal_Img.emit()


def slot_btn_changToVideo(self):
    self.signal_Video.emit()


def signal_ChangToAi_slot(self):
    self.hide()
    self.t = AiMain.AiMain()
    self.t.show()


def signal_ChangToImg_slot(self):
    self.hide()
    self.t = ImageMain.ImageMain()
    self.t.show()


def signal_ChangToVideo_slot(self):
    self.hide()
    self.t = VideoMain.VideoMain()
    self.t.show()