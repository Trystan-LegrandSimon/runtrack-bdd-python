-- Sélectionner la base de données
USE LaPlateforme;

/* On sélection tout les étudiant qui ont un prénom qui commence par B */
SELECT * FROM etudiant WHERE prenom LIKE 'B%';