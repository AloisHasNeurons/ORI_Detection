#################################################
#-----Calcul du taux de GC----------------------#
#################################################
def tauxgc(i, chaine, taille) :
    tg = chaine[i:i+taille].count("g")
    tc = chaine[i:i+taille].count("c")
    tgc = ((tg + tc)/taille) *100
    return str(tgc)

#################################################
#-----Suppression des retours chariots----------#
#################################################
def supprrc(chaine) :
    return chaine.replace("\n", "")