#declarer fonction de liste de mots

l = ["Salut", "alors", "ça", "va", "ma", "grosse", "puce","yellow", "?"]

def liste_mots(i):
#retourner la liste avec les mots dont la premiere lettre est une voyelle
    for i in l:
#prendre l'index de la première lettre de chaque mot
        if i[0] in "aeiouyAEIOUY":
            print(i)
liste_mots(l)

