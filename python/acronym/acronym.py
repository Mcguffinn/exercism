def abbreviate(words):
    words = words.replace('-', ' ')
    words = words.split(' ')
    # print(words)
    bank = []

    for letter in words:
        letter = letter.upper()
        if len(letter) > 0:
            bank.append(letter[0])
            print(bank)
    
    return ''.join(bank)

    