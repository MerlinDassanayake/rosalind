# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection.
# (If several possible consensus strings exist, then you may return any one of them.)

# First parse fasta file and return list of strings?

def read_FASTA(filePath):
    with open(filePath, 'r') as f:
        FASTAFile = [l.strip() for l in f.readlines()]

    global FASTADict
    FASTADict = {}
    FASTALabel = ""

    for line in FASTAFile:
        if '>' in line:
            FASTALabel = line
            FASTADict[FASTALabel] = ""
        else:
            FASTADict[FASTALabel] += line

    return FASTADict
 
read_FASTA("rosalind.fa")

for dna in FASTADict.values():
    print(dna) 

def profile_matrix(dna_sequences):
    """function takes dna sequences and returns a consensus matrix"""

    length = len(dna_sequences[0]) # takes length value from first sequence

    profile_matrix = {
        'A':[0] * length,
        'C':[0] * length,
        'T':[0] * length,
        'G':[0] * length,
    }

    for seq in dna_sequences:
        for i, nucleotide in enumerate(seq):
            profile_matrix[nucleotide][i] += 1

    consensus = []




    
