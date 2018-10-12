from itertools import combinations

def is_equilateral(sides):
    a, b, c = sides
       
    if (a + b <= c) or (a + c <= b) or (b + c <= a): 
        return False
    elif (a == b and c):
        return True
    else: 
        return False 

def is_isosceles(sides):
    a, b, c = sides

    if (a + b < c):
        return False
    if (a == b) or (a == c) or (b == c):
        return True
    else:
        return False

def is_scalene(sides):
    a, b, c = sides
    t1 = a + b > c
    t2 = b + c > a 
    t3 = a + c > b 

    if a == b or c == b or a == c:
        return False
    elif t1 and t2 and t3:
        return True  
    else:
        return False
