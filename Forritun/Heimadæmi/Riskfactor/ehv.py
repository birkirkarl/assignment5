from operator import itemgetter 

appender_csv = []

def append_csv(csv_content):
    try:
        for csv_line in csv_content[1:]:
            appender_csv.append(csv_line.split(","))
    except:
        return ""

def read_csv(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().replace("%","").split("\n")
    except:
        print("Cannot find file {}".format(filename))

#Main()
csv_content = read_csv('riskFactors.csv')

if csv_content != "":
    
    append_csv(csv_content)
    count = 1
    splitter = csv_content[0].split(",")

    print("{:<33s} {:<21s} {:6s} {:>15s}".format("Indicator", "", "Min", "Max"))
    print("---------------------------------------------------------------------------------------")

    while count < len(splitter):
       
        indicator_value = splitter[count]

        indicator_max = max(appender_csv,key=itemgetter(count))
        max_1 = str(indicator_max[count])
        state_max = indicator_max[0]
       
        indicator_min = min(appender_csv,key=itemgetter(count))
        min_1 = str(indicator_min[count])
        state_min = indicator_min[0]

        print("{:<33s}: {:<21s} {} {:6} {} {:>15s} {}".format(indicator_value, state_min, "", min_1, "", state_max, max_1))
        count += 1