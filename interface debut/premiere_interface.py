# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'premiere_interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import first
from threading import Thread
from random import choice
import time

class Fpara(Thread):
    def __init__(self, fonction):
        Thread.__init__(self)
        self.fonction=fonction

    def run(self):
        self.fonction()

class Ui_confirmation(object):
    def connect(self):
        sexe = self.comboBox.currentText()
        liste = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        v = 1
        nom = self.lineEdit.text()
        for i in range(len(nom)):
            if nom[i] in liste:
                v = 0
        if v == 0:
            buttonReply = QMessageBox.about(confirmation, 'INFORMATION', "Nom ne peut contenir de chiffre")
        else:
            prenom = self.lineEdit_2.text()
            licence = self.lineEdit_4.text()
            if licence not in self.ll:
                buttonReply = QMessageBox.about(confirmation, 'INFORMATION', "Licence invalide")
            else:
                passe = self.lineEdit_.text()
                confirmer = self.lineEdit_6.text()
                if confirmer != passe:
                    buttonReply = QMessageBox.about(confirmation, 'INFORMATION', "Erreur Mot de passe")
                else:
                    recup = self.lineEdit_3.text()
                    if recup == "" or nom == "" or passe == "" or licence == "" or prenom == "" or confirmer == "":
                        buttonReply = QMessageBox.about(confirmation, 'INFORMATION', " un champ est vide")
                    else:
                        mac = get_mac()
                        conn, cursor = connect_db()
                        req = """INSERT INTO users(nom, prenom,sexe,passe,confirmer,mot_recup,mac) VALUES("{}","{}","{}","{}","{}","{}","{}","{}")""".format(
                            nom, prenom, sexe, passe, confirmer, recup, (base64.b64encode(mac.encode('ascii'))).decode('utf-8'))
                        cursor.execute(req)
                        save_mac()
                        save_li(licence)
                        close_db(conn)
                        open_Page_Acceuil()
                        confirmation.hide()

    def comparer(self):
        if self.user.mot_passe == self.lineEdit.text():
            self.valider()
        else:
            buttonReply = QMessageBox.about(confirmation, 'INFORMATION', "erreur lors de la saisi du mot de passe")

    def valider(self):
        open_Page_Acceuil(self.user)
        confirmation.hide()

    def change(self):
        list = ["1 -03.jpg", "1_2.jpg", "78.jpg"]
        j = 0
        while 1:
            i = choice(list)
            a=confirmation.styleSheet()
            ch="border-image: url(:/newPrefix/{});".format(i)
            while a==ch:
                i=choice(list)
                ch = "border-image: url(:/newPrefix/{});".format(i)
            confirmation.setStyleSheet(ch)
            time.sleep(15)

    def setup_create(self):
        confirmation.setMaximumSize(QtCore.QSize(989, 601))
        confirmation.resize(989, 601)
        confirmation.setMinimumSize(QtCore.QSize(989, 601))
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
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
        self.lineEdit_6.raise_()
        self.lineEdit_3.raise_()
        self.pushButton.raise_()
        self.pushButton.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.pushButton.raise_()
        self.frame_3.raise_()
        self.retranslate_create(confirmation)

    def setup_connect(self):
        confirmation.setMinimumSize(QtCore.QSize(959, 601))
        confirmation.resize(959, 601)
        confirmation.setMaximumSize(QtCore.QSize(959, 601))
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
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
        self.pushButton_2.clicked.connect(self.setup_oublie)
        self.retranslate_connect(confirmation)

    def setup_oublie(self):
        del self.pushButton_2
        del self.pushButton
        confirmation.setMinimumSize(QtCore.QSize(984, 599))
        confirmation.resize(984, 599)
        confirmation.setMaximumSize(QtCore.QSize(984, 599))
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
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
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.retranslate_oublie(confirmation)

    def retranslate_create(self,confirmation):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("confirmation", "Entrer"))
        self.comboBox.setItemText(0, _translate("confirmation", "HOMME "))
        self.comboBox.setItemText(1, _translate("confirmation", "FEMME"))

    def retranslate_connect(self,confirmation):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("confirmation", "Entrer"))
        self.pushButton_2.setText(_translate("confirmation", "Oublié?"))

    def retranslate_oublie(self,confirmation):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("confirmation", "Enter"))



    def setupUi(self, confirmation, ll, user=None):
        self.user=user
        confirmation.setObjectName("confirmation")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        confirmation.setWindowIcon(icon)
        confirmation.setStyleSheet("border-image: url(:/newPrefix/78.jpg);")
        self.centralwidget = QtWidgets.QWidget(confirmation)
        self.centralwidget.setObjectName("centralwidget")
        if self.user==None:
            self.setup_create()
        else:
            self.setup_connect()
        confirmation.setCentralWidget(self.centralwidget)


        self.retranslateUi(confirmation)
        QtCore.QMetaObject.connectSlotsByName(confirmation)

    def retranslateUi(self, confirmation):
        _translate = QtCore.QCoreApplication.translate
        confirmation.setWindowTitle(_translate("confirmation", "EDU-CLASSEUR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    confirmation = QtWidgets.QMainWindow()
    ui = Ui_confirmation()
    ui.setupUi(confirmation, user)
    confirmation.show()
    sys.exit(app.exec_())

