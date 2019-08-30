import csv
import random as r
# lowercase strings(names) before working with them
# create function that will return a random male or female name'

class Randy(object):
    def __init__(self, gender = 1):
        object.__init__(self)
        self.setCol(gender)

    def setCol(self, gender):
        try:
            gender = int(gender)
            if gender == 1:
                self.__gender = 1
            elif gender == 2:
                self.__gender = 3
            elif gender == 3:
                self.__gender = 5
        except:
            print("invalid input")
            self.__gender = 1
    
    def getCol(self):
        return self.__gender

    gender = property(fget = getCol, fset = setCol)

    def setRandomName(self):
        randomint = r.randint(1, 200)
        col =  self.getCol()
        with open('names.txt') as nmz:
            nameFile = csv.reader(nmz, delimiter=',')
            count = 1 
            for row in nameFile:
                if count == randomint:
                    self.__randomName = row[col]
                    count +=1
                else:
                    count +=1

        return self.__randomName

    def getRandomName(self):
        return self.setRandomName()

    def getFirstThree(self):
        name = self.getRandomName()
        print(name)
        self.__firstLetters = name[0:3]
        return self.__firstLetters

    def getName(self):
        firstLetters = self.getFirstThree()
        endLetter = firstLetters[2:3]
        x = True
        while x:
            secName = self.getRandomName()
            count = 0
            if firstLetters == secName[0:3]:
                continue
            else:
                for i in secName:
                    if count == 0:
                        count +=1
                    elif secName[count] == endLetter:
                        if len(secName[count+1:len(secName)]) >= 3:
                            nameEnding = secName[count+1:len(secName)]
                            print("+\n" + secName + "\n=")
                            x = False
                            break
                        else:
                            count +=1
                    else:
                        count +=1

        self.__fancyName = firstLetters + nameEnding
        return self.__fancyName



            # print(f'Processed {line_count} lines.')

def main():
    gnd = input("""
    Have you ever wondered how writers come up with the unique
    names in their novels, need to name a baby but just don't 
    have enough time, is the name Lucky just not zesty enough
    for your new fur friend? Well look no further. This program
    randomly combines two names to create a new name. These names
    are selected from a list of the top 200 male and female names
    between the years 2010-2018. You could modify this list and 
    create a completely new name set. Maybe a roman empire set or 
    something like that. Anyway. Have fun. \n
    Please pick 1 or 2:
    1. Two male names
    2. Two female names
    3. Two Medieval names (both genders)\n""")
    x = Randy()
    x.gender = gnd
    print(x.getName())

if __name__ == "__main__":
    main()

# print description
# ask for user input (male or female) and set as variable
# based on the users response select a random row in specified column

# create another function that will generate a random name by combining two names
# ask the user if they would like to combine 2 males names, 2 female names, 1 male 1 female
# randomize the first name grab the first 2 letters of the string set as a variable
# grab the second letter of the variable (1stname[1]) and set as a search variable
# randomize anther name set as a variable
# for i in 2ndname while 2ndname[i] != 1stname[i] if letter equals second letter grab the index else continue
# if letter matches the 2nd letter of the 1stname continue if not randomize another name
# set matching letter +1 to the end of the 2nd string as a varible
# concat first 2 letters of the first string with the remaining letters of the second string
# this is your new name
# ask to go again
