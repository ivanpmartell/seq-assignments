import sys

input_sequence1 = sys.argv[1]
input_sequence2 = sys.argv[2]

bit_dict = {'A': '00',
            'C': '01',
            'G': '10',
            'T': '11'}

def bit_representation(sequence):
    bits_representation_sequence = ''
    for c in sequence:
        bits_representation_sequence += bit_dict[c.upper()]
    return bits_representation_sequence

def recursive_binary(number):
        if(number == 0):
            return  ''
        else:
            return recursive_binary(number // 2) + str(number % 2)

def pretty_binary(number):
    result = recursive_binary(number)
    while (len(result) < len(input_sequence1)*2-1):
        result = '00' + result
    if (len(result) % 2 != 0):
        return '0' + result
    else:
        return result
    

bits_sequence1 = int(bit_representation(input_sequence1), 2)
bits_sequence2 = int(bit_representation(input_sequence2), 2)
print(int.popcnt(bits_sequence1))
print(pretty_binary(bits_sequence1))

int.popcnt(bits_sequence1 & bits_sequence2)