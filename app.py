import json
import difflib
from difflib import get_close_matches #TO MATCH STRINGS AND RETURNS CLOSEST MATCH

data = json.load(open("Z:\\python\\dictionary\\data.json"))
#print(data) #Prints all the data in the json file
def search_key(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) >0:
        close_match=get_close_matches(word,data.keys())[0]
        #Conforming from user
        print( "\nDid you mean: ",close_match)
        yn= input("Enter Y if yes otherwise enter N:")
        if yn == "Y" or yn=="y":
            return data[close_match]
        else:
            return ("\n!!~~Word does not exist~~!!\nCheck and Search again!\n")

    else:
        return ("\n!!~~Word does not exist~~!!\nCheck and Search again!\n")


word=input("Enter word: ")
result=search_key(word)

if type(result)== list:
    for item in result:
        print("\n>",item)
else:
    print(result)
