#####################################
#-----Calcul du taux de GC----------#
#####################################
def tauxgc(i, chaine, taille) :
    tg = chaine[i:i+taille].count("g")
    tc = chaine[i:i+taille].count("c")
    return ((tg + tc)/taille) *100