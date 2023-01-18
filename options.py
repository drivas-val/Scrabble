#words_alpha.txt https://github.com/dwyl/english-words/blob/master/words_alpha.txt

import os
import helper

currFile = "words_alpha.txt" #change to any text file (use dict.txt if dictionary.py was run and finished)

#show current working menu options
def showMenu():
    print("Please Select an Option...")
    print("[1] - Unscrabbler")
    print("[2] - Check Dictionary")
    print("[3] - Words Containing... ")
    print("[4] - Clear")
    print("[5] - Exit")

#unscrabble any word with options
def unscrabbler():
    directionUnscrambler = {
        "1" : helper.unscrabbler1,
        "2" : helper.unscrabbler2,
        "3" : helper.unscrabbler3,
    }
    print("Please Select an Option...")
    print("[1] - About")
    print("[2] - Filter")
    print("[3] - Run")
    print("[4] - Menu")
    usrIn = input(">> ")
    if usrIn == "4":
        None
    else:
        action = directionUnscrambler.get(usrIn)
        action()
        unscrabbler()

#check if word exsists
def checkDict():
    directionCheckDict = {
        "1" : helper.checkDict1,
        "2" : helper.checkDict2,
    }
    print("Please Select an Option...")
    print("[1] - About")
    print("[2] - Run")
    print("[3] - Menu")
    usrIn = input(">> ")
    if usrIn == "3":
        None
    else:
        action = directionCheckDict.get(usrIn)
        action()
        checkDict()

#words containing...
def wordsCont():
    directionWordsCont = {
        "1" : helper.wordsCont1,
        "2" : helper.wordsCont2,
        "3" : helper.wordsCont3
    }
    print("Please Select an Option...")
    print("[1] - About")
    print("[2] - Filter")
    print("[3] - Run")
    print("[4] - Menu")
    usrIn = input(">> ")
    if usrIn == "4":
        None
    else:
        action = directionWordsCont.get(usrIn)
        action()
        wordsCont()
    

                    