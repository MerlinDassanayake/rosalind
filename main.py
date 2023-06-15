# DNA Toolset/Code testing file
from DNAToolkit import *
from utilities import colored
import random

rndDNAStr = ''.join([random.choice(Nucleotides)
                     for nuc in range(50)])

DNAStr = validateSeq(rndDNAStr)

print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')

print(f"[4] + DNA String + Reverse Complement:\n5' {colored(DNAStr)} 3' ")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr)[::-1])} 5'\n")

print(f'[5] + GC Content: {gc_content(DNAStr)}%\n')
print(
    f'[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')
print(
    f'[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr, 0)}\n')
print(
    f'[8] + Codon frequency (L): {codon_usage(DNAStr, "L")}\n')