# lesson 20 - Exception
import sys

input_file = 'Readme1.md'


while True:
    try:
        print("Inside try")
        myfile = open(input_file, mode='r', encoding='latin_1')
    except Exception:
        print("Inside EXCEPTION")
        print("ERROR! Don`t open file")
        print(sys.exc_info()[1]) #output system message about error
        input_file = input("Plese enter a correct file name! ")
    else:
        print("Inside else")
        print(myfile.read())
        sys.exit()
    finally:
        print("inside finaly")



#    myfile.close()