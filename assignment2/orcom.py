import sys

input_file = sys.argv[1]

def is_orcom(kmer):
    for i in range(0,len(kmer)-3):
        if(kmer[i] == kmer[i+1] == kmer[i+2]):
            return False
    return True

def minimizer[K](sequence: seq):
    assert len(sequence) >= K.len()
    kmer_min = K(s'TTTTTTTTTTTT')
    orcom_min = K(s'TTTTTTTTTTTT')
    for kmer in sequence.kmers[K](1):
        rc_kmer = ~kmer
        current_min_kmer = min(kmer, rc_kmer)
        if current_min_kmer < kmer_min: kmer_min = current_min_kmer
        if is_orcom(kmer):
            if kmer < orcom_min: orcom_min = kmer
        if is_orcom(rc_kmer):
            if rc_kmer < orcom_min: orcom_min = rc_kmer
    return kmer_min, orcom_min

for r in FASTQ(input_file):
    s = r.read
    name = r.name
    canonical_minimizer, orcom_minimizer = minimizer[Kmer[12]](s)
    if(is_orcom(orcom_minimizer)):
        print(f"{name} {canonical_minimizer} {orcom_minimizer}")
    else:
        print(f"{name} {canonical_minimizer}")
    

