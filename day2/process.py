import sys
from functools import reduce
import itertools 

def check_diff(comb):
    diff_letter = ''
    for idx, letter in enumerate(comb[1]):
        if comb[0][idx] != letter:
            if diff_letter:
                return None
            else:
                diff_letter = letter
    if diff_letter:
        return comb[1].replace(diff_letter, '')

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

    >>> box_ids = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
    >>> combinations = itertools.combinations(box_ids, 2)
    >>> str_comb = [letters.strip() for letters in [check_diff(comb) for comb in combinations] if letters][0]
    >>> str_comb
    'fgij'
    '''
    input_file = open('input.txt', 'r')
    box_ids = input_file.readlines()
    input_file.close()

    combinations = itertools.combinations(box_ids, 2)
    str_comb = [letters.strip() for letters in [check_diff(comb) for comb in combinations] if letters ][0]
    print(f'combination is {str_comb}')

if __name__ == "__main__":
    if len(sys.argv) > 3 and sys.argv[2] == 'doctest':
        import doctest
        doctest.testmod()
        
    else:
        calculate_checksum()