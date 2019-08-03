from PyQt5.QtWidgets import  QDialog, QFrame, QPushButton, QLabel
from PyQt5.QtCore import QSize, QRect, QCoreApplication, QMetaObject, Qt
from PyQt5.QtGui import QIcon, QFont, QCursor, QPixmap

class Message_y_n(QDialog):
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
        icon = QIcon()
        self.setWindowIcon(icon)
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 351, 161))
        self.frame.setMinimumSize(QSize(0, 161))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(270, 130, 61, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(30, 20, 300, 100))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setWordWrap(True)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setGeometry(QRect(200, 130, 61, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.appn)
        self.pushButton_2.clicked.connect(self.appy)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)
        self.show()
        self.exec_()

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", self.titre))
        self.pushButton.setText(_translate("MainWindow", "Non"))
        self.label.setText(_translate("MainWindow", self.text))
        self.pushButton_2.setText(_translate("MainWindow", "Oui"))