-- Sélectionner la base de données
USE LaPlateforme;

-- Calcule de la capacité totale de toutes les salles
SELECT CONCAT('La capacité de toute les salles est de : ', SUM(capacite)) AS capacite_totale
FROM salle;