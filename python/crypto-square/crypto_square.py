from math import sqrt, ceil

def encode(plain_text):
    # plain_text = plain_text.strip().lower().punctuation()
    # # print(len(plain_text))
    # print(plain_text)
    # return plain_text
    
    if not plain_text:
        return ''

    # Checks for alaphanumeric chars then lowers it
    filtered = ''.join(filter(str.isalnum,  plain_text.lower()))
    # things = filtered.replace(""," ")[1:-1]


    # if len(filtered) < 2:
    #     return filtered

    # Returns the square root of the length of the filtered plain_text
    crypt = ceil(sqrt(len(filtered)))
    print(crypt, filtered)

    return ' '.join([filtered[x::crypt] for x in range(crypt)])