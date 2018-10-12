import re

def is_pangram(sentence):
    # reg_test = r'([ _"".a-zA-Z]+)'
    # alpha = 'abcdefghijklmnopqrstuvwxyz'
    # sen = sentence.lower()

    # if sen == reg_test:
    #     if stuff in alpha:
        
    #     return True
    # else:
    #     print(sentence)
    #     return False
    
    alpha = set('abcdefghijklmnopqrstuvwxyz')
    sen = set(sentence.lower())
    if alpha.issubset(sen):        
        return True
    else: 
        return False