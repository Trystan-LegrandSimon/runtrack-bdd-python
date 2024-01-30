-- Sélectionner la base de données
USE LaPlateforme;

-- Calcule l’ensemble de la superficie des étages et afficher le résultat
SELECT CONCAT('La superficie de La Plateforme est de ', SUM(superficie), ' m2') AS message
FROM etage;