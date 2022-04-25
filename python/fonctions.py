#################################################
#------------Calcul du taux de GC---------------#
#################################################


def tauxgc(i, chaine, taille, position, longueur):
    if (position >= longueur - taille):
        tailleM = longueur - position
    else:
        tailleM = taille
    tg = chaine[i:i+tailleM].count("G")
    tc = chaine[i:i+tailleM].count("C")
    tgc = ((tg + tc)/tailleM) * 100
    tgc = round(tgc, 2)
    return str(tgc)


def calcgc(i, chaine, taille, position, longueur):
    if (position >= longueur - taille):
        tailleM = longueur - position
    else:
        tailleM = taille
    tg = chaine[i:i+tailleM].count("G")
    tc = chaine[i:i+tailleM].count("C")
    tgc = ((tg - tc)/(tg + tc)) * 100
    tgc = round(tgc, 2)
    return str(tgc)


#################################################
#-----------Validation de la sequence-----------#
#################################################


def validation(chaine):
    for i in chaine:
        if i not in "ATGCKMNRSWY":
            return False
    return True


#################################################
#-----------Ecrire sur le fichier---------------#
#################################################


def ecriture(position, tauxgcV, file):
    strposition = str(position)
    ecrire = strposition+"\t"+tauxgcV+"\n"
    file.write(ecrire)


#################################################
#------Suppression des retours chariots---------#
#################################################


def supprrc(chaine):
    newseq = chaine.replace("\n", "")
    newseq = newseq.upper()
    return newseq


#################################################
#-----------Changement de la position-----------#
#################################################


def checkposition(position, chaine, pas):
    position = position + pas
    return position


#################################################
#-----Demande des valeurs des variables---------#
#################################################


def inputfp():
    tailleF = int(input("Entrez la taille de la fenetre : "))
    while tailleF < 0:
        tailleF = int(input("Entrez une taille de fenêtre > 0 : "))
    pas = int(input("Entrez le pas : "))
    while pas > tailleF | pas <= 0:
        pas = int(input("Entrez un pas inférieur à la taille de la fenêtre et supérieur à 0 svp : "))
    return tailleF, pas


def menu():
    reponse = int(input("Choisissez une option : \n 1 - Taux de GC \n 2 - G-C/G+C \n 3 - Les deux calculs \n"))
    # Check that reponse is between 1 and 3
    while reponse < 1 or reponse > 3:
        reponse = int(input("Choisissez une option : \n 1 - Taux de GC \n 2 - G-C/G+C \n 3 - Les deux calculs \n"))
    return reponse


#################################################
#--------Ecriture du fichier de sortie----------#
#################################################


def traitement(pas, tailleF, file, longueur, chaine):
    position = 0
    for i in (range(0, longueur, pas)):
        if (position >= longueur - tailleF):
            tauxgcV = tauxgc(i, chaine, tailleF, position, longueur)
            ecriture(position/1000, tauxgcV, file)
            position = checkposition(position, chaine, pas)
            break
        tauxgcV = tauxgc(i, chaine, tailleF, position, longueur)
        ecriture(position/1000, tauxgcV, file)
        position = checkposition(position, chaine, pas)


def traitement2(pas, tailleF, file, longueur, chaine):
    position = 0
    for i in (range(0, longueur, pas)):
        if (position >= longueur - tailleF):
            tauxgcV = calcgc(i, chaine, tailleF, position, longueur)
            ecriture(position/1000, tauxgcV, file)
            position = checkposition(position, chaine, pas)
            break
        tauxgcV = calcgc(i, chaine, tailleF, position, longueur)
        ecriture(position/1000, tauxgcV, file)
        position = checkposition(position, chaine, pas)


#################################################
#--------Création du fichier de sortie----------#
#################################################


def createFile(reponse, pas, tailleF, longueur, chaine):
    if (reponse == 3):
        createFile(1, pas, tailleF, longueur, chaine)
        createFile(2, pas, tailleF, longueur, chaine)
    elif (reponse == 1):
        file = open("sortie/tauxgc.txt", "w")
        file.write("Position(Kb)\tTaux de GC\n")
        traitement(pas, tailleF, file, longueur, chaine)
        file.close()
        print("Le fichier tauxgc.txt a été créé")
    elif (reponse == 2):
        file = open("sortie/calcGC.txt", "w")
        file.write("Position(Kb)\tG-C/G+C\n")
        traitement2(pas, tailleF, file, longueur, chaine)
        file.close()
        print("Le fichier calcGC.txt a été créé")
