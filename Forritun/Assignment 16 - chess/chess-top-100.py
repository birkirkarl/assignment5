

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


def create_country_dict(players_dict):
    # key = country Value =[ each individual player]
        # loop thru the dict of players
        #if this is the first time we see that country
            #create a list with one value with that player
            #if list already exists +1
        country_dict = {}
        for fullname, attribute_list in players_dict.items():
            country = attribute_list[COUNTRY]
            sub_list = [fullname, attribute_list[RATING]]
            if country not in country_dict:
                country_dict[country]=[sub_list]                
            else:
                players_list = country_dict[country]
                players_list.append(sub_list)
                country_dict[country]= players_list
        return country_dict

def get_average_score(players):
    score_sum=0
    for player in players:
        score_sum+= player[1]
    return score_sum/len(players)

def print_player(player):
    print("{:>40} {:>10d}".format(player[0],player[1]))


def print_grouped_by_country(country_dict):
    for country, players in sorted(country_dict.items()):
        number_of_players = len(players)
        average_score = get_average_score(players)
        print("{} ({}) ({:.1f}):".format(country, number_of_players, average_score))
        for player in players:
            print_player(player)

def print_header(header_string):
    print(header_string)
    print("-"*len(header_string))

def main():
    
    #open csv file
    filename = input("Enter filename: ")
    players_dict = create_players_dict(filename)
    print_header("Players by country:")
    country_dict = create_country_dict(players_dict)
    print_grouped_by_country(country_dict)
    #read the file into a dictionary key= FullName value Tuple/list [RANK , COUNTRY, RATING, BIRTHYR]
    #Take the players dictionary and order by country
    #Print out the information


main()