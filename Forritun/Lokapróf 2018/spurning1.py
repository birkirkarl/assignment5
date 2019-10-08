from operator import itemgetter


def fileopener():
    filename='flights.txt'
    all_data=open(filename,'r')
    return all_data


def file_workbox(all_data):
    traveler_dict={}
    for line in all_data:
        clean_line=line.strip().split(' ')
        Name=clean_line[0]
        Country=str(clean_line[1])
        if Name not in traveler_dict:
            traveler_dict[Name] = Country
        elif Name in traveler_dict and Country in traveler_dict[Name]:
            continue
        else:
            traveler_dict[Name] += ' ' +  Country
    return traveler_dict 


def dict_output(a_dict):
    right_order=sorted(a_dict)
    Most_countries=0
    for key in right_order:
        print('{}: '.format(key))
        counter=0
        for i in sorted(a_dict[key].split(' ')):
            print('\t{}'.format(i))
            counter+=1
        if counter >= Most_countries:
            Most_countries = counter
            the_best_traveler=str(key)
    print('\n\n{} has been to {} countries'.format(the_best_traveler,Most_countries))
            


def main():

    all_data=fileopener()
    traveler_dict=file_workbox(all_data)
    dict_output(traveler_dict)
    

main()