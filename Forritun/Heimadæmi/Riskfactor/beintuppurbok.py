def create_milage_list(epa_file):
    milage_list=[]
    for line in epa_file:
        if line[0:5]='CLASS'
            continue
        line_list=line.split(',')
        car_tuple=(int(line_list[9],line_list[1],line_list[2]))
        milage_list.append(car_tuple)
    return milage_list

def find_max_min_milage(milage_list, max_milage, min_milage):
    max_milage_list=[]
    min_milage_list=[]

    for car_tuple in milage_list:
        if car_tuple[0] == max_milage:
            max_milage_list.append(car_tuple)
        if car_tuple[0] == min_milage:
            min_milage_list.append(car_tuple)

    return max_milage_list, min_milage_list

epa_file=open("epaData.csv","r")
print("EPA CAR MILAGE")
print()

milage_list=create_milage_list(epa_file)
max_milage=max(milage_list)[0]
min_milage=min(milage_list)[0]
print("Max and Min milage: ", max_milage, min_milage)
print()

max_milage_list,min_milage_list= find_max_min_milage(milage_list, max_milage,min_milage)

print("Maximum milage cars: ")
for car_tuple in max_milage_list:
    print(" ", car_tuple[1],car_tuple[2])
print("Minimum Milage cars: ")
for car_tuple in min_milage_list:
    print(" ",car_tuple[1],car_tuple[2])