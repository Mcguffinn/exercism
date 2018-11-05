def verify(isbn):
    isbn = isbn.replace('-','')
    y = 0

    if len(isbn) <= 9 or len(isbn) > 10:
        return False
    
    for a,x in enumerate(isbn):
        
        if x == 'X' and a == 9:
            x = 10
        # print(x,type(x),x.isdigit()
        if x == 10 or x.isdigit():
            # pass
            y += int(x) * (10 - a)
            print(y)
        else:
            return False
    
    print(y)
    return y % 11 == 0