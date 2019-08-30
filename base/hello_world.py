import csv
import random as r
# lowercase strings(names) before working with them
# create function that will return a random male or female name'
def instructions():
    gnd = input("""
    We are going to select a random name from a list the \n
    top 200 male and female names between 2010-2018. \n\n
    What gender identity would you like this name to belong to? \n
    1. Male \n
    2. Female\n""")
    return gnd

def setCol(column):
    inp = int(column)
    if inp == 1:
        col = 1
    else:
        col = 3
    return col

def getrandomName():
    randomint = r.randint(1, 200)
    print(randomint)
    col = setCol(instructions())
    with open('names.txt') as nmz:
        nameFile = csv.reader(nmz, delimiter=',')
        count = 1 
        for row in nameFile:
            if count == randomint:
                randomName = row[col]
                count +=1
            else:
                count +=1

    return randomName


        # print(f'Processed {line_count} lines.')

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
print(getrandomName())