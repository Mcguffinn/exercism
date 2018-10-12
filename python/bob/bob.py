def hey(phrase):
    # print("Say something to bob!")
    rep = "Whatever."
    typing = (phrase).strip()
    punctuation = list('!?.')

    if typing == '':
        rep = "Fine. Be that way!"

    elif typing.isupper() and typing.endswith("?"):
        print(typing)
        rep = "Calm down, I know what I'm doing!" 

    elif typing.isupper():
        rep = 'Whoa, chill out!'

    elif typing[-1] == punctuation[1]:
        print(typing)
        rep = 'Sure.'
   
    return rep

