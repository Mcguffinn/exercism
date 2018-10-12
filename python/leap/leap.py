def is_leap_year(year):
    # year = [1996, 2000, 2015, 2100]
    # # print(year)
    # for leap in year:
    #     if leap % 4 == 0: 
    #         return leap,True
    #     elif leap % 4 != 0:
    #         return leap,False
    #     elif leap % 100 != 0:
    #         return leap,False
    #     elif leap % 100 == 0 and leap % 400 != 0:
    #         leap = False
    #     elif leap % 400 == 0:
    #         leap = False
    #     else: 
    #         pass
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    else:
        return False
    # if year % 4 != 0:
    #     return False