-- Sélectionner la base de données
USE LaPlateforme;

/* On sélection tout les étudiant qui ont entre 18 et 25 ans dans l'ordre croissant */
SELECT * FROM etudiant WHERE age BETWEEN 18 AND 25 ORDER BY age ASC;