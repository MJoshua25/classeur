from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import first
from threading import Thread

class Message_y_n(QtWidgets.QDialog):

    def appy(self):
        self.ui.buttonReply = self.yes
        self.hide()


    def appn(self):
        self.ui.buttonReply=self.no
        self.hide()


    def __init__(self,titre,text,ui, *args, **kwargs):
        super(Message_y_n, self).__init__(*args, **kwargs)
        self.setupUi(titre,text,ui)

    def setupUi(self,titre,text,ui):
        self.ui= ui
        self.titre=titre
        self.text=text
        self.yes="Yes"
        self.no="No"
        self.setObjectName("MainWindow")
        self.resize(350, 162)
        self.ui.buttonReply=self.no
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 351, 161))
        self.frame.setMinimumSize(QtCore.QSize(0, 161))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/INTERFACE INFO-05.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(270, 130, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 50, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 130, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.appn)
        self.pushButton_2.clicked.connect(self.appy)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()
        self.exec_()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", self.titre))
        self.pushButton.setText(_translate("MainWindow", "Non"))
        self.label.setText(_translate("MainWindow", self.text))
        self.pushButton_2.setText(_translate("MainWindow", "Oui"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Message_y_n("a","a")
    print(mainWindow)
