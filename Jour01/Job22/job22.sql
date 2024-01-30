-- Sélectionner la base de données
USE LaPlateforme;

-- Récupérer les informations de l'étudiant le plus jeune
SELECT * FROM etudiant ORDER BY age ASC LIMIT 1;