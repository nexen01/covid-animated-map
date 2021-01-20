import datetime
import random

dt = datetime.datetime.now()
#timestamp_name = dt.strftime("%X") + "." + (dt.strftime("%f"))
timestamp_name = dt.strftime("%H") + "-" + dt.strftime("%M") + "-" + dt.strftime("%S")


#print(my_file)
timestamp_name += ".svg"
# print(timestamp_name)
# copied_file = open("copy.txt", "x")
# copied_file.write("First Line\n")
#s = "copy2.svg"
my_file = open("originalCountyMap.svg", "r" )
new_file = open(str(timestamp_name), "x")
#s = my_file.read()
pretendMaxInt = 10000
pretendInputInt = random.randint(1, pretendMaxInt)
inttest = int(256 * (pretendInputInt / pretendMaxInt))
#convert dec to hex
secondDigit = inttest % 16
firstDigit = int(inttest / 16)

#Converts number less than 16 to a hex digit
def verifyDigit(verifyMe):
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

firstDigit = verifyDigit(firstDigit)
secondDigit = verifyDigit(secondDigit)

myColor = str(firstDigit) + str(secondDigit) + "0000"

print(str(inttest) + " " + str(firstDigit) + " " + str(secondDigit))

maxInt = 100
for x in my_file:
    #Deciding the color
    newInt = random.randint(1, maxInt)
    useThis = int(256 * (newInt / maxInt))
    secondDigit = verifyDigit(useThis % 16)
    firstDigit = verifyDigit(int(useThis / 16))
    useThisColor = "00" + str(firstDigit) + str(secondDigit) + "00"
    #print(useThisColor)

    #Actually writing stuff
    if 'id="FIPS' in x:
        #print("=========we found one!!!!!")
        place = x.find("id=")
        FIPS_end = x.find('" d=')
        print(x[place+9:FIPS_end])
        #print(x[0:place] + 'fill="#FF00FF" ' + x[place:])
        new_file.write(x[0:place] + 'fill="#' + useThisColor + '" ' + x[place:])
    else:
        new_file.write(x)

#print(s)

my_file.close()
new_file.close()
# copied_file.close()
