#Run if you want to export a list of all words from websters online dictionary into a txt file. 
#A premade txt file is already created; however, it may be incomplete or outdated
#Webster has an API for the dictionary though I wanted to work with BeautifulSoup to extract the words. 


import string
from requests_html import HTMLSession
from bs4 import BeautifulSoup
alphabet = list(string.ascii_lowercase)
phraseList = []

#Iterate for every letter and for every page 
for letter in alphabet:
    page = 1
    while True:
        url = f'https://www.merriam-webster.com/browse/dictionary/{letter}/{page}'
        session = HTMLSession()
        response = session.get(url)
        #Raise Error
        if response.status_code != 200:
            raise TypeError("Error: Did not get status code 200")
        #Retrieve site info into data
        print(f'Parsing: {response.html.url}')
        data = BeautifulSoup(response.html.html, 'html.parser')
        #Pass individual words into phrases
        phrases = data.select('div.mw-grid-table-list span')
        #Append words accounting for duplicates and words-with-spaces
        currentFirst = [letter, letter.upper()]
        for phrase in phrases:
            if "-" in phrase.contents[0] or "/" in phrase.contents[0] or phrase.contents[0][0] not in currentFirst:
                continue
            elif " " not in phrase.contents[0] and phrase.contents[0] not in phraseList:
                phraseList.append(phrase.contents[0])
                continue
            spaceIndex = 0
            for index in range(len(phrase.contents[0])-1):
                if phrase.contents[0][index] == " ":
                    spaceIndex = index
                    break
            if phrase.contents[0][:spaceIndex] not in phraseList:
                phraseList.append(phrase.contents[0][:spaceIndex])
            else:
                continue 
        #check for last page 
        isDisabled = data.select('.next.disabled')
        if isDisabled:
            print(phraseList)
            break
        else:
            #flip page 
            page += 1

#write elements in list into txt file
with open(r'dict.txt', 'w') as filep:
    for elem in phraseList:
        filep.write("%s\n" % elem)

        

