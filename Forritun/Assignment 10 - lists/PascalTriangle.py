def make_new_row(row):
    new_row = []
    for i in range(0,len(row)+1):
        if i == 0 or i == len(row):
            new_row.append(1)
        else:
            new_row.append(row[i]+row[i-1])
    return new_row
    
    

# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
    print(new_row)