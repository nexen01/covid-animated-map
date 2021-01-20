#The plan:
"""
0. Loop through all dates
1. Go through the SVG county by county
2. ID the FIPS code
    a. Locate the number of cases for that FIPS code that day
    b. Convert that number into a hex color by defining a max
        i. Make sure you know what to do if cases go over said amount
    c. Change the fill of you new file using your new hex code
3. Repeat for every hex code
"""
import datetime
import csv
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM

#Timestamp code so that I can test multiple times
dt = datetime.datetime.now()
timestamp_name = dt.strftime("%H") + "-" + dt.strftime("%M") + "-" + dt.strftime("%S")
timestamp_name += ".svg"

#A list of the FIPS codes
with open("covid_confirmed_usafacts.csv") as csvfile:
    readCSV2 = csv.reader(csvfile,delimiter=",")
    FIPS_codes = []
    for row in readCSV2:
        for ele in row:
            FIPS_codes.append(ele)
            break
    #print(FIPS_codes)
FIPS_codes.pop(0)
#print(FIPS_codes)

#A list of our dates
with open("covid_confirmed_usafacts.csv") as csvfile:
    readCSV2 = csv.reader(csvfile,delimiter=",")
    dates = []
    for row in readCSV2:
        for ele in row:
            dates.append(ele)
        break
for i in range(4):
    dates.pop(0)
print(dates)

#Converts number less than 16 to a hex digit
def hexifyDigit(verifyMe):
    if verifyMe > 9:
        if verifyMe == 10:
            return "A"
        elif verifyMe == 11:
            return "B"
        elif verifyMe == 12:
            return "C"
        elif verifyMe == 13:
            return "D"
        elif verifyMe == 14:
            return "E"
        elif verifyMe == 15:
            return "F"
        else:
            return "0"
    else:
        return verifyMe


#A bunch of variables I'll hopefully get rid of when I'm done
current_date = "6/22/20"
max_cases = 1000
folder_name = "copies"

counter = 0
yesterdays_cases = []
for current_date in dates:
    #Generate case count per day for our current day
    example_FIPS = 1005
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
                todays_cases.append(current_row[titles.index(current_date)])
                #print(current_row[titles.index(example_date)])
            #print("")
        #print(todays_cases)
        #An example of how to find FIPS cases for that day for a specific county
        print(todays_cases[FIPS_codes.index(str(example_FIPS))])

    #An example of finding new cases for a day
    if(yesterdays_cases == []):
        print(todays_cases[FIPS_codes.index(str(example_FIPS))])
    else:
        new_cases_test = int(todays_cases[FIPS_codes.index(str(example_FIPS))]) - int(yesterdays_cases[FIPS_codes.index(str(example_FIPS))])
        print(new_cases_test)

    #Go through SVG county by county
    originalCountyMap = open("originalCountyMap.svg", "r" ) #Our original file
    newMapName = folder_name + "/" + str(counter) + ".svg"
    counter+=1
    newCountyMap = open(str(newMapName), "x")
    print(yesterdays_cases)
    for x in originalCountyMap:
        if 'id="FIPS' in x:
            #Temporary variable
            #useThisColor = "0000FF"

            #Find the FIPS code
            place = x.find("id=")
            FIPS_end = x.find('" d=')
            theFIPS = x[place+9:FIPS_end]
            theFIPS = str(int(theFIPS))
            #print(theFIPS)

            #Find cases for that FIPS Code
            try:
                cases_in_current_county = int(todays_cases[FIPS_codes.index(str(theFIPS))])
            except:
                print("County not found")

            #Find new cases in that code
            if(yesterdays_cases == []):
                try:
                    new_cases_in_current_county = int(todays_cases[FIPS_codes.index(str(theFIPS))])
                except:
                    print("County not found: new cases edition")
            else:
                try:
                    new_cases_in_current_county = int(todays_cases[FIPS_codes.index(str(theFIPS))]) - int(yesterdays_cases[FIPS_codes.index(str(theFIPS))])
                    #print("made it here")
                except:
                    print("County not found: old  cases edition")

            #Convert that to a color
            if new_cases_in_current_county > max_cases:
                color_percentage = 1
            else:
                color_percentage = new_cases_in_current_county / max_cases
            color_percentage = 1 - color_percentage
            color_amount = int(255 * color_percentage)
            firstDigit = int(color_amount / 16)
            secondDigit = color_amount % 16
            firstDigit = hexifyDigit(firstDigit)
            secondDigit = hexifyDigit(secondDigit)
            use_this_color = str(firstDigit) + str(secondDigit) + str(firstDigit) + str(secondDigit) + "FF"

            #print(x[place+9:FIPS_end])
            #print(x[0:place] + 'fill="#FF00FF" ' + x[place:])

            #Color in the county
            newCountyMap.write(x[0:place] + 'fill="#' + use_this_color + '" ' + x[place:])
        else:
            newCountyMap.write(x)
    originalCountyMap.close()
    newCountyMap.close()
    yesterdays_cases = todays_cases[:]

#convert all the svg's to png's
drawing = svg2rlg("originalCountyMap.svg")
renderPDF.drawToFile(drawing, "file.pdf")
renderPM.drawToFile(drawing, "file2.png", fmt="PNG")
for i in range(0, counter):
    file_name = str(i)
    file_name_png = "copies/" + file_name + ".png"
    file_name += ".svg"
    file_name = "copies/" + file_name
    drawing = svg2rlg(file_name)
    renderPM.drawToFile(drawing, file_name_png, fmt="PNG")
