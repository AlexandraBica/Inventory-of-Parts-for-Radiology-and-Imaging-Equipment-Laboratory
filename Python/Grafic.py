# -*- coding: utf-8 -*-
"""

@author: alexb
"""

import matplotlib.pyplot as plt
import sqlite3

connection = sqlite3.connect("Tabel_PCLP.db")
cursor = connection.cursor()

cursor.execute("SELECT Denumire_Piesa, Cantitate FROM tblPiese")
date = cursor.fetchall()

# Separa datele in doua liste
nume_piese = [row[0] for row in date]
cantitati = [row[1] for row in date]

plt.figure(figsize=(10,6))
plt.bar(nume_piese, cantitati, color='skyblue')
plt.xlabel('Denumire Piesa')
plt.ylabel('Cantitate')
plt.title('Cantitatea de piese pe denumire')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()