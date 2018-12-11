import os

class Card:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def printCode(self, coordinates):
        if not isValideCoordinatesLength(coordinates):
            print("Wrong coordinates length: " + coordinates)
        else:
            i = 0
            code = ''
            while i < len(coordinates):
                c = getChar(coordinate[i:i+1])
                if c:
                    code = code + c
                i = i + 2

            if len(coordinates) == len(code)*2:
                print("card n°" + name + ": " + code)

    def getChar(self, coordinate):
        if isValidColumn(coordinate[0]) and isValidRow(coordinate[1]):
            column = ord(coordinate[0].lower()) - ord('a')
            row = int(coordinate[1]) - 1
            return self.data[row][column]
        else:
            print("Wrong coordinate: " + coordinate)
            return False

    def isValideCoordinatesLength(self, coordinates):
        if len(coordinates)%2:
            return False
        else:
            return True

    def isValidColumn(self, c):
        if 'a' <= c.lower() <= 'j':
            return True
        else:
            return False

    def isValidRow(self, c):
        if '1' <= c <= '5':
            return True
        else:
            return False

if hasattr(__builtins__, 'raw_input'):
    input=raw_input

file_path = "card.txt"

# check first if file exsits
if not os.path.exists(file_path):
   print(file_path + " not found")
else:
    with open(file_path, 'r') as file:
        file_data = file.readlines()

    strin = input("Entre card coordinates: ")

    # check user input
    if len(strin)%2:
        print(strin + " are wrong coordinates")
    else:
        i = 0
        strout = ''
        while i<len(strin):
            if not ('a' <= strin[i].lower() <= 'j') or not ('1' <= strin[i+1] <= '5'):
                print(strin[i] + strin[i+1] + " are wrong coordinates")
            else:
                column = ord(strin[i].lower()) - ord('a')
                row = int(strin[i+1]) - 1
                strout = strout + file_data[row][column]

            i = i+2

        if len(strin) == len(strout)*2:
            print("Code decrypted: " + strout)
