from fonctions import *
#######################################################
#-------------Déclaration des variables---------------#
#######################################################
position = 1
adn = True
ligne = 0
#######################################################
#-------------Traitement des fichiers-----------------#
#######################################################
# On ouvre le fichier et on stocke les valeurs dans une variable
file = open("seq_TD1.txt", "r")
seq = file.readlines()

# Récupération du nombre de lignes
for line in seq:
    ligne = ligne + 1

chaine = ''.join([str(elem)for elem in seq[1:ligne+1]])
chaine = supprrc(chaine)
longueur = len(chaine)
file.close()

# Vérification de la séquence
adn = validation(chaine)

#######################################################
#-------------Ecriture du fichier de sortie-----------#
#######################################################
# On peut calculer le taux de GC uniquement si la séquence est valide
if (adn == True):
    print("Séquence valide")
    tailleF, pas = inputfp()
    file_write = open("tauxGC.txt", "w")
    for i in (range(0, longueur+1, pas)):
        # Calcul du taux de GC dans la taille de la fenêtre
        tauxgcV = tauxgc(i, chaine, tailleF)
        ecriture(position, tauxgcV, file_write)
        position = checkposition(position, chaine, pas)
    print("Fichier de taux de GC créé")
    file_write.close()
else:
    print("Séquence invalide")
