## V00884733 hame
import sys

input_sequence1 = sys.argv[1]
input_sequence2 = sys.argv[2]

bit_dict = {'A': 0,
            'C': 1,
            'G': 2,
            'T': 3}

def bit_representation(sequence):
    bits = 0
    for i in range(len(sequence)):
        bits = bits << 2
        bits |= bit_dict[sequence[i]]
    return bits

bits_sequence1 = bit_representation(input_sequence1)
bits_sequence2 = bit_representation(input_sequence2)

odd_mask = 6148914691236517205
even_mask = 12297829382473034410

differences = bits_sequence1 ^ bits_sequence2
compress_even = (differences & even_mask) >> 1
compress_odd = (differences & odd_mask) | compress_even
hamming_distance = int.popcnt(compress_odd)
print(hamming_distance)