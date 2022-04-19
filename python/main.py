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
file = open("La-patate-ideale/Sequence/Borrelia_burgdorferi_B31_complete_genome.txt", "r")
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

    ########- Ecriture du fichier de taux de GC -########
    file_write = open("La-patate-ideale/sortie/tauxGC.txt", "w")
    file_write.write("Position"+"\t"+"TauxGC"+"\n")
    traitement(pas, tailleF, file_write, longueur, chaine)
    print("Fichier de taux de GC créé")
    file_write.close()

    ########- Ecriture du fichier de G-C/G+C -########
    file_write = open("La-patate-ideale/sortie/tauxGC2.txt", "w")
    file_write.write("Position"+"\t"+"G-C/G+C"+"\n")
    traitement2(pas, tailleF, file_write, longueur, chaine)
    print("Fichier du G-C/G+C créé")
    file_write.close()

    print("Lancement du programme R")
    subprocess.call(["Rscript", "La-patate-ideale/R/graph_plot.r"])

else:
    print("Séquence invalide")