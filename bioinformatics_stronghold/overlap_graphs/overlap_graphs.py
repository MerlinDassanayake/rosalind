"""
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjecency list corresponding to O3. You may return edges in any order.
"""


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

    fasta_dictionary = {}
    fasta_label = ""

    for line in fasta_file:
        if '>' in line:
            fasta_label = line
            fasta_dictionary[fasta_label] = ""
        else:
            fasta_dictionary[fasta_label] += line

    return fasta_dictionary


def adjecency_list(fasta_dict):
    """
    A function that returns an adjacency list corresponding to O3.

    Args:
        fasta_dict (dict): A dictionary created by parsing a fasta file.

    Returns:
        ***
    """


def main():
    'Main function'
    print(read_fasta("rosalind.fa"))

if __name__ == "__main__":
    main()
