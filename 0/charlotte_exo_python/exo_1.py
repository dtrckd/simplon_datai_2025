#saisir un nombre entier positif
n = int(input("Entrer un nombre entier positif : "))

# Vérifier si n est positif
if n <= 0:
    print("Le nombre doit être positif.")
else:
    print("Nombres pairs de 1 à", n, "sont :")
    for i in range(1, n +1):
        print(i)
