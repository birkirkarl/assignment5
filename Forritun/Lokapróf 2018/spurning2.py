

# 5x5 
# Notandinn byrjar efst í vinstra horni á skjánum og getur í sérhverri færslu fært sig til vinstri, hægri, upp eða niður.
#  Notandinn gefur færslur til kynna með eftirfarandi bókstöfum (allir aðrir bókstafir enda keyrslu forritsins):
# 'l' fyrir vinstri
# 'r' fyrir hægri
# 'u' fyrir upp
# 'd' fyrir niður
# Notandi færist aldrei út úr hnitakerfinu. 
# Ef notandi er t.d. staddur í dálki lengst til vinstri og ýtir á 'l' þá færist hann í dálkinn lengst til hægri.


# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'
Zero=0
End=4
def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid(current):
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)
    
    grid[current[0]][current[1]] = POSITION  # Current position

    return grid

def game_board(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            print("{} ".format(grid[i][j]), end=" ")
        print()
    print()
def move_maker(move,current):
    x=current[0]
    y=current[1]
    if move=='l':  #left
        if y==Zero:
            y=End
        else:
            y -= 1
    elif move=='r': #right
        if y == End:
            y=Zero
        else:
            y +=1
    elif move=='u': #up
        if x==Zero:
            x=End
        else:
            x-=1
    else: # down
        if x==End:
            x=Zero
        else:
            x+=1
    current[0]=x
    current[1]=y
    return current
def main():
    current=[0,0]
    while True:
        grid=initialize_grid(current)
        game_board(grid)
        the_move=get_move()
        if the_move=='q':
            break
        current=move_maker(the_move,current)
main()