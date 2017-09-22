import json
import difflib
from difflib import SequenceMatcher as sq
from difflib import get_close_matches as gcm
data=json.load(open("data.json"))
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(gcm(word,data.keys(),cutoff=0.8))>0:
        yn= input("did you mean ' %s ' instead ? If yes then type 'y' else type 'n'  :"  %gcm(word,data.keys(),cutoff=0.8)[0])
        if yn=="y":
            return data[gcm(word,data.keys(),cutoff=0.8)[0]]
        elif yn=="n":
            if len(gcm(word,data.keys(),cutoff=0.8))>1:
                yn1= input("did you mean ' %s ' instead ? If yes then type 'y' else type 'n' :"   %gcm(word,data.keys(),cutoff=0.8)[1])
                if yn1=="y":
                    return data[gcm(word,data.keys(),cutoff=0.8)[1]]
                elif yn1=="n" :
                    return "the Word dosent exist! please recheck it !"
                else :
                    return "we did not understand your reply !"
            else :
                return "the Word dosent exist! please recheck it !"
        else :
            return "we did not understand your reply !"
    else:
        return "the Word dosent exist! please recheck it !"


word=input("enter word to be searched\n")

output = translate(word)
if type(output)== list:
    for item in output:
        print(item)
else :
    print(output)
