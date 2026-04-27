# -*- coding: utf-8 -*-
"""

@author: alexb
"""

import sqlite3
connection = sqlite3.connect("Tabel_PCLP.db")
print(connection.total_changes)
cursor = connection.cursor()
cursor.execute("""CREATE TABLE tblPiese 
(id_Piesa NUMBER PRIMARY KEY UNIQUE,
Cod_Piesa NUMBER,
Denumire_Piesa TEXT,
Pret_Piesa NUMBER,
Cantitate NUMBER)""")


cursor.execute("""CREATE TABLE tblProducator
(id_Producator NUMBER PRIMARY KEY NOT NULL UNIQUE,
Nume_Companie TEXT,
id_Piesa NUMBER,
Nr_telefon TEXT,
Mail TEXT, 
Adresa TEXT,
Site TEXT,
FOREIGN KEY (id_Piesa) REFERENCES tblPiese(id_Piesa))""")

cursor.execute("""CREATE TABLE tblClient
(id_Client NUMBER PRIMARY KEY NOT NULL UNIQUE,
Nume_Client TEXT,
Prenume_Client TEXT,
CNP NUMBER,
Nr_telefon TEXT,
Mail TEXT,
Problema TEXT,
Locatie TEXT)""")

cursor.execute("""CREATE TABLE tblOfertare
(id_Oferta NUMBER PRIMARY KEY UNIQUE,
id_Client NUMBER,
Cod_Piesa NUMBER,
id_Producator NUMBER,
Perioada DATE,
Locatie TEXT,
Pret_Lucrare NUMBER,
FOREIGN KEY (id_Client) REFERENCES tblClient(id_Client),
FOREIGN KEY (id_Producator) REFERENCES Producator(id_Producator),
FOREIGN KEY (Locatie) REFERENCES Client(Locatie) )""")


cursor.execute("INSERT INTO tblPiese VALUES (1, 01, 'Monitor monocrom', 1234, 1)")
cursor.execute("INSERT INTO tblPiese VALUES (2, 02, 'Tub de raze X', 4432, 1)")
cursor.execute("INSERT INTO tblPiese VALUES (3, 03, 'Software de procesare 2D, 3D, 4D',9972, 1)")
cursor.execute("INSERT INTO tblPiese VALUES (4, 04, 'Sondă ecografică convexă', 1570, 2)")
cursor.execute("INSERT INTO tblPiese VALUES (5, 05, 'Colimator ajustabil', 2100, 2)")
cursor.execute("INSERT INTO tblPiese VALUES (6, 06, 'Bobină RMN pentru genunchi', 3670, 6)")
cursor.execute("INSERT INTO tblPiese VALUES (7, 07, 'Detector digital DR', 8900, 1)")
cursor.execute("INSERT INTO tblPiese VALUES (8, 08, 'Panou plat digital DR', 8500, 1)")
cursor.execute("INSERT INTO tblPiese VALUES (9, 09, 'Sondă ecografică liniară', 2100, 2)")
cursor.execute("INSERT INTO tblPiese VALUES (10, 10, 'Bobină RMN pentru cap', 4300, 3)")
cursor.execute("INSERT INTO tblPiese VALUES (11, 11, 'Injectomat pentru substanță de contrast', 3200, 1)")
cursor.execute("INSERT INTO tblPiese VALUES (12, 12, 'Grilă anti-scattering', 950, 4)")
connection.commit()


cursor.execute("INSERT INTO tblProducator VALUES (1, 'ImagiST', 1, '07123456789', 'imagist@yahoo.com', 'Bucuresti', 'imagist.com')")
cursor.execute("INSERT INTO tblProducator VALUES (2, 'MediTech', 2, '0722333444', 'contact@meditech.ro', 'Cluj-Napoca', 'meditech.ro')")
cursor.execute("INSERT INTO tblProducator VALUES (3, 'Radix Systems', 3, '0733555666', 'info@radix.com', 'Iasi', 'radixsystems.com')")
cursor.execute("INSERT INTO tblProducator VALUES (4, 'EchoScan', 4, '0744666777', 'support@echoscan.net', 'Timisoara', 'echoscan.net')")
cursor.execute("INSERT INTO tblProducator VALUES (5, 'BioScanTech', 5, '0755111222', 'office@bioscantech.com', 'Oradea', 'bioscantech.com')")
cursor.execute("INSERT INTO tblProducator VALUES (6, 'MedVision', 6, '0766222333', 'contact@medvision.ro', 'Constanta', 'medvision.ro')")
cursor.execute("INSERT INTO tblProducator VALUES (7, 'UltraImage Systems', 7, '0777333444', 'info@ultraimage.com', 'Brasov', 'ultraimage.com')")
cursor.execute("INSERT INTO tblProducator VALUES (8, 'DiagnoTech', 8, '0788123456', 'office@diagnotech.ro', 'Cluj', 'diagnotech.ro')")
cursor.execute("INSERT INTO tblProducator VALUES (9, 'NovaMed Systems', 9, '0799123456', 'contact@novamed.com', 'Bucuresti', 'novamed.com')")
cursor.execute("INSERT INTO tblProducator VALUES (10, 'ImageLine', 10, '0771123456', 'info@imageline.ro', 'Sibiu', 'imageline.ro')")
cursor.execute("INSERT INTO tblProducator VALUES (11, 'MedForLife', 11, '0712124567', 'MedForLife@yahoo.com', 'Bucuresti', 'MedForLife.com')")
cursor.execute("INSERT INTO tblProducator VALUES (12, 'ForTechnology', 12, '0755111333', 'ForTechnology@gmail.com', 'Oradea', 'ForTechnology.com')")
connection.commit()

cursor.execute("INSERT INTO tblClient VALUES (1, 'Popescu', 'Ioana', 1234567891011, '0723456785', 'popescu.ioana@gmail.com', 'eroare procesare', 'Bucuresti')")
cursor.execute("INSERT INTO tblClient VALUES (2, 'Ionescu', 'Andrei', 2980523123456, '0722123456', 'ionescu.andrei@gmail.com', 'eroare soft', 'Cluj')")
cursor.execute("INSERT INTO tblClient VALUES (3, 'Georgescu', 'Maria', 2960418123456, '0733444555', 'georgescu.maria@yahoo.com', 'problema monitor', 'Iasi')")
cursor.execute("INSERT INTO tblClient VALUES (4, 'Dumitru', 'Cristian', 1990101123456, '0744567890', 'dumitru.cristian@mail.com', 'blocare sistem', 'Constanta')")
cursor.execute("INSERT INTO tblClient VALUES (5, 'Lazar', 'Elena', 2940729123456, '0766789001', 'lazar.elena@outlook.com', 'defectiune hardware', 'Timisoara')")
cursor.execute("INSERT INTO tblClient VALUES (6, 'Stan', 'Mihai', 1981231123456, '0788990112', 'stan.mihai@gmail.com', 'eroare ecran', 'Brasov')")
cursor.execute("INSERT INTO tblClient VALUES (7, 'Tudor', 'Anca', 2970617123456, '0700111222', 'tudor.anca@yahoo.com', 'sunet lipsa', 'Oradea')")
cursor.execute("INSERT INTO tblClient VALUES (8, 'Barbu', 'Ion', 1960528123456, '0723450000', 'barbu.ion@mail.com', 'scurtcircuit', 'Ploiesti')")
cursor.execute("INSERT INTO tblClient VALUES (9, 'Matei', 'Silvia', 2950803123456, '0755666777', 'matei.silvia@gmail.com', 'necesita calibrare', 'Bacau')")
cursor.execute("INSERT INTO tblClient VALUES (10, 'Dragan', 'Paul', 1991102123456, '0799888777', 'dragan.paul@med.ro', 'reinitializare', 'Galati')")
connection.commit()


cursor.execute("INSERT INTO tblOfertare VALUES (1, 2, 01, 1, '2024-11-01', 'Bucuresti', 1234)")
cursor.execute("INSERT INTO tblOfertare VALUES (2, 3, 02, 1, '2024-12-15', 'Cluj', 4432)")
cursor.execute("INSERT INTO tblOfertare VALUES (3, 5, 03, 2, '2025-01-10', 'Constanta', 9972)")
cursor.execute("INSERT INTO tblOfertare VALUES (4, 7, 04, 5, '2025-03-05', 'Brasov', 8500)")
cursor.execute("INSERT INTO tblOfertare VALUES (5, 8, 05, 8, '2025-04-22', 'Ploiesti', 2100)")
cursor.execute("INSERT INTO tblOfertare VALUES (6, 9, 06, 10, '2025-05-20', 'Bacau', 3670)")
connection.commit()


cursor.execute("SELECT AVG(Pret_Lucrare) AS Pret_Mediu FROM tblOfertare;")
result = cursor.fetchone()  
print("Pret mediu:", result[0])
