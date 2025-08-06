# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10kbp)
# Return: The protein string encoded by s.

# Create RNA codon/ protein amino acid dictionary
codon_table = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
               'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
               'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
               'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
               'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
               'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
               'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
               'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
               'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
               'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
               'UAA':'Stop', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
               'UAG':'Stop', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
               'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
               'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
               'UGA':'Stop', 'CGA':'R', 'AGA':'R', 'GGA':'G',
               'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}

def translate(rna_sequence, init_pos=0):
    """Function to translate input rna sequence string into protein sequence string"""
    protein_seq = '' # Initialize protein sequence string
    for pos in range(init_pos, len(rna_sequence)-2, 3):
        codon = rna_sequence[pos:pos+3]
        amino_acid = codon_table[codon]
        if amino_acid == 'Stop': # Stop translation of stop codon is encountered
            break
        protein_seq += amino_acid
    return protein_seq

# read txt file and extract rna sequence string
def read_rna_sequence(filename):
    with open(filename, 'r') as file:
        return file.read().strip().replace('\n', '')

if __name__ == "__main__":
    # read from file
    rna_sequence = read_rna_sequence('rosalind_prot.txt')

    # Return protein sequence from rna sequence read from file
    protein = translate(rna_sequence)
    
    # Print given rna sequence and output protein sequence
    print(f"RNA Sequence: {rna_sequence}")
    print(f"Protein: {translate(rna_sequence)}")
