####################################################################
#Ce programme calcule le taux de GC dans un fichier au format FASTA#
####################################################################

# déclaration des variables #############
adn = True
ligne = 0

# on ouvre le fichier ###################
with open("seq_TD1.txt") as f:
   chaine = f.readlines()

# on compte le nombre de lignes #########
   for line in chaine : 
        ligne = ligne +1

seq = "".join([str(elem)for elem in chaine[1:ligne+1]])
# seq = seq.lower()

# on compte les différents nucléotides dans le fichier
for i in seq :
    #  on vérifie que la chaîne est une séquence d'ADN
    if i not in "actg\n" :
        adn = False
        break
    tc = seq.count("c")
    tg = seq.count("g")
    ta = seq.count("a")
    tt = seq.count("t")
    total = ta + tt + tc + tg

# on calcule le taux de CG ###############
tcg = ((tc + tg)/total)*100

# on gère les affichages #################
if adn == False :
    print("La séquence d'ADN n'est pas valide")
else :
    print("La séquence est valide")
    print('Le taux de GC contenu est ', tcg,'%')

print("total = ",total)
