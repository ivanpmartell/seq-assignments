#!/bin/bash
cd data/squeeze/
#Uncompressed
samtools view -h ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/phase3/data/HG00275/alignment/HG00275.mapped.ILLUMINA.bwa.FIN.low_coverage.20120522.bam 22 > HG00275.mapped.ILLUMINA.bwa.FIN.low_coverage.20120522.sam
#Compressed
samtools view -o HG00275.mapped.ILLUMINA.bwa.FIN.low_coverage.20120522.bam --write-index -h ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/phase3/data/HG00275/alignment/HG00275.mapped.ILLUMINA.bwa.FIN.low_coverage.20120522.bam 22