def to_rna(dna_strand):
    dna_map = {
        'C' : 'G',
        'G' :'C',
        'T' : 'A',
        'A' : 'U',
    }

    # if dna_strand == 'C':
    #     dna_strand = 'G'
    # elif dna_strand == 'T':
    #     dna_strand = 'A'
    # elif dna_strand == 'A':
    #     dna_strand = 'T'
    # elif dna_strand == 'U':
    #     dna_strand = 'A'
    # else:
    #     dna_strand = ''

    x = ""

    for letter in dna_strand:
        y = dna_map[letter]
        x = x + y 
    return x
        
        #letter can be a key to the map
    
