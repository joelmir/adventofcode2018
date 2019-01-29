import sys
from functools import reduce
from functools import partial

def diff_shift(offsets, x, y):
    offset_change = int(x) + int(y)
    if offset_change in offsets:
        raise Exception(f'Duplication detected at frequence {offset_change}')
    else:
        offsets.append(offset_change)
    return offset_change

def calculate_frequence_shift():
    '''
    >>> shift_offset = partial(diff_shift, [0])
    >>> first_value = 0
    >>> freq_shifts_file = ["+3", "+3", "+4", "-2", "-4"]
    >>> while 1: 
    ...     freq_shifts = [str(first_value)] + freq_shifts_file
    ...     first_value = reduce(shift_offset, freq_shifts)
    Traceback (most recent call last):
    ...
    Exception: Duplication detected at frequence 10

    >>> shift_offset = partial(diff_shift, [0])
    >>> first_value = 0
    >>> freq_shifts_file = ["-6", "+3", "+8", "+5", "-6"]
    >>> while 1: 
    ...     freq_shifts = [str(first_value)] + freq_shifts_file
    ...     first_value = reduce(shift_offset, freq_shifts)
    Traceback (most recent call last):
    ...
    Exception: Duplication detected at frequence 5

    >>> shift_offset = partial(diff_shift, [0])
    >>> first_value = 0
    >>> freq_shifts_file = ["+7", "+7", "-2", "-7", "-4"]
    >>> while 1: 
    ...     freq_shifts = [str(first_value)] + freq_shifts_file
    ...     first_value = reduce(shift_offset, freq_shifts)
    Traceback (most recent call last):
    ...
    Exception: Duplication detected at frequence 14
    '''
    shift_offset = partial(diff_shift, [0])
    first_value = 0

    input_file = open('input.txt', 'r')
    freq_shifts_file = input_file.readlines()
    input_file.close()
    count = 1

    while 1:
        print(f'turn: {count}')
        freq_shifts = [str(first_value)] + freq_shifts_file
        first_value = reduce(shift_offset, freq_shifts)
        count += 1

if __name__ == "__main__":
    if len(sys.argv) > 3 and sys.argv[2] == 'doctest':
        import doctest
        doctest.testmod()
        
    else:
        print(f'The final frequence is {calculate_frequence_shift()}')