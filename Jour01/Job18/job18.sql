-- Sélectionner la base de données
USE LaPlateforme;

-- Supprimer John Doe de la table etudiant
DELETE FROM etudiant WHERE nom = 'Doe' AND prenom = 'John';

-- Vérification de la suppression
SELECT * FROM etudiant