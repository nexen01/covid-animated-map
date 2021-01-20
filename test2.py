import csv

example_date = "6/22/20"
example_fips = 1009

with open("covid_confirmed_usafacts.csv") as csvfile:
    readCSV2 = csv.reader(csvfile,delimiter=",")
    FIPS_codes = []
    for row in readCSV2:
        for ele in row:
            FIPS_codes.append(ele)
            break
    print(FIPS_codes)
FIPS_codes.pop(0)
print(FIPS_codes)

with open("covid_confirmed_usafacts.csv") as csvfile:
    todays_cases = []
    readCSV = csv.reader(csvfile,delimiter=",")
    titles = []
    firstLine = True
    for row in readCSV:
        current_row = []
        for ele in row:
            current_row.append(ele)
        if(firstLine):
            titles = current_row
            firstLine = False
        else:
            #print(current_row)
            #if(current_row[0]==str(example_fips)):
            todays_cases.append(current_row[titles.index(example_date)])
            #print(current_row[titles.index(example_date)])
        #print("")
    print(todays_cases)
#print(len(todays_cases))
#print(len(FIPS_codes))
print(FIPS_codes.index(str(example_fips)))
for x in FIPS_codes:
    print(todays_cases[(FIPS_codes.index(str(x)))])
#print(todays_cases[(FIPS_codes.index(str(example_fips)))])

    # if(example_date in titles):
    #     print(titles.index(example_date))

# my_csv = open("SmallCSV.csv", "r")
# print(my_csv.read())
# my_csv.close()
