from random import random

def getHollJjack():
    rnd = int(random()*99+1)
    print("rnd ", rnd)
    if rnd % 2 == 0:
        return "짝"
    else :
        return "홀"

com = getHollJjack()
print("com", com)