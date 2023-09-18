#liste de nb
l = [1,2,-3,-4,5,7,17,-16]
#nouvelle liste avec les nombre paire que j'ai select dans la première
def newlist(i):
    #parcourir la liste
    for i in l:
    #sortir les nombre pairs
        if i%2==0:
            print(i)
newlist(l)

