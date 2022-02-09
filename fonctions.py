#####################################
#-----Calcul du taux de GC----------#
#####################################
def tauxgc(i, chaine, taille) :
    tg = chaine[i:i+taille].count("g")
    tc = chaine[i:i+taille].count("c")
    return ((tg + tc)/taille) *100

#########################################
#-----Validationde la sequence----------#
#########################################
def validation (chaine):
    for i in chaine:
        if i not in "atgc":
            return False
        else:
            return True
######################################
#-----Ecrire sur le fichier----------#
######################################
def ecriture(strposition, strtauxgc, file):
    ecrire = "("+strposition+",\t"+strtauxgc+")"+"\n"
    file.write(ecrire)