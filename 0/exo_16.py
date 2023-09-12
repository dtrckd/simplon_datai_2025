#fonction run demarre en etant vraie 
run = True
#tant que run est vrai, on demande a l'utilisateur d'entrer un nombre
while run:
#Demander un nb au user => l'input definit comme integer 
    user_input = int(input('Enter Number: '))
#si le nb est 7, on affiche "you won" et on arrete la boucle
    if user_input == 7:
        print('You won!')
#si le nb n'est pas égale a 7 il devient false
        run = False
    else:
        print('try again!')