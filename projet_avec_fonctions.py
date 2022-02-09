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
seq = file.readlines()
for line in seq:
    ligne = ligne + 1
chaine = ''.join([str(elem)for elem in seq[1:ligne+1]])
longueur = len(chaine)
newseq = chaine.replace("\n", "")
file.close()

chaine = newseq
file_write = open("seq_TD1_sortie.txt", "w")

#####################################
#-----Calcul du taux de GC----------#
#####################################
def tauxgc(i) :
    tg = chaine[i:i+taille].count("g")
    tc = chaine[i:i+taille].count("c")
    return ((tg + tc)/taille) *100

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
#On peut calculer le taux de GC uniquement si la séquence est valide
if (adn == True):
    print("Séquence valide")
    for i in (range(0, longueur+1, taille)):
        #Calcul du taux de GC pour i 
        tauxgcV = tauxgc(i)
        strtauxgc = str(tauxgcV)

        #Récupération de la position de i 
        if position > len(chaine):
            diff = position - len(chaine)
            position = position - diff
        strposition = str(position)
        
        #
        ecrire = "("+strposition+",\t"+strtauxgc+")"+"\n"
        file_write.write(ecrire)
        position += taille
    print("Fichier creer")
else:
    print("Séquence invalide")
