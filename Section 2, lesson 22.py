import sys

print(sys.argv)
print("-----------------------------------")
i = 0
for inputing in sys.argv:
    i =+ i
    print(str(inputing)[i]+"\n")