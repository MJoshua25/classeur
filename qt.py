import sys
from pprint import pprint
from PyQt5.QtWidgets import QWidget,QProgressBar,QPushButton,QApplication
from PyQt5.QtCore import QBasicTimer
from PyQt5 import QtCore
import time
class Tutorial(QWidget):
    def started(self):
        while self.progressbar.value()<1000:
            time.sleep(0.002)
            self.progressbar.setValue(self.progressbar.value()+1)

    def __init__(self):
        super(Tutorial,self).__init__()
        self.progressbar=QProgressBar(self)
        self.progressbar.setGeometry(220,280,591,4)
        self.progressbar.setTextVisible(False)
        self.progressbar.setMaximum(1000)
        self.progressbar.setAlignment(QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter)
        self.start=QPushButton('Start',self)
        self.start.move(40,80)
        self.start.clicked.connect(self.started)
        self.timer=QBasicTimer()
        self.step=0





if __name__=='__main__':
     app=QApplication(sys.argv)
     tutorial=Tutorial()
     tutorial.show()
     sys.exit(app.exec_())


