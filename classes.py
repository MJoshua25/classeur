from fonctions_db import connect_db,close_db
from operator import itemgetter, attrgetter
from threading import Thread

class Fpara(Thread):
    def __init__(self,fonction):
        Thread.__init__(self)
        self.fonction=fonction

    def run(self):
        self.fonction()

class Note(object):
    def __init__(self, id_note, cursor=None, stop=1, note=None):
        if cursor == None:
            conn, cursor = connect_db()
        if note == None:
            cursor.execute("""SELECT * FROM notes WHERE id = '{}'""".format(id_note))
            note = cursor.fetchone()
        if stop == 1:
            close_db(conn)
        self.id, self.id_eleve, self.type, self.coefficient, self.note, self.trimestre, self.numero, self.date, self.id_classe = note[
                                                                                                                     0], \
                                                                                                                 note[
                                                                                                                     1], \
                                                                                                                 note[
                                                                                                                     2], \
                                                                                                                 note[
                                                                                                                     3], \
                                                                                                                 note[
                                                                                                                     4], \
                                                                                                                 note[
                                                                                                                     5], \
                                                                                                                 note[
                                                                                                                     6], \
                                                                                                                 note[7], note[8]


class Eleve(object):
    def __init__(self, id_eleve, cursor=None, stop=1, eleve=None, id_note=None):
        if cursor == None:
            conn, cursor = connect_db()
        if eleve == None:
            cursor.execute("""SELECT * FROM eleve WHERE id = '{}'""".format(id_eleve))
            eleve = cursor.fetchone()
        self.id, self.id_classe, self.nom, self.prenom= eleve[0], eleve[1], eleve[2], eleve[3]
        if id_note==None:
            id_note=[]
            cursor.execute("""SELECT * FROM notes WHERE id_eleve='{}' AND type=' IN' ORDER BY numero""".format(self.id))
            aux = cursor.fetchall()
            id_note += aux
            cursor.execute(
                """SELECT * FROM notes WHERE id_eleve='{}' AND type!=' IN' ORDER BY type,numero""".format(self.id))
            aux = cursor.fetchall()
            id_note += aux
        self.notes = [[Note(aux[0], cursor=cursor, stop=0, note=aux) for aux in id_note if aux[5] == n] for n in range(1,4)]
        if stop == 1:
            close_db(conn)
        self.moyenne, self.rang = [None, None, None], [None, None, None]
        for i in range(len(self.notes)):
            if len(self.notes[i]) > 0:
                self.moyenne[i] = (sum(n.note for n in self.notes[i] if n.note!=None) / sum(n.coefficient for n in self.notes[i]))
            else:
                self.moyenne[i] = 0


class Classe(object):
    def delete_student(self, student):
        self.eleves.remove(student)
        if len(self.eleves) > 0:
            for i in range(3):
                if len(self.eleves[0].notes[i]) > 0:
                    self.list_rang[i] = self.rang(i)

    def add_student(self, student):
        self.eleves.append(student)
        self.eleves = sorted(self.eleves, key=attrgetter("nom", "prenom", "id"))
        if len(self.eleves) > 0:
            for i in range(3):
                if len(self.eleves[0].notes[i]) > 0:
                    self.list_rang[i]=self.rang(i)

    def update_student(self, id_eleve, nom, prenom):
        for i in range(len(self.eleves)):
            aux = self.eleves[i]
            if aux.id == id_eleve:
                aux.nom, aux.prenom = nom, prenom
                self.eleves[i] = aux
                break
        self.eleves=sorted(self.eleves, key=attrgetter("nom", "prenom", "id"))

    def rang(self, tri):
        liste_moy, liste_rang = [], []
        for i in self.eleves:
            liste_moy.append([i.id, i.moyenne[tri]])

        liste_moy = sorted(liste_moy, key=itemgetter(1), reverse=True)

        for i in range(1, len(liste_moy) + 1):
            aux = str(i)
            if i == 1:
                aux += "er"
            else:
                aux += "ème"
                if liste_moy[i - 2][1] == liste_moy[i - 1][1]:
                    aux = liste_moy[i - 2][2]
                    if " Ex" not in aux:
                        aux += " Ex"
            liste_moy[i - 1].append(aux)
            liste_rang.append(aux)

        for i in liste_moy:
            for j in self.eleves:
                if i[0] == j.id:
                    j.rang[tri] = i[2]
                    break
        return liste_rang

    def charge_eleves(self):
        conn, cursor = connect_db()
        cursor.execute("""SELECT * FROM eleve WHERE id_classe='{}' ORDER BY nom,prenom,id""".format(self.id))
        id_eleve, list_note = cursor.fetchall(), []
        cursor.execute("""SELECT * FROM notes WHERE id_classe='{}' AND type=' IN' ORDER BY numero""".format(self.id))
        aux2 = cursor.fetchall()
        list_note += aux2
        cursor.execute(
            """SELECT * FROM notes WHERE id_classe='{}' AND type!=' IN' ORDER BY type,numero""".format(self.id))
        aux2 = cursor.fetchall()
        list_note += aux2
        self.eleves =[Eleve(aux[0], cursor=cursor, stop=0, eleve=aux, id_note=[nd for nd in list_note if nd[1] == aux[0]]) for aux in id_eleve]
        if len(id_eleve) > 0:
            for i in range(3):
                if len(self.eleves[0].notes[i]) > 0:
                    self.list_rang[i] = self.rang(i)
        close_db(conn)

    def __init__(self, id_classe, cursor=None, stop=1, classe=None, eleve=None):
        if cursor == None:
            conn, cursor = connect_db()
        if classe == None:
            cursor.execute("""SELECT * FROM classe WHERE id = '{}' """.format(id_classe))
            classe = cursor.fetchone()
        self.id, self.id_etablissement, self.niveau, self.serie, self.numero = classe[0], classe[1], classe[2], classe[
            3], classe[4]
        self.eleves, self.list_rang = [], [[], [], []]
        if eleve==None:
            self.charge_eleves()
        if stop == 1:
            close_db(conn)


class Etablissement(object):
    def delete_classe(self, classe):
        self.classes.remove(classe)

    def add_classe(self, classe):
        self.classes.append(classe)
        self.classes = sorted(self.classes, key=attrgetter("serie", "numero"))
        self.classes = sorted(self.classes, key=attrgetter("niveau"),reverse=True)

    def update_school(self, id_classe, niveau, serie, numero):
        for i in range(len(self.classes)):
            aux = self.classes[i]
            if aux.id == id_classe:
                aux.niveau, aux.serie, aux.numero = niveau, serie, numero
                self.classes[i] = aux
                break
        self.classes = sorted(self.classes, key=attrgetter("serie", "numero"))
        self.classes = sorted(self.classes, key=attrgetter("niveau"), reverse=True)

    def __init__(self, id_etablissement, cursor=None, stop=1, etablissement=None):
        if cursor == None:
            conn, cursor = connect_db()
        if etablissement == None:
            cursor.execute("""SELECT * FROM etablissement WHERE id = '{}' """.format(id_etablissement))
            etablissement = cursor.fetchone()
        self.id, self.nom, self.annee = etablissement[0], etablissement[1], etablissement[2]
        cursor.execute(
            """SELECT * FROM classe WHERE id_etablissement='{}' ORDER BY niveau DESC,serie,numero""".format(self.id))
        id_classe = cursor.fetchall()
        self.classes = [Classe(aux[0], cursor=cursor, stop=0, classe=aux, eleve="yes") for aux in id_classe]
        if stop == 1:
            close_db(conn)


class User(object):
    def delete_school(self, school):
        self.etablissements.remove(school)

    def add_school(self, school):
        self.etablissements.append(school)
        self.etablissements = sorted(self.etablissements, key=attrgetter("annee"), reverse=True)
        self.etablissements = sorted(self.etablissements, key=attrgetter("nom"))


    def update_school(self, eta):
        for i in range(len(self.etablissements)):
            aux = self.etablissements[i]
            if aux.id == eta.id:
                self.etablissements[i] = eta
                break
        self.etablissements = sorted(self.etablissements, key=attrgetter("annee"), reverse=True)
        self.etablissements = sorted(self.etablissements, key=attrgetter("nom"))

    def reper_classe(self, classe):
        for i in range(len(self.etablissements)):
            aux = self.etablissements[i]
            if aux.id == classe.id_etablissement:
                ind = (i, aux.classes.index(classe))
        return ind

    def refresh_classe(self, classe, ind):
        self.etablissements[ind[0]].classes[ind[1]] = classe

    def refresh_school(self, school):
        for i in range(len(self.etablissements)):
            aux = self.etablissements[i]
            if aux.id == school.id:
                self.etablissements[i] = school
                break
        self.etablissements = sorted(self.etablissements, key=attrgetter("annee"), reverse=True)
        self.etablissements = sorted(self.etablissements, key=attrgetter("nom"))

    def __init__(self):
        conn, cursor = connect_db()
        cursor.execute("""SELECT nom,prenom,sexe,passe FROM users""")
        param_us = cursor.fetchone()
        self.nom, self.prenom, self.sexe, self.mot_passe = param_us[0], param_us[1], param_us[2],param_us[3]
        cursor.execute("""SELECT * FROM etablissement ORDER BY nom,annee DESC""")
        id_etablissement = cursor.fetchall()
        self.etablissements = [Etablissement(aux[0], cursor=cursor, stop=0, etablissement=aux) for aux in
                               id_etablissement]
        close_db(conn)
