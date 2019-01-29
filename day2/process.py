import sys
from functools import reduce

def calculate_checksum():
    '''
    >>> acumulator = {
    ...     2: 0,
    ...     3: 0
    ... }
    >>> box_ids = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
    >>> for box_id in box_ids:
    ...     result_set = list(acumulator.keys())
    ...     for letter in set(box_id):
    ...         counter = len([l for l in box_id if l == letter])
    ...         if counter in result_set:
    ...             acumulator[counter] += 1
    ...             result_set.remove(counter)
    >>> reduce(lambda x,y : x*y, acumulator.values())
    12
    '''
    input_file = open('input.txt', 'r')
    box_ids = input_file.readlines()
    input_file.close()

    acumulator = {
        2: 0,
        3: 0
    }

    for box_id in box_ids:
        result_set = list(acumulator.keys())
        for letter in set(box_id):
            counter = len([l for l in box_id if l == letter])
            if counter in result_set:
                acumulator[counter] += 1
                result_set.remove(counter)

    checksum  = reduce(lambda x,y : x*y, acumulator.values())
    print(f'checksum is {checksum}')

if __name__ == "__main__":
    if len(sys.argv) > 3 and sys.argv[2] == 'doctest':
        import doctest
        doctest.testmod()
        
    else:
        calculate_checksum()