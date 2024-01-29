-- Modifier l'âge de Betty Spaghetti à 20 ans
UPDATE etudiant SET age = 20 WHERE nom = 'Spaghetti' AND prenom = 'Betty';

-- Vérifier que la modification a été effectuée
SELECT 'L\'âge de Betty Spaghetti a été corrigé.';

-- Vérifier que la modification a été effectuée
SELECT * FROM etudiant WHERE nom = 'Spaghetti' AND prenom = 'Betty';