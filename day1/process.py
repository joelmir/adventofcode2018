from functools import reduce

def calculate_frequence_shift():
    with open('input.txt', 'r') as input_file:
        freq_shifts = input_file.readlines()
        return reduce(lambda x,y: int(x) + int(y), freq_shifts)

if __name__ == "__main__":
    print(f'The final frequence is {calculate_frequence_shift()}')