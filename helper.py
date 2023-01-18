import os

currFile = "words_alpha.txt" #change to any text file (use dict.txt if dictionary.py was run and finished)
unscrabblerMode = 1
wordsContMode = 1

#about
def unscrabbler1():
    print("Unscrabbler allows you to input a group of letters and find words in the dictionary containing those letters")


#filter
def unscrabbler2():
    global unscrabblerMode
    print("Please select an option...")
    print("[1] - Anagram Mode (word is only as long as the input)")
    print("[2] - Diverse Mode (word can be longer then the input)")
    usrIn = input(">> ")
    if usrIn == "1":
        unscrabblerMode = 1
    elif usrIn == "2":
        unscrabblerMode = 2
    else:
        print("Not a valid input try again!")
        unscrabbler2()

#run
def unscrabbler3():
    print("Type in letters or 1 to exit...")
    usrIn = input(">> ")
    if usrIn == "1":
        None
    else:
        if unscrabblerMode == 2:
            currList = []
            with open(currFile) as f:
                for line in f:
                    usrInCpy = str(usrIn)
                    dicLine = line.rstrip()
                    for letter in dicLine:
                        #check if it is empty
                        if letter in usrInCpy:
                            usrInCpy = usrInCpy.replace(letter, "")
                        if len(usrInCpy) == 0:
                            currList.append(line)
            currList.sort(key=len)
            print(currList)
            unscrabbler3()
        elif unscrabblerMode == 1:
            with open(currFile) as f:
                for line in f:
                    if sorted(line.rstrip()) == sorted(usrIn):
                        print(line.rstrip())
            unscrabbler3()
#about
def checkDict1():
    print("Check Dictionary allows you to check if a word exsits in the english language or not.")

#run
def checkDict2():
    checkBool = False
    print("Type in a word or 1 to exit...")
    usrIn = input(">> ")
    if usrIn == "1":
        None
    else:
        with open(currFile) as f:
            for line in f:
                if usrIn == line.rstrip():
                    checkBool = True
        if checkBool == True:
            print(str(usrIn) + " is a word!")
            checkDict2()
        else:
            print(str(usrIn) + " is NOT a word!")
            checkDict2()
                            



#about
def wordsCont1():
    print("Retrives any word containing the input string.")

#filter
def wordsCont2():
    global wordsContMode
    print("Please select an option...")
    print("[1] - String anywhere in the word")
    print("[2] - String at the beginning of a word")
    print("[3] - String at the end of the word")
    usrIn = input(">> ")
    if usrIn == "1":
        wordsContMode = 1
    elif usrIn == "2":
        wordsContMode = 2
    elif usrIn == "3":
        wordsContMode = 3
    else:
        print("Not a valid input try again!")
        wordsCont2()

#run
def wordsCont3():
    found = 0
    print("Type in a set of letters or 1 to exit...")
    usrIn = input(">> ")
    if usrIn == "1":
        None
    else:
        if wordsContMode == 1:
            with open(currFile) as f:
                for line in f:
                    if usrIn in line.rstrip():
                        print(line)
                        found = 1
            if found == 0:
                print("No words contain " + str(usrIn) + "!")
            wordsCont3()
        elif wordsContMode == 2:
            with open(currFile) as f:
                for line in f:
                    newLine = line.rstrip()
                    if newLine[:len(usrIn)] == usrIn:
                        print(newLine)
            wordsCont3()
        elif wordsContMode == 3:
            with open(currFile) as f:
                for line in f:
                    newLine = line.rstrip()
                    if newLine[-len(usrIn):] == usrIn:
                        print(newLine)
            wordsCont3()

        

#clears terminal
def clear():
    os.system('clear')

#exit program
def end():
    quit()

