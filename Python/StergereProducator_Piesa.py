# -*- coding: utf-8 -*-
"""
Created on Sun 

@author: alexb
"""

import sqlite3

# Deschide conexiunea cu timeout mai mare 
connection = sqlite3.connect("Tabel_PCLP.db", timeout=5)

def sterge_producator_si_piese(nume_producator):
    with connection:
        cursor = connection.cursor()
        # Luam id-urile producatorilor cu numele dat
        cursor.execute("""
            SELECT id_Producator, id_Piesa FROM tblProducator
            WHERE Nume_Companie = ?
        """, (nume_producator,))
        rezultate = cursor.fetchall()

        # Sterge piesele asociate
        for id_producator, id_piesa in rezultate:
            cursor.execute("DELETE FROM tblPiese WHERE id_Piesa = ?", (id_piesa,))

        # Sterge producatorii
        cursor.execute("DELETE FROM tblProducator WHERE Nume_Companie = ?", (nume_producator,))


sterge_producator_si_piese("Producator Default")