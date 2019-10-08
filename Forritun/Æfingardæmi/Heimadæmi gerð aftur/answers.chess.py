# The following constants indicate the position of the respective
# fields in the list stored as the value for the key in the players dictionary
RANK = 0
COUNTRY = 1
RATING = 2
BYEAR = 3
NUM_ATTRIBUTES = 4 # number of attributes 


def create_players_dict(filename):
    ''' Reads the given file and returns a dictionary in which
        the name of a chess player is the key, the value is a list: [rank, country, rating, b-year]
    '''

    def get_value_list():
        ''' Return a list of the given values '''
        a_list = [None] * NUM_ATTRIBUTES
        a_list[RANK] = int(rank)
        a_list[COUNTRY] = country
        a_list[RATING] = int(rating)
        a_list[BYEAR] = int(byear)
        return a_list

    the_dict = {}
    try:
        file = open(filename, 'r')
        for line in file:	# process each line
            rank, name, country, rating, byear = line.split(';')
            # The name is one field separated by ","
            lastname, firstname = name.split(",")
            # Strip leading spaces
            firstname = firstname.strip()
            lastname = lastname.strip()
            country = country.strip()

            key = "{} {}".format(firstname, lastname)
            value_list = get_value_list()
            the_dict[key] = value_list
        file.close
    except FileNotFoundError:
        pass
    return the_dict

def create_countries_dict(dict_players):
    ''' Uses a players dictionary to creata a countries dictionary
        in which countries are keys and tuple of player names are values
    '''
    country_dict = {}
    for a_tuple in dict_players.items():
        chess_player = a_tuple[0]
        # The data is a list
        chess_player_data = a_tuple[1]
        country = chess_player_data[COUNTRY]
        if country in country_dict:
            name_list = country_dict[country]
            name_list.append(chess_player)
        else:
            name_list = [chess_player]
            country_dict[country] = name_list
    
    return country_dict

def get_average_rating(players, dict_players):
    ''' Returns the average ratings for the given players'''
    ratings = [ dict_players[player][RATING] for player in players]
    average = sum(ratings)/len(ratings)
    return average

def print_sorted(the_dict, dict_players):
    ''' Prints information sorted on the key of the_dict '''
    sorted_dict = sorted(the_dict.items())
    for key, players in sorted_dict:
        average_rating = get_average_rating(players, dict_players)
        print("{} ({}) ({:.1f}):".format(key, len(players), average_rating))
        for player in players:
            rating = dict_players[player][RATING]
            print("{:>40}{:>10d}".format(player, rating))

def print_header(header_str):
    print(header_str)
    dashes = '-' * len(header_str)
    print(dashes)


# The main program starts here

filename = input("Enter filename: ")
dict_players = create_players_dict(filename)
dict_countries = create_countries_dict(dict_players)
print_header("Players by country:")
print_sorted(dict_countries, dict_players)