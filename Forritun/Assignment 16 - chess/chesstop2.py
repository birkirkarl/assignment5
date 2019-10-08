#open csv file
#read the file into a dictionary key= FullName value Tuple/list [RANK , COUNTRY, RATING, BIRTHYR]
#Take the players dictionary and order by country
#Print out the information

RANK=0
COUNTRY=1
RATING=2
BIRTH=3


def create_attribute_list(rank,country,rating,byear):
    a_list = [int(rank), country.strip(), int(rating), int(byear)]
    return a_list



def create_players_dict(filename):
    try:
        file_stream=open(filename, "r")
        players_dict = {}
        for line in file_stream:
            rank,name,country,rating,byear = line.split(";")
            lastname, firstname= name.split(",")
            key= "{} {}".format(firstname.strip(), lastname.strip())
            attribute_list = create_attribute_list(rank,country,rating,byear)
            players_dict[key] = attribute_list
        return players_dict
    except FileNotFoundError:
        return {}


def create_attribute_dict(players_dict, attribute_key):
    # key = country Value =[ each individual player]
        # loop thru the dict of players
        #if this is the first time we see that country
            #create a list with one value with that player
            #if list already exists +1
        attribute_dict = {}
        for fullname, attribute_list in players_dict.items():
            attribute_of_player = attribute_list[attribute_key]
            if attribute_of_player not in attribute_dict:
                attribute_dict[attribute_of_player]=[fullname]                
            else:
                players_list = attribute_dict[attribute_of_player]
                players_list.append(fullname)
                
        return attribute_dict

def get_average_score(list_of_player_names,players_dict):
    score_sum=0
    for player_name in list_of_player_names:
        player_rating=get_attribute_from_dict( player_name, RATING, players_dict)
        score_sum+= players_rating
    return score_sum/len(list_of_players_names)

def get_attribute_from_dict(player_name, attributeKey, players_dict):
    return players_dict[player_name][attributeKey]

def print_player(player):
    print("{:>40} {:>10d}".format(player[0],player[1]))

def print_attribute(attribute,number_of_players,players_dict):
    print("{} ({})({:.1f}):".format(attribute,number_of_players,players_dict))


def print_grouped_by_attribute(attribute_dict,players_dict):
    for attribute, list_of_players_names in sorted(attribute_dict.items()):
        number_of_players = len(list_of_players_names)
        average_score = get_average_score(list_of_players_names,players_dict)
        print_attribute(attribute, number_of_players,average_score)
        for name in list_of_player_names:
            print_player(name,players_dict[name][RATING])

def print_header(header_string):
    print(header_string)
    print("-"*len(header_string))

def main():
    
    #open csv file
    filename = input("Enter filename: ")
    players_dict = create_players_dict(filename)
    print_header("Players by country:")
    country_dict = create_attribute_dict(players_dict,COUNTRY)
    print_grouped_by_attribute(country_dict,players_dict)
    byear_dict=create_attribute_dict(players_dict,byear)
    print_header("players by birth year")
    print_grouped_by_attribute(byear_dict,players_dict)
    #read the file into a dictionary key= FullName value Tuple/list [RANK , COUNTRY, RATING, BIRTHYR]
    #Take the players dictionary and order by country
    #Print out the information


main()