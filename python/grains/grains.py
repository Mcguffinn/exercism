def on_square(integer_number):
    if integer_number == 0:
        raise ValueError('bad value')
    elif integer_number == 65:
        raise ValueError('Too high')
    else:    
        return 1 << (integer_number - 1)

def total_after(integer_number):
    if integer_number == 0:
        raise ValueError('bad value')
    elif integer_number == 65:
        raise ValueError('Too high')
    else:    
        return (1<<integer_number) - 1
