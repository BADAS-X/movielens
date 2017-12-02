notes = [
    [1, -1, 0, 1, 0, -1],
    [-1, 0, 1, -1, 1, 1],
    [1, 1, 1, 1, -1, -1],
    [1, 1, 0, 0, 1, -1],
    [1, -1, 1, 1, -1, 0]
]
nb_gens = 5
nb_films = 6
prenoms = ['Alice', 'Bob', 'Charles', 'Daisy', 'Everett']
films = ['007', 'Batman 1', 'Shrek 2', 'Toy Story 3', 'Star Wars 4', 'Twilight 5']
NB_VOISINS = 3
NB_PREDICTIONS = 2

# from big import notes, nb_gens, nb_films, prenoms, films, NB_VOISINS, NB_PREDICTIONS


def calculer_score(i, j):
    """
    Score de proximité entre
    les personnes i et j
    """
    pass

# print(calculer_score(0, 1))  # score(Alice, Bob) = -3
# print(calculer_score(0, 2))  # score(Alice, Charles) = 2


def calculer_tous_scores():
    """
    Matrice des scores de proximité
    entre toutes les personnes
    """
    pass

"""for ligne in calculer_tous_scores():  # À éviter lorsque le dataset est gros
    print(ligne)"""


def plus_proches_voisins(i):
    """
    Liste des plus proches voisins
    de la personne i
    """
    pass


def calculer_prediction(i, i_film, voisins):
    """
    Estimation du score du film i_film
    pour la personne i à partir de ses voisins
    """
    pass


def calculer_toutes_predictions(i, voisins):
    """
    Renvoie les prédictions pour la personne i
    à partir de ses voisins
    """
    pass

"""print('Prédictions pour Alice')
voisins = plus_proches_voisins(0)
for ligne in calculer_toutes_predictions(0, voisins):
    print(ligne)"""


def nouvel_inscrit():
    """
    (facultatif)
    Que faire quand on a un nouvel inscrit ?
    """
    pass


# mon_id = nouvel_inscrit()
# voisins = plus_proches_voisins(mon_id)
# for ligne in calculer_toutes_predictions(mon_id, voisins):
#     print(ligne)
