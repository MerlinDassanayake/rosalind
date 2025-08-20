"""Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format. 
Return: A consensus string and profile matrix for the collection."""
import sys


def read_fasta(file_path):
    """
    Function parses fasta file into dictionary of labels and sequences.
    
    Args:
        file_path (str): The filepath to the fasta file.
    
    Returns:
        dict: A dictionary of fasta labels and sequences.
    """
    with open(file_path, 'r', encoding="utf-8") as f:
        fasta_file = [l.strip() for l in f.readlines()]

    global fasta_dictionary
    fasta_dictionary = {}
    fasta_label = ""

    for line in fasta_file:
        if '>' in line:
            fasta_label = line
            fasta_dictionary[fasta_label] = ""
        else:
            fasta_dictionary[fasta_label] += line

    return fasta_dictionary

def get_consensus(dna_sequences):
    """
    function takes dna sequences and returns a consensus matrix
    
    Args:
        dna_sequences (list): A list of DNA sequences.
        
    Returns:
        str, dict: A string of the consensus sequence and a dictionary of the profile matrix.
    """

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
    "main function"
    if len(sys.argv) !=2:
        print("Usage: python script.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    fasta_dict = read_fasta(fasta_file)
    dna_sequences = list(fasta_dict.values())

    consensus = get_consensus(dna_sequences)
    consensus, profile_matrix = get_consensus(dna_sequences)
    print(consensus)
    for nucleotide in ['A','C','G','T']:
        print(f"{nucleotide}: {' '.join(map(str, profile_matrix[nucleotide]))}")

if __name__ == "__main__":
    main()
