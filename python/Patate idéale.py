from fonctions import *
import rpy2.robjects as robjects
import subprocess

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

#######################################################
#-------------Ecriture du fichier de sortie-----------#
#######################################################

# On peut calculer le taux de GC uniquement si la séquence est valide
if (adn == True):
    print("Séquence valide")
    tailleF, pas = inputfp()
    file_write = open("sortie/tauxGC.txt", "w")
    file_write.write("Position"+"\t"+"TauxGC"+"\n")
    traitement(pas, tailleF, file_write, longueur, chaine)
    print("Fichier de taux de GC créé")   
    file_write.close()
    print("Lancement du programme R")
    subprocess.call(["Rscript", "R/graph_plot.r"])
else:
    print("Séquence invalide")