#####################################
#-----Déclaration des variables-----#
#####################################
position = 1
adn = True
taille = int(input("Entrer la taille de la fenetre"))
ligne = 0

#####################################
#-----Traitement des fichiers-------#
#####################################
#
file = open("seq_TD1.txt", "r")
sans_espace = open("seq_TD1_sans_espace.txt", "w")
seq = file.readlines()
for line in seq:
    ligne = ligne + 1
chaine = ''.join([str(elem)for elem in seq[1:ligne+1]])
newseq = chaine.replace("\n", "")
file.close()

#Création d'un fichier exploitable
file = open("seq_TD1_sans_espace.txt", "w")
file.write(newseq)
file.close()

file = open("seq_TD1_sans_espace.txt", "r")
chaine = file.read()
file_write = open("seq_TD1_sortie.txt", "w")

#####################################
#-----Calcul du taux de GC----------#
#####################################
def tauxgc(i) :
    tg = chaine[i:i+taille].count("g")
    tc = chaine[i:i+taille].count("c")
    tauxgc = ((tg + tc)/taille) *100

#####################################
#-----Vérification de la séquence---#
#####################################
for i in chaine:
    if i not in "atgc\n":
        adn = False
        break

#####################################
#-----Ecriture du fichier de sortie-#
#####################################

chaine = ''.join([str(elem)for elem in seq[1:ligne+1]])
print (position)
