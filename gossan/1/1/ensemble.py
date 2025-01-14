from PyQt5 import QtCore, QtGui, QtWidgets
import first
import time
def changer_1():
    global ui,MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
def changer_2():
    global ui, MainWindow_2, confirmation
    MainWindow_2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow_2)
    MainWindow_2.show()
class Ui_MainWindow(object):
    def oublie(self):
        changer_2()
        MainWindow_2.hide()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(984, 599)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 991, 601))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/1 -03.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 991, 601))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/2.01.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(640, 256, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(780, 290, 71, 23))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.oublie)
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))

class Ui_MainWindow_2(object):

    def setupUi(self, MainWindow_2):
        MainWindow_2.setObjectName("MainWindow_2")
        MainWindow_2.resize(959, 601)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_2.setWindowIcon(icon)
        MainWindow_2.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow_2)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 961, 601))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/1.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 961, 601))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/2.0.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(620, 255, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(760, 290, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 290, 61, 23))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/15.png);\n"
"\n"
"color: rgb(11, 170, 75);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_2)

    def retranslateUi(self, MainWindow_2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_2.setWindowTitle(_translate("MainWindow_2", "EDU-CLASSEUR"))
        self.pushButton.setText(_translate("MainWindow_2", "Entrer"))
        self.pushButton_2.setText(_translate("MainWindow_2", "Oublié?"))





class Ui_confirmation(object):
    def charger(self):
        changer_2()
        confirmation.hide()
    def setupUi(self, confirmation):
        confirmation.setObjectName("confirmation")
        confirmation.resize(989, 601)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        confirmation.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(confirmation)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 991, 601))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/78.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1001, 601))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/2.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(590, 150, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(590, 200, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_ = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_.setGeometry(QtCore.QRect(590, 297, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit_.setFont(font)
        self.lineEdit_.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit_.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_.setClearButtonEnabled(True)
        self.lineEdit_.setObjectName("lineEdit_")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(590, 340, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(590, 346, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(590, 392, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(590, 440, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(840, 490, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.charger)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-image: url(:/newPrefix/6.png);")
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(580, 249, 341, 21))
        self.frame_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(10, 0, 321, 22))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_3.raise_()
        self.pushButton.raise_()
        self.pushButton.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.pushButton.raise_()
        self.frame_3.raise_()
        confirmation.setCentralWidget(self.centralwidget)

        self.retranslateUi(confirmation)
        QtCore.QMetaObject.connectSlotsByName(confirmation)

    def retranslateUi(self, confirmation):
        _translate = QtCore.QCoreApplication.translate
        confirmation.setWindowTitle(_translate("confirmation", "EDU-CLASSEUR"))
        self.pushButton.setText(_translate("confirmation", "Entrer"))
        self.comboBox.setItemText(0, _translate("confirmation", "Homme"))
        self.comboBox.setItemText(1, _translate("confirmation", "Femme"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirmation = QtWidgets.QMainWindow()
    ui = Ui_confirmation()
    ui.setupUi(confirmation)
    confirmation.show()
    sys.exit(app.exec_())

