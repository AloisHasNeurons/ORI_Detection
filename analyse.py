# Test est ce que tu as les modifications
file = open("Demarche scientifique/seq_TD1.txt", "r")
file_write = open("Demarche scientifique/seq_TD1_sortie.txt", "w")
sans_espace = open("Demarche scientifique/seq_TD1_sans_espace.txt", "w")
seq = file.readlines()
position = 1
adn = True
taille = int(input("Entrer la taille de la fenetre"))
ligne = 0
for line in seq:
    ligne = ligne + 1
chaine = ''.join([str(elem)for elem in seq[1:ligne+1]])
for i in chaine:
    if i not in "atgc\n":
        adn = False
        break
seq = file.read()
newseq = chaine.replace("\n", "")
file.close()
file = open("Demarche scientifique/seq_TD1_sans_espace.txt", "w")
file.write(newseq)
file.close()
file = open("Demarche scientifique/seq_TD1_sans_espace.txt", "r")
chaine = file.read()
longueur = len(chaine)
if (adn == True):
    print("Valide")
    for i in (range(0, longueur+1, taille)):
        tg = chaine[i:i+taille].count("g")
        tc = chaine[i:i+taille].count("c")
        ta = chaine[i:i+taille].count("a")
        tt = chaine[i:i+taille].count("t")
        tauxgc = ((tg + tc) / taille) * 100
        if position > len(chaine):
            diff = position - len(chaine)
            position = position - diff
        strposition = str(position)
        strtauxgc = str(tauxgc)
        ecrire = "("+strposition+",\t"+strtauxgc+")"+"\n"
        file_write.write(ecrire)
        print(position)
        position += taille
    print("Fichier creer")
else:
    print("Invalide")
