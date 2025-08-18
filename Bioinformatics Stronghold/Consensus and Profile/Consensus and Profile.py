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


def get_consensus(dna_sequences):
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

    for i in range(length):
        max_count = 0
        max_nucleotide = "A"
        for nucleotide in ['A','C','G','T']:
            if profile_matrix[nucleotide][i] > max_count:
                max_count = profile_matrix[nucleotide][i]
                max_nucleotide = nucleotide
        consensus.append(max_nucleotide)
    return ''.join(consensus), profile_matrix
    
def main():
    import sys
    if len(sys.argv) !=2:
        print("Usage: python script.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    fasta_dict = read_FASTA(fasta_file)
    dna_sequences = list(fasta_dict.values())

    consensus = get_consensus(dna_sequences)
    consensus, profile_matrix = get_consensus(dna_sequences)
    print(consensus)
    for nucleotide in ['A','C','G','T']:
        print(f"{nucleotide}: {' '.join(map(str, profile_matrix[nucleotide]))}")

if __name__ == "__main__":
    main()