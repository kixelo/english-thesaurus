import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def foo(w):
    w = w.lower()
    if w in data:
        return data[w]

    #elif w.capitalize() in data:
    #    return data[w.capitalize()]
    elif w.title() in data:
        w = w.title()
        return data[w]
        #return data[w.title()]

    elif w.upper() in data:
        w = w.upper()
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean {} instead? If yes type Y, if no type N: ".format(get_close_matches(w, data.keys())[0]))
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The world does not exist. Please double check it."
        else:
            return "I do not understand your query."

    else:
        return "The word does not exist. Please double check it."

word = input("Enter word: ")

output = foo(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
