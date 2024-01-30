-- Sélectionner la base de données
USE LaPlateforme;

-- Compter le nombre d'étudiants mineurs
SELECT COUNT(*) AS nombre_etudiants_mineurs FROM etudiant WHERE age < 18;