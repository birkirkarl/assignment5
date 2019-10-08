def create_board(vidd): # vidd er ehv tala sem byr til tölur 1-vidd^2
    tolurnar=[]
    tmp=[]
    for i in range(1,(vidd**2)+1):
        tmp.append(i)
        if len(tmp)==vidd:
            tolurnar.append(tmp)
            tmp=[]
    return tolurnar

def create_tic(bordid): #prenta her board eftir hvern leik
    for i in range(len(bordid)):
        for j in range(len(bordid)):
            print("{:>5}".format(bordid[i][j]), end=" ")
        print()

def finna_tolu(bordid, tala):
    global player1
    global player2
    for i in bordid:
        if tala in i:
            x=i.index(tala)
            if player1==True:
                i[x]='X'
            else:
                i[x]='O'
            return bordid

def spilari_gerir(bordid):
    global player1
    global player2
    leikur_gerdur=True
    while leikur_gerdur:
        try:
            if player1==True:
                tala=int(input("X position: "))
            elif player2==True:
                tala=int(input("O position: "))
            nyjabordid=finna_tolu(bordid,tala)
            if nyjabordid == None:
                print("Illegal move!")
            else:
                leikur_gerdur=False
                if player1==True:
                    player1=False
                    player2=True
                else:
                    player1=True
                    player2=False
                return nyjabordid
        except Exception:
            print("Illegal move!")

def horizontal_victory_checker(bordid):
    for win_list in bordid: #þetta er lárétti checkerinn
        sigur=last_check_if_victory(win_list)
        if sigur == False:
            break
    return sigur

def diagonal_victory_checker(bordid,vidd):
    win_list=[]
    for i in range(vidd): #lóðrétti checkerinn
        for j in range(vidd):
            win_list.append(bordid[j][i])
        sigur=last_check_if_victory(win_list)
        return sigur

def left_slope_victory(bordid,vidd):
    win_list=[]
    for i in range(vidd): #skácheckari
        win_list.append(bordid[i][i])
    sigur=last_check_if_victory(win_list)
    return sigur

def right_slope_victory(bordid,vidd):#skácheckari
    win_list=[]
    count=vidd-1
    for i in range(vidd):
        win_list.append(bordid[count][i])
        count -=1
    sigur=last_check_if_victory(win_list)
    return sigur

def last_check_if_victory(win_list):
    if len(set(win_list))==1:
        sigur=False
        return sigur
    else:
        return True

def is_it_draw(bordid):
    draw_list=[]
    for i in bordid:
        for j in i:
            draw_list.append(j)
    if len(set(draw_list))==2:
        return False
    else:
        return True

def victory_check(bordid,vidd):
    sigur1=horizontal_victory_checker(bordid)
    sigur2=diagonal_victory_checker(bordid,vidd)
    sigur3=left_slope_victory(bordid,vidd)
    sigur4=right_slope_victory(bordid,vidd)
    no_winner=is_it_draw(bordid)
    if sigur1==False or sigur2==False or sigur3==False or sigur4==False:
        sigur=False
        if player1==False:
            winner='X'
        else:
            winner='O'
        print("Winner is: "+winner)
        return sigur
    elif no_winner==False:
        sigur=no_winner
        print("Draw!")
        return sigur
    return True,None

#main loop
player1=True
player2=False
sigur=True
vidd=int(input("Input dimension of the board: "))
bordid=create_board(vidd)
create_tic(bordid)
while sigur:
    bordid=spilari_gerir(bordid)
    create_tic(bordid)
    sigur=victory_check(bordid,vidd)
