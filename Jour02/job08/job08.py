import mysql.connector

# Paramètres de la connexion à la base de données
config = {
    'user': 'root',
    'password': 'okmi',
    'host': 'localhost',
    'database': 'zoo'
}

# Connexion à la base de données
cnx = mysql.connector.connect(**config)

# Fonction pour ajouter un nouvel animal
def ajouter_animal(nom, race, id_cage, date_naissance, pays_origine):
    cursor = cnx.cursor()
    query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
    values = (nom, race, id_cage, date_naissance, pays_origine)
    cursor.execute(query, values)
    cnx.commit()
    print("L'animal a été ajouté avec succès.")

# Fonction pour supprimer un animal par son identifiant
def supprimer_animal(id_animal):
    cursor = cnx.cursor()
    query = "DELETE FROM animal WHERE id = %s"
    values = (id_animal,)
    cursor.execute(query, values)
    cnx.commit()
    print("L'animal a été supprimé avec succès.")

# Fonction pour modifier l'id de la cage d'un animal par son identifiant
def modifier_cage_animal(id_animal, id_cage):
    cursor = cnx.cursor()
    query = "UPDATE animal SET id_cage = %s WHERE id = %s"
    values = (id_cage, id_animal)
    cursor.execute(query, values)
    cnx.commit()
    print("L'animal a été modifié avec succès.")

# Fonction pour récupérer tous les animaux et les cages associées
def afficher_animaux_et_cages():
    cursor = cnx.cursor()
    query = "SELECT animal.nom, animal.race, cage.id, cage.superficie, cage.capacite_max FROM animal LEFT JOIN cage ON animal.id_cage = cage.id"
    cursor.execute(query)
    resultats = cursor.fetchall()
    for resultat in resultats:
        print(resultat)

# Fonction pour calculer la superficie totale de toutes les cages
def calculer
