"""
http://jill-jenn.net/algo/stage-python/welcome.html
"""

print("Coucou !")
print(2 * 3)
print((3 + 3) * 7)

nbEtoiles = 5
print("*" * nbEtoiles)
print("Il y a", nbEtoiles, "etoiles")
print("S'il y en avait deux fois plus, il y en aurait", nbEtoiles * 2)

nbClients = 0
nbClients += 10
nbClients = nbClients * 2 + 10
print(nbClients)

for i in range(5):
    print("Coucou !")
    
jour = 25
mois = "Decembre"
if jour == 25 and mois == "Decembre":
    print("Joyeux Noel !")
    print("Toutes les instructions de ce cote-ci sont executees")
else:
    print("Rien a signaler")
    print("Les instructions de ce cote-la ne sont pas executees")
    
nbAllumettes = 5
if nbAllumettes < 1:
    print("Ce nombre est trop faible")
elif nbAllumettes > 3:
    print("Ce nombre est trop grand")
else:
    print("Ce nombre est correct")

liste = [1, 2, 3]
print(liste[0])
print(liste[2])
print("La liste a", len(liste), "elements")
liste[1] = 1000  # Remplacement d'un element de la liste
print(liste)

agesSoeurs = [14, 17, 47]
for idSoeur in range(len(agesSoeurs)):
    print("La soeur numero", idSoeur, "a", agesSoeurs[idSoeur], "ans")
for age in agesSoeurs:
    print(age)

chaine = "abracadabra"
print(chaine)

liste = [3, 1, 2]
print(liste)
liste.sort()
print(liste)

liste = [(3, "bonjour"), (1, "salut"), (2, 'coucou')]
print(liste)
liste.sort()
print(liste)

liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(liste[:4])
print(liste[-3:])