-- Calculer la moyenne d'âge des étudiants et petit plus arrondi à un nombre entier
SELECT ROUND(AVG(age)) AS moyenne_age_arrondie FROM etudiant;

----------------------------------------------------------------

-- Au cas ou...
-- La basiqiue
SELECT AVG(age) AS moyenne_age FROM etudiant;