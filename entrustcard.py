import os

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
        print(strin + " is wrong coordinates")
    else:
        i = 0
        strout = ''
        while i<len(strin):
            if not ('a' <= strin[i].lower() <= 'j') or not ('1' <= strin[i+1] <= '5'):
                print(strin[i] + strin[i+1] + " is wrong coordinates")
            else:
                column = ord(strin[i].lower()) - ord('a')
                row = int(strin[i+1]) - 1
                strout = strout + file_data[row][column]

            i = i+2

        if len(strin) == len(strout)*2:
            print("Code decrypted: " + strout)
