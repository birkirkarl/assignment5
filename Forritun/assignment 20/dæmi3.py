We want to make a row of bricks that is goal inches long.
 We have a number of small bricks (1 inch each) and big bricks (5 inches each).
  Create a function that takes 3 parameter, the numbers of small bricks, the number of big bricks and the goal length.
   The function should return True if it is possible to make the goal long row by choosing from the given bricks.
    This can be done without any loops so don´t use any loops.


def brickmaker(small,large,goal):
    if goal > large*5:
        leftovers= goal - large*5
        if leftovers > small:
            return False
        elif leftovers <= small:
            return True
    if goal<large*5 and 



    def check_bricks(num_small,num_big,goal):
    big=5
    if goal>=big*num_big:
        afgangur=goal-big*num_big
    else:
        temp=goal//5
        afgangur=goal-temp


    if num_small>=afgangur:
        svar=True
    else:
        svar=False
    return svar
        