
class chessplayer():
    
    def __init__(self, name='',b_year=0,chess_rating=0):
        self.name=name
        self.b_year=b_year
        self.chess_rating=chess_rating
        
    def get_highest_rated_player(players):
        
        for i in players:
            for j in chessplayer():
                if i.chess_rating >= j.chess_rating:
                    the_best=i
        return the_best

    def get_average_rating(self):
        pass

    def __str__(self):
        return 'Name: {}\nYear: {}\nRating: {}'.format(self.name, self.b_year, self.chess_rating)

###################################################################################################################################
def reader():
    name=input('Enter name: ')
    b_year=input('Enter Year: ')
    chess_rating=input('Enter Rating: ')
    return name,b_year,chess_rating




def main():

    number_of_players = int(input("Number of players: "))
    players = []
    
    print("--- Reading players ---")
    read_complete=number_of_players
    while read_complete !=0:
        name,b_year,chess_rating=reader()
        player=chessplayer(name,b_year,chess_rating)
        read_complete -= 1
        players.append(player)
    
    print("--- Displaying players --- ")
    for i in players:
        print(i)
        print()
    print(players)
    highest_rated_player = get_highest_rated_player(players)
    print("Highest rated player: ")
    print(highest_rated_player)

    #average_rating = get_average_rating(players)
    #print("Average rating:", average_rating)

main()