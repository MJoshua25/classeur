from sqlite3 import connect
import base64
import pathlib
from os import popen


def connect_db():
    """Fonction permettant de se connecter à la base de donnée"""
    conn = connect('c++.dll.sqlite3')
    cursor = conn.cursor()
    return conn, cursor

def close_db(conn):
    """Fonction permettant de fermer la base de donnée"""
    conn.commit()
    conn.close()

def charge_user():
    """Fonction permettant de charger les données de l'utilisateur"""
    conn, cursor = connect_db()
    cursor.execute("""SELECT nom, prenom,sexe,passe,mac FROM users""")
    param_us = cursor.fetchone()
    conn.close()
    return param_us

def charge_classe():
    """Fonction permettant de charger les classes"""
    conn, cursor = connect_db()
    cursor.execute("""SELECT * FROM classe""")
    classes= cursor.fetchone()
    conn.close()
    return classes

def create_table_users():
    conn, cursor = connect_db()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     nom TEXT,
     prenom TEXT,
     sexe TEXT,
     passe TEXT,
     confirmer TEXT,
     mot_recup TEXT,
     mac TEXT
)
""")
    close_db(conn)

def create_table_note():
    conn, cursor = connect_db()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         id_eleve INTERGER,
         type TEXT,
         coefficient FLOAT,
         note FLOAT,
         trimestre INTERGER,
         numero INTERGER,
         date DATE,
         id_classe INTERGER,
         FOREIGN KEY(id_eleve) REFERENCES eleve(id),
         FOREIGN KEY(id_classe) REFERENCES classe(id)

   )
    """)
    close_db(conn)

def create_table_eleve():
    conn, cursor = connect_db()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eleve(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         id_classe INTERGER,
         nom TEXT,
         prenom TEXT,
         FOREIGN KEY(id_classe) REFERENCES classe(id)
    )
    """)
    close_db(conn)

def create_table_classe():
    conn, cursor = connect_db()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS classe(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         id_etablissement INTERGER,
         niveau TEXT,
         serie TEXT,
         numero INTERGER,
         FOREIGN KEY(id_etablissement) REFERENCES etablissement(id)
    )
    """)
    close_db(conn)

def create_table_etalissement():
    conn, cursor = connect_db()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS etablissement(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         nom TEXT,
         annee YEAR
    )
    """)
    close_db(conn)

def get_mac():
    ipconfig = popen('getmac').readlines()
    mac = ""
    ligne=ipconfig[4]
    mac += ligne.split(' ')[0].strip() + "\n"
    return mac

def save_mac():
    mac = get_mac()
    pathlib.Path("lib\ ").mkdir(parents=True, exist_ok=True)
    file = open("lib\{}".format((base64.b64encode("mac".encode("ascii"))).decode("utf-8")), "w")
    file.write((base64.b64encode(mac.encode("ascii"))).decode("utf-8"))
    file.close()

def get_li(mac):
    li=(base64.b16encode(mac.encode("ascii"))).decode("utf-8")
    return li

def save_li(lic):
    file = open("lib/{}".format((base64.b64encode("Licence".encode("ascii"))).decode("utf-8")), "w")
    file.write((base64.b64encode(lic.encode("ascii"))).decode("utf-8"))
    file.close()

def read_mac():
    file = open("lib/{}".format((base64.b64encode("mac".encode("ascii"))).decode("utf-8")), "r")
    a=file.read()
    a=base64.b64decode(a.encode("utf-8")).decode("utf-8","ignore")
    return a

def read_li():
    file = open("lib/{}".format((base64.b64encode("Licence".encode("ascii"))).decode("utf-8")), "r")
    a = file.read()
    a = base64.b64decode(a.encode("utf-8")).decode("utf-8", "ignore")
    return a

def view_activate(mac):
    act = (base64.b64encode(mac.encode("ascii"))).decode("utf-8")
    act = (base64.b32encode(act.encode("ascii"))).decode("utf-8")
    file = open("activateur.txt", "w")
    file.write(act)
    file.close()


def create_tables():
    create_table_users()
    create_table_etalissement()
    create_table_classe()
    create_table_eleve()
    create_table_note()

#Début des fonctions pour les eleves
def verif_students_in_classe(classe,user):
    if len(classe.eleves) == 0:
        ind = user.reper_classe(classe)
        classe.charge_eleves()
        user.refresh_classe(classe, ind)
    return classe, user
