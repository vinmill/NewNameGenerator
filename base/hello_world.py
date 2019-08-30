# import csv library to read csv. import random to randomize integers
import csv
import random as r

# Instructions for the program and return the users response
def instructions():
    gnd = input("""
    We are going to select a random name from a list the \n
    top 200 male and female names between 2010-2018. \n\n
    What gender identity would you like this name to belong to? \n
    1. Male \n
    2. Female\n""")
    return gnd

# Create a function that can return a column index based on user input.
def setCol(column):
    inp = int(column)
    if inp == 1:
        col = 1
    else:
        col = 3
    return col

# Create function that will return a random male or female name from a data file based on input.
def getrandomName():
    # Assign a random int based on the number of lines in the data file.
    randomint = r.randint(1, 200)
    print(randomint)
    # Set the column location based on user input.
    col = setCol(instructions())
    # Open data file and read
    with open('names.txt') as nmz:
        nameFile = csv.reader(nmz, delimiter=',')
        count = 1 
        # Iterate on the data file line by line to find the row corresponding to the random integer you have assigned
        for row in nameFile:
            # When the correct row is located, find the corresponding name value
            if count == randomint:
                randomName = row[col]
                count +=1
            else:
                count +=1

    return randomName

#Print the random name.
print(getrandomName())