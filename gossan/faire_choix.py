# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'faire_choix.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import first
class Ui_select_classe(object):
    def setupUi(self, select_classe):
        select_classe.setObjectName("select_classe")
        select_classe.resize(440, 173)
        select_classe.setMinimumSize(QtCore.QSize(440, 173))
        select_classe.setMaximumSize(QtCore.QSize(440, 173))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        select_classe.setWindowIcon(icon)
        select_classe.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(select_classe)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-460, -320, 1131, 741))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/revue et correction_Plan de travail 1 copie 6.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(610, 380, 261, 21))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 261, 22))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(828, 424, 58, 25))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.retour = QtWidgets.QPushButton(self.frame_4)
        self.retour.setGeometry(QtCore.QRect(0, 0, 58, 25))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.retour.setFont(font)
        self.retour.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retour.setStyleSheet("color: rgb(11, 170, 75);\n"
"background-color: rgb(11, 170, 75);")
        self.retour.setObjectName("retour")
        self.afficher = QtWidgets.QPushButton(self.frame)
        self.afficher.setGeometry(QtCore.QRect(760, 425, 58, 25))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.afficher.setFont(font)
        self.afficher.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.afficher.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
"color: rgb(255, 255, 255);")
        self.afficher.setObjectName("afficher")
        select_classe.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_classe)
        QtCore.QMetaObject.connectSlotsByName(select_classe)

    def retranslateUi(self, select_classe):
        _translate = QtCore.QCoreApplication.translate
        select_classe.setWindowTitle(_translate("select_classe", "Selectionner une classe"))
        self.retour.setText(_translate("select_classe", "Annuler"))
        self.afficher.setText(_translate("select_classe", "Entrer"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_classe = QtWidgets.QMainWindow()
    ui = Ui_select_classe()
    ui.setupUi(select_classe)
    select_classe.show()
    sys.exit(app.exec_())

