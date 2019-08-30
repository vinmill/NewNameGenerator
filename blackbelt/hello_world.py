import csv
import random as r
# lowercase strings(names) before working with them
# create function that will return a random male or female name'

#Create a class and allow it to take 1 argument
class Randy(object):
    def __init__(self, gender = 1):
        object.__init__(self)
        self.setCol(gender)

    # Create a method that can set a column index based on user input.
    def setCol(self, gender):
        try:
            gender = int(gender)
            if gender == 1:
                self.__gender = 1
            elif gender == 2:
                self.__gender = 3
            elif gender == 3:
                self.__gender = 5
            # For int variables that are not in the accepted set go ahead and set to 5.
            else:
                print("invalid input")
                self.__gender = 5
        # If the variable cannot be turned into an int set as 5
        except:
            print("invalid input")
            self.__gender = 5
    
    # Create a method that gets the column index
    def getCol(self):
        return self.__gender
    # Create a property that gets and sets the gender index
    gender = property(fget = getCol, fset = setCol)

    #Create a method that sets a random name
    def setRandomName(self):
        # Assign a random int based on the number of lines in the data file.
        randomint = r.randint(1, 200)
        # Set the column location based on user input.
        col =  self.getCol()
        # Open data file and read
        with open('names.txt') as nmz:
            nameFile = csv.reader(nmz, delimiter=',')
            count = 1 
            # Iterate on the data file line by line to find the row corresponding to the random integer you have assigned.
            for row in nameFile:
                # When the correct row is located, find the corresponding name value.
                if count == randomint:
                    self.__randomName = row[col]
                    count +=1
                else:
                    count +=1

        return self.__randomName

    #Create a method that gets the random name
    def getRandomName(self):
        return self.setRandomName()

    #Create a method that gets the first three letters of the first name
    def getFirstLetters(self):
        name = self.getRandomName()
        print(name)
        self.__firstLetters = name[0:3]
        return self.__firstLetters

    #Create a method that gets a combined name from two random names
    def getName(self):
        firstLetters = self.getFirstLetters()
        #Create a variable that represents the last letter of the start of the name
        endLetter = firstLetters[2:3]
        x = True
        # Create a loop that will randomize the second name until conditions are met.
        while x:
            #Assign a random name
            secName = self.getRandomName()
            count = 0
            #If the first three letters of both names match try again, else continue.
            if firstLetters == secName[0:3]:
                continue
            else:
                #Iterate through each letter in the second name to find a match to the last letter in the start of the name
                for i in secName:
                    #Skip the header row
                    if count == 0:
                        count +=1
                    #if a match is found terminate the loop
                    elif secName[count] == endLetter:
                        #Make sure that the ending string is a certain length
                        if len(secName[count+1:len(secName)]) >= 3:
                            #Create the ending string with characters after the matching letter of the second name.
                            nameEnding = secName[count+1:len(secName)]
                            print("+\n" + secName + "\n=")
                            x = False
                            break
                        else:
                            count +=1
                    else:
                        count +=1
        #Combine the two sub-names to create a new name
        self.__fancyName = firstLetters + nameEnding
        return self.__fancyName

#Run the main program by instanitating an instance of the class and running thhat instance.
def main():
    print("""
    Have you ever wondered how writers come up with the unique
    names in their novels, need to name a baby but just don't 
    have enough time, is the name Lucky just not zesty enough
    for your new fur friend? Well look no further. This program
    randomly combines two names to create a new name. These names
    are selected from a list of the top 200 male and female names
    between the years 2010-2018 along with 200 additional medieval 
    names. You could modify this list and create a completely new 
    name set. Maybe a roman empire set or something like that. 
    Anyways. Have fun. \n""")
    a = True
    while a == True:
        gnd = input("""
        Please pick 1 or 2:
        1. Two male names
        2. Two female names
        3. Two Medieval names (both genders)\n""")
        x = Randy()
        x.gender = gnd
        print(x.getName())

if __name__ == "__main__":
    main()