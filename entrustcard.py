import os

class Card:
    def __init__(self, name, file_path):
        self.name = name
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                self.data = file.readlines()
            self.isValid = True
        else:
            print(file_path + " not found")
            self.isValid = False

    def printCode(self, coordinates):
        if not self.isValideCoordinatesLength(coordinates):
            print("Wrong coordinates length: " + coordinates)
        else:
            i = 0
            code = ''
            while i < len(coordinates):
                c = self.getChar(coordinates[i:i+2])
                if c:
                    code = code + c
                i = i + 2

            if len(coordinates) == len(code)*2:
                print("card n°" + self.name + ": " + code)

    def getChar(self, coordinate):
        if self.isValidColumn(coordinate[0]) and self.isValidRow(coordinate[1]):
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

    def isValid(self):
        return self.isValid

#############################################################

if hasattr(__builtins__, 'raw_input'):
    input=raw_input

cards = []
cards.append(Card("14268", "card14268.txt"))
cards.append(Card("14407", "card14407.txt"))

coordinates = input("Entre card coordinates: ")

for card in cards:
    card.printCode(coordinates)
