# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voir_etablissement.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import first
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 651)
        MainWindow.setStyleSheet("background-color: rgb(11, 170, 75);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 771, 611))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(102, 255, 185);")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 788, 23))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.menuBar.setFont(font)
        self.menuBar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(0, 0, 0);")
        self.menuBar.setObjectName("menuBar")
        self.menuAjouter = QtWidgets.QMenu(self.menuBar)
        self.menuAjouter.setStyleSheet("background-color: rgb(102, 255, 185);\n"
"background-color: rgb(11, 170, 75);")
        self.menuAjouter.setObjectName("menuAjouter")
        self.menuNavigation = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.menuNavigation.setFont(font)
        self.menuNavigation.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.menuNavigation.setObjectName("menuNavigation")
        MainWindow.setMenuBar(self.menuBar)
        self.actionAjouter = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/2.0.7.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAjouter.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionAjouter.setFont(font)
        self.actionAjouter.setObjectName("actionAjouter")
        self.actionVoir = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/2.0.6.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVoir.setIcon(icon1)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionVoir.setFont(font)
        self.actionVoir.setObjectName("actionVoir")
        self.actionSupprimer = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/2.0.5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSupprimer.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionSupprimer.setFont(font)
        self.actionSupprimer.setObjectName("actionSupprimer")
        self.actionListe_de_classes = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/2.0.1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionListe_de_classes.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionListe_de_classes.setFont(font)
        self.actionListe_de_classes.setObjectName("actionListe_de_classes")
        self.actionRetour = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/2.08.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRetour.setIcon(icon4)
        self.actionRetour.setObjectName("actionRetour")
        self.menuAjouter.addAction(self.actionAjouter)
        self.menuAjouter.addAction(self.actionVoir)
        self.menuAjouter.addAction(self.actionSupprimer)
        self.menuNavigation.addAction(self.actionListe_de_classes)
        self.menuNavigation.addAction(self.actionRetour)
        self.menuBar.addAction(self.menuAjouter.menuAction())
        self.menuBar.addAction(self.menuNavigation.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EDU-CLASSEUR"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "      Nom etablissement"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Année"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "    Nombre classes"))
        self.menuAjouter.setTitle(_translate("MainWindow", "Etablissement"))
        self.menuNavigation.setTitle(_translate("MainWindow", "Navigation"))
        self.actionAjouter.setText(_translate("MainWindow", "Ajouter"))
        self.actionVoir.setText(_translate("MainWindow", "Modifier"))
        self.actionSupprimer.setText(_translate("MainWindow", "Supprimer"))
        self.actionListe_de_classes.setText(_translate("MainWindow", "Liste des classes"))
        self.actionRetour.setText(_translate("MainWindow", "Retour"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

