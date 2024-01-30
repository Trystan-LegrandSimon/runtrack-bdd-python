-- Sélectionner la base de données
USE LaPlateforme;

-- Création de la table "etudiant"
INSERT INTO etudiant (nom, prenom, age, email) VALUES
    ('Spaghetti', 'Betty', 23, 'betty.Spaghetti@laplateforme.io'),
    ('Chuck', 'Steak', 45, 'chuck.steak@laplateforme.io'),
    ('Doe', 'John', 18, 'john.doe@laplateforme.io'),
    ('Barnes', 'Binkie', 16, 'binkie.barnes@laplateforme.io'),
    ('Dupuis', 'Gertrude', 20, 'gertrude.dupuis@laplateforme.io');


-- Vérification des données
SHOW TABLES;