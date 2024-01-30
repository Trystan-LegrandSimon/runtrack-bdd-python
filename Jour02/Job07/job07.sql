-- Active: 1706522342473@@127.0.0.1@3306@McDo
--1. Créer la base de données et la table "employe":
CREATE DATABASE IF NOT EXISTS McDo;
USE McDo;

CREATE TABLE employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10, 2),
    id_service INT
);

-- Insérer des employés dans la table "employe"
INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
('Doe', 'John', 3500.00, 1),
('Smith', 'Jane', 4000.00, 2),
('Johnson', 'Bob', 2800.00, 1);


--2. Récupérer les employés dont le salaire est supérieur à 3 000 €:
SELECT * FROM employe WHERE salaire > 3000;

-- Ajouter la table "service"
CREATE TABLE service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255)
);


--3. Insérer des services dans la table "service"
INSERT INTO service (nom) VALUES
('Service A'),
('Service B'),
('Service C');


--4. Récupérer tous les employés et leur service respectif:
SELECT employe.id, employe.nom, employe.prenom, employe.salaire, service.nom AS service
FROM employe
JOIN service ON employe.id_service = service.id;