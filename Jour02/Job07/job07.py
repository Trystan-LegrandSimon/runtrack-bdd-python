#!/usr/local/bin/python3.12

import mysql.connector

class Salarie:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="McDo"
        )
        self.cursor = self.conn.cursor()

    def create(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()

    def read_all(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def update(self, employee_id, new_salary):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salary, employee_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete(self, employee_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employee_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

# Exemple d'utilisation de la classe
salarie_manager = Salarie()
salarie_manager.create('Nouveau', 'Employe', 3200.00, 3)
all_employees = salarie_manager.read_all()
print("Tous les employés :", all_employees)
salarie_manager.update(1, 3800.00)
salarie_manager.delete(2)
salarie_manager.close_connection()