# Ajouter élève
INSERT INTO etudiants (prenom, nom, age, email)
VALUES ('Martin', 'Dupuis', 18, 'martin.dupuis@laplateforme.io');

# Tri meme famille
SELECT * FROM etudiants
WHERE nom = 'Dupuis';
