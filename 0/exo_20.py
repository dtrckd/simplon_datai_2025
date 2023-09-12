import runpy


run = True
l = []
def funk(i):
    while runpy:
        user_input = str(input("choisis un petit mot ma poulette"))
        if len(user_input) > 5:
            print("Le mot fait plus de 5 caractiflute ma puce")

        else:
            print("Le mot fait moins de 5 caractiflute ma puce")
            run = False

funk(l)
