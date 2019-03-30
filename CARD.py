def HAND(player):
    hand=[]
    import random
    roop=1
    while roop <= player*2:
        roop=roop+1
        X=random.randint(4,55)
        if X in hand:
            roop=roop-1
        else:
            hand.append(X)
    return hand

def BOARD(hand):
    board=[]
    import random
    roop=1

    while roop <= 5:
        roop=roop+1
        X=random.randint(4,55)
        if X in hand or X in board:
            roop=roop-1
        else:
            board.append(X)
    return board


def CHANGE(LIST):
    SHDQ=["s","h","d","q"]
    roop=1
    X=-1
    LISTS=[]
    LISTM=[]
    while roop <= len(LIST):
        roop=roop+1
        X=X+1
        Y=LIST[X] // 4
        W=LIST[X] % 4
        Z=SHDQ[W]
        LISTS.append(Y)
        LISTM.append(Z)

    return LISTS,LISTM

def TEKIHAND(CARD):
    tekihand=[]
    import random
    roop=1
    while roop <= 2:
        roop=roop+1
        X=random.randint(4,55)
        if X in CARD or X in tekihand:
            roop=roop-1
        else:
            tekihand.append(X)
    return tekihand
        
        
    
