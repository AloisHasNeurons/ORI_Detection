file = open("sequence/seq_TD1.txt", "r")
file_write = open("sortie/seq_TD1_sortie.txt", "a")
seq = file.readlines()
adn = True
ligne = 0
n = "\n"
n  = str(n)
while 'n' in seq:
    seq.remove(n)
print(seq)
for line in seq: 
    ligne = ligne + 1
chaine = ''.join([str(elem)for elem in seq[1:ligne+1]])
for i in chaine:
    if i not in "atgc\n":
        adn = False
        break
if (adn == True):
    print("Valide")
    for i in (range(1,11)):
        tg = chaine[i:i+10].count("g")
        tc = chaine[i:i+10].count("c")
        ta = chaine[i:i+10].count("a")
        tt = chaine[i:i+10].count("t")
        total = tg + tc + ta + tt
    tauxgc = ((tg + tc) / total) *100
    print(total)
    print(tauxgc)
else:
    print("Invalide")
