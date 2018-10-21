from math import sqrt, ceil

def encode(plain_text):
    # plain_text = plain_text.strip().lower().punctuation()
    # # print(len(plain_text))
    # print(plain_text)
    # return plain_text
    
    if not plain_text:
        return ''

    # Checks for alaphanumeric charsthen lowers it
    filtered = ''.join(filter(str.isalnum,  plain_text.lower()))

    # Returns the square root of the length of the filtered plain_text
    crypt = ceil(sqrt(len(filtered)))

    return ''.join([filtered[x::crypt] for x in range(crypt)])