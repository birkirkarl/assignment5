
# class chess_players(object):
#     def __init__(self, Rank, Name, Country, Rating, B_year):
#         fullname=Name.replace(' ','').split(',')
#         self.rank=Rank
#         self.name=str(fullname[1])+str(fullname[0])
#         self.country=Country
#         self.rating=Rating
#         self.b_year=B_year

#     def __str__(self):
#         return '{} {} {} {} {}'.format(self.rank,self.name,self.country,self.rating,self.b_year)




# 1; Carlsen, Magnus; NOR; 2839; 1990
# 2; Caruana, Fabiano; USA; 2827; 1992
# 3; Mamedyarov, Shakhriyar; AZE; 2820; 1985
#  Rank; Name; Country; Rating; B-Year.
# #part 1

from operator import itemgetter

class chess_players(object):
    def __init__(self,Rank, Name, Country, Rating, B_year):
        fullname=Name.replace(' ','').split(',')
        self.rank=Rank
        self.name=str(fullname[1])+str(fullname[0])
        self.country=Country
        self.rating=Rating
        self.b_year=B_year
        self.country_howmany_average=[]
    def players_by_country(self):
        result = 'Players by country:\n'
        result += '-------------------\n'
        countrypop, countryrate=country_and_population()
        for i in len(countrypop):
            result += '{} ({}) ({:.1f}):\n'.format(contrypop[i], contrypop[i].get(countrypop[i]), countryrate.get(contrypop[i]))
            #result += '{:>40}{:>10d}\n'.format(playername , his rating)
        return result
    
    #def country_lenght_ave(self):
        #self.country_howmany_average.append(self.country,)
        

    def country_and_population(self):# hérna fæ ég löndin í réttri röð með fjölda
        country_population={}
        country_rating={}
        for player in chess_players():
            key=player.country
            rating=player.rating
            if key not in country_population:
                country_population[key]=1
                country_rating[key]+=int(rating)
            else:
                country_population[key]+=1 
                country_rating[key]+=int(rating)
        return sorted(country_population), sorted(contry_rating)
        










def file_reader():
    file_name=input('Input the name of the chess file: ')
    all_data=open(file_name,'r')
    for line in all_data:
        Rank, Name, Country, Rating, B_year=line.strip().split(';')
        chess_players(Rank,Name,Country,Rating,B_year)


file_reader()

