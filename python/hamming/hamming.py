import difflib
def distance(strand_a, strand_b):
    #length of the error
    length = 0

    #check if the strands lengths match
    if len(strand_a) != len(strand_b):
        raise ValueError('Strand lengths dont match')

    for pos, strand in enumerate(strand_a):

        if strand != strand_b[pos]:
            length += 1
         
    print(length)
    return length
    # check for differences

            

    



            
        
               

