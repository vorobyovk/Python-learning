# Lesson 19 - operation with file
from statistics import mode

inputfile = '../all_pass.txt'
outputfile = '../result.txt'

myfile = open(inputfile, mode='r', encoding='latin_1')
out_myfile = open(outputfile, mode='w')

for enum, line in enumerate(myfile, 1):
    if "kirill" in line:
        print("Line № " + str(enum) + " " + line)
        out_myfile.write("Line № " + str(enum) + " " + line)
    if "Kirill" in line:
        print("Line № " + str(enum) + " " + line)
        out_myfile.write("Line № " + str(enum) + " " + line)

