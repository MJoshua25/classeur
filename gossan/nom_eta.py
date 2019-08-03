# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nom_eta.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import first
class Ui_Dialog(object):
    def change(self):
        self.spinBox.setSuffix("-{}".format(self.spinBox.value()+1))
    def setupUi(self, M_eta):
        M_eta.setObjectName("M_eta")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        M_eta.setWindowIcon(icon)
        M_eta.resize(390, 185)
        M_eta.setMaximumSize(QtCore.QSize(390, 185))
        M_eta.setMinimumSize(QtCore.QSize(390, 185))
        M_eta.setAcceptDrops(False)
        M_eta.setDocumentMode(False)
        M_eta.setTabShape(QtWidgets.QTabWidget.Rounded)
        M_eta.setDockNestingEnabled(False)
        M_eta.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(M_eta)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-430, -250, 1051, 631))
        self.widget.setStyleSheet("border-image: url(:/newPrefix/revue et correction_Plan de travail 1 copie 7.png);")
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(570, 296, 211, 21))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 214, 20))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setGeometry(QtCore.QRect(569, 343, 211, 20))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(0, 0, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.a=datetime.date.today().year
        self.spinBox.setMaximum(self.a)
        self.spinBox.setMinimum(2000)
        self.spinBox.setValue(self.a)
        self.spinBox.valueChanged.connect(self.change)
        self.frame.raise_()
        self.spinBox.raise_()
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setGeometry(QtCore.QRect(672, 404, 55, 21))
        self.frame_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 55, 23))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(11, 170, 75);\n"
"color: rgb(255, 255, 255);\n"
"border-image: url(:/newPrefix/6.png);")
        self.pushButton.setObjectName("pushButton")
        self.frame_4 = QtWidgets.QFrame(self.widget)
        self.frame_4.setGeometry(QtCore.QRect(738, 403, 51, 20))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 51, 23))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(11, 170, 75);")
        self.pushButton_2.setObjectName("pushButton_2")
        M_eta.setCentralWidget(self.centralwidget)

        self.retranslateUi(M_eta)
        QtCore.QMetaObject.connectSlotsByName(M_eta)

    def retranslateUi(self, M_eta):
        _translate = QtCore.QCoreApplication.translate
        M_eta.setWindowTitle(_translate("M_eta", "Ajouter un établissement"))
        self.lineEdit.setPlaceholderText(_translate("M_eta", "Devmax"))
        self.spinBox.setSuffix(_translate("M_eta", "-{}").format(str(self.a+1)))
        self.pushButton.setText(_translate("M_eta", "Entrer"))
        self.pushButton_2.setText(_translate("M_eta", "Annuler"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

