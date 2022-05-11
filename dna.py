import sys
import csv
import functools
import re



if len(sys.argv) != 3:
    print("Error!")
    exit(1)

directory = {}
STRsInSequence = []
STRs = []
result = []


# Open a the csv file containing the directory of names and gene STR values
with open(sys.argv[1], "r") as file:

    # Use a special fundtion from import csv (reader) to create a list out of each line
    csv_file = csv.reader(file)

    # reading the first row of the .csv file into a list (row_one) of short tandem repeats (STRs) for testing
    STRs = next(csv_file)
    #print (STRs)

    # the first item in the .csv file header is just "name" which we can remove
    STRs.pop(0)
    #print (STRs).... name gets excluded in this list



    # Going through each line of the .csv file, the first item in the line with the name, followed by the number of STRs
    for line in csv_file:

        # In prep for a dictionary, the key is the first item (the name)
        key = line[0];
        #print (key)

        # Temporary list for a persons STR values
        STRsforPerson = []

        # iterating over each line in the csv
        for i in range(1, len(line)):
            STRsforPerson.append(int(line[i]))

        #print(STRsforPerson)

        # creating a dictionary for each name
        directory[key] = STRsforPerson
        #print (directory)



# Opening a single line DNA sequence .txt file
with open(sys.argv[2], "r") as sequence:

    # Reading the line into a string variable called line
    line = sequence.read()

    # Iterating through the list of testable short tandem repeats
    for i in range(len(STRs)):

        # Current STR "Unit" to be tested
        currentUnit = STRs[i]
        tempValue = 0
        finalValue = 0


        pattern = re.compile(rf'({currentUnit})+')
        matches = pattern.finditer(line)
        for match in matches:
            start = match.start()
            end = match.end()
            length = end - start
            tempValue = length / len(currentUnit)
            if tempValue > finalValue:
                finalValue = tempValue


        result.append(finalValue)
        #print(result)


for i in directory.keys():

    candidate = directory[i]

    #https://www.journaldev.com/37089/how-to-compare-two-lists-in-python
    if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q, candidate, result), True):
        print(i)
        sys.exit()
    else:
        pass

print("No match")