from difflib import get_close_matches
import json

# Open json file
data = json.load(open("data.json"))


# return data
# print(data['rain'])

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        match = get_close_matches(w, data.keys())[0]
        yn = input("Did you mean %s instead? Enter Y if Yes or N if No: " % match)
        if yn == "Y":
            return data[match]
        elif yn == "N":
            return "Please check your spelling and try again"
        else:
            return "We did not understand your input"
    else:
        return "Word does not exist"


word = input("Enter the word that you are looking for: ")


output = (translate(word))
if type(output) == list:
    for w in output:
        print(w)
else:
    print(output)
