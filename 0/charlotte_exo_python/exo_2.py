#declarer liste de nb
l = [1,2,-3,-4,5,7,17,-16]

def function(n):
# Verifier la liste et ne sortir que les nb positifs
    for i in n:
        if i > 0:
            print(i)
        
function(l)