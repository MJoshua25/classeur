# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableau_nom.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import first
class Ui_MainWindow(object):
    def setupUi(self, Add_many_student):
        Add_many_student.setObjectName("Add_many_student")
        Add_many_student.resize(788, 664)
        Add_many_student.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.v = QtWidgets.QVBoxLayout()
        self.v.setObjectName("v")
        self.centralwidget = QtWidgets.QWidget(Add_many_student)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 771, 611))
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(102, 255, 185);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
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
        Add_many_student.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(Add_many_student)
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
        Add_many_student.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAjouter = QtWidgets.QAction(Add_many_student)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/AJOUTER.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAjouter.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionAjouter.setFont(font)
        self.actionAjouter.setObjectName("actionAjouter")
        self.actionRetour = QtWidgets.QAction(Add_many_student)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/RETOUR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRetour.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionRetour.setFont(font)
        self.actionRetour.setObjectName("actionRetour")
        self.actionEnregistrer = QtWidgets.QAction(Add_many_student)
        self.actionEnregistrer.setCheckable(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icon_Plan de travail 1 copie.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.actionEnregistrer.setIcon(icon3)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionEnregistrer.setFont(font)
        self.actionEnregistrer.setVisible(True)
        self.actionEnregistrer.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionEnregistrer.setIconVisibleInMenu(True)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionSupprimer_2 = QtWidgets.QAction(Add_many_student)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/icon-06.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSupprimer_2.setIcon(icon5)
        font = QtGui.QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionSupprimer_2.setFont(font)
        self.actionSupprimer_2.setObjectName("actionSupprimer_2")
        self.toolBar.addAction(self.actionAjouter)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSupprimer_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEnregistrer)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRetour)

        self.v.addWidget(self.tableWidget)
        self.centralwidget.setLayout(self.v)

        self.actionAjouter.triggered.connect(self.plus)
        self.actionSupprimer_2.triggered.connect(self.moins)
        self.actionEnregistrer.triggered.connect(self.ajouter)
        self.actionRetour.triggered.connect(self.retour)

        self.retranslateUi(Add_many_student)
        QtCore.QMetaObject.connectSlotsByName(Add_many_student)

    def retranslateUi(self, Add_many_student):
        _translate = QtCore.QCoreApplication.translate
        Add_many_student.setWindowTitle(
            _translate("Add_many_student", "{}{}{}".format(self.classe.niveau, self.classe.serie, self.classe.numero)))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Add_many_student", "   Nom "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Add_many_student", "Prénoms"))
        self.toolBar.setWindowTitle(_translate("Add_many_student", "toolBar"))
        self.actionAjouter.setText(_translate("Add_many_student", "Ajouter"))
        self.actionAjouter.setToolTip(_translate("Add_many_student", "<html><head/><body><p><span style=\" font-size:12pt;\">Ajouter</span></p></body></html>"))
        self.actionRetour.setText(_translate("Add_many_student", "Retour"))
        self.actionRetour.setToolTip(_translate("Add_many_student", "<html><head/><body><p><span style=\" font-size:12pt;\">Retour</span></p></body></html>"))
        self.actionEnregistrer.setText(_translate("Add_many_student", "Enregistrer"))
        self.actionEnregistrer.setToolTip(_translate("Add_many_student", "<html><head/><body><p><span style=\" font-size:12pt;\">Enregistrer</span></p></body></html>"))
        self.actionSupprimer_2.setText(_translate("Add_many_student", "Retirer"))
        self.actionSupprimer_2.setToolTip(_translate("Add_many_student", "<html><head/><body><p><span style=\" font-size:12pt;\">Retirer</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
