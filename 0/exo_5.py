# demander a l'utilisateur de choisir un mot
word = (input("Choisis un mot petite perruche : "))
# appliquer la fonction qui permet de compter le nombre de caractere
if len(word) > 5: # type: ignore
    print("Le mot est trop long")
