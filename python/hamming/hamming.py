import difflib
def distance(strand_a, strand_b):
    length = 0

    if len(strand_a) != len(strand_b):
        raise ValueError('thing')
    
    for i,x in enumerate(strand_a):
        print(x)
        if x != strand_b[i]:
            length += 1
    return length
    
            

    



            
        
               

