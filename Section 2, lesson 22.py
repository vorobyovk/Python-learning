import sys
import os

print(sys.argv)
print("-----------------------------------")
i = 0
for inputing in sys.argv:
    i =+ i
    print(str(inputing)[i]+"\n")
print("----------------------------------")

x = len(sys.argv)
for j in range(1,x,1):
    if sys.argv[j] == "h":
        print("Help option")
    elif sys.argv[j] == "c":
        print("Hello world")
    else:
        print("I don`t know to print!")


