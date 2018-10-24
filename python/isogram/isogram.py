def is_isogram(string):
    string = string.lower()
    string = string.strip()
    string = string.replace(" ", "")
    exclude = ('-')
    string = ''.join(ch for ch in string if ch not in exclude)
    d = {}

    # print(string)
    for letter in string:
        if letter in d:
            d[letter] += 1
            print(d)
        else:
            d[letter] = 1
            print(d)
    if all(x == 1 for x in d.values()):
        return True
    else:
        return False
    



