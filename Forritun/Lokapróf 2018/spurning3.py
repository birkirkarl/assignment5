import random

TEAM_SIZE = 5
GAME_LENGTH = 48
GOAL = 2
AIRBALL= 0
class Team:
    def __init__(self, name):
        self.__name = name #nafn á liði
        self.__team = []
        self.__points = 0
        for i in range(TEAM_SIZE):
            player = BasketballPlayer(i+1) # i+1 is the number for the player
            self.__team.append(player)

    def play_offence(self):
        random_index = random.randint(0, TEAM_SIZE-1)
        self.__points += self.__team[random_index].shoot_ball()
        


    def get_player_with_highest_score(self):
        highest_player = self.__team[0]
        for player in self.__team:
            if player > highest_player:
                highest_player = player
        return highest_player

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def __str__(self):
        the_str = ''
        for player in self.__team:
            the_str += str(player)
        return the_str

# Klasinn á sér tvær tilvikabreytur (attributes): number (númer leikmanns) og points (skoruð stig).
class BasketballPlayer(Team):
    def __init__(self,number):
        self.numberofplayer=number
        self.points_of_player=0

    def shoot_ball(self):
        accuracy=random.randint(0,1)
        if accuracy==1:
            self.points_of_player += GOAL
            return GOAL
        else:
            return AIRBALL
    def get_points_of_player(self):
        return int(self.points_of_player)
    def __str__(self):
        return '{},{} '.format(self.numberofplayer,self.points_of_player)
#Þetta fall velur af handahófi hvort leikmaðurinn hitti eða hitti ekki í körfuna í skottilraun (50% líkur).
#Notið random.randint() til að ákvarða hvort leikmaður hitti eða hitti ekki.
#Ef leikmaður hittir þá bætir hann við sig tveimur stigum, annars 0.  Fallið skilar viðbættum stigum.



#randint(a,b): Býr til heiltölu N af handahófi á bilinu a <= N <= b.
def print_winner(team_a, team_b):
    A=int(team_a.get_points())
    B=int(team_b.get_points())
    if A == B:
        print('Tie!')
    elif B > A:
        print('{} won!'.format(team_b.get_name()))
    else:
        print('{} won!'.format(team_a.get_name()))

def print_scores(team_a, team_b):
    A=team_a.get_name()
    B=team_b.get_name()
    print(Team(A))
    print('{} scored {} points!'.format(A,team_a.get_points()))
    print('{} scored {} points!\n'.format(B,team_b.get_points()))
    print('{} scoring:'.format(A))
    for i in Team(A).split(' '):
        i=i.split(',')
        print('Number: {} Points: {}'.format(i[0],i[1]))
    print('{} scoring:'.format(A))
    for i in Team(B).split(' '):
        i=i.split(',')
        print('Number: {} Points: {}'.format(i[0],i[1]))
    ''' You need to implent this function.  Print out:
        how many points each team scored
        the scoring of each player in each team
        the highest scoring player in each team  
    '''

def play(team_a, team_b):
    for _ in range(GAME_LENGTH):
        team_a.play_offence()    
        team_b.play_offence()
        
def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)

def main():
    # You are not allowed to change this main function
    random_seed()
    chicago_bulls = Team("Chicago Bulls")
    la_lakers = Team("LA Lakers")

    play(chicago_bulls, la_lakers)
    print_winner(chicago_bulls, la_lakers)
    print_scores(chicago_bulls, la_lakers)

main()
