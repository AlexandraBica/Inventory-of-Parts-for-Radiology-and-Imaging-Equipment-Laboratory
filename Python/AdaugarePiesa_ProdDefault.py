# -*- coding: utf-8 -*-
"""


@author: alexb
"""
import sqlite3

# Deschidem conexiunea cu timeout, Python așteaptă 5 secunde ca blocajul sa se elibereze, pentru a evita eroarea „database is locked” 
connection = sqlite3.connect("Tabel_PCLP.db", timeout=5)

# Functie pentru adaugare piesa + producator automat
def adauga_piesa_cu_producator(id_piesa, cod_piesa, denumire, pret, cantitate):
    with connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO tblPiese (id_Piesa, Cod_Piesa, Denumire_Piesa, Pret_Piesa, Cantitate)
            VALUES (?, ?, ?, ?, ?)""", (id_piesa, cod_piesa, denumire, pret, cantitate))

        cursor.execute("""
            INSERT INTO tblProducator (id_Producator, Nume_Companie, id_Piesa, Nr_telefon, Mail, Adresa, Site)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (id_piesa, "Producator Default", id_piesa, "0000000000", "default@mail.com", "Adresa Default", "www.default.com"))

adauga_piesa_cu_producator(15, 45, "Filtru de aer", 456, 2)

