from fonctions_db import connect_db,close_db
import datetime

def verife_table_note(table):
    valide = 0
    list=[]
    ligne=-1
    for i in range(table.rowCount()):
        data = table.item(i, 2)
        if data == None:
            list.append(1)
            if valide < 2:
                valide = 1
            continue
        data = data.data(0)
        if data == "":
            list.append(1)
            if valide < 2:
                valide = 1
        else:
            try:
                data = float(data)
            except:
                list.append(2)
                valide = 2
                if ligne==-1:
                    ligne=i+1
            else:
                if ((data < 0) or (data > 20)):
                    list.append(2)
                    valide = 2
                    if ligne == -1:
                        ligne = i+1
                else :
                    list.append(0)
    return valide,list,ligne

def enregistrer(data, eleve, cursor, valide, thype, coef, tri, num):
    if valide>0:
        cursor.execute(
            """INSERT INTO notes(id_eleve,type,coefficient,trimestre,numero,date,id_classe) VALUES("{}","{}","{}","{}","{}","{}","{}")""".format(
                int(eleve.id), str(thype), coef, int(tri), int(num), str(datetime.date.today()),eleve.id_classe))
    else:
        note = float(data.data(0)) * coef
        cursor.execute(
            """INSERT INTO notes(id_eleve,type,coefficient,note,trimestre,numero,date,id_classe) VALUES("{}","{}","{}","{}","{}","{}","{}","{}")""".format(
                int(eleve.id), str(thype), coef, note, int(tri), int(num),
                str(datetime.date.today()), eleve.id_classe))

def enregistrement(classe, table, list, thype, coef, tri, num):
    conn, cursor = connect_db()
    for k in range(len(classe.eleves)):
        data = table.item(k, 2)
        enregistrer(data, classe.eleves[k], cursor, list[k], thype, coef, tri, num)
    close_db(conn)

def supprimer_note(c, tr, classe):
    conn, cursor = connect_db()
    note = classe.eleves[0].notes[tr][c - 2]
    cursor.execute("""DELETE FROM notes WHERE id_classe="{}" AND numero="{}" AND type="{}" AND trimestre="{}"  """.format(note.id_classe, note.numero, note.type, note.trimestre))
    close_db(conn)