import xlrd
from fonctions_db import connect_db,close_db
import os
import pathlib
import xlsxwriter


def emplacement_nom(fileName):
    workbook = xlrd.open_workbook(str(fileName[0]))
    sheet, value, trouve, empl, typ = workbook.sheet_by_index(0), "", 0, 0, 0
    for i in range(sheet.nrows):
        for j in range(sheet.ncols):
            value = sheet.cell_value(i, j)
            if ("nom" or "noms") in value.lower():
                empl, trouve = (i, j), 1
                break
        if value != "":
            break
    if trouve == 1:
        a = str(sheet.cell_value(empl[0]+1, empl[1]))
        a = (a.strip())
        a = a.split(" ")
        if len(a) > 1:
            typ = 1
    return trouve, empl, sheet, typ

def direct(sheet,empl, id_classe):
    conn, cursor = connect_db()
    for i in range(empl[0] + 1, sheet.nrows):
        nom, prenom = str(sheet.cell_value(i, empl[1])), str(sheet.cell_value(i, empl[1] + 1))
        nom, prenom = nom.replace(" ", "").capitalize(), prenom.split(" ")
        for j in range(len(prenom)):
            prenom[j] = prenom[j].capitalize()
        prenom = " ".join(prenom)
        if nom != "" and prenom != "":
            cursor.execute(
                """INSERT INTO eleve(id_classe,nom,prenom) VALUES('{}',"{}","{}")""".format(
                    id_classe, nom, prenom))
        else:
            break
    close_db(conn)

def nom_import(sheet,empl,id_classe):
    conn, cursor = connect_db()
    for i in range(empl[0] + 1, sheet.nrows):
        nom_prenom = str(sheet.cell_value(i, empl[1]))
        nom_prenom = nom_prenom.split(" ")
        nom, prenom = nom_prenom[0], nom_prenom[1:]
        nom= nom.replace(" ", "").capitalize()
        for j in range(len(prenom)):
            prenom[j] = prenom[j].capitalize()
        prenom = " ".join(prenom)
        if nom != "" and prenom != "":
            cursor.execute(
                """INSERT INTO eleve(id_classe,nom,prenom) VALUES('{}',"{}","{}")""".format(
                    id_classe, nom, prenom))
        else:
            break
    close_db(conn)

def importer(sheet, empl, id_classe, typ):
    if typ==0:
        direct(sheet,empl,id_classe)
    else:
        nom_import(sheet,empl,id_classe)

def ex_dir(tab, etablissement, classe, user):
    current2 = os.getcwd()
    user2 = os.getlogin()
    directory = 'C:\\Users\\{}\\Documents\\EDU-Classeur\\{}\\{}\\{}{}{}\\'.format(user2, etablissement.nom,
                                                                                  etablissement.annee,
                                                                                  classe.niveau, classe.serie,
                                                                                  classe.numero)
    pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
    current = tab.currentIndex()
    workbook = xlsxwriter.Workbook('{}Trimestre {}.xlsx'.format(directory, current + 1))
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    merge_format = workbook.add_format({'align': 'left'})
    worksheet.set_column(3, 3, 45)
    worksheet.set_column(2, 2, 15)
    worksheet.set_column(0, 0, 5)
    worksheet.set_column(1, 1, 10)
    worksheet.merge_range('A1:C1', '', merge_format)
    worksheet.write_rich_string(0, 0, bold, "Année scolaire : ",
                                "{}-{}".format(etablissement.annee, etablissement.annee + 1))
    worksheet.merge_range('A2:C2', '', merge_format)
    worksheet.write_rich_string(1, 0, bold, "Etablissement : ", etablissement.nom)
    sexe = {"HOMME ": "Mr.", "FEMME": "Mme"}
    prenom = user.prenom.split(" ")
    prenom = prenom[0]
    worksheet.merge_range('A3:C3', '', merge_format)
    worksheet.write_rich_string(2, 0, bold, "Classe : ",
                                "{}{} {}".format(classe.niveau, classe.serie, classe.numero))
    worksheet.merge_range('A4:C4', '', merge_format)
    worksheet.write_rich_string(3, 0, bold, "Trimestre : ", "{}".format(current + 1))
    worksheet.merge_range('A5:C5', '', merge_format)
    worksheet.write_rich_string(4, 0, bold, "Enseignant : ",
                                "{} {} {}".format(sexe[user.sexe], user.nom, prenom))
    worksheet.write_rich_string(5, 0, bold, "Matière : ")
    worksheet.write_rich_string(7, 0, bold, "N°")
    worksheet.write_rich_string(7, 1, bold, "Matricule")
    worksheet.write_rich_string(7, 2, bold, "Nom")
    worksheet.write_rich_string(7, 3, bold, "Prenoms")
    if (len(classe.eleves) > 0):
        if (len(classe.eleves[0].notes[current]) > 0):
            for i in range(len(classe.eleves[0].notes[current])):
                j = classe.eleves[0].notes[current][i]
                worksheet.write_rich_string(7, i + 4, bold, "{} {}".format(j.type, j.numero))
            worksheet.write_rich_string(7, i + 5, bold, "Moyenne")
            worksheet.write_rich_string(7, i + 6, bold, "Rang")
        for i in range(len(classe.eleves)):
            j = classe.eleves[i]
            worksheet.write(i + 8, 0, i + 1)
            worksheet.write(i + 8, 2, j.nom)
            worksheet.write(i + 8, 3, j.prenom)
            if (len(classe.eleves[0].notes[current]) > 0):
                for k in range(len(j.notes[current])):
                    l = classe.eleves[i].notes[current][k]
                    note = l.note
                    if l.note == None:
                        note = 0
                    worksheet.write(i + 8, k + 4, note)
                aux = "{0:.2f}".format(j.moyenne[current])
                aux = float(aux)
                worksheet.write(i + 8, k + 5, aux)
                worksheet.write(i + 8, k + 6, j.rang[current])
    if (len(classe.eleves) > 0):
        if (len(classe.eleves[0].notes[current]) > 0):
            worksheet.add_table(7, 0, i + 8, k + 6, {'header_row': False})
        else:
            worksheet.add_table(7, 0, i + 8, 3, {'header_row': False})
    else:
        worksheet.add_table(7, 0, 7, 1, {'header_row': False})
    return workbook

def ex_fus(tab, etablissement, classe, user):
    current2 = os.getcwd()
    user2 = os.getlogin()
    directory = 'C:\\Users\\{}\\Documents\\EDU-Classeur\\{}\\{}\\{}{}{}\\'.format(user2, etablissement.nom,
                                                                                  etablissement.annee,
                                                                                  classe.niveau, classe.serie,
                                                                                  classe.numero)
    pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
    current = tab.currentIndex()
    workbook = xlsxwriter.Workbook('{}Trimestre {}.xlsx'.format(directory, current + 1))
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    merge_format = workbook.add_format({'align': 'left'})
    worksheet.set_column(2, 2, 45)
    worksheet.set_column(0, 0, 5)
    worksheet.set_column(1, 1, 15)
    worksheet.merge_range('A1:C1', '', merge_format)
    worksheet.write_rich_string(0, 0, bold, "Année scolaire : ",
                                "{}-{}".format(etablissement.annee, etablissement.annee + 1))
    worksheet.merge_range('A2:C2', '', merge_format)
    worksheet.write_rich_string(1, 0, bold, "Etablissement : ", etablissement.nom)
    sexe = {"HOMME ": "Mr.", "FEMME": "Mme"}
    prenom = user.prenom.split(" ")
    prenom = prenom[0]
    worksheet.merge_range('A3:C3', '', merge_format)
    worksheet.write_rich_string(2, 0, bold, "Classe : ",
                                "{}{} {}".format(classe.niveau, classe.serie, classe.numero))
    worksheet.merge_range('A4:C4', '', merge_format)
    worksheet.write_rich_string(3, 0, bold, "Trimestre : ", "{}".format(current + 1))
    worksheet.merge_range('A5:C5', '', merge_format)
    worksheet.write_rich_string(4, 0, bold, "Enseignant : ",
                                "{} {} {}".format(sexe[user.sexe], user.nom, prenom))
    worksheet.write_rich_string(5, 0, bold, "Matière : ")
    worksheet.write_rich_string(7, 0, bold, "N°")
    worksheet.write_rich_string(7, 1, bold, "Matricule")
    worksheet.write_rich_string(7, 2, bold, "Nom & Prenoms")
    if (len(classe.eleves) > 0):
        if (len(classe.eleves[0].notes[current]) > 0):
            for i in range(len(classe.eleves[0].notes[current])):
                j = classe.eleves[0].notes[current][i]
                worksheet.write_rich_string(7, i + 3, bold, "{} {}".format(j.type, j.numero))
            worksheet.write_rich_string(7, i + 4, bold, "Moyenne")
            worksheet.write_rich_string(7, i + 5, bold, "Rang")
        for i in range(len(classe.eleves)):
            j = classe.eleves[i]
            worksheet.write(i + 8, 0, i + 1)
            worksheet.write(i + 8, 2, "{} {}".format(j.nom, j.prenom))
            if (len(classe.eleves[0].notes[current]) > 0):
                for k in range(len(j.notes[current])):
                    l = classe.eleves[i].notes[current][k]
                    note = l.note
                    if l.note == None:
                        note = 0
                    worksheet.write(i + 8, k + 3, note)
                aux = "{0:.2f}".format(j.moyenne[current])
                aux = float(aux)
                worksheet.write(i + 8, k + 4, aux)
                worksheet.write(i + 8, k + 5, j.rang[current])
    if (len(classe.eleves) > 0):
        if (len(classe.eleves[0].notes[current]) > 0):
            worksheet.add_table(7, 0, i + 8, k + 5, {'header_row': False})
        else:
            worksheet.add_table(7, 0, i + 8, 2, {'header_row': False})
    else:
        worksheet.add_table(7, 0, 7, 1, {'header_row': False})
    return workbook

def exporter(tab, etablissement, classe, user, typ):
    if typ==0:
        workbook=ex_dir(tab, etablissement, classe, user)
    else:
        workbook=ex_fus(tab, etablissement, classe, user)
    return workbook