#Definir une list de nb en entrée 
l = [1,2,3,4,5,6,7,8,9]
#definir la fonction qui renvoie les nombres paires de la liste
def funky(i):
     #parcourir la liste
    for i in l:
    #sortir les nombre pairs
        if i%2==0:
            #renvoyer le tableau 
            print(i)
funky(l)
