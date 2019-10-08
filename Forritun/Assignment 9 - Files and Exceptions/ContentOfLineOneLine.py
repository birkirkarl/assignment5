data_file=open('test.txt')

for data in data_file:  
    data=data.strip()
    data=data.replace(" ","")
    print(data, end="")
