# Lesson 19 - operation with file
from statistics import mode

inputfile = 'names.txt'
outputfile = '../result.txt'

myfile = open(inputfile, mode='r')
out_myfile = open(outputfile, mode='w')

for enum, line in enumerate(myfile, 1):
    if "am" in line:
        print("Line № " + str(enum) + " " + line)
        out_myfile.write("Line № " + str(enum) + " " + line)

