def verify(isbn):
    logic = isbn.split("-")
    new_isbn = "".join(logic)
    y = 0
    
    if len(new_isbn) != 10:
        return False 
    for i,x in enumerate(new_isbn):
        if x is 'X' and i == 9:
            x = 10
        if x == 10 or x.isdigit():
            y += int(x) * (10-i)
        else:
            return False
        
    return y % 11 == 0
