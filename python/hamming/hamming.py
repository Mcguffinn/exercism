import difflib
def distance(strand_a, strand_b):
    count = 0

    if len(strand_a) != len(strand_b):
        raise ValueError("wrong")

    for indx, x in enumerate(strand_a):
        if x not in strand_b[indx]:
            count += 1

    return count


            

    



            
        
               

