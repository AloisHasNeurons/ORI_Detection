from fonctions import *
#######################################################
#-------------Déclaration des variables---------------#
#######################################################
position = 1
adn = True
tailleF = int(input("Entrer la taille de la fenetre"))
ligne = 0

#######################################################
#-------------Traitement des fichiers-----------------#
#######################################################
#On ouvre le fichier et on stocke les valeurs dans une variable
file = open("seq_TD1.txt", "r")
seq = file.readlines()

#Récupération du nombre de lignes
for line in seq:
    ligne = ligne + 1
chaine = ''.join([str(elem)for elem in seq[1:ligne+1]])
longueur = len(chaine)
chaine = supprrc(chaine)
file.close()

file_write = open("seq_TD1_sortie.txt", "w")

#####################################
#-----Vérification de la séquence---#
#####################################
for i in chaine:
    if i not in "atgc":
        adn = False
        break

#####################################
#-----Ecriture du fichier de sortie-#
#####################################
#On peut calculer le taux de GC uniquement si la séquence est valide
if (adn == True):
    print("Séquence valide")
    for i in (range(0, longueur+1, tailleF)):
        #Calcul du taux de GC pour i 
        tauxgcV = tauxgc(i, chaine, tailleF)

        #Récupération de la position de i 
        if position > len(chaine):
            diff = position - len(chaine)
            position = position - diff
        strposition = str(position)
        
        #
        ecrire = "("+strposition+",\t"+tauxgcV+")"+"\n"
        file_write.write(ecrire)
        position += tailleF
    print("Fichier creer")
else:
    print("Séquence invalide")
