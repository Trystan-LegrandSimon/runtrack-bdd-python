-- Sélectionner la base de données
USE LaPlateforme;

=======
>>>>>>> 1bdd7bf (Jour02 : add Job02)
-- Création de la table "etage"
CREATE TABLE etage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    numero INT,
    superficie INT
);

-- Création de la table "salle"
CREATE TABLE salle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    id_etage INT,
    capacite INT
);