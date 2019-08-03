# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prenom.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import first2
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, Add_student):
        Add_student.setMinimumSize(QtCore.QSize(405, 186))
        Add_student.setMaximumSize(QtCore.QSize(405, 186))
        Add_student.setObjectName("Add_student")
        Add_student.resize(405, 186)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Add_student.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Add_student)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-20, -11, 431, 201))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/Sans titre - 2-02.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(156, 57, 223, 20))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.nom = QtWidgets.QLineEdit(self.frame_2)
        self.nom.setGeometry(QtCore.QRect(0, 0, 225, 20))
        self.nom.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.nom.setClearButtonEnabled(True)
        self.nom.setObjectName("nom")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(152, 102, 231, 20))
        self.frame_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(3, 0, 225, 20))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(266, 159, 61, 22))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/6.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(266, 157, 61, 23))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(334, 158, 63, 23))
        self.frame_5.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 61, 23))
        self.pushButton_2.setStyleSheet("color: rgb(11, 170, 75);")
        self.pushButton_2.setObjectName("pushButton_2")
        Add_student.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_student)
        QtCore.QMetaObject.connectSlotsByName(Add_student)

    def retranslateUi(self, Add_student):
        _translate = QtCore.QCoreApplication.translate
        Add_student.setWindowTitle(_translate("Add_student", "Ajouter un élève"))
        self.pushButton.setText(_translate("Add_student", "VALIDER"))
        self.pushButton_2.setText(_translate("Add_student", "ANNULER"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

