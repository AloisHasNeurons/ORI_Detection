file = open("sequence/seq_TD1.txt", "r")
file_write = open("sortie/seq_TD1_sortie.txt", "w")
seq = file.readlines()
adn = True
taille = int(input("Entrer la taille de la fenetre"))
ligne = 0
for line in seq: 
    ligne = ligne + 1
chaine = ''.join([str(elem)for elem in seq[1:ligne+1]])
for i in chaine:
    if i not in "atgcn\n":
        adn = False
        break
if (adn == True):
    print("Valide")
    for i in (range(1,len(chaine),taille)):
        tg = chaine[i:i+taille].count("g")
        tc = chaine[i:i+taille].count("c")
        ta = chaine[i:i+taille].count("a")
        tt = chaine[i:i+taille].count("t")
        tauxgc = ((tg + tc) /taille) *100
        stri = str(i)
        strtauxgc = str(tauxgc)
        ecrire = stri+"\t"+strtauxgc+"\n"
        file_write.write(ecrire)
    print("Fichier creer")
else:
    print("Invalide")
