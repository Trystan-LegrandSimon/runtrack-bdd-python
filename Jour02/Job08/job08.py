#!/usr/local/bin/python3.12

import mysql.connector

class ZooManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoo"
        )
        self.cursor = self.conn.cursor()

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"Animal {nom} ajouté avec succès.")

    def supprimer_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s"
        values = (animal_id,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"Animal avec l'ID {animal_id} supprimé avec succès.")

    def modifier_animal(self, animal_id, nom, race, id_cage, date_naissance, pays_origine):
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        values = (nom, race, id_cage, date_naissance, pays_origine, animal_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print(f"Animal avec l'ID {animal_id} modifié avec succès.")

    def afficher_animaux(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("\nAnimaux présents dans le zoo :")
        for row in result:
            print(row)

    def afficher_animaux_cages(self):
        query = "SELECT a.*, c.superficie, c.capacite_max FROM animal a JOIN cage c ON a.id_cage = c.id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("\nAnimaux dans les cages avec informations sur les cages :")
        for row in result:
            print(row)

    def calculer_superficie_totale(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        superficie_totale = result[0] if result[0] is not None else 0
        print(f"\nLa superficie totale de toutes les cages est de {superficie_totale} m2.")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

# Exemple d'utilisation
zoo_manager = ZooManager()
zoo_manager.ajouter_animal("Lion", "Félin", 1, "2022-01-01", "Afrique")
zoo_manager.ajouter_animal("Éléphant", "Mammifère", 2, "2022-02-01", "Asie")
zoo_manager.afficher_animaux()
zoo_manager.afficher_animaux_cages()
zoo_manager.calculer_superficie_totale()
zoo_manager.close_connection()