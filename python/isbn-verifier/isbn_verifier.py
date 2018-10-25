def verify(isbn):
    isbn = isbn.split("-")
    isbn = ''.join(isbn)

    count = 0

    #check if its tthe right length
    if len(isbn) != 10:
        return False

    for a, x in enumerate(isbn):

        if x == "X" and a == 9:
            x = 10
        
        # calculate
        if x == 10 or x.isdigit():
            count += int(x) * (10 - a)
        else: 
            return False
        
    print(count)
    return count % 11 == 0

