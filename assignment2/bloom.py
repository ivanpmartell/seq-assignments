import sys

def MurmurHash64A(k,l,seed):
    m = 0xc6a4a7935bd1e995
    r = 47
    h = seed ^ (l * m)

    data = int(k.as_int())
    end = data + (l/8)
    while(data != end):
        data += 1
        kk = data
        
        kk *= m
        kk ^= kk >> r
        kk *= m
        
        h ^= kk
        h *= m
    data2 = str(data)
    match l & 7:
        case 7: 
            h ^= int(data2[6]) << 48
        case 6: 
            h ^= int(data2[5]) << 40
        case 5: 
            h ^= int(data2[4]) << 32
        case 4: 
            h ^= int(data2[3]) << 24
        case 3:
            h ^= int(data2[2]) << 16
        case 2:
            h ^= int(data2[1]) << 8
        case 1:
            h ^= int(data2[0])
        case _:
            h *= m
    h ^= h >> r
    h *= m
    h ^= h >> r
    return h

input_file = sys.argv[1]
threshold = sys.argv[2]
hashes = dict[int, int]()
for r in FASTA(input_file, fai=False):
    s = r.seq
    kmers = s.kmers[Kmer[20]](1)
    for k in kmers:
        try:
            hashes[MurmurHash64A(k, 8, 73473)] += 1
        except:
            hashes[MurmurHash64A(k, 8, 73473)] = 1

for k, v in hashes.items():
    if v > int(threshold):
        print(v)