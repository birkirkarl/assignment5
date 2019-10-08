class Players(object):
    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating

    def __str__(self):
        return "Name: {} \nYear: {} \nRating: {}\n".format(self.name, self.year, self.rating)


def get_highest_rated_player(players):
    highest = 0
    for x in players:
        print(type(x[2]))
        if int(x[2]) > highest:
            highest = int(x[2])
            h = Players(x[0], x[1], x[2])
    return h


def get_average_rating(players):
    rating = 0
    for x in players:
        rating += int(x[2])
    return "{:.2f}".format(rating / len(players))


def main():
    number_of_players = int(input("Number of players: "))
    players = []

    print("--- Reading players ---")
    # here you should get info from the user about
    # number_of_players many chess player
    # code goes here....
    for x in range(number_of_players):
        name = input("Enter Name: ")
        year = input("Enter Year: ")
        rating = input("Enter Rating: ")
        print('')
        players.append([name, year, rating])

    print("--- Displaying players --- ")
    # here you should print each player
    # code goes here....
    for x in players:
        print(Players(x[0], x[1], x[2]))

    highest_rated_player = get_highest_rated_player(players)
    print("Highest rated player: ")
    print(highest_rated_player)

    average_rating = get_average_rating(players)
    print("Average rating:", average_rating)


main()