import json
from difflib import get_close_matches

def isValideInput(word):
    if (len(get_close_matches(word, dataSource.keys())) > 0):
        iptWord=input("Do you mean "+ get_close_matches(word, dataSource.keys())[0] +" instead? (yes/no) :")
        iptWord=iptWord.lower()
        if(iptWord == "yes"):
            return dataSource[get_close_matches(word, dataSource.keys())[0]]
        elif iptWord == "no":
            return "The word does not exist. Please double check the word."
        else:
            return "We don't understand the input."
    else:
        return "The word does not exist. Please double check the word."

def translate(word):
    if (word in dataSource.keys()):
        return dataSource[word]
    else:
        return isValideInput(word)

def loadDatasouce():
    data = json.load(open("C:/Users/91976/Documents/Python/Application1/data.json",'r'))
    return data

word = input("Enter the word: ")
word=word.lower()
dataSource=loadDatasouce()
output = translate(word)

if(type(output) == list):
    for definations in output : 
        print(definations)
else:
    print(output)