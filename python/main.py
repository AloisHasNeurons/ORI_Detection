from fonctions import *
import subprocess

#######################################################
#-------------Déclaration des variables---------------#
#######################################################

adn = True
ligne = 0

#######################################################
#-------------Traitement des fichiers-----------------#
#######################################################

# On ouvre le fichier et on stocke les valeurs dans une variable
file = open("Sequence/Borrelia_burgdorferi_B31_complete_genome.txt", "r")
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

######################################################################
#-------------Ecriture du fichier de sortie et appel du R -----------#
######################################################################

# On peut calculer le taux de GC uniquement si la séquence est valide
if (adn == True):
    print("Séquence valide")
    tailleF, pas = inputfp()
    reponse = menu()
    createFile(reponse,pas, tailleF, longueur, chaine)
    # Lancement du programme R en fonction de l'option choisie
    print("Lancement du programme R")
    if (reponse == 3):
        subprocess.call(["Rscript", "R/graph_plot.r"])
    elif (reponse == 1):
        subprocess.call(["Rscript", "R/graph_plot_tauxGC.r"])
    elif (reponse == 2):
        subprocess.call(["Rscript", "R/graph_plot_calcGC.r"])
else:
    print("Séquence invalide")