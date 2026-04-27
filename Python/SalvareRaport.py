# -*- coding: utf-8 -*-
"""
Created on Sun

@author: alexb
"""

import sqlite3
import csv

def salveaza_tabel_csv(nume_tabel, nume_fisier_csv):
    # Deschide conexiunea la baza de date
    connection = sqlite3.connect("Tabel_PCLP.db")
    cursor = connection.cursor()

    # Preia toate datele din tabel
    cursor.execute(f"SELECT * FROM {nume_tabel}")
    coloane = [desc[0] for desc in cursor.description]  # Numele coloanelor

    # Scrie datele în fișier CSV
    with open(nume_fisier_csv, mode='w', newline='', encoding='utf-8') as fisier_csv:
        writer = csv.writer(fisier_csv)
        writer.writerow(coloane)          # Scrie header-ul (coloanele)
        writer.writerows(cursor.fetchall())  # Scrie randurile

    print(f"Tabelul '{nume_tabel}' a fost salvat în fișierul '{nume_fisier_csv}'.")
    connection.close()

# Ex
nume_tabel = "tblProducator"  # Sau "tblClient", "tblProducator", "tblOfertare", "tblClienti"

salveaza_tabel_csv(nume_tabel, f"{nume_tabel}_raport.csv")
