#!/usr/local/bin/python3.12

import mysql.connector

# Remplacez ces informations par les détails de votre base de données
host = "localhost"
user = "root"
password = ""
database = "LaPlateforme"

# Connexion à la base de données
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

# Exécution de la requête pour récupérer les noms et les capacités de la table "salle"
query = "SELECT nom, capacite FROM salle"
cursor.execute(query)

# Récupération des résultats
salles = cursor.fetchall()

# Affichage des résultats en console
for salle in salles:
    print(salle)

# Fermeture des connexions
cursor.close()
conn.close()