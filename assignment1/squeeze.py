import sys
input_file = sys.argv[1]


file_rnames = open('data/squeeze/file_readnames.txt', 'w')
file_pos =    open('data/squeeze/file_positions.txt', 'w')
file_cigars = open('data/squeeze/file_cigars.txt', 'w')
file_flags =  open('data/squeeze/file_flags.txt', 'w')
file_reads =  open('data/squeeze/file_reads.txt', 'w')
file_scores = open('data/squeeze/file_qualityscores.txt', 'w')
for r in SAM(input_file):
    """ Part 1
    print r.name
    print r.pos
    print r.cigar
    print r._htsr.flag
    print r.read
    print r.qual #Could be r.mapq """
    #Part 2
    file_rnames.write(r.name + "\n")
    file_pos.write(str(r.pos) + "\n")
    file_cigars.write(str(r.cigar) + "\n")
    file_flags.write(str(r._htsr.flag) + "\n")
    file_reads.write(str(r.read) + "\n")
    file_scores.write(r.qual + "\n")
file_rnames.close()
file_pos.close()
file_cigars.close()
file_flags.close()
file_reads.close()
file_scores.close()
