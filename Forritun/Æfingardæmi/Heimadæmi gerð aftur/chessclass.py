
class Player(object):
    def __init__(self, name, year, rating):
        self.__name = name
        self.__year = int(year)
        self.__rating = int(rating)

    def __str__(self):
        s = "Name: {}\n".format(self.__name)
        s += "Year: {}\n".format(self.__year)
        s += "Rating: {}\n".format(self.__rating)
        return s

    def __gt__(self, other):
        return self.__rating > other.__rating

    def get_rating(self):
        return self.__rating

def read_player():
    name = input("Enter Name: ")
    year = input("Enter Year: ")
    rating = input("Enter Rating: ")
    print()
    
    return (name,year,rating)

def get_highest_rated_player(players):
    highest_rated_player = players[0]
    for player in players:
        if player.get_rating() > highest_rated_player.get_rating():
            highest_rated_player = player

    return highest_rated_player

def get_average_rating(players):
    total = 0
    for player in players:
        total += player.get_rating()
    return total / len(players)

def main():

    number_of_players = int(input("Number of players: "))
    players = []
    
    print("--- Reading players ---")
    for _ in range(number_of_players):
        name, year, rating = read_player()
        player = Player(name, year, rating)
        players.append(player)

    print("--- Displaying players ---")
    for player in players:
        print(player)

    highest_rated_player = get_highest_rated_player(players)
    print("Highest rated player: ")
    print(highest_rated_player)

    average_rating = get_average_rating(players)
    print("Average rating: {:.2f}".format(average_rating))

main()