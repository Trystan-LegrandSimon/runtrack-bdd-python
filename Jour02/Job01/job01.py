#!/usr/local/bin/python3.12

import mysql.connector

# Remplacez ces informations par les détails de votre base de données
host = "localhost"
user = "root"
password = ""
database = "LaPlateforme"

# Connexion à la base de données
conn = mysql.connector.connect(host = host, user = user, password = password, database = database)
cursor = conn.cursor()

# Exécution de la requête pour récupérer tous les étudiants
query = "SELECT * FROM etudiant"
cursor.execute(query)

# Récupération des résultats
students = cursor.fetchall()

# Affichage des résultats en console
for student in students:
    print(student)

# Fermeture des connexions
cursor.close()
conn.close()