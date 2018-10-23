import re
import string

def word_count(phrase):

    #create dictionary
    c = {}

    # clean sentence
    phrase = phrase.lower()
    exclude = set('.?!/!@#$%^&*:')
    spacer = set("_,")
    phrase = ''.join(ch for ch in phrase if ch not in exclude)
    phrase = ''.join([a if a not in spacer else ' ' for a in phrase])
    phrase = phrase.split()

    
    #add counter for each count of the same word
    for item in phrase:
        item = item.strip("'")

        
        # for item in c: 
        if item in c:
            c[item] += 1
        else:
            c[item] = 1
    print(c)
    # c.get(item,0) 
    # print(phrase,"xxxxxxxxxxx")
    return c
    

    


