import difflib
def distance(strand_a, strand_b):
    asshatpoints = 0
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands not the same length!')
    for i,x in enumerate(strand_a):
        if x != strand_b[i]:
            asshatpoints += 1
    return asshatpoints
        
               

