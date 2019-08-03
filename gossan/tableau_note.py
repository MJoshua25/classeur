# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableau_note.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import first
class Ui_MainWindow(object):
    def setupUi(self, V_CLASSE_3):
        V_CLASSE_3.setObjectName("V_CLASSE_3")
        V_CLASSE_3.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo-01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        V_CLASSE_3.setWindowIcon(icon)
        V_CLASSE_3.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.centralwidget = QtWidgets.QWidget(V_CLASSE_3)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 771, 611))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(102, 255, 185);")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.EditKeyPressed)
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
        self.toolBar = QtWidgets.QToolBar(V_CLASSE_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.toolBar.setFont(font)
        self.toolBar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet("background-color: rgb(11, 170, 75);\n"
"alternate-background-color: rgb(11, 170, 75);\n"
"background-color: rgb(255, 255, 255);")
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        V_CLASSE_3.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionRetour = QtWidgets.QAction(V_CLASSE_3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/RETOUR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRetour.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionRetour.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icon_Plan de travail 1 copie.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.actionRetour.setObjectName("actionRetour")
        self.actionEnregistrer = QtWidgets.QAction(V_CLASSE_3)
        self.actionEnregistrer.setCheckable(False)
        self.actionEnregistrer.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionEnregistrer.setFont(font)
        self.actionEnregistrer.setVisible(True)
        self.actionEnregistrer.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionEnregistrer.setIconVisibleInMenu(True)
        self.actionEnregistrer.setObjectName("actionEnregistrer")

        self.actionEnregistrer.triggered.connect(self.select)
        self.actionRetour.triggered.connect(self.retour)


        self.toolBar.addAction(self.actionEnregistrer)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRetour)
        V_CLASSE_3.setCentralWidget(self.centralwidget)
        self.v = QtWidgets.QVBoxLayout()
        self.v.addWidget(self.tableWidget)
        self.centralwidget.setLayout(self.v)

        self.retranslateUi(V_CLASSE_3)
        QtCore.QMetaObject.connectSlotsByName(V_CLASSE_3)

    def retranslateUi(self, V_CLASSE_3):
        _translate = QtCore.QCoreApplication.translate
        V_CLASSE_3.setWindowTitle(_translate("V_CLASSE_3", "{} {}-{} {}{}{} Trimestre{}".format(self.etablissement.nom,
                                                                                                self.etablissement.annee,
                                                                                                self.etablissement.annee + 1,
                                                                                                self.classe.niveau,
                                                                                                self.classe.serie,
                                                                                                self.classe.numero,
                                                                                                self.tri)))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("V_CLASSE_3", "   Nom "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("V_CLASSE_3", "Prénoms"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("V_CLASSE_3", "{}{} {}".format(self.thype, self.num, self.coef)))
        self.toolBar.setWindowTitle(_translate("V_CLASSE_3", "toolBar"))
        self.actionRetour.setText(_translate("V_CLASSE_3", "retour"))
        self.actionRetour.setToolTip(_translate("V_CLASSE_3", "<html><head/><body><p><span style=\" font-size:12pt;\">Retour</span></p></body></html>"))
        self.actionEnregistrer.setText(_translate("V_CLASSE_3", "Enregistrer"))
        self.actionEnregistrer.setToolTip(_translate("V_CLASSE_3", "<html><head/><body><p><span style=\" font-size:12pt;\">Enregistrer</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

