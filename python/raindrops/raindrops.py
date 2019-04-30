def raindrops(number):
    pling = False
    plang = False
    plong = False

    if number % 3 == 0:
        pling = True
    if number % 5 == 0:
        plang = True
    if number % 7 == 0:
        plong = True
    if pling == plang == plong == False:
        return str(number)    

    result = str.format('{}{}{}',('','Pling')[pling],('','Plang')[plang],('','Plong')[plong])

    return result