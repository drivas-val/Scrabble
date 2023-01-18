import options
import helper

#runner func
def scrabbler():
    while True:
        directionMain = {
            "1" : options.unscrabbler,
            "2" : options.checkDict,
            "3" : options.wordsCont,
            "4" : helper.clear,
            "5" : helper.end  
        }
        options.showMenu()
        usrIn = input(">> ")
        if usrIn not in directionMain.keys():
            print("Not a valid option, try again!")
            scrabbler()
        action = directionMain.get(usrIn)
        action()

scrabbler()