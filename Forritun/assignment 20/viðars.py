def getinfo():
    name=input('Enter Name: ')
    year=input('Enter Year: ')
    rating=input('Enter Rating: ')
    return (name, year, rating)

        
def main():
    
    number_of_players = int(input("Number of players: "))
    players = []
    mydict={}

    print("--- Reading players ---")
    for i in range(0,number_of_players):
        name,year,rating=getinfo()
        print()
        players.append(name)
        info=(int(year),int(rating))
        mydict[name]=info
    
    print("--- Displaying players --- ")
    for player in players:
        print('Name: {}\nYear: {}\nRating: {}'.format(player,mydict[player][0],mydict[player][1]))
        print()
    

    #highest_rated_player = get_highest_rated_player(players)
    highest_rating=0
    for player in players:
        if mydict[player][1]>highest_rating:
            highest_rated_player=player
            highest_rating=mydict[player][1]
    print("Highest rated player: ")
    print('Name: {}\nYear: {}\nRating: {}'.format(highest_rated_player,mydict[highest_rated_player][0],mydict[highest_rated_player][1]))

    #average_rating = get_average_rating(players)
    sum_of_rating=0
    for player in players:
        sum_of_rating+=mydict[player][1]
    average_rating=sum_of_rating/len(players)
    print("Average rating: {:.2f}".format(average_rating))

main()