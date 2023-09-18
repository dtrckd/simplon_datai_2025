#ecrire une Fonction qui prend en entrée une liste de nombre 
l = int(input("Entrer un nombre : "))
#definir la fonction qui renvoie si le nombre est positif, negatif, ou nul
def function(n):
    if n > 0:
        print("Le nombre est positif")
    elif n < 0:
        print("Le nombre est négatif")
    else:
        print("Le nombre est nul")
#appeler la fonction
function(l)