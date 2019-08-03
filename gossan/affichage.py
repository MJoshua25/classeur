# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'affichage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import first
class Ui_Message(object):
    def setupUi(self, Message):
        Message.setObjectName("Message")
        Message.resize(351, 161)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Message.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Message)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
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
        Message.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/15.png);\n"
"color: rgb(11, 170, 75);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 50, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.label.setObjectName("label")
        Message.setCentralWidget(self.centralwidget)
        self.retranslateUi(Message)
        QtCore.QMetaObject.connectSlotsByName(Message)


    def retranslateUi(self, Message):
        _translate = QtCore.QCoreApplication.translate
        Message.setWindowTitle(_translate("Message", "Information"))
        self.pushButton.setText(_translate("Message", "ok"))
        self.label.setText(_translate("Message", "c'est ici que tu écrit tes messages"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Message = QtWidgets.QMainWindow()
    ui = Ui_Message()
    ui.setupUi(Message)
    Message.show()
    sys.exit(app.exec_())

