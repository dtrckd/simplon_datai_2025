#créer une liste de mots
l = ["Salut", "alors", "ça", "va", "ma", "grosse", "puce","yellow", "?"]
#definir la fonction qui renvoie les mots dont la première lettre est une voyelle
def funk(i):
    for i in l:
#prendre l'index de la première lettre de chaque mot
        if i[0] in "aeiouyAEIOUY":
            print(i)
funk(l)