import sys
import math

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

def best_size(n: int, p: float):
    return int(-(n*math.log(p))/math.pow(math.log(2.0),2.0))

def best_hashing(n: int, m: int):
    return int((m/n)*math.log(2.0))

input_file = sys.argv[1]
threshold = sys.argv[2]
length = 8
n = 1999982 #estimated number of kmers
m = best_size(n, 0.1)
h = max(1,best_hashing(n, m))
bloom_filter = [0 for i in range(m)]
print("Estimated size:", m)
print("Estimated amount of hashing functions:", h)

for r in FASTA(input_file, fai=False):
    s = r.seq
    kmers = s.kmers[Kmer[20]](1)
    kmers_set = set[Kmer[20]]()
    for k in kmers:
        kmers_set.add(k)
        for i in range(h):
            index = MurmurHash64A(k, length, i) % len(bloom_filter)    
            bloom_filter[index] += 1
    for k in kmers_set:
        below_threshold = False
        counts = list[int]()
        for i in range(h):
            index = MurmurHash64A(k, length, i) % len(bloom_filter)
            current_count = bloom_filter[index]
            if current_count < int(threshold):
                below_threshold = True
                break
            else:
                counts.append(current_count)
        if below_threshold == False:
            print(max(counts), k)
        
