from sys import exit, argv

from PyQt5.QtWidgets import QProgressBar, QDialog, QApplication, QToolBar, QTabWidget, QSpinBox, QTableWidgetItem, QAbstractItemView, QTableWidget, QAction, QMenu, QMenuBar, QComboBox, QFrame, QPushButton, QSpacerItem, QFileDialog, QHBoxLayout, QLineEdit, QMainWindow, QSplashScreen, QSizePolicy, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QSize, QRect, QCoreApplication, QMetaObject, Qt
from PyQt5.QtGui import QIcon, QFont, QCursor, QPixmap


from time import time, sleep
from classes import *
from fonctions_db import *
from fonctions_note import *
from fonctions_eleves import *

import ressources,ressource,first,first1,first2


def open_Page_Acceuil(user=None):
    global Page_Acceuil, ui
    Page_Acceuil = QMainWindow()
    ui = Ui_Page_Acceuil()
    ui.setupUi(Page_Acceuil, user)
    Page_Acceuil.show()


def open_add_school(user):
    global Dialog, uim
    Dialog = QMainWindow()
    uim = Ui_Dialog()
    uim.setupUi(Dialog, user)
    Dialog.show()


def open_select_classe(user):
    global select_classe, uic
    select_classe = QMainWindow()
    uic = Ui_select_classe()
    uic.setupUi(select_classe, user)
    select_classe.show()


def open_v_school(user):
    global V_ETABLISSEMENT, ui
    V_ETABLISSEMENT = QMainWindow()
    ui = Ui_V_ETABLISSEMENT()
    ui.setupUi(V_ETABLISSEMENT, user)
    V_ETABLISSEMENT.showMaximized()


def open_Add_class(user, etablissement=None, sender=None):
    global Add_class, uic
    Add_class = QMainWindow()
    uic = Ui_Add_class()
    uic.setupUi(Add_class, user, etablissement, sender)
    Add_class.show()


def open_class(user, classe, etablissement=None, sender=None):
    global V_CLASSE, ui
    V_CLASSE = QMainWindow()
    ui = Ui_V_CLASSE()
    ui.setupUi(V_CLASSE, user, classe, etablissement, sender)
    V_CLASSE.showMaximized()
    a = Fpara(ui.loadData2)
    a.start()


def open_ensemble(user=None, etablissement=None, sender=None):
    global MainWindow, ui
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, user, etablissement, sender)
    MainWindow.showMaximized()


def open_modif_eta(user, eta):
    global M_eta, uim
    M_eta = QMainWindow()
    uim = Ui_M_eta()
    uim.setupUi(M_eta, user, eta)
    M_eta.show()


def open_add_student(user, classe):
    global Add_student, uiac
    Add_student = QMainWindow()
    uiac = Ui_Add_student()
    uiac.setupUi(Add_student, user, classe)
    Add_student.show()


def open_m_class(user, classe, eleve):
    global M_clas, uim
    M_clas = QMainWindow()
    uim = Ui_M_clas()
    uim.setupUi(M_clas, user, classe, eleve)
    M_clas.show()


def open_note(user, classe):
    global Dialog_3, uin
    Dialog_3 = QMainWindow()
    uin = Ui_Dialog_3()
    uin.setupUi(Dialog_3, user, classe)
    Dialog_3.show()


def open_clas(user, classe, trimestre, thype, coef, num):
    global V_CLASSE_2, ui
    V_CLASSE_2 = QMainWindow()
    ui = Ui_V_CLASSE_2()
    ui.setupUi(V_CLASSE_2, user, classe, trimestre, thype, coef, num)
    V_CLASSE_2.showMaximized()


def recherche(user):
    global ui, Recherche
    Recherche = QMainWindow()
    ui = Ui_Recherche()
    ui.setupUi(Recherche, user)
    Recherche.show()


def recherches(user, liste):
    global ui, Tableau
    Tableau = QMainWindow()
    ui = Ui_Tableau()
    ui.setupUi(Tableau, user, liste)
    Tableau.showMaximized()


def seul(user, liste, listet):
    global uis, Seul
    Seul = QMainWindow()
    uis = Ui_Seul()
    uis.setupUi(Seul, user, liste, listet)
    Seul.show()


def open_clav(user, classe, aux, au, tri, r):
    global V_CLASSE_3, ui
    V_CLASSE_3 = QMainWindow()
    ui = Ui_V_CLASSE_3()
    ui.setupUi(V_CLASSE_3, user, classe, aux, au, tri, r)
    V_CLASSE_3.showMaximized()


def open_Add_many_student(user, classe):
    global Add_many_student, ui
    Add_many_student = QMainWindow()
    ui = Ui_Add_many_student()
    ui.setupUi(Add_many_student, user, classe)
    Add_many_student.showMaximized()


def open_confirmation(ll,user=None):
    global confirmation, ui
    confirmation = QMainWindow()
    ui = Ui_confirmation()
    ui.setupUi(confirmation, ll, user)
    confirmation.show()


def open_licence_manque(param_us, lic, ll):
    global Li_Manque, ui
    Li_Manque = QMainWindow()
    ui = Ui_Li_Manque()
    ui.setupUi(Li_Manque, param_us[3], ll, param_us)
    Li_Manque.show()


def open_splash(ll, user):
    global splash, ui
    splash_pix = QPixmap(':/newPrefix/char.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    ui = Ui_Splash()
    ui.setupUi(splash, splash_pix, ll, user)
    splash.show()
    b = Fpara(ui.charge)
    b.start()
    for i in range(1, 999):
        ui.progressBar.setValue(i)
        t = time()
        while time() < t + 0.004:
            app.processEvents()
    b.join(1)
    ui.suivant()


def open_mess_ok(Titre, text):
    global Message, uim
    Message = QMainWindow()
    uim = Ui_Message()
    uim.setupUi(Message, Titre, text)
    Message.show()



#interface de licence manquante
class Ui_Li_Manque(object):
    def verife(self):
        li = self.lineEdit.text()
        if li !=self.ll:
            open_mess_ok('INFORMATION', "Licence incorrect")
        else:
            mac = get_mac()
            conn, cursor = connect_db()
            cursor.execute(
                """ UPDATE users SET mac="{}",licence=="{}"  WHERE nom="{}" """.format(mac, li, self.param_us[0]))
            close_db(conn)
            open_mess_ok('INFORMATION', "Licence enregistrée")
            open_Page_Acceuil()
            Li_Manque.hide()

    def setupUi(self, Li_Manque, lic, ll, param_us):
        self.licence = lic
        self.ll = ll
        if self.licence in self.ll:
            self.ll.remove(self.licence)
        self.param_us = param_us
        Li_Manque.setObjectName("Li_Manque")
        Li_Manque.resize(300, 80)
        Li_Manque.setMaximumSize(QSize(300, 80))
        Li_Manque.setMinimumSize(QSize(300, 80))
        self.centralwidget = QWidget(Li_Manque)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/Logo/etablissement.png"), QIcon.Normal, QIcon.Off)
        Li_Manque.setWindowIcon(icon)
        self.verticalLayoutWidget.setGeometry(QRect(-1, 0, 301, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QLabel(self.verticalLayoutWidget)
        font = QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit = QLineEdit(self.verticalLayoutWidget)
        font = QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(29)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        Li_Manque.setCentralWidget(self.centralwidget)

        self.retranslateUi(Li_Manque)
        QMetaObject.connectSlotsByName(Li_Manque)

    def retranslateUi(self, Li_Manque):
        _translate = QCoreApplication.translate
        Li_Manque.setWindowTitle(_translate("Li_Manque", "Licence manquante"))
        self.label.setText(_translate("Li_Manque", "Entrez la licence :"))
        self.pushButton.setText(_translate("Li_Manque", "Valider"))


#interface pour la connexion d'un nouvel utilisateur
class Ui_confirmation(object):
    def comparer_recup(self):
        global mot_recup
        recupe = self.lineEdit.text()
        conn, cursor = connect_db()
        cursor.execute("""SELECT mot_recup  FROM users """)
        recup = cursor.fetchone()
        if recupe == recup[0]:
            cursor.execute("""SELECT passe  FROM users """)
            passe = cursor.fetchone()
            open_mess_ok('INFORMATION', "Votre mot de passe est :{}".format(passe[0]))
        else:
            open_mess_ok('INFORMATION', "Mot de récupération invalide")

    def recharge(self):
        open_confirmation(self.ll, self.user)

    def connect(self):
        sexe = self.comboBox.currentText()
        liste = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        v = 1
        nom = self.lineEdit.text()
        for i in range(len(nom)):
            if nom[i] in liste:
                v = 0
        if v == 0:
            open_mess_ok('INFORMATION', "Nom ne peut contenir de chiffre")
        else:
            prenom = self.lineEdit_2.text()
            #licence = self.lineEdit_4.text()
            #if licence != self.ll:
            #    open_mess_ok('INFORMATION', "Licence invalide")
            #else:
            passe = self.lineEdit_.text()
            confirmer = self.lineEdit_6.text()
            if confirmer != passe:
                open_mess_ok('INFORMATION', "Erreur Mot de passe")
            else:
                recup = self.lineEdit_3.text()
                if recup == "" or nom == "" or passe == "" or prenom == "" or confirmer == "":
                    open_mess_ok('INFORMATION', " un champ est vide")
                else:
                    mac = get_mac()
                    conn, cursor = connect_db()
                    req = """INSERT INTO users(nom, prenom,sexe,passe,confirmer,mot_recup,mac) VALUES("{}","{}","{}","{}","{}","{}","{}")""".format(
                        nom, prenom, sexe, passe, confirmer, recup, (base64.b64encode(mac.encode('ascii'))).decode('utf-8'))
                    cursor.execute(req)
                    save_mac()
                    #save_li(licence)
                    close_db(conn)
                    open_Page_Acceuil()
                    m = open_mess_ok("EDU-Classeur", "Bonjour\nMerci de tester notre version d'éssaie du logiciel EDU-Classeur\nCette version est valide jusqu'au 31 juillet 2019\nSi vous avez des idées perméttant d'améliorer le logiciel merci de nous contacter")
                    confirmation.hide()

    def comparer(self):
        if self.user.mot_passe == self.lineEdit.text():
            self.valider()
        else:
            self.lineEdit.clear()
            open_mess_ok('INFORMATION', "erreur lors de la saisi du mot de passe")

    def valider(self):
        open_Page_Acceuil(self.user)
        confirmation.hide()

    def setup_create(self):
        confirmation.setMaximumSize(QSize(989, 601))
        confirmation.resize(989, 601)
        confirmation.setMinimumSize(QSize(989, 601))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setGeometry(QRect(0, 0, 1001, 601))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/2.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QRect(590, 150, 331, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QRect(590, 200, 331, 20))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_ = QLineEdit(self.frame_2)
        self.lineEdit_.setGeometry(QRect(590, 297, 331, 20))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit_.setFont(font)
        self.lineEdit_.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit_.setEchoMode(QLineEdit.Password)
        self.lineEdit_.setClearButtonEnabled(True)
        self.lineEdit_.setObjectName("lineEdit_")
        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QRect(590, 346, 331, 20))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit_6.setEchoMode(QLineEdit.Password)
        self.lineEdit_6.setClearButtonEnabled(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QRect(590, 392, 331, 20))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QRect(590, 440, 331, 20))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText("Ne rien écrire")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setGeometry(QRect(840, 490, 91, 31))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "border-image: url(:/newPrefix/6.png);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.connect)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setGeometry(QRect(580, 249, 341, 21))
        self.frame_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setGeometry(QRect(10, 0, 321, 22))
        font = QFont()
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
        confirmation.setMinimumSize(QSize(989, 601))
        confirmation.resize(989, 601)
        confirmation.setMaximumSize(QSize(989, 601))
        confirmation.setStyleSheet("border-image: url(:/newPrefix/1_2.jpg);")
        try:
            self.frame_2.setGeometry(QRect(0, 0, 1001, 601))
        except:
            self.frame_2 = QFrame(self.centralwidget)
            self.frame_2.setGeometry(QRect(0, 0, 1001, 601))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/2.0.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        try:
            self.lineEdit.setGeometry(QRect(640, 256, 201, 16))
        except:
            self.lineEdit = QLineEdit(self.frame_2)
            self.lineEdit.setGeometry(QRect(640, 256, 201, 16))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.clear()
        try:
            self.pushButton.setGeometry(QRect(780, 290, 71, 23))
        except:
            self.pushButton = QPushButton(self.frame_2)
            self.pushButton.setGeometry(QRect(780, 290, 71, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        try:
            self.pushButton.clicked.disconnect()
        except Exception: pass
        self.pushButton.clicked.connect(self.comparer)
        try:
            self.pushButton_2.setGeometry(QRect(640, 290, 71, 23))
        except:
            self.pushButton_2 = QPushButton(self.frame_2)
            self.pushButton_2.setGeometry(QRect(640, 290, 71, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/15.png);\n"
                                        "\n"
                                        "color: rgb(11, 170, 75);\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        try:
            self.pushButton_2.clicked.disconnect()
        except Exception: pass
        self.pushButton_2.clicked.connect(self.setup_oublie)
        self.retranslate_connect(confirmation)

    def setup_oublie(self):
        confirmation.setMinimumSize(QSize(989, 601))
        confirmation.resize(989, 601)
        confirmation.setMaximumSize(QSize(989, 601))
        confirmation.setStyleSheet("border-image: url(:/newPrefix/1 -03.jpg);")
        self.frame_2.setGeometry(QRect(0, 0, 1001, 601))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/2.01.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lineEdit.setGeometry(QRect(640, 256, 201, 16))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.clear()
        self.pushButton.setGeometry(QRect(780, 290, 71, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2.setGeometry(QRect(640, 290, 71, 23))
        try:
            self.pushButton_2.clicked.disconnect()
        except Exception: pass
        try:
            self.pushButton.clicked.disconnect()
        except Exception: pass
        self.pushButton_2.clicked.connect(self.setup_connect)
        self.pushButton.clicked.connect(self.comparer_recup)
        self.retranslate_oublie(confirmation)

    def retranslate_create(self,confirmation):
        _translate = QCoreApplication.translate
        self.pushButton.setText(_translate("confirmation", "Entrer"))
        self.comboBox.setItemText(0, _translate("confirmation", "HOMME "))
        self.comboBox.setItemText(1, _translate("confirmation", "FEMME"))

    def retranslate_connect(self,confirmation):
        _translate = QCoreApplication.translate
        self.pushButton.setText(_translate("confirmation", "Entrer"))
        self.pushButton_2.setText(_translate("confirmation", "Oublié?"))

    def retranslate_oublie(self,confirmation):
        _translate = QCoreApplication.translate
        self.pushButton.setText(_translate("confirmation", "Enter"))
        self.pushButton_2.setText(_translate("confirmation", "Retour"))



    def setupUi(self, confirmation, ll, user=None):
        self.user=user
        self.ll=ll
        confirmation.setObjectName("confirmation")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        confirmation.setWindowIcon(icon)
        confirmation.setStyleSheet("border-image: url(:/newPrefix/78.jpg);")
        self.centralwidget = QWidget(confirmation)
        self.centralwidget.setObjectName("centralwidget")
        if self.user==None:
            self.setup_create()
        else:
            self.setup_connect()
        confirmation.setCentralWidget(self.centralwidget)


        self.retranslateUi(confirmation)
        QMetaObject.connectSlotsByName(confirmation)

    def retranslateUi(self, confirmation):
        _translate = QCoreApplication.translate
        confirmation.setWindowTitle(_translate("confirmation", "EDU-CLASSEUR"))


#interface de la page d'acceuil
class Ui_Page_Acceuil(object):
    def valider(self):
        nom = self.lineEdit.text()
        liste = self.recherche(nom)
        if nom != "":
            if len(liste) != 0:
                recherches(self.u, liste)
                Page_Acceuil.hide()
            else:
                open_mess_ok('Information', "Aucun resultat......")
        else:
            open_mess_ok('Information', " Vous n'avez rien saisi")

    def recherche(self, name):
        name=name.lower()
        nom = name.split(" ")
        liste = []
        for z in nom:
            for i in self.u.etablissements:
                for j in i.classes:
                    for k in j.eleves:
                        if (z in k.nom.lower()) or (z in k.prenom.lower()) and (z not in liste):
                            liste.append((k, j, i))

        return liste

    def open_select_classe(self):
        classe = charge_classe()
        if  classe==None:
            open_mess_ok('Information', "il n'ya pas de classe")
        else:
            open_select_classe(self.u)

    def open_ensemble(self):
        open_ensemble(user=self.u)
        Page_Acceuil.hide()

    def open_add_school(self, ):
        open_add_school(self.u)
        uim.pushButton.clicked.connect(uim.ajouter)
        uim.pushButton_2.clicked.connect(uim.retour)

    def open_v_school(self):
        open_v_school(self.u)
        Page_Acceuil.hide()

    def open_add_class(self):
        if len(self.u.etablissements) == 0:
            open_mess_ok('Information', "il n'ya pas d'etablissement")
        else:
            open_Add_class(self.u)

    def change_picture(self):
        list=["image.jpg","images (1).jpg","téléchargement.jpg"]
        for i in range(3):
            sleep(5)
            self.scrollArea.setStyleSheet("border-image: url(:/arriere/{});".format(list[i]))

    def setupUi(self, Page_Acceuil, user):
        if user == None:
            self.u = User()
        else:
            self.u = user
        Page_Acceuil.setObjectName("Page_Acceuil")
        Page_Acceuil.resize(989, 601)
        Page_Acceuil.setMaximumSize(QSize(989, 601))
        Page_Acceuil.setMaximumSize(QSize(989, 601))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        Page_Acceuil.setWindowIcon(icon)
        self.centralwidget = QWidget(Page_Acceuil)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(0, 0, 989, 601))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(17)
        self.frame.setFont(font)
        self.frame.setStyleSheet("border-image: url(:/newPrefix/revue et correction_Plan de travail 1 copie 4.jpg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(360, 387, 152, 59))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setGeometry(QRect(510, 387, 371, 59))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QRect(10, 0, 361, 56))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        Page_Acceuil.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Page_Acceuil)
        self.menubar.setGeometry(QRect(0, 0, 989, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuEtablissemnt = QMenu(self.menubar)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.menuEtablissemnt.setFont(font)
        self.menuEtablissemnt.setObjectName("menuEtablissemnt")
        self.menuClasse = QMenu(self.menubar)
        self.menuClasse.setObjectName("menuClasse")
        Page_Acceuil.setMenuBar(self.menubar)
        self.actionAjouter = QAction(Page_Acceuil)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/AJOUTER.png"), QIcon.Normal, QIcon.Off)
        self.actionAjouter.setIcon(icon)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionAjouter.setFont(font)
        self.actionAjouter.setObjectName("actionAjouter")
        self.actionVoir = QAction(Page_Acceuil)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/newPrefix/VOIR.png"), QIcon.Normal, QIcon.Off)
        self.actionVoir.setIcon(icon1)
        self.actionVoir.setObjectName("actionVoir")
        self.actionAjouter_2 = QAction(Page_Acceuil)
        self.actionAjouter_2.setIcon(icon)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionAjouter_2.setFont(font)
        self.actionAjouter_2.setObjectName("actionAjouter_2")
        self.actionVoir_une_classe = QAction(Page_Acceuil)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/newPrefix/VOIR ENSEMBLE-05.png"), QIcon.Normal, QIcon.Off)
        self.actionVoir_une_classe.setIcon(icon2)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionVoir_une_classe.setFont(font)
        self.actionVoir_une_classe.setObjectName("actionVoir_une_classe")
        self.actionVoir_l_ensemble_des_classes = QAction(Page_Acceuil)
        self.actionVoir_l_ensemble_des_classes.setIcon(icon1)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionVoir_l_ensemble_des_classes.setFont(font)
        self.actionVoir_l_ensemble_des_classes.setObjectName("actionVoir_l_ensemble_des_classes")

        self.pushButton.clicked.connect(self.valider)
        self.actionAjouter.triggered.connect(self.open_add_school)
        self.actionAjouter_2.triggered.connect(self.open_add_class)
        self.actionVoir.triggered.connect(self.open_v_school)
        self.actionVoir_l_ensemble_des_classes.triggered.connect(self.open_ensemble)
        self.actionVoir_une_classe.triggered.connect(self.open_select_classe)

        self.menuEtablissemnt.addAction(self.actionAjouter)
        self.menuEtablissemnt.addAction(self.actionVoir)
        self.menuClasse.addAction(self.actionAjouter_2)
        self.menuClasse.addAction(self.actionVoir_une_classe)
        self.menuClasse.addAction(self.actionVoir_l_ensemble_des_classes)
        self.menubar.addAction(self.menuEtablissemnt.menuAction())
        self.menubar.addAction(self.menuClasse.menuAction())

        self.retranslateUi(Page_Acceuil)
        QMetaObject.connectSlotsByName(Page_Acceuil)

    def retranslateUi(self, Page_Acceuil):
        _translate = QCoreApplication.translate
        Page_Acceuil.setWindowTitle(_translate("Page_Acceuil", "Page Acceuil"))
        self.pushButton.setText(_translate("Page_Acceuil", "Recherche"))
        self.menuEtablissemnt.setTitle(_translate("Page_Acceuil", "Etablissement"))
        self.menuClasse.setTitle(_translate("Page_Acceuil", "Classe"))
        self.actionAjouter.setText(_translate("Page_Acceuil", "Ajouter"))
        self.actionVoir.setText(_translate("Page_Acceuil", "Voir"))
        self.actionAjouter_2.setText(_translate("Page_Acceuil", "Ajouter"))
        self.actionVoir_une_classe.setText(_translate("Page_Acceuil", "Voir une classe"))
        self.actionVoir_l_ensemble_des_classes.setText(_translate("Page_Acceuil", "Voir l\'ensemble des classes"))


#interface pour la recherche d'un éleve
class Ui_Recherche(object):
    def valider(self):
        nom = self.lineEdit.text()
        liste = self.recherche(nom)
        if nom != "":
            if len(liste) != 0:
                recherches(self.user, liste)
                Recherche.hide()
            else:
                open_mess_ok('Information', "Aucun resultat......")
        else:
            open_mess_ok('Information', " Vous n'avez rien saisi")

    def recherche(self, name):
        nom = name.split(" ")
        if len(nom) > 0:
            prenom = " ".join(nom[1:])
        nom = name.split(" ")[0]
        liste = []
        for i in self.user.etablissements:
            for j in i.classes:
                for k in j.eleves:
                    if k.nom == nom and k.prenom == prenom:
                        liste.append((k, j, i))

        return liste

    def retour(self):
        open_Page_Acceuil(self.user)
        Recherche.hide()

    def setupUi(self, Recherche, user):
        Recherche.setObjectName("Recherche")
        self.user = user
        Recherche.resize(341, 76)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/téléchargement.jpeg"), QIcon.Normal, QIcon.Off)
        Recherche.setWindowIcon(icon)
        Recherche.setMaximumSize(QSize(341, 76))
        Recherche.setMinimumSize(QSize(341, 76))
        self.centralwidget = QWidget(Recherche)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(10, 20, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QRect(110, 20, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QRect(10, 50, 75, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(180, 180, 180);\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.retour)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(290, 20, 31, 21))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                      "background-color: rgb(0, 170, 255);")
        self.pushButton.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/newPrefix/images.jpeg"), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.clicked.connect(self.valider)
        self.pushButton.setObjectName("pushButton")
        Recherche.setCentralWidget(self.centralwidget)
        self.actionImage = QAction(Recherche)
        self.actionImage.setIcon(icon)
        self.actionImage.setObjectName("actionImage")

        self.retranslateUi(Recherche)
        QMetaObject.connectSlotsByName(Recherche)

    def retranslateUi(self, Recherche):
        _translate = QCoreApplication.translate
        Recherche.setWindowTitle(_translate("Recherche", "Recherche"))
        self.label.setText(_translate("Recherche",
                                      "<html><head/><body><p><span style=\" font-size:10pt;\">Nom et prenom</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Recherche", "Retour"))
        self.actionImage.setText(_translate("Recherche", "image"))


#interface affichant les résultats la recherche
class Ui_Tableau(object):
    def info(self):
        selected = self.tableWidget.selectedItems()
        if self.tableWidget.selectedItems():
            r = selected[0].row()
            liste = self.liste[r]
            seul(self.user, liste, self.liste)
        else:
            open_mess_ok('Information', "Vous n'avez rien selectionner")

    def retour(self):
        open_Page_Acceuil(self.user)
        Tableau.hide()

    def load_data(self):
        self.data(self.liste, self.tableWidget)

    def data(self, liste, table):
        for i in range(len(liste)):
            eleve, classe, eta = liste[i][0], liste[i][1], liste[i][2]
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(eta.nom)))
            table.setItem(i, 1, QTableWidgetItem(str(eta.annee)))
            table.setItem(i, 2, QTableWidgetItem(str(eleve.nom)))
            table.setItem(i, 3, QTableWidgetItem(str(eleve.prenom)))
            table.setItem(i, 4, QTableWidgetItem(str(classe.niveau)))
            table.setItem(i, 5, QTableWidgetItem(str(classe.serie)))
            table.setItem(i, 6, QTableWidgetItem(str(classe.numero)))

    def setupUi(self, Tableau, user, liste):
        self.liste = liste
        self.user = user
        Tableau.setObjectName("Tableau")
        Tableau.resize(800, 600)
        Tableau.setStyleSheet("background-color: rgb(11, 170, 75);")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        Tableau.setWindowIcon(icon)
        self.centralwidget = QWidget(Tableau)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QTableWidget()
        self.tableWidget.setGeometry(QRect(10, 10, 771, 611))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "alternate-background-color: rgb(102, 255, 185);")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.menuBar = QMenuBar(Tableau)
        self.menuBar.setGeometry(QRect(0, 0, 788, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.menuBar.setFont(font)
        self.menuBar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "alternate-background-color: rgb(0, 0, 0);")
        self.menuBar.setObjectName("menuBar")
        self.menuAjouter = QMenu(self.menuBar)
        self.menuAjouter.setStyleSheet("background-color: rgb(102, 255, 185);\n"
                                       "background-color: rgb(11, 170, 75);")
        self.menuAjouter.setObjectName("menuAjouter")
        Tableau.setMenuBar(self.menuBar)
        self.actionAjouter = QAction(Tableau)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/2.0.7.png"), QIcon.Normal, QIcon.Off)
        self.actionAjouter.setIcon(icon)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionAjouter.setFont(font)
        self.actionAjouter.setObjectName("actionAjouter")
        self.actionVoir = QAction(Tableau)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/newPrefix/2.08.png"), QIcon.Normal, QIcon.Off)
        self.actionVoir.setIcon(icon1)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionVoir.setFont(font)
        self.actionVoir.setObjectName("actionVoir")
        self.menuAjouter.addAction(self.actionAjouter)
        self.menuAjouter.addAction(self.actionVoir)
        self.menuBar.addAction(self.menuAjouter.menuAction())
        self.actionVoir.triggered.connect(self.retour)
        self.actionAjouter.triggered.connect(self.info)

        self.v1 = QVBoxLayout()
        self.v1.addWidget(self.tableWidget)
        self.centralwidget.setLayout(self.v1)
        Tableau.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tableau)
        QMetaObject.connectSlotsByName(Tableau)

    def retranslateUi(self, Tableau):
        _translate = QCoreApplication.translate
        Tableau.setWindowTitle(_translate("Tableau", "Tableau recherche"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Tableau", "Nom etablissement"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Tableau", "Année"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Tableau", "Nom "))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Tableau", "Prenoms"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Tableau", "Niveau"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Tableau", "Série"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Tableau", "Numéro"))
        self.menuAjouter.setTitle(_translate("Tableau", "Information"))
        self.actionAjouter.setText(_translate("Tableau", "Information"))
        self.actionVoir.setText(_translate("Tableau", "Retour"))
        self.load_data()


#interface pour affichant un élève de la recherche
class Ui_Seul(object):
    def retour(self):
        if Tableau.isHidden()==True:
            recherches(self.user, self.listet)
        Seul.hide()

    def fonction(self, note, ide):
        _translate = QCoreApplication.translate
        if note < 4:
            ide.setText(_translate("Seul",
                                   "Mauvais"))
            ide.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                              "color: rgb(255, 85, 0);")
        if note > 4 and note < 6:
            ide.setText(_translate("Seul",
                                   "Très Faible"))
            ide.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                              "color: rgb(255, 85, 0);")
        if note > 6 and note < 8:
            ide.setText(_translate("Seul",
                                   "Faible"))
            ide.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                              "color: rgb(255, 85, 0);")
        if note > 8 and note < 10:
            ide.setText(_translate("Seul",
                                   "Insuffisant"))
            ide.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                              "color: rgb(255, 85, 0);")
        if note >= 10 and note < 12:
            ide.setText(_translate("Seul",
                                   "Passable"))
            ide.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                              "color: rgb(0, 85, 255);")
        if note >= 12 and note < 14:
            ide.setText(_translate("Seul",
                                   "Assez Bien"))
            ide.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                              "color: rgb(0, 85, 255);")
        if note >= 14 and note < 16:
            ide.setText(_translate("Seul",
                                   "Bien"))
            ide.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                              "color: rgb(0, 85, 255);")
        if note >= 16 and note < 18:
            ide.setText(_translate("Seul",
                                   "Très Bien"))
            ide.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                              "color: rgb(0, 85, 255);")
        if note >= 18 and note <= 20:
            ide.setText(_translate("Seul",
                                   "Excellent"))
            ide.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                              "color: rgb(85, 255, 127);")

    def setupUi(self, Seul, user, liste, listet):
        self.eleve = liste[0]
        self.etablissement = liste[2]
        self.classe = liste[1]
        self.listet = listet
        self.user = user
        Seul.setObjectName("Seul")
        Seul.resize(934, 601)
        Seul.setMaximumSize(QSize(934, 601))
        Seul.setMinimumSize(QSize(934, 601))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        Seul.setWindowIcon(icon)
        self.centralwidget = QWidget(Seul)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(0, 0, 991, 601))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setStyleSheet("border-image: url(:/newPrefix/IMG-20180422-WA0007.jpg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(420, 65, 421, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setText(self.eleve.nom)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.frame)
        self.label_2.setGeometry(QRect(420, 110, 421, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setText(self.eleve.prenom)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setGeometry(QRect(420, 150, 421, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_3.setText(self.etablissement.nom)
        self.label_4 = QLabel(self.frame)
        self.label_4.setGeometry(QRect(420, 200, 421, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_4.setText("{}{}{}".format(self.classe.niveau, self.classe.serie, self.classe.numero))
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(self.frame)
        self.label_5.setGeometry(QRect(420, 240, 421, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_5.setText("{}-{}".format(self.etablissement.annee, self.etablissement.annee + 1))
        self.label_5.setObjectName("label_5")
        self.label_6 = QLabel(self.frame)
        self.label_6.setGeometry(QRect(420, 290, 421, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(self.frame)
        self.label_7.setGeometry(QRect(420, 330, 421, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);")
        if type(self.eleve.moyenne[0]) is float:
            self.label_6.setText(str(self.eleve.moyenne[0]))
            self.fonction(self.eleve.moyenne[0], self.label_7)
        else:
            self.label_6.setText("Pas de moyenne")
            self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QLabel(self.frame)
        self.label_8.setGeometry(QRect(420, 380, 421, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QLabel(self.frame)
        self.label_9.setGeometry(QRect(420, 430, 421, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);")
        if type(self.eleve.moyenne[1]) is float:
            self.label_8.setText(str(self.eleve.moyenne[1]))
            self.fonction(self.eleve.moyenne[1], self.label_9)
        else:
            self.label_8.setText("Pas de moyenne")
            self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QLabel(self.frame)
        self.label_10.setGeometry(QRect(420, 480, 421, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);\n"
                                    "color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QLabel(self.frame)
        self.label_11.setGeometry(QRect(420, 530, 421, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-image: url(:/newPrefix/terminer.jpg);")
        if type(self.eleve.moyenne[2]) is float:
            self.label_10.setText(str(self.eleve.moyenne[2]))
            self.fonction(self.eleve.moyenne[2], self.label_11)
        else:
            self.label_10.setText("Pas de moyenne")
            self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(821, 557, 103, 25))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.retour)
        Seul.setCentralWidget(self.centralwidget)

        self.retranslateUi(Seul)
        QMetaObject.connectSlotsByName(Seul)

    def retranslateUi(self, Seul):
        _translate = QCoreApplication.translate
        Seul.setWindowTitle(_translate("Seul", "EDU-Classeur"))
        self.pushButton.setText(_translate("Seul", "OK"))


#interface pour l'ajout d'une classe
class Ui_Add_class(object):
    def charge_etablissement(self):
        self.list_eta.clear()
        if self.etablissement == None:
            for i in self.user.etablissements:
                self.list_eta.append(i)
                self.comboBox.addItem("{} {}".format(i.nom, i.annee))
        else:
            self.list_eta.append(self.etablissement)
            self.comboBox.addItem("{} {}".format(self.etablissement.nom, self.etablissement.annee))

    def retour(self):
        if self.sender == None:
            if Page_Acceuil.isHidden()==True:
                open_Page_Acceuil(self.user)
        else:
            if MainWindow.isHidden() == True:
                open_ensemble(user=self.user, etablissement=self.etablissement)
        Add_class.hide()

    def ajouter(self):
        seq = self.comboBox.currentIndex()
        eta = self.list_eta[seq]
        niveau = self.NIVEAU.currentText()
        serie = self.SERIE.currentText()
        if serie == " ":
            serie = ""
        numero = self.NUMER.value()
        conn, cursor = connect_db()
        cursor.execute(
            """ SELECT niveau,serie,numero FROM classe WHERE id_etablissement='{}' AND niveau='{}' AND serie='{}'AND numero='{}' """.format(
                eta.id, niveau, serie, numero))
        id_clas = cursor.fetchall()
        if len(id_clas) != 0:
            open_mess_ok('Information',"cette classe existe vous ne pouvez la cree")
        else:
            cursor.execute(
                """INSERT INTO classe(id_etablissement,niveau,serie,numero) VALUES('{}','{}','{}','{}')""".format(
                    eta.id, niveau, serie, numero))
            classe = Classe(cursor.lastrowid, cursor=cursor, stop=0)
            close_db(conn)
            eta.add_classe(classe)
            self.retour()

    def setupUi(self, Add_class, user, etablissement, sender):
        self.user = user
        self.etablissement = etablissement
        self.list_eta = []
        self.sender = sender
        self.buttonReply=None
        Add_class.setObjectName("Add_class")
        Add_class.resize(439, 223)
        Add_class.setMinimumSize(QSize(439, 223))
        Add_class.setMaximumSize(QSize(439, 223))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        Add_class.setWindowIcon(icon)
        Add_class.setWindowTitle("Ajouter une classe")
        self.centralwidget = QWidget(Add_class)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(-390, -220, 1001, 631))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/revue et correction_Plan de travail 1 copie 5.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setGeometry(QRect(550, 250, 201, 21))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setGeometry(QRect(0, 0, 201, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(8)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setGeometry(QRect(550, 290, 201, 20))
        self.frame_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.NIVEAU = QComboBox(self.frame_3)
        self.NIVEAU.setGeometry(QRect(0, 0, 201, 20))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.NIVEAU.setFont(font)
        self.NIVEAU.setObjectName("NIVEAU")
        self.NIVEAU.addItem("")
        self.NIVEAU.addItem("")
        self.NIVEAU.addItem("")
        self.NIVEAU.addItem("")
        self.NIVEAU.addItem("")
        self.NIVEAU.addItem("")
        self.NIVEAU.addItem("")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setGeometry(QRect(550, 326, 201, 21))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.SERIE = QComboBox(self.frame_4)
        self.SERIE.setGeometry(QRect(0, 0, 201, 22))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.SERIE.setFont(font)
        self.SERIE.setObjectName("SERIE")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.SERIE.addItem("")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setGeometry(QRect(550, 366, 201, 20))
        self.frame_5.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.NUMER = QSpinBox(self.frame_5)
        self.NUMER.setGeometry(QRect(0, 0, 201, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.NUMER.setFont(font)
        self.NUMER.setMinimum(1)
        self.NUMER.setObjectName("NUMER")
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setGeometry(QRect(650, 400, 54, 25))
        self.frame_6.setStyleSheet("border-image: url(:/newPrefix/6.png);\n""background-color: rgb(11, 170, 75);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.valider = QPushButton(self.frame_6)
        self.valider.setCursor(QCursor(Qt.PointingHandCursor))
        self.valider.setGeometry(QRect(0, 0, 54, 25))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.valider.setFont(font)
        self.valider.setStyleSheet("background-color: rgb(11, 170, 75);\n"
                                   "color: rgb(255, 255, 255);")
        self.valider.setObjectName("valider")
        self.frame_7 = QFrame(self.frame)
        self.frame_7.setGeometry(QRect(710, 400, 54, 25))
        self.frame_7.setStyleSheet("border-image: url(:/newPrefix/15.png);\n"
                                   "background-color: rgb(11, 170, 75);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.annuler = QPushButton(self.frame_7)
        self.annuler.setCursor(QCursor(Qt.PointingHandCursor))
        self.annuler.setGeometry(QRect(0, 0, 54, 25))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.annuler.setFont(font)
        self.annuler.setStyleSheet("color: rgb(11, 170, 75);")
        self.annuler.setObjectName("annuler")
        Add_class.setCentralWidget(self.centralwidget)
        self.retranslateUi(Add_class)
        self.annuler.clicked.connect(self.retour)
        self.valider.clicked.connect(self.ajouter)
        QMetaObject.connectSlotsByName(Add_class)

    def retranslateUi(self, Add_class):
        _translate = QCoreApplication.translate
        self.NIVEAU.setItemText(0, _translate("Add_class", "6ème"))
        self.NIVEAU.setItemText(1, _translate("Add_class", "5ème"))
        self.NIVEAU.setItemText(2, _translate("Add_class", "4ème"))
        self.NIVEAU.setItemText(3, _translate("Add_class", "3ème"))
        self.NIVEAU.setItemText(4, _translate("Add_class", "2nd"))
        self.NIVEAU.setItemText(5, _translate("Add_class", "1ère"))
        self.NIVEAU.setItemText(6, _translate("Add_class", "Tle"))
        self.SERIE.setItemText(1, _translate("Add_class", "D"))
        self.SERIE.setItemText(2, _translate("Add_class", "C"))
        self.SERIE.setItemText(3, _translate("Add_class", "A"))
        self.SERIE.setItemText(4, _translate("Add_class", "A1"))
        self.SERIE.setItemText(5, _translate("Add_class", "A2"))
        self.SERIE.setItemText(6, _translate("Add_class", "B"))
        self.SERIE.setItemText(7, _translate("Add_class", "G1"))
        self.SERIE.setItemText(8, _translate("Add_class", "G2"))
        self.SERIE.setItemText(9, _translate("Add_class", "AB"))
        self.SERIE.setItemText(10, _translate("Add_class", "F1"))
        self.SERIE.setItemText(11, _translate("Add_class", "F2"))
        self.SERIE.setItemText(12, _translate("Add_class", "F3"))
        self.SERIE.setItemText(13, _translate("Add_class", "T"))
        self.SERIE.setItemText(14, _translate("Add_class", "E"))
        self.SERIE.setItemText(15, _translate("Add_class", "H1"))
        self.SERIE.setItemText(16, _translate("Add_class", "H2"))
        self.SERIE.setItemText(17, _translate("Add_class", "H3"))
        self.SERIE.setItemText(15, _translate("Add_class", "L"))
        self.SERIE.setItemText(16, _translate("Add_class", "ES"))
        self.SERIE.setItemText(17, _translate("Add_class", "S"))
        self.valider.setText(_translate("Add_class", " Entrer"))
        self.annuler.setText(_translate("Add_class", "Annuler"))
        self.charge_etablissement()


class Ui_MainWindow(object):
    def ajouter(self):
        if len(self.user.etablissements) == 0:
            open_mess_ok('Information', "Il n'ya pas d'etablissement")
        else:
            open_Add_class(self.user)
            MainWindow.hide()

    def delet(self):
        selected = self.tableWidget.selectedItems()
        if self.tableWidget.selectedItems():
            r = selected[0].row()
            classe = self.liste_classe[r]
            buttonReply = Message_y_n('ATTENTION!!!',
                                      "Voulez-vous supprimer cette classe {}{}{}".format(classe.niveau,
                                                                                                 classe.serie,
                                                                                                 classe.numero),
                                      self)
            if self.buttonReply == "Yes":
                conn, cursor = connect_db()
                cursor.execute("""DELETE FROM classe WHERE id='{}'""".format(classe.id))
                cursor.execute("""DELETE FROM eleve WHERE id_classe='{}'""".format(classe.id))
                for i in classe.eleves:
                    cursor.execute("""DELETE FROM notes WHERE id_eleve='{}'""".format(i.id))
                close_db(conn)
                ind = self.user.reper_classe(classe)
                self.user.etablissements[ind[0]].delete_classe(classe)
                if self.etablissement != None:
                    self.etablissement = self.user.etablissements[ind[0]]
                self.loadDat()
        else:
            open_mess_ok('Information', "vous ne pouvez supprimer sans cliquez")

    def loadDat(self):
        k = 0
        self.liste_classe.clear()
        self.tableWidget.setRowCount(0)
        if self.etablissement == None:
            for i in range(len(self.user.etablissements)):
                for j in range(len(self.user.etablissements[i].classes)):
                    self.tableWidget.insertRow(k)
                    self.tableWidget.setItem(k, 0, QTableWidgetItem(str(self.user.etablissements[i].nom)))
                    self.tableWidget.setItem(k, 1, QTableWidgetItem(str(self.user.etablissements[i].annee)))
                    self.tableWidget.setItem(k, 2, QTableWidgetItem(
                        str(self.user.etablissements[i].classes[j].niveau)))
                    self.tableWidget.setItem(k, 3, QTableWidgetItem(
                        str(self.user.etablissements[i].classes[j].serie)))
                    self.tableWidget.setItem(k, 4, QTableWidgetItem(
                        str(self.user.etablissements[i].classes[j].numero)))
                    self.liste_classe.append(self.user.etablissements[i].classes[j])
                    k += 1
        else:
            for j in self.etablissement.classes:
                self.tableWidget.insertRow(k)
                self.tableWidget.setItem(k, 0, QTableWidgetItem(str(self.etablissement.nom)))
                self.tableWidget.setItem(k, 1, QTableWidgetItem(str(self.etablissement.annee)))
                self.tableWidget.setItem(k, 2, QTableWidgetItem(str(j.niveau)))
                self.tableWidget.setItem(k, 3, QTableWidgetItem(str(j.serie)))
                self.tableWidget.setItem(k, 4, QTableWidgetItem(str(j.numero)))
                self.liste_classe.append(j)
                k += 1

    def voir_classe(self):
        selected = self.tableWidget.selectedItems()
        if self.tableWidget.selectedItems():
            r = selected[0].row()
            classe = self.liste_classe[r]
            if len(classe.eleves) == 0:
                ind = self.user.reper_classe(classe)
                classe.charge_eleves()
                self.user.refresh_classe(classe, ind)
            if self.etablissement == None:
                open_class(self.user, classe, sender="eta")
            else:
                open_class(self.user, classe, etablissement=self.etablissement, sender="eta")
            MainWindow.hide()
        else:
            open_mess_ok('Information', "Vous n'avez selectionner aucune classe")

    def retour(self):
        if self.sender == None:
            open_Page_Acceuil(self.user)
        else:
            open_v_school(self.user)
        MainWindow.hide()

    def retour_acceuil(self):
        open_Page_Acceuil(self.user)
        MainWindow.hide()

    def setupUi(self, MainWindow, user, etablissement, sender):
        self.etablissement = etablissement
        self.user = user
        self.sender = sender
        self.liste_classe = []
        self.buttonReply=None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 598)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QTableWidget()
        self.tableWidget.setGeometry(QRect(10, 10, 621, 571))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "alternate-background-color: rgb(102, 255, 185);")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(15)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 639, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuClasse = QMenu(self.menubar)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.menuClasse.setFont(font)
        self.menuClasse.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.menuClasse.setObjectName("menuClasse")
        self.menuNavigation = QMenu(self.menubar)
        self.menuNavigation.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.menuNavigation.setObjectName("menuNavigation")
        MainWindow.setMenuBar(self.menubar)
        self.actionAjouter = QAction(MainWindow)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/2.0.7.png"), QIcon.Normal, QIcon.Off)
        self.actionAjouter.setIcon(icon)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionAjouter.setFont(font)
        self.actionAjouter.setObjectName("actionAjouter")
        self.actionVoir = QAction(MainWindow)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/newPrefix/2.0.6.png"), QIcon.Normal, QIcon.Off)
        self.actionVoir.setIcon(icon1)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionVoir.setFont(font)
        self.actionVoir.setObjectName("actionVoir")
        self.actionSupprimer = QAction(MainWindow)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/newPrefix/2.0.5.png"), QIcon.Normal, QIcon.Off)
        self.actionSupprimer.setIcon(icon2)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionSupprimer.setFont(font)
        self.actionSupprimer.setObjectName("actionSupprimer")
        if self.sender != None:
            self.actionRetour_L_acceuil = QAction(MainWindow)
            font = QFont()
            font.setFamily("Walkway UltraBold")
            font.setPointSize(12)
            icon4 = QIcon()
            icon4.addPixmap(QPixmap(":/newPrefix/2.08.png"), QIcon.Normal, QIcon.Off)
            self.actionRetour_L_acceuil.setIcon(icon4)
            self.actionRetour_L_acceuil.setFont(font)
            self.actionRetour_L_acceuil.setObjectName("actionRetour_L_acceuil")
            self.menuNavigation.addAction(self.actionRetour_L_acceuil)
            self.actionRetour_L_acceuil.triggered.connect(self.retour_acceuil)
        self.actionRetour = QAction(MainWindow)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/newPrefix/2.08.png"), QIcon.Normal, QIcon.Off)
        self.actionRetour.setIcon(icon3)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionRetour.setFont(font)
        self.actionRetour.setObjectName("actionRetour")
        self.menuClasse.addAction(self.actionAjouter)
        self.menuClasse.addAction(self.actionVoir)
        self.menuClasse.addAction(self.actionSupprimer)
        self.menuNavigation.addAction(self.actionRetour)
        self.menubar.addAction(self.menuClasse.menuAction())
        self.menubar.addAction(self.menuNavigation.menuAction())

        self.actionAjouter.triggered.connect(self.ajouter)
        self.actionVoir.triggered.connect(self.voir_classe)
        self.actionSupprimer.triggered.connect(self.delet)
        self.actionRetour.triggered.connect(self.retour)

        self.v = QVBoxLayout()
        self.v.addWidget(self.tableWidget)
        self.centralwidget.setLayout(self.v)

        self.retranslateUi(MainWindow, self.sender)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, sender):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Liste des classes"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nom établissement"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Année"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Niveau"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Série"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Numéro"))
        self.menuClasse.setTitle(_translate("MainWindow", "Classe"))
        self.menuNavigation.setTitle(_translate("MainWindow", "Navigation"))
        self.actionAjouter.setText(_translate("MainWindow", "Ajouter"))
        self.actionVoir.setText(_translate("MainWindow", "Voir"))
        self.actionSupprimer.setText(_translate("MainWindow", "Supprimer"))
        self.actionRetour.setText(_translate("MainWindow", "Retour"))
        if sender != None:
            self.actionRetour_L_acceuil.setText(_translate("MainWindow", "Retour à L\'acceuil"))
        self.loadDat()


#interface pour la modification des classes
class Ui_M_clas(object):
    def retour(self):
        if V_CLASSE.isHidden() == True:
            open_class(self.user,self.classe)
        else:
            ui.loadData2()
        M_clas.hide()
    def ajouter(self):
        nom2=self.nom.text()
        nom2=nom2.replace(" ","").capitalize()
        prenom2=self.lineEdit.text()
        prenom2=prenom2.capitalize()
        if nom2=="" or prenom2=="":
            open_mess_ok('Information'," Un champ est vide")
        else:
            conn,cursor=connect_db()
            cursor.execute("""UPDATE eleve SET nom="{}",prenom="{}" WHERE id='{}' """.format(nom2,prenom2,self.eleve.id))
            close_db(conn)
            self.classe.update_student(self.eleve.id,nom2,prenom2)
            self.user.refresh_classe(self.classe,self.ind)
            self.retour()
    def setupUi(self, M_clas,user,classe,eleve):
        self.classe=classe
        self.nom=self.classe.eleves
        self.user=user
        self.ind=self.user.reper_classe(self.classe)
        self.eleve=eleve
        M_clas.setMinimumSize(QSize(405, 186))
        M_clas.setMaximumSize(QSize(405, 186))
        M_clas.setObjectName("M_clas")
        M_clas.resize(405, 186)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        M_clas.setWindowIcon(icon)
        self.centralwidget = QWidget(M_clas)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(-20, -11, 431, 201))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/Sans titre - 2-02.jpg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setGeometry(QRect(156, 57, 223, 20))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.nom = QLineEdit(self.frame_2)
        self.nom.setGeometry(QRect(0, 0, 225, 20))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(14)
        self.nom.setFont(font)
        self.nom.setEchoMode(QLineEdit.Normal)
        self.nom.setClearButtonEnabled(True)
        self.nom.setObjectName("nom")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setGeometry(QRect(152, 102, 231, 20))
        self.frame_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QRect(3, 0, 225, 20))
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setGeometry(QRect(266, 159, 61, 22))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/6.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(266, 157, 61, 23))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setGeometry(QRect(334, 158, 63, 23))
        self.frame_5.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setGeometry(QRect(0, 0, 61, 23))
        self.pushButton_2.setStyleSheet("color: rgb(11, 170, 75);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.nom.setText("{}".format(self.eleve.nom))
        self.lineEdit.setText("{}".format(self.eleve.prenom))
        M_clas.setCentralWidget(self.centralwidget)

        self.retranslateUi(M_clas)
        self.pushButton.clicked.connect(self.ajouter)
        self.pushButton_2.clicked.connect(self.retour)
        QMetaObject.connectSlotsByName(M_clas)

    def retranslateUi(self, M_clas):
        _translate = QCoreApplication.translate
        M_clas.setWindowTitle(_translate("M_clas", "Modifier élève"))
        self.pushButton.setText(_translate("M_clas", "VALIDER"))
        self.pushButton_2.setText(_translate("M_clas", "ANNULER"))


#interface pour la selection d'une classe
class Ui_select_classe(object):
    def retou(self):
        select_classe.hide()

    def load_classe(self):
        for i in range(len(self.user.etablissements)):
            a = self.user.etablissements[i]
            for j in range(len(a.classes)):
                c = a.classes[j]
                self.classe.append(c)
                self.comboBox.addItem("{} {} : {}{} {}".format(a.annee, a.nom, c.niveau, c.serie, c.numero))

    def affiche(self):
        seq = self.comboBox.currentIndex()
        classe = self.classe[seq]
        classe, self.user = verif_students_in_classe(classe, self.user)
        open_class(self.user, classe)
        if Page_Acceuil.isHidden()==False:
            Page_Acceuil.hide()
        select_classe.hide()

    def setupUi(self, select_classe, user):
        self.classe = []
        self.user = user
        select_classe.setObjectName("select_classe")
        select_classe.resize(440, 173)
        select_classe.setMinimumSize(QSize(440, 173))
        select_classe.setMaximumSize(QSize(440, 173))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        select_classe.setWindowIcon(icon)
        select_classe.setStyleSheet("")
        self.centralwidget = QWidget(select_classe)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(-460, -320, 1131, 741))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/revue et correction_Plan de travail 1 copie 6.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setGeometry(QRect(610, 380, 261, 21))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setGeometry(QRect(0, 0, 261, 22))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setGeometry(QRect(828, 424, 58, 25))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.retour = QPushButton(self.frame_4)
        self.retour.setGeometry(QRect(0, 0, 58, 25))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.retour.setFont(font)
        self.retour.setCursor(QCursor(Qt.PointingHandCursor))
        self.retour.setStyleSheet("color: rgb(11, 170, 75);\n"
                                  "background-color: rgb(11, 170, 75);")
        self.retour.setObjectName("retour")
        self.afficher = QPushButton(self.frame)
        self.afficher.setGeometry(QRect(760, 425, 58, 25))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.afficher.setFont(font)
        self.afficher.setCursor(QCursor(Qt.PointingHandCursor))
        self.afficher.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                    "color: rgb(255, 255, 255);")
        self.afficher.setObjectName("afficher")
        select_classe.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_classe)
        self.afficher.clicked.connect(self.affiche)
        self.retour.clicked.connect(self.retou)
        QMetaObject.connectSlotsByName(select_classe)

    def retranslateUi(self, select_classe):
        _translate = QCoreApplication.translate
        select_classe.setWindowTitle(_translate("select_classe", "Selectionner une classe"))
        self.retour.setText(_translate("select_classe", "Annuler"))
        self.afficher.setText(_translate("select_classe", "Entrer"))
        self.load_classe()


#interface pour voir une classe et ses eleves
class Ui_V_CLASSE(object):
    def ajouter_many(self):
        open_Add_many_student(self.user, self.classe)
        V_CLASSE.hide()

    def selectee(self, classe, tri, r):
        aux = classe.eleves[0].notes[tri][r - 2]
        aux1 = r - 2
        open_clav(self.user, self.classe, aux.type, aux.numero, tri, aux1)
        V_CLASSE.hide()

    def verif(self, table, tri):
        if table.selectedItems():
            selected = table.selectedItems()
            r = selected[0].column()
            if ((r == table.columnCount() - 1) or (r == 0) or (r == table.columnCount() - 2) or (r == 1)):
                open_mess_ok('INFORMATION', "Cette colonne n'est pas une colonnes de notes")
            else:
                buttonReply = Message_y_n('Modification', "Voulez vous modifier ces notes?",self)
                if self.buttonReply == "Yes":
                    self.selectee(self.classe, tri, r)

    def modif(self):
        current = self.tabWidget.currentIndex()
        if current == 0:
            self.verif(self.tableWidget, current)
        elif current == 1:
            self.verif(self.tableWidget_2, current)
        else:
            self.verif(self.tableWidget_3, current)

    def add_note(self):
        if len(self.classe.eleves) > 0:
            open_note(self.user, self.classe)
        else:
            open_mess_ok('INFORMATION', "Il n'y a pas d'éleves dans la classe")

    def verificaion(self, tab):
        v = 0
        c = 0
        if tab.columnCount() > 2:
            if tab.selectedItems():
                selected = tab.selectedItems()
                c = selected[0].column()
                v = 1
                if c < 2 or c > (tab.columnCount() - 3):
                    open_mess_ok('Information', "Ceci n'est pas une note")
                    v = 0
            else:
                open_mess_ok('Information', "Aucune note sélectionné")
        else:
            open_mess_ok('Information', "Les éleves n'ont pas de notes")
        return v, c

    def change_note_number(self, acnote, classe):
        conn, cursor = connect_db()
        for i in classe.eleves:
            for j in i.notes[acnote.trimestre - 1]:
                if (j.type == acnote.type) and (j.numero > acnote.numero):
                    cursor.execute(""" UPDATE notes SET numero='{}' WHERE id='{}' """.format(j.numero - 1, j.id))
        close_db(conn)

    def verife_tab(self):
        current = self.tabWidget.currentIndex()
        if current == 0:
            v, c = self.verificaion(self.tableWidget)
        elif current == 1:
            v, c = self.verificaion(self.tableWidget_2)
        else:
            v, c = self.verificaion(self.tableWidget_3)
        if v == 1:
            aux = self.classe.eleves[0].notes[current][c - 2]
            buttonReply = Message_y_n('Attention!!!',
                                      "Êtes vous sûr de vouloir supprimer cette note : Trimestre{} {}{}".format(
                                                   aux.trimestre, aux.type, aux.numero),self)
            if self.buttonReply == "Yes":
                supprimer_note(c, current, self.classe)
                self.change_note_number(aux, self.classe)
                self.classe = Classe(self.classe.id)
                self.user.refresh_classe(self.classe, self.ind)
                self.loadData2()

    def modifier(self):
        if self.tableWidget.selectedItems():
            selected = self.tableWidget.selectedItems()
            r = selected[0].row()
            eleve = self.classe.eleves[r]
            buttonReply = Message_y_n('Attention!!!',
                                      "Voulez-vous modifier le nom et prenom de {} {} ?".format(
                                                   eleve.nom, eleve.prenom),self)
            if self.buttonReply == "Yes":
                open_m_class(self.user, self.classe, eleve)
        else:
            open_mess_ok('INFORMATION',"toutes modifications d'élèves se font seulement au trimestre 1 ou sementre 1")

    def delet(self):
        selected = self.tableWidget.selectedItems()
        if self.tableWidget.selectedItems():
            r = selected[0].row()
            eleve = self.classe.eleves[r]
            buttonReply = Message_y_n('ATTENTION!!!',
                                      "Vous avez selectionner  {} {}".format(eleve.nom,
                                                                                      eleve.prenom) + "\n" + " Voulez-vous supprimer cet eleve?  ",
                                      self)
            if self.buttonReply == "Yes":
                conn, cursor = connect_db()
                cursor.execute("""DELETE FROM eleve WHERE id='{}'  """.format(eleve.id))
                cursor.execute("""DELETE FROM notes WHERE id_eleve='{}'  """.format(eleve.id))
                close_db(conn)
                self.classe.delete_student(eleve)
                self.user.refresh_classe(self.classe, self.ind)
                self.loadData2()
        else:
            open_mess_ok('INFORMATION',
                        "vous ne pouvez supprimer sans cliquez " + "\n" + "pour supprimer veiller cliquez sur l'eleve dans la liste de classe au TR1/SE1")

    def retour(self):
        if self.sender == None:
            open_Page_Acceuil(self.user)
        else:
            open_ensemble(self.user, etablissement=self.etablissement)
        V_CLASSE.hide()

    def retouracceuil(self):
        open_Page_Acceuil(self.user)
        V_CLASSE.hide()

    def importation(self):
        if len(self.classe.eleves) != 0:
            open_mess_ok('Information',"vous ne pouvez pas importer la liste car il y'a des eleves dans la classe")
        else:
            fileName = QFileDialog.getOpenFileName(V_CLASSE, "Sélectionner le fichier", "", "Excel  (*.xlsx);")
            if fileName:
                if str(fileName[0]) != "":
                    trouve, empl, sheet, typ = emplacement_nom(fileName)
                    if trouve ==1:
                        importer(sheet, empl, self.classe.id, typ)
                        self.classe = Classe(self.classe.id)
                        self.user.refresh_classe(self.classe, self.ind)
                        self.loadData2()
                        open_mess_ok('Information', "Importation terminé")
                    else:
                        open_mess_ok('Information',"Il n'y a pas de colone Nom dans votre fichier excel")

    def ajouter_eleve(self):
        open_add_student(self.user, self.classe)

    def loadstudent(self, table, classe):
        table.setRowCount(0)
        table.setRowCount(len(classe.eleves))
        for row, data in enumerate(classe.eleves):
            table.setItem(row, 0, QTableWidgetItem(str(data.nom)))
            table.setItem(row, 1, QTableWidgetItem(str(data.prenom)))
        return table

    def loadnote(self, table, classe, nb, tr):
        aux2 = classe.eleves[0].notes[tr - 1]
        for i in range(nb):
            item = QTableWidgetItem()
            font = QFont()
            font.setFamily("Walkway UltraBold")
            font.setPointSize(12)
            item.setFont(font)
            aux3 = aux2[i]
            aux4 = int(20 * aux3.coefficient)
            item.setText("{}{}   /{}".format(aux3.type, aux3.numero, aux4))
            table.setHorizontalHeaderItem(i + 2, item)
            for row, data in enumerate(classe.eleves):
                data = data.notes[tr - 1][i]
                data = data.note
                if data == None:
                    data = ""
                table.setItem(row, i + 2, QTableWidgetItem(str(data)))
        for row, data in enumerate(classe.eleves):
            data2 = data.rang[tr - 1]
            data = data.moyenne[tr - 1]
            table.setItem(row, nb + 2, QTableWidgetItem("{0:.2f}".format(data)))
            table.setItem(row, nb + 3, QTableWidgetItem(str(data2)))
        return table

    def loadtable(self, table, tr):
        table.setColumnCount(2)
        aux = 0
        table = self.loadstudent(table, self.classe)
        if len(self.classe.eleves) > 0:
            aux = len(self.classe.eleves[0].notes[tr - 1])
        if aux > 0:
            table.setColumnCount(4 + aux)
            item = QTableWidgetItem()
            font = QFont()
            font.setFamily("Walkway UltraBold")
            font.setPointSize(12)
            item.setFont(font)
            item.setText("Moyenne")
            table.setHorizontalHeaderItem(aux + 2, item)
            item2 = QTableWidgetItem()
            font = QFont()
            font.setFamily("Walkway UltraBold")
            font.setPointSize(12)
            item2.setFont(font)
            item2.setText("Rang")
            table.setHorizontalHeaderItem(aux + 3, item2)
            table = self.loadnote(table, self.classe, aux, tr)
        return table

    def loadData2(self):
        self.tableWidget = self.loadtable(self.tableWidget, 1)
        self.tableWidget_2 = self.loadtable(self.tableWidget_2, 2)
        self.tableWidget_3 = self.loadtable(self.tableWidget_3, 3)

    def exportation(self):
        buttonReply = Message_y_n('ATTENTION!!!',
                                  "Voulez-vous fusionner les colonnes Nom et prenoms ?",
                                  self)
        if self.buttonReply == "Yes":
            workbook = exporter(self.tabWidget, self.etablissement, self.classe, self.user, 1)
        if self.buttonReply == "No":
            workbook = exporter(self.tabWidget, self.etablissement, self.classe, self.user, 0)
        try:
            workbook.close()
        except:
            open_mess_ok('Information', "Exportation impossible car fichier ouvert")
        else:
            open_mess_ok('Information', "Exportation terminé")

    def setupUi(self, V_CLASSE, user, classe, etablissement, sender):
        self.classe = classe
        self.user = user
        self.ind = self.user.reper_classe(self.classe)
        self.buttonReply=None
        self.etablissement = etablissement
        if self.etablissement == None:
            self.etablissement = self.user.etablissements[self.ind[0]]
        self.sender = sender
        V_CLASSE.setObjectName("V_CLASSE")
        V_CLASSE.resize(800, 600)
        V_CLASSE.setStyleSheet("background-color: rgb(11, 170, 75);")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        V_CLASSE.setWindowIcon(icon)
        V_CLASSE.setStyleSheet("background-color: rgb(75, 170, 75);")
        self.centralwidget = QWidget(V_CLASSE)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QTabWidget()
        self.tabWidget.setGeometry(QRect(0, 10, 751, 561))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QTableWidget()
        self.v1 = QVBoxLayout()
        self.v1.addWidget(self.tableWidget)
        self.tab.setLayout(self.v1)
        self.tableWidget.setGeometry(QRect(0, 0, 751, 531))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QTableWidget()
        self.v2 = QVBoxLayout()
        self.v2.addWidget(self.tableWidget_2)
        self.tab_2.setLayout(self.v2)
        self.tableWidget_2.setGeometry(QRect(0, 0, 751, 531))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QTableWidget()
        self.v3 = QVBoxLayout()
        self.v3.addWidget(self.tableWidget_3)
        self.tab_3.setLayout(self.v3)
        self.tableWidget_3.setGeometry(QRect(0, 0, 751, 531))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setRowCount(0)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.tab_3, "")
        self.menubar = QMenuBar(V_CLASSE)
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.menubar.setObjectName("menubar")
        self.menuEl_ve = QMenu(self.menubar)
        self.menuEl_ve.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.menuEl_ve.setObjectName("menuEl_ve")
        self.menuNote = QMenu(self.menubar)
        self.menuNote.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.menuNote.setObjectName("menuNote")
        self.menuExcel = QMenu(self.menubar)
        self.menuExcel.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.menuExcel.setObjectName("menuExcel")
        self.menuAutre = QMenu(self.menubar)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.menuAutre.setFont(font)
        self.menuAutre.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.menuAutre.setObjectName("menuAutre")
        V_CLASSE.setMenuBar(self.menubar)
        self.actionAjouter = QAction(V_CLASSE)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/2.0.7.png"), QIcon.Normal, QIcon.Off)
        self.actionAjouter.setIcon(icon)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionAjouter.setFont(font)
        self.actionAjouter.setObjectName("actionAjouter")
        self.actionAjouter_plusieurs_l_ves = QAction(V_CLASSE)
        self.actionAjouter_plusieurs_l_ves.setIcon(icon)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionAjouter_plusieurs_l_ves.setFont(font)
        self.actionAjouter_plusieurs_l_ves.setObjectName("actionAjouter_plusieurs_l_ves")
        self.actionModifier_un_l_ve = QAction(V_CLASSE)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/newPrefix/2.0.6.png"), QIcon.Normal, QIcon.Off)
        self.actionModifier_un_l_ve.setIcon(icon1)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionModifier_un_l_ve.setFont(font)
        self.actionModifier_un_l_ve.setObjectName("actionModifier_un_l_ve")
        self.actionSupprimer_un_l_ve = QAction(V_CLASSE)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/newPrefix/2.0.5.png"), QIcon.Normal, QIcon.Off)
        self.actionSupprimer_un_l_ve.setIcon(icon2)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionSupprimer_un_l_ve.setFont(font)
        self.actionSupprimer_un_l_ve.setObjectName("actionSupprimer_un_l_ve")
        self.actionAjouter_note = QAction(V_CLASSE)
        self.actionAjouter_note.setIcon(icon)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionAjouter_note.setFont(font)
        self.actionAjouter_note.setObjectName("actionAjouter_note")
        self.actionModifier_note = QAction(V_CLASSE)
        self.actionModifier_note.setIcon(icon1)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionModifier_note.setFont(font)
        self.actionModifier_note.setObjectName("actionModifier_note")
        self.actionSupprimer = QAction(V_CLASSE)
        self.actionSupprimer.setIcon(icon2)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionSupprimer.setFont(font)
        self.actionSupprimer.setObjectName("actionSupprimer")
        self.actionImportation_de_la_liste_de_classe = QAction(V_CLASSE)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/newPrefix/excel.png"), QIcon.Normal, QIcon.Off)
        self.actionImportation_de_la_liste_de_classe.setIcon(icon3)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionImportation_de_la_liste_de_classe.setFont(font)
        self.actionImportation_de_la_liste_de_classe.setObjectName("actionImportation_de_la_liste_de_classe")
        self.actionExportation_d_excel = QAction(V_CLASSE)
        self.actionExportation_d_excel.setIcon(icon3)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionExportation_d_excel.setFont(font)
        self.actionExportation_d_excel.setObjectName("actionExportation_d_excel")
        self.actionRetour = QAction(V_CLASSE)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/newPrefix/2.08.png"), QIcon.Normal, QIcon.Off)
        self.actionRetour.setFont(font)
        self.actionRetour.setIcon(icon4)
        self.actionRetour.setObjectName("actionRetour")
        if self.sender != None:
            self.actionRetourAcceuil = QAction(V_CLASSE)
            self.actionRetourAcceuil.setIcon(icon4)
            self.actionRetourAcceuil.setFont(font)
            self.actionRetourAcceuil.setObjectName("actionRetourAcceuil")
        self.menuEl_ve.addAction(self.actionAjouter)
        self.menuEl_ve.addAction(self.actionAjouter_plusieurs_l_ves)
        self.menuEl_ve.addAction(self.actionModifier_un_l_ve)
        self.menuEl_ve.addAction(self.actionSupprimer_un_l_ve)
        self.menuNote.addAction(self.actionAjouter_note)
        self.menuNote.addAction(self.actionModifier_note)
        self.menuNote.addAction(self.actionSupprimer)
        self.menuExcel.addAction(self.actionImportation_de_la_liste_de_classe)
        self.menuExcel.addAction(self.actionExportation_d_excel)
        self.menuAutre.addAction(self.actionRetour)
        self.menubar.addAction(self.menuEl_ve.menuAction())
        self.menubar.addAction(self.menuNote.menuAction())
        self.menubar.addAction(self.menuExcel.menuAction())
        self.menubar.addAction(self.menuAutre.menuAction())

        self.actionImportation_de_la_liste_de_classe.triggered.connect(self.importation)
        self.actionExportation_d_excel.triggered.connect(self.exportation)
        self.actionAjouter.triggered.connect(self.ajouter_eleve)

        self.actionAjouter_plusieurs_l_ves.triggered.connect(self.ajouter_many)

        self.actionModifier_un_l_ve.triggered.connect(self.modifier)
        self.actionSupprimer_un_l_ve.triggered.connect(self.delet)
        self.actionAjouter_note.triggered.connect(self.add_note)
        self.actionModifier_note.triggered.connect(self.modif)
        self.actionSupprimer.triggered.connect(self.verife_tab)
        self.actionRetour.triggered.connect(self.retour)
        if self.sender != None:
            self.actionRetourAcceuil.triggered.connect(self.retouracceuil)

        self.v = QVBoxLayout()
        self.v.addWidget(self.tabWidget)
        self.centralwidget.setLayout(self.v)
        V_CLASSE.setCentralWidget(self.centralwidget)
        self.tabWidget.setCurrentIndex(0)

        self.retranslateUi(V_CLASSE, self.sender)
        QMetaObject.connectSlotsByName(V_CLASSE)

    def retranslateUi(self, V_CLASSE, sender):
        _translate = QCoreApplication.translate
        V_CLASSE.setWindowTitle(_translate("V_CLASSE", "{} {}-{}  {}{} {}".format(self.etablissement.nom,self.etablissement.annee,self.etablissement.annee+1,self.classe.niveau,
                                                                                 self.classe.serie,self.classe.numero)))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("V_CLASSE", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("V_CLASSE", "Prenoms"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("V_CLASSE", " Trim/Sem 1"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("V_CLASSE", "Nom"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("V_CLASSE", "Prenoms"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("V_CLASSE", "Trim/Sem 2"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("V_CLASSE", "Nom"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("V_CLASSE", "Prenoms"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("V_CLASSE", "Trimestre 3"))
        self.menuEl_ve.setTitle(_translate("V_CLASSE", "Elève"))
        self.menuNote.setTitle(_translate("V_CLASSE", "Note"))
        self.menuExcel.setTitle(_translate("V_CLASSE", "Excel"))
        self.menuAutre.setTitle(_translate("V_CLASSE", "Autre"))
        self.actionAjouter.setText(_translate("V_CLASSE", "Ajouter un élève"))
        self.actionAjouter_plusieurs_l_ves.setText(_translate("V_CLASSE", "Ajouter plusieurs élèves"))
        self.actionModifier_un_l_ve.setText(_translate("V_CLASSE", "Modifier un élève"))
        self.actionSupprimer_un_l_ve.setText(_translate("V_CLASSE", "Supprimer un élève"))
        self.actionAjouter_note.setText(_translate("V_CLASSE", "Ajouter note"))
        self.actionModifier_note.setText(_translate("V_CLASSE", "Modifier note"))
        self.actionSupprimer.setText(_translate("V_CLASSE", "Supprimer"))
        self.actionImportation_de_la_liste_de_classe.setText(
            _translate("V_CLASSE", "Importation de la liste de classe"))
        self.actionExportation_d_excel.setText(_translate("V_CLASSE", "Exportation vers excel"))
        self.actionRetour.setText(_translate("V_CLASSE", "Retour"))
        if sender != None:
            self.actionRetourAcceuil.setText(_translate("V_CLASSE", "Retour à l'acceuil"))
            self.actionRetourAcceuil.setToolTip(_translate("V_CLASSE", "Retour"))


#interface pour ajouter un eleve
class Ui_Add_student(object):
    def retour(self):
        if V_CLASSE.isHidden()==True:
            open_class(self.user, self.classe)
        ui.loadData2()
        Add_student.hide()

    def note(self, id_eleve, cursor):
        if len(self.classe.eleves) > 0:
            for i in self.classe.eleves[0].notes:
                if len(i) > 0:
                    for j in i:
                        cursor.execute(
                            """INSERT INTO notes(id_eleve,type,coefficient,trimestre,numero,date,id_classe) VALUES("{}","{}","{}","{}","{}","{}","{}")""".format(
                                id_eleve, j.type, j.coefficient, j.trimestre, j.numero, j.date, j.id_classe))

    def ajouter(self):
        nom2 = self.nom.text()
        aux = nom2.split(" ")
        if len(aux) > 1:
            open_mess_ok('INFORMATION', "Le nom entrée est invalide")
        else:
            nom2 = nom2.replace(" ", "").capitalize()
            prenom2 = self.lineEdit.text()
            if nom2 == "" or prenom2 == "":
                open_mess_ok('INFORMATION', " un champ est vide")
            else:
                prenom2 = prenom2.split(" ")
                for i in range(len(prenom2)):
                    aux2 = prenom2[i]
                    aux2 = aux2.capitalize()
                    prenom2[i] = aux2
                prenom2 = " ".join(prenom2)
                conn, cursor = connect_db()
                cursor.execute(
                    """INSERT INTO eleve(id_classe,nom,prenom) VALUES('{}',"{}","{}")""".format(self.classe.id, nom2,
                                                                                                prenom2))
                id_eleve = cursor.lastrowid
                self.note(id_eleve, cursor)
                eleve = Eleve(id_eleve, cursor=cursor, stop=0)
                close_db(conn)
                self.classe.add_student(eleve)
                self.user.refresh_classe(self.classe, self.ind)
                self.retour()

    def setupUi(self, Add_student, user, classe):
        self.classe = classe
        self.user = user
        self.ind = self.user.reper_classe(self.classe)
        self.buttonReply=None
        Add_student.setMinimumSize(QSize(405, 186))
        Add_student.setMaximumSize(QSize(405, 186))
        Add_student.setObjectName("Add_student")
        Add_student.resize(405, 186)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        Add_student.setWindowIcon(icon)
        self.centralwidget = QWidget(Add_student)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(-20, -11, 431, 201))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/Sans titre - 2-02.jpg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setGeometry(QRect(156, 57, 223, 20))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.nom = QLineEdit(self.frame_2)
        self.nom.setGeometry(QRect(0, 0, 225, 20))
        self.nom.setEchoMode(QLineEdit.Normal)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(14)
        self.nom.setFont(font)
        self.nom.setClearButtonEnabled(True)
        self.nom.setObjectName("nom")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setGeometry(QRect(152, 102, 231, 20))
        self.frame_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QRect(3, 0, 225, 20))
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setGeometry(QRect(266, 159, 61, 22))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/6.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(266, 157, 61, 23))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setGeometry(QRect(334, 158, 63, 23))
        self.frame_5.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setGeometry(QRect(0, 0, 61, 23))
        self.pushButton_2.setStyleSheet("color: rgb(11, 170, 75);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        Add_student.setCentralWidget(self.centralwidget)

        self.retranslateUi(Add_student)
        self.pushButton.clicked.connect(self.ajouter)
        self.pushButton_2.clicked.connect(self.retour)
        QMetaObject.connectSlotsByName(Add_student)

    def retranslateUi(self, Add_student):
        _translate = QCoreApplication.translate
        Add_student.setWindowTitle(_translate("Add_student", "Ajouter un élève"))
        self.pushButton.setText(_translate("Add_student", "VALIDER"))
        self.pushButton_2.setText(_translate("Add_student", "ANNULER"))


#interface pour ajouter plusieurs eleves
class Ui_Add_many_student(object):
    def verife(self, table):
        valide = 0
        for j in range(2):
            for i in range(table.rowCount()):
                data = table.item(i, j)
                if data == None:
                    valide = 1
                else:
                    data = data.data(0)
                    if data == "":
                        if valide < 2:
                            valide = 1
        return valide

    def verifier(self, table, r):
        valide = 0
        for j in range(2):
            data = table.item(r, j)
            if data == None:
                valide = 1
            else:
                data = data.data(0)
                if data == "":
                    valide = 1
        return valide

    def retour(self):
        open_class(self.user, self.classe)
        Add_many_student.hide()

    def note(self, id_eleve, cursor):
        if len(self.classe.eleves) > 0:
            for i in self.classe.eleves[0].notes:
                if len(i) > 0:
                    for j in i:
                        cursor.execute(
                            """INSERT INTO notes(id_eleve,type,coefficient,trimestre,numero,date,id_classe) VALUES("{}","{}","{}","{}","{}","{}","{}")""".format(
                                id_eleve, j.type, j.coefficient, j.trimestre, j.numero, j.date, j.id_classe))

    def add_student(self, cursor, id_classe, nom, prenom):
        cursor.execute(
            """INSERT INTO eleve(id_classe,nom,prenom) VALUES('{}',"{}","{}")""".format(id_classe, nom, prenom))
        id_eleve = cursor.lastrowid
        self.note(id_eleve, cursor)
        eleve = Eleve(id_eleve, cursor=cursor, stop=0)
        self.classe.add_student(eleve)

    def enre(self, cursor, table, id_classe):
        for r in range(table.rowCount()):
            v = self.verifier(table, r)
            if v == 0:
                nom2 = table.item(r, 0)
                nom2 = nom2.data(0)
                aux = nom2.split(" ")
                if len(aux) > 1:
                    continue
                nom2 = nom2.replace(" ", "").capitalize()
                prenom2 = table.item(r, 1)
                prenom2 = prenom2.data(0)
                prenom2 = prenom2.split(" ")
                for i in range(len(prenom2)):
                    aux2 = prenom2[i]
                    aux2 = aux2.capitalize()
                    prenom2[i] = aux2
                prenom2 = " ".join(prenom2)
                self.add_student(cursor, id_classe, nom2, prenom2)

    def ajouter(self):
        valide = self.verife(self.tableWidget)
        if valide == 0:
            conn, cursor = connect_db()
            self.enre(cursor, self.tableWidget, self.classe.id)
            close_db(conn)
            self.user.refresh_classe(self.classe, self.ind)
            self.retour()
        else:
            buttonReply = Message_y_n('INFORMATION',
                                      "Des cases sont vides\nVoulez vous qu'à même procéder à l'enregistrement?",
                                      self)
            if self.buttonReply == "Yes":
                conn, cursor = connect_db()
                self.enre(cursor, self.tableWidget, self.classe.id)
                close_db(conn)
                self.user.refresh_classe(self.classe, self.ind)
                self.retour()

    def plus(self):
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)

    def moins(self):
        if self.tableWidget.rowCount() > 0:
            self.tableWidget.setRowCount(self.tableWidget.rowCount() - 1)

    def setupUi(self, Add_many_student, user, classe):
        self.classe = classe
        self.user = user
        self.ind = self.user.reper_classe(self.classe)
        self.buttonReply=None
        Add_many_student.setObjectName("Add_many_student")
        Add_many_student.resize(800, 600)
        Add_many_student.setStyleSheet("background-color: rgb(11, 170, 75);")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        Add_many_student.setWindowIcon(icon)
        self.v = QVBoxLayout()
        self.v.setObjectName("v")
        self.centralwidget = QWidget(Add_many_student)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QTableWidget()
        self.tableWidget.setGeometry(QRect(10, 10, 771, 611))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "alternate-background-color: rgb(102, 255, 185);")
        self.tableWidget.setEditTriggers(
            QAbstractItemView.AnyKeyPressed | QAbstractItemView.CurrentChanged | QAbstractItemView.EditKeyPressed)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        Add_many_student.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(Add_many_student)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.toolBar.setFont(font)
        self.toolBar.setFocusPolicy(Qt.StrongFocus)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet("background-color: rgb(11, 170, 75);\n"
                                   "alternate-background-color: rgb(11, 170, 75);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        Add_many_student.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.actionAjouter = QAction(Add_many_student)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/AJOUTER.png"), QIcon.Normal, QIcon.Off)
        self.actionAjouter.setIcon(icon)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionAjouter.setFont(font)
        self.actionAjouter.setObjectName("actionAjouter")
        self.actionRetour = QAction(Add_many_student)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/newPrefix/RETOUR.png"), QIcon.Normal, QIcon.Off)
        self.actionRetour.setIcon(icon4)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionRetour.setFont(font)
        self.actionRetour.setObjectName("actionRetour")
        self.actionEnregistrer = QAction(Add_many_student)
        self.actionEnregistrer.setCheckable(False)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/newPrefix/icon_Plan de travail 1 copie.png"), QIcon.Normal,
                        QIcon.Off)
        self.actionEnregistrer.setIcon(icon3)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionEnregistrer.setFont(font)
        self.actionEnregistrer.setVisible(True)
        self.actionEnregistrer.setMenuRole(QAction.TextHeuristicRole)
        self.actionEnregistrer.setIconVisibleInMenu(True)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionSupprimer_2 = QAction(Add_many_student)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(":/newPrefix/icon-06.png"), QIcon.Normal, QIcon.Off)
        self.actionSupprimer_2.setIcon(icon5)
        font = QFont()
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
        QMetaObject.connectSlotsByName(Add_many_student)

    def retranslateUi(self, Add_many_student):
        _translate = QCoreApplication.translate
        Add_many_student.setWindowTitle(
            _translate("Add_many_student", "{}{}{}".format(self.classe.niveau, self.classe.serie, self.classe.numero)))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Add_many_student", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Add_many_student", "Prénoms"))
        self.toolBar.setWindowTitle(_translate("Add_many_student", "toolBar"))
        self.actionAjouter.setText(_translate("Add_many_student", "Ajouter"))
        self.actionAjouter.setToolTip(_translate("Add_many_student",
                                                 "<html><head/><body><p><span style=\" font-size:12pt;\">Ajouter</span></p></body></html>"))
        self.actionRetour.setText(_translate("Add_many_student", "Retour"))
        self.actionRetour.setToolTip(_translate("Add_many_student",
                                                "<html><head/><body><p><span style=\" font-size:12pt;\">Retour</span></p></body></html>"))
        self.actionEnregistrer.setText(_translate("Add_many_student", "Enregistrer"))
        self.actionEnregistrer.setToolTip(_translate("Add_many_student",
                                                     "<html><head/><body><p><span style=\" font-size:12pt;\">Enregistrer</span></p></body></html>"))
        self.actionSupprimer_2.setText(_translate("Add_many_student", "Retirer"))
        self.actionSupprimer_2.setToolTip(_translate("Add_many_student",
                                                     "<html><head/><body><p><span style=\" font-size:12pt;\">Retirer</span></p></body></html>"))


class Ui_Dialog(object):
    def change(self):
        self.spinBox.setSuffix("-{}".format(self.spinBox.value()+1))

    def retour(self):
        if Page_Acceuil.isHidden()==True:
            open_Page_Acceuil(self.user)
        Dialog.hide()

    def retour_to_SL(self):
        if V_ETABLISSEMENT.isHidden()==True:
            open_v_school(self.user)
        else:
            ui.loadData()
        Dialog.hide()

    def ajouter_to_SL(self):
        nom2 = self.lineEdit.text()
        annee = self.spinBox.value()
        if nom2 == "":
            open_mess_ok('INFORMATION', " un champ est vide")
        else:
            conn, cursor = connect_db()
            cursor.execute("""SELECT * FROM etablissement WHERE  nom="{}" AND annee='{}' """.format(nom2, annee))
            id_eta = cursor.fetchall()
            close_db(conn)
            if len(id_eta) != 0:
                open_mess_ok('Information',"cette etablissement existe vous ne pouvez le cree")
            else:
                conn, cursor = connect_db()
                cursor.execute("""INSERT INTO etablissement(nom,annee) VALUES("{}",'{}')""".format(nom2, annee))
                eta = Etablissement(cursor.lastrowid, cursor=cursor, stop=0)
                close_db(conn)
                self.user.add_school(eta)
                self.retour_to_SL()

    def ajouter(self):
        nom2 = self.lineEdit.text()
        annee = self.spinBox.value()
        if nom2 == "":
            open_mess_ok('Information', " un champ est vide")
        else:
            conn, cursor = connect_db()
            cursor.execute("""SELECT * FROM etablissement WHERE nom="{}" AND annee='{}' """.format(nom2, annee))
            id_eta = cursor.fetchall()
            close_db(conn)
            if len(id_eta) != 0:
                open_mess_ok('Information',"cette etablissement existe vous ne pouvez le cree")
            else:
                conn, cursor = connect_db()
                cursor.execute("""INSERT INTO etablissement(nom,annee) VALUES("{}",'{}')""".format(nom2, annee))
                eta = Etablissement(cursor.lastrowid, cursor=cursor, stop=0)
                close_db(conn)
                self.user.add_school(eta)
                self.retour()

    def setupUi(self, Dialog, user):
        self.user = user
        self.buttonReply=None
        Dialog.setObjectName("Dialog")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.resize(390, 185)
        Dialog.setMaximumSize(QSize(390, 185))
        Dialog.setMinimumSize(QSize(390, 185))
        Dialog.setAcceptDrops(False)
        Dialog.setDocumentMode(False)
        Dialog.setTabShape(QTabWidget.Rounded)
        Dialog.setDockNestingEnabled(False)
        Dialog.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(-430, -250, 1051, 631))
        self.widget.setStyleSheet("border-image: url(:/newPrefix/revue et correction_Plan de travail 1 copie 7.png);")
        self.widget.setObjectName("widget")
        self.frame = QFrame(self.widget)
        self.frame.setGeometry(QRect(570, 296, 211, 21))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setGeometry(QRect(0, 0, 214, 20))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setGeometry(QRect(569, 343, 211, 20))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.spinBox = QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QRect(0, 0, 211, 22))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.a = datetime.date.today().year
        self.spinBox.setMaximum(self.a)
        self.spinBox.setMinimum(2000)
        self.spinBox.setValue(self.a)
        self.spinBox.valueChanged.connect(self.change)
        self.frame.raise_()
        self.spinBox.raise_()
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setGeometry(QRect(672, 404, 55, 21))
        self.frame_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setGeometry(QRect(0, 0, 55, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(11, 170, 75);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-image: url(:/newPrefix/6.png);")
        self.pushButton.setObjectName("pushButton")
        self.frame_4 = QFrame(self.widget)
        self.frame_4.setGeometry(QRect(738, 403, 51, 20))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setGeometry(QRect(0, 0, 51, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(11, 170, 75);")
        self.pushButton_2.setObjectName("pushButton_2")
        Dialog.setCentralWidget(self.centralwidget)
        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ajouter un établissement"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Devmax"))
        self.spinBox.setSuffix(_translate("Dialog", "-{}").format(str(self.a + 1)))
        self.pushButton.setText(_translate("Dialog", "Entrer"))
        self.pushButton_2.setText(_translate("Dialog", "Annuler"))


#interface pour voir la liste des etablissemens
class Ui_V_ETABLISSEMENT(object):
    def test(self):
        selected = self.tableWidget.selectedItems()
        a = selected[0].row()
        c = selected[0].column() + 1
        b = self.tableWidget.item(a, c)

    def lister(self):
        selected = self.tableWidget.selectedItems()
        if self.tableWidget.selectedItems():
            r = selected[0].row()
            eta = self.list_id[r]
            open_ensemble(user=self.u, etablissement=eta, sender="eta")
        else:
            open_ensemble(user=self.u, sender="eta")
        V_ETABLISSEMENT.hide()

    def loadData(self):
        self.tableWidget.setRowCount(0)
        self.list_id.clear()
        for row_number, data in enumerate(self.u.etablissements):
            self.tableWidget.insertRow(row_number)
            self.list_id.append(data)
            self.tableWidget.setItem(row_number, 0, QTableWidgetItem(data.nom))
            self.tableWidget.setItem(row_number, 1, QTableWidgetItem(str(data.annee)))
            self.tableWidget.setItem(row_number, 2, QTableWidgetItem(str(len(data.classes))))

    def delete(self):
        selected = self.tableWidget.selectedItems()
        if self.tableWidget.selectedItems():
            r = selected[0].row()
            eta = self.list_id[r]
            buttonReply = Message_y_n('ATTENTION!!!',"Voulez-vous supprimer cette établissement({} {})?".format(eta.nom,
                                                                                                         eta.annee),
                                      self)
            if self.buttonReply == "Yes":
                conn, cursor = connect_db()
                for i in eta.classes:
                    for j in i.eleves:
                        cursor.execute("""DELETE FROM notes WHERE id_eleve='{}' """.format(j.id))
                    cursor.execute("""DELETE FROM eleve WHERE id_classe='{}' """.format(i.id))
                cursor.execute("""DELETE FROM classe WHERE id_etablissement='{}' """.format(eta.id))
                cursor.execute("""DELETE FROM etablissement WHERE id='{}' """.format(eta.id))
                close_db(conn)
                self.u.delete_school(eta)
                self.loadData()
        else:
            open_mess_ok('INFORMATION', "vous ne pouvez supprimer sans cliquez")

    def modifier(self):
        selected = self.tableWidget.selectedItems()
        if self.tableWidget.selectedItems():
            r = selected[0].row()
            eta = self.list_id[r]
            open_modif_eta(self.u, eta)
        else:
            open_mess_ok('INFORMATION', "vous ne pouvez modifier sans cliquez")

    def open_add_school(self):
        open_add_school(self.u)
        uim.pushButton.clicked.connect(uim.ajouter_to_SL)
        uim.pushButton_2.clicked.connect(uim.retour_to_SL)

    def retour(self):
        open_Page_Acceuil(self.u)
        V_ETABLISSEMENT.hide()

    def setupUi(self, V_ETABLISSEMENT, user):
        self.u = user
        self.list_id = []
        self.buttonReply=None
        V_ETABLISSEMENT.setObjectName("V_ETABLISSEMENT")
        V_ETABLISSEMENT.resize(656, 553)
        V_ETABLISSEMENT.setStyleSheet("background-color: rgb(11, 170, 75);")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        V_ETABLISSEMENT.setWindowIcon(icon)
        self.centralwidget = QWidget(V_ETABLISSEMENT)
        self.centralwidget.setObjectName("centralwidget")
        V_ETABLISSEMENT.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(V_ETABLISSEMENT)
        self.menuBar.setGeometry(QRect(0, 0, 656, 21))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.menuBar.setFont(font)
        self.menuBar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "alternate-background-color: rgb(0, 0, 0);")
        self.menuBar.setObjectName("menuBar")
        self.menuAjouter = QMenu(self.menuBar)
        self.menuAjouter.setStyleSheet("background-color: rgb(102, 255, 185);\n"
                                       "background-color: rgb(11, 170, 75);")
        self.menuAjouter.setObjectName("menuAjouter")
        self.menuNavigation = QMenu(self.menuBar)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.menuNavigation.setFont(font)
        self.menuNavigation.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.menuNavigation.setObjectName("menuNavigation")
        V_ETABLISSEMENT.setMenuBar(self.menuBar)
        self.actionAjouter = QAction(V_ETABLISSEMENT)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/2.0.7.png"), QIcon.Normal, QIcon.Off)
        self.actionAjouter.setIcon(icon)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionAjouter.setFont(font)
        self.actionAjouter.setObjectName("actionAjouter")
        self.actionVoir = QAction(V_ETABLISSEMENT)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/newPrefix/2.0.6.png"), QIcon.Normal, QIcon.Off)
        self.actionVoir.setIcon(icon1)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionVoir.setFont(font)
        self.actionVoir.setObjectName("actionVoir")
        self.actionSupprimer = QAction(V_ETABLISSEMENT)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/newPrefix/2.0.5.png"), QIcon.Normal, QIcon.Off)
        self.actionSupprimer.setIcon(icon2)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionSupprimer.setFont(font)
        self.actionSupprimer.setObjectName("actionSupprimer")
        self.actionListe_de_classes = QAction(V_ETABLISSEMENT)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/newPrefix/2.0.1.png"), QIcon.Normal, QIcon.Off)
        self.actionListe_de_classes.setIcon(icon3)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionListe_de_classes.setFont(font)
        self.actionListe_de_classes.setObjectName("actionListe_de_classes")
        self.actionRetour = QAction(V_ETABLISSEMENT)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/newPrefix/2.08.png"), QIcon.Normal, QIcon.Off)
        self.actionRetour.setIcon(icon4)
        self.actionRetour.setObjectName("actionRetour")
        self.menuAjouter.addAction(self.actionAjouter)
        self.menuAjouter.addAction(self.actionVoir)
        self.menuAjouter.addAction(self.actionSupprimer)
        self.menuNavigation.addAction(self.actionListe_de_classes)
        self.menuNavigation.addAction(self.actionRetour)
        self.menuBar.addAction(self.menuAjouter.menuAction())
        self.menuBar.addAction(self.menuNavigation.menuAction())
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget = QTableWidget()
        self.tableWidget.setFont(font)
        self.tableWidget.setGeometry(QRect(0, 0, 521, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "alternate-background-color: rgb(102, 255, 185);")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.actionAjouter.triggered.connect(self.open_add_school)
        self.actionVoir.triggered.connect(self.modifier)
        self.actionSupprimer.triggered.connect(self.delete)
        self.actionRetour.triggered.connect(self.retour)
        self.actionListe_de_classes.triggered.connect(self.lister)
        self.v = QVBoxLayout()
        self.v.addWidget(self.tableWidget)
        self.centralwidget.setLayout(self.v)
        self.retranslateUi(V_ETABLISSEMENT)
        QMetaObject.connectSlotsByName(V_ETABLISSEMENT)

    def retranslateUi(self, V_ETABLISSEMENT):
        _translate = QCoreApplication.translate
        V_ETABLISSEMENT.setWindowTitle(_translate("V_ETABLISSEMENT", "Liste des établissements"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("V_ETABLISSEMENT", "   Nom Etablissement"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("V_ETABLISSEMENT", "Annee"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("V_ETABLISSEMENT", "Nombre Classe"))
        self.menuNavigation.setTitle(_translate("V_ETABLISSEMENT", "Navigation"))
        self.menuAjouter.setTitle(_translate("V_ETABLISSEMENT", "Etablissement"))
        self.actionRetour.setText(_translate("V_ETABLISSEMENT", "Retour"))
        self.actionRetour.setToolTip(_translate("V_ETABLISSEMENT", "Retour à la page d\'acceuil"))
        self.actionListe_de_classes.setText(_translate("V_ETABLISSEMENT", "Liste des classes"))
        self.actionListe_de_classes.setToolTip(
            _translate("V_ETABLISSEMENT", "Afficher la liste des classes de l\'établissement"))
        self.actionAjouter.setText(_translate("V_ETABLISSEMENT", "Ajouter"))
        self.actionAjouter.setToolTip(_translate("V_ETABLISSEMENT", "Ajouter un établissement"))
        self.actionVoir.setText(_translate("V_ETABLISSEMENT", "Modifier"))
        self.actionVoir.setToolTip(_translate("V_ETABLISSEMENT", "Modifier un établissement"))
        self.actionSupprimer.setText(_translate("V_ETABLISSEMENT", "Supprimer"))
        self.actionSupprimer.setToolTip(_translate("V_ETABLISSEMENT", "Supprimer un établissement"))
        self.loadData()


#interface pour modifier un etablissement
class Ui_M_eta(object):
    def change(self):
        self.spinBox.setSuffix("-{}".format(self.spinBox.value()+1))

    def retour(self):
        if V_ETABLISSEMENT.isHidden()==True:
            open_v_school(self.user)
        else:
            ui.loadData()
        M_eta.hide()

    def modifier(self):
        nom2=self.lineEdit.text()
        annee=self.spinBox.value()
        if nom2=="":
            open_mess_ok('INFORMATION'," un champ est vide")
        else:
            conn,cursor=connect_db()
            cursor.execute("""UPDATE etablissement SET nom="{}",annee='{}' WHERE id='{}' """.format(nom2,annee,self.etablissement.id))
            close_db(conn)
            self.etablissement.nom=nom2
            self.etablissement.annee=annee
            self.user.update_school(self.etablissement)
            self.retour()

    def setupUi(self, M_eta,user,eta):
        self.etablissement=eta
        self.user=user
        M_eta.setObjectName("M_eta")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        M_eta.setWindowIcon(icon)
        M_eta.resize(390, 185)
        M_eta.setMaximumSize(QSize(390, 185))
        M_eta.setMinimumSize(QSize(390, 185))
        M_eta.setAcceptDrops(False)
        M_eta.setTabShape(QTabWidget.Rounded)
        M_eta.setDockNestingEnabled(False)
        M_eta.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(M_eta)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QRect(-430, -250, 1051, 631))
        self.widget.setStyleSheet("border-image: url(:/newPrefix/revue et correction_Plan de travail 1 copie 7.png);")
        self.widget.setObjectName("widget")
        self.frame = QFrame(self.widget)
        self.frame.setGeometry(QRect(570, 296, 211, 21))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setGeometry(QRect(0, 0, 214, 20))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(self.etablissement.nom)
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setGeometry(QRect(569, 343, 211, 20))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.spinBox = QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QRect(0, 0, 211, 22))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.a = datetime.date.today().year
        self.spinBox.setMaximum(self.a)
        self.spinBox.setMinimum(2000)
        self.spinBox.setValue(self.etablissement.annee)
        self.spinBox.valueChanged.connect(self.change)
        self.frame.raise_()
        self.spinBox.raise_()
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setGeometry(QRect(672, 404, 55, 21))
        self.frame_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setGeometry(QRect(0, 0, 55, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(11, 170, 75);\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "border-image: url(:/newPrefix/6.png);")
        self.pushButton.setObjectName("pushButton")
        self.frame_4 = QFrame(self.widget)
        self.frame_4.setGeometry(QRect(738, 403, 51, 20))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setGeometry(QRect(0, 0, 51, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(11, 170, 75);")
        self.pushButton_2.setObjectName("pushButton_2")
        M_eta.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.modifier)
        self.pushButton_2.clicked.connect(self.retour)

        self.retranslateUi(M_eta)
        QMetaObject.connectSlotsByName(M_eta)

    def retranslateUi(self, M_eta):
        _translate = QCoreApplication.translate
        M_eta.setWindowTitle(_translate("M_eta", "EDU-Classeur"))
        self.lineEdit.setPlaceholderText(_translate("M_eta", "Devmax"))
        self.spinBox.setSuffix(_translate("M_eta", "-{}").format(str(self.etablissement.annee + 1)))
        self.pushButton.setText(_translate("M_eta", "Entrer"))
        self.pushButton_2.setText(_translate("M_eta", "Annuler"))


#interface pour ajouter une note
class Ui_V_CLASSE_2(object):
    def select(self):
        valide,list,ligne = verife_table_note(self.tableWidget)
        if valide == 0:
            enregistrement(self.classe, self.tableWidget, list, self.thype, float(self.coef), self.tri, self.num)
            self.classe = Classe(self.classe.id)
            self.user.refresh_classe(self.classe, self.ind)
            self.retour()
        elif valide == 1:
            buttonReply = Message_y_n('Validation',
                                      "Des élèves ont des notes vides\nVoulez vous procéder à l'enregistrement ?",
                                      self)
            if self.buttonReply == "Yes":
                enregistrement(self.classe, self.tableWidget, list, self.thype, self.coef, self.tri, self.num)
                self.classe = Classe(self.classe.id)
                self.user.refresh_classe(self.classe, self.ind)
                self.retour()
        else:
            open_mess_ok('Information', "Note invalide à la ligne {}".format(ligne))

    def retour(self):
        open_class(self.user, self.classe)
        V_CLASSE_2.hide()

    def loadstudent(self, table, classe):
        table.setRowCount(0)
        for row, data in enumerate(classe.eleves):
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(str(data.nom)))
            table.setItem(row, 1, QTableWidgetItem(str(data.prenom)))
        return table

    def loadData(self):
        self.tableWidget = self.loadstudent(self.tableWidget, self.classe)

    def setupUi(self, V_CLASSE_2, user, classe, trimestre, thype, coef, num):
        self.classe = classe
        self.user = user
        self.ind = self.user.reper_classe(self.classe)
        self.etablissement = self.user.etablissements[self.ind[0]]
        self.tri = trimestre
        self.thype = thype
        self.coef = coef
        self.num = num
        self.a = datetime.date.today()
        self.buttonReply=None

        V_CLASSE_2.setObjectName("V_CLASSE_2")
        V_CLASSE_2.resize(800, 600)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        V_CLASSE_2.setWindowIcon(icon)
        V_CLASSE_2.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.centralwidget = QWidget(V_CLASSE_2)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QTableWidget()
        self.tableWidget.setGeometry(QRect(10, 10, 771, 611))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "alternate-background-color: rgb(102, 255, 185);")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(
            QAbstractItemView.AnyKeyPressed | QAbstractItemView.CurrentChanged | QAbstractItemView.EditKeyPressed)
        self.tableWidget.setColumnCount(3)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.toolBar = QToolBar(V_CLASSE_2)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.toolBar.setFont(font)
        self.toolBar.setFocusPolicy(Qt.StrongFocus)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet("background-color: rgb(11, 170, 75);\n"
                                   "alternate-background-color: rgb(11, 170, 75);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        V_CLASSE_2.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.actionRetour = QAction(V_CLASSE_2)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/newPrefix/RETOUR.png"), QIcon.Normal, QIcon.Off)
        self.actionRetour.setIcon(icon4)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionRetour.setFont(font)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/newPrefix/icon_Plan de travail 1 copie.png"), QIcon.Normal,
                        QIcon.Off)
        self.actionRetour.setObjectName("actionRetour")
        self.actionEnregistrer = QAction(V_CLASSE_2)
        self.actionEnregistrer.setCheckable(False)
        self.actionEnregistrer.setIcon(icon3)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionEnregistrer.setFont(font)
        self.actionEnregistrer.setVisible(True)
        self.actionEnregistrer.setMenuRole(QAction.TextHeuristicRole)
        self.actionEnregistrer.setIconVisibleInMenu(True)
        self.actionEnregistrer.setObjectName("actionEnregistrer")

        self.actionEnregistrer.triggered.connect(self.select)
        self.actionRetour.triggered.connect(self.retour)

        self.toolBar.addAction(self.actionEnregistrer)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRetour)
        V_CLASSE_2.setCentralWidget(self.centralwidget)
        self.v = QVBoxLayout()
        self.v.addWidget(self.tableWidget)
        self.centralwidget.setLayout(self.v)

        self.retranslateUi(V_CLASSE_2)
        QMetaObject.connectSlotsByName(V_CLASSE_2)

    def retranslateUi(self, V_CLASSE_2):
        _translate = QCoreApplication.translate
        V_CLASSE_2.setWindowTitle(_translate("V_CLASSE_2", "{} {}-{} {}{} {} Trimestre{}".format(self.etablissement.nom,
                                                                                                self.etablissement.annee,
                                                                                                self.etablissement.annee + 1,
                                                                                                self.classe.niveau,
                                                                                                self.classe.serie,
                                                                                                self.classe.numero,
                                                                                                self.tri)))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("V_CLASSE_2", "   Nom "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("V_CLASSE_2", "Prénoms"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("V_CLASSE_2", "{}{} {}".format(self.thype, self.num, self.coef)))
        self.toolBar.setWindowTitle(_translate("V_CLASSE_2", "toolBar"))
        self.actionRetour.setText(_translate("V_CLASSE_2", "retour"))
        self.actionRetour.setToolTip(_translate("V_CLASSE_2",
                                                "<html><head/><body><p><span style=\" font-size:12pt;\">Retour</span></p></body></html>"))
        self.actionEnregistrer.setText(_translate("V_CLASSE_2", "Enregistrer"))
        self.actionEnregistrer.setToolTip(_translate("V_CLASSE_2",
                                                     "<html><head/><body><p><span style=\" font-size:12pt;\">Enregistrer</span></p></body></html>"))
        self.loadData()


#interface pour modifier une note
class Ui_V_CLASSE_3(object):
    def verife(self, table):
        valide = 0
        ligne=-1
        for i in range(table.rowCount()):
            data = table.item(i, 2)
            if data == None:
                if valide < 2:
                    valide = 1
                continue
            data = data.data(0)
            if data == "":
                if valide < 2:
                    valide = 1
            else:
                try:
                    data = float(data)
                except:
                    valide = 2
                    if ligne == -1:
                        ligne = i + 1
                else:
                    if ((data < 0) or (data > (20 * self.classe.eleves[0].notes[self.tri][self.r].coefficient))):
                        valide = 2
                        if ligne == -1:
                            ligne = i + 1
        return valide,ligne

    def enregistrer(self, data, eleve, cursor):
        for i in eleve.notes[self.tri]:
            if (i.type == self.type) and (i.numero == self.num):
                id_note = i.id
        if data == None:
            cursor.execute(""" UPDATE notes SET note=null WHERE id='{}' """.format(id_note))
        else:
            data = data.data(0)
            if data == "":
                cursor.execute(""" UPDATE notes SET note=null WHERE id='{}' """.format(id_note))
            else:
                note = float(data)
                cursor.execute("""UPDATE notes SET note="{}" WHERE id='{}' """.format(note, id_note))

    def select(self):
        valide,ligne = self.verife(self.tableWidget)
        if valide == 0:
            conn, cursor = connect_db()
            for k in range(len(self.classe.eleves)):
                data = self.tableWidget.item(k, 2)
                self.enregistrer(data, self.classe.eleves[k], cursor)
            close_db(conn)
            self.classe = Classe(self.classe.id)
            self.user.refresh_classe(self.classe, self.ind)
            self.retour()
        elif valide == 1:
            buttonReply = Message_y_n('Validation',
                                               "Des élèves ont des notes vides\nVoulez vous procéder à l'enregistrement ?",
                                               self)
            if self.buttonReply == "Yes":
                conn, cursor = connect_db()
                for k in range(len(self.classe.eleves)):
                    data = self.tableWidget.item(k, 2)
                    self.enregistrer(data, self.classe.eleves[k], cursor)
                close_db(conn)
                self.classe = Classe(self.classe.id)
                self.user.refresh_classe(self.classe, self.ind)
                self.retour()
        else:
            open_mess_ok('Information', "Note invalide à la ligne {}".format(ligne))

    def retour(self):
        open_class(self.user, self.classe)
        V_CLASSE_3.hide()

    def loadstudent(self, table, classe):
        table.setRowCount(0)
        for row, data in enumerate(classe.eleves):
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(str(data.nom)))
            table.setItem(row, 1, QTableWidgetItem(str(data.prenom)))
            if data.notes[self.tri][self.r].note == None:
                data.notes[self.tri][self.r].note = ""
            table.setItem(row, 2, QTableWidgetItem(str(data.notes[self.tri][self.r].note)))
        return table

    def fonc(self, table):
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        item.setText('{}{}  /{}'.format(self.type, self.num,
                                        int(20 * self.classe.eleves[0].notes[self.tri][self.r].coefficient)))
        table.setHorizontalHeaderItem(2, item)

    def loadData(self):
        self.tableWidget = self.loadstudent(self.tableWidget, self.classe)
        self.fonc(self.tableWidget)

    def setupUi(self, V_CLASSE_3, user, classe, aux, au, tri, r):
        self.classe = classe
        self.user = user
        self.type = aux
        self.num = au
        self.tri = tri
        self.r = r
        self.ind = self.user.reper_classe(self.classe)
        self.buttonReply=None
        V_CLASSE_3.setObjectName("V_CLASSE_3")
        V_CLASSE_3.resize(800, 600)
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        V_CLASSE_3.setWindowIcon(icon)
        V_CLASSE_3.setStyleSheet("background-color: rgb(11, 170, 75);")
        self.centralwidget = QWidget(V_CLASSE_3)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QTableWidget()
        self.tableWidget.setGeometry(QRect(10, 10, 771, 611))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                       "alternate-background-color: rgb(102, 255, 185);")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(
            QAbstractItemView.AnyKeyPressed | QAbstractItemView.CurrentChanged | QAbstractItemView.EditKeyPressed)
        self.tableWidget.setColumnCount(3)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.toolBar = QToolBar(V_CLASSE_3)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.toolBar.setFont(font)
        self.toolBar.setFocusPolicy(Qt.StrongFocus)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet("background-color: rgb(11, 170, 75);\n"
                                   "alternate-background-color: rgb(11, 170, 75);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        V_CLASSE_3.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.actionRetour = QAction(V_CLASSE_3)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/newPrefix/RETOUR.png"), QIcon.Normal, QIcon.Off)
        self.actionRetour.setIcon(icon4)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionRetour.setFont(font)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/newPrefix/icon_Plan de travail 1 copie.png"), QIcon.Normal,
                        QIcon.Off)
        self.actionRetour.setObjectName("actionRetour")
        self.actionEnregistrer = QAction(V_CLASSE_3)
        self.actionEnregistrer.setCheckable(False)
        self.actionEnregistrer.setIcon(icon3)
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.actionEnregistrer.setFont(font)
        self.actionEnregistrer.setVisible(True)
        self.actionEnregistrer.setMenuRole(QAction.TextHeuristicRole)
        self.actionEnregistrer.setIconVisibleInMenu(True)
        self.actionEnregistrer.setObjectName("actionEnregistrer")

        self.actionEnregistrer.triggered.connect(self.select)
        self.actionRetour.triggered.connect(self.retour)

        self.toolBar.addAction(self.actionEnregistrer)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRetour)
        V_CLASSE_3.setCentralWidget(self.centralwidget)
        self.v = QVBoxLayout()
        self.v.addWidget(self.tableWidget)
        self.centralwidget.setLayout(self.v)

        self.retranslateUi(V_CLASSE_3)
        QMetaObject.connectSlotsByName(V_CLASSE_3)

    def retranslateUi(self, V_CLASSE_3):
        _translate = QCoreApplication.translate
        V_CLASSE_3.setWindowTitle(_translate("V_CLASSE_3", "{}{} {} Trimestre{}".format(self.classe.niveau,
                                                                                                self.classe.serie,
                                                                                                self.classe.numero,
                                                                                                self.tri+1)))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("V_CLASSE_3", "   Nom "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("V_CLASSE_3", "Prénoms"))
        self.toolBar.setWindowTitle(_translate("V_CLASSE_3", "toolBar"))
        self.actionRetour.setText(_translate("V_CLASSE_3", "retour"))
        self.actionRetour.setToolTip(_translate("V_CLASSE_3",
                                                "<html><head/><body><p><span style=\" font-size:12pt;\">Retour</span></p></body></html>"))
        self.actionEnregistrer.setText(_translate("V_CLASSE_3", "Enregistrer"))
        self.actionEnregistrer.setToolTip(_translate("V_CLASSE_3",
                                                     "<html><head/><body><p><span style=\" font-size:12pt;\">Enregistrer</span></p></body></html>"))
        self.loadData()


#interface pour la selection des parametres de la note
class Ui_Dialog_3(object):
    def ajouter(self):
        typ = self.comboBox.currentText()
        coef = float(self.comboBox_2.currentText())
        trimestre = int(self.spinBox.value())
        numero = 1
        for i in self.classe.eleves[0].notes[trimestre - 1]:
            if i.type == typ:
                numero += 1
        if V_CLASSE.isHidden() == False:
            V_CLASSE.hide()
        open_clas(self.user, self.classe, trimestre, typ, coef, numero)
        Dialog_3.hide()

    def retour(self):
        if V_CLASSE.isHidden()==True:
            open_class(self.user, self.classe)
        Dialog_3.hide()

    def setupUi(self, Dialog_3, user, classe):
        self.classe = classe
        self.user = user
        Dialog_3.setObjectName("Dialog_3")
        Dialog_3.resize(606, 223)
        Dialog_3.setMaximumSize(QSize(606, 223))
        Dialog_3.setMinimumSize(QSize(606, 223))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        Dialog_3.setWindowIcon(icon)
        self.centralwidget = QWidget(Dialog_3)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(0, 0, 611, 231))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/IMG-20180422-WA0008.jpg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setGeometry(QRect(309, 18, 251, 31))
        self.frame_2.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.spinBox = QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QRect(0, 0, 251, 31))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(3)
        self.spinBox.setObjectName("spinBox")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setGeometry(QRect(310, 77, 251, 31))
        self.frame_3.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setGeometry(QRect(0, 0, 251, 31))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setGeometry(QRect(320, 136, 241, 31))
        self.frame_4.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.comboBox_2 = QComboBox(self.frame_4)
        self.comboBox_2.setGeometry(QRect(0, 0, 241, 31))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("0.5")
        self.comboBox_2.addItem("1")
        self.comboBox_2.addItem("2")
        self.comboBox_2.addItem("3")
        self.comboBox_2.addItem("4")
        self.comboBox_2.addItem("5")
        self.comboBox_2.addItem("6")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(350, 188, 102, 26))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setGeometry(QRect(466, 187, 101, 27))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/15.png);\n"
                                        "color: rgb(11, 170, 75);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(self.ajouter)
        self.pushButton_2.clicked.connect(self.retour)
        Dialog_3.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dialog_3)
        QMetaObject.connectSlotsByName(Dialog_3)

    def retranslateUi(self, Dialog_3):
        _translate = QCoreApplication.translate
        Dialog_3.setWindowTitle(_translate("Dialog_3", "EDU-Classeur"))
        self.comboBox.setItemText(0, _translate("Dialog_3", " IN"))
        self.comboBox.setItemText(1, _translate("Dialog_3", " D"))
        self.comboBox.setItemText(2, _translate("Dialog_3", " DST"))
        self.pushButton.setText(_translate("Dialog_3", "Entrer"))
        self.pushButton_2.setText(_translate("Dialog_3", "Annuler"))


#interface splash screen
class Ui_Splash(object):
    def started(self):
        while self.progressBar.value()<999:
            time.sleep(0.004)
            self.progressBar.setValue(self.progressBar.value()+1)
        self.suivant()


    def charge(self):
        a=datetime.date.today()
        a=a.year
        for i in range(len(self.user.etablissements)):
            if (a-self.user.etablissements[i].annee)<=2:
                for j in range(len(self.user.etablissements[i].classes)):
                    self.user.etablissements[i].classes[j].charge_eleves()

    def suivant(self):
        open_confirmation(self.ll, self.user)
        splash.finish(confirmation)

    def setupUi(self, splash, splash_pix, ll, user):
        splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        splash.setEnabled(False)
        self.user=user
        self.ll=ll
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(9)
        self.progressBar = QProgressBar(splash)
        self.progressBar.setMaximum(1000)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("color:rgb(255,255,255);")
        self.progressBar.setGeometry(50, splash_pix.height() - 70, splash_pix.width()-75, 15)


class Ui_Message(object):
    def retour(self):
        Message.hide()

    def setupUi(self, Message, Titre, Text):
        self.text=Text
        self.titre=Titre
        Message.setObjectName("Message")
        Message.resize(351, 161)
        Message.setMaximumSize(QSize(351, 161))
        Message.setMinimumSize(QSize(351, 161))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        Message.setWindowIcon(icon)
        self.centralwidget = QWidget(Message)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(0, 0, 351, 161))
        self.frame.setMinimumSize(QSize(0, 161))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/INTERFACE INFO-05.jpg);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setGeometry(QRect(270, 130, 61, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        Message.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/15.png);\n"
"color: rgb(11, 170, 75);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.retour)
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(30, 20, 300, 80))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.label.setObjectName("label")
        self.label.setWordWrap(True)
        Message.setCentralWidget(self.centralwidget)
        self.retranslateUi(Message)
        QMetaObject.connectSlotsByName(Message)


    def retranslateUi(self, Message):
        _translate = QCoreApplication.translate
        Message.setWindowTitle(_translate("Message", self.titre))
        self.label.setText(_translate("Message", self.text))
        self.pushButton.setText(_translate("Message", "ok"))

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
        icon.addPixmap(QPixmap(":/newPrefix/logo-01.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 351, 161))
        self.frame.setMinimumSize(QSize(0, 161))
        self.frame.setStyleSheet("border-image: url(:/newPrefix/INTERFACE INFO-05.jpg);")
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
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(30, 20, 300, 100))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setStyleSheet("border-image: url(:/newPrefix/15.png);")
        self.label.setObjectName("label")
        self.label.setWordWrap(True)
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setGeometry(QRect(200, 130, 61, 23))
        font = QFont()
        font.setFamily("Walkway UltraBold")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-image: url(:/newPrefix/6.png);\n"
                                        "color: rgb(255, 255, 255);")
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

mac=get_mac()
ll=get_li(mac)
view_activate(mac)


create_tables()
param_us=charge_user()
app = QApplication(argv)
if datetime.date.today() >= datetime.date(2019, 7, 31):
    m = open_mess_ok("EDU-Classeur", "Votre période d'éssaie est terminée\nMerci de contacter Devmax")
else:
    if param_us == None:
        open_confirmation(ll)
    else:
        param_us = [i for i in param_us]
        param_us[4] = base64.b64decode(param_us[4].encode("utf-8")).decode("utf-8", "ignore")
        maclu = read_mac()
        #li = read_li()
        if (mac!=param_us[4]):
            # suite du if: or mac!=maclu) or (li != ll
            m = open_mess_ok("EDU-Classeur", "Logiciel bloqué")
        else:
            user = User()
            open_splash(ll, user)
exit(app.exec_())


