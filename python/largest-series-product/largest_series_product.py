from functools import reduce
def largest_product(series, size):
    if size < 0:
        raise ValueError('size must be positive')
    if size > len(series):
        raise ValueError('size must be less than series length')
    if series.islower():
        raise ValueError('series cant contain letters')

    final_product = 1


    for idx, ch in enumerate(list(series)):        
        test = series[idx: idx + size]
        
        test_product = 1

        # print(list(test))
        for numbers in list(test):
            test_product *= int(numbers) 
        print(idx,size,"**************************",test,test_product)

        if idx == 0 or test_product > final_product:
            final_product = test_product
        
        if (idx + size ) == len(series):
            break

    return final_product




