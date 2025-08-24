"""
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
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
            fasta_label = line[1:] # remove > from label
            fasta_dictionary[fasta_label] = ""
        else:
            fasta_dictionary[fasta_label] += line

    return fasta_dictionary


def adjacency_list(fasta_dict, k):
    """
    A function that returns an adjacency list corresponding to O3.

    Args:
        fasta_dict (dict): A dictionary created by parsing a fasta file.

    Returns:
        ***
    """
    overlap_list = []
    for label_a, seq_a in fasta_dict.items():
        for label_b, seq_b in fasta_dict.items():
            if label_a != label_b:
                if seq_a[-k:] == seq_b[:k]:
                    overlap_list.append((label_a, label_b))
    return overlap_list

def main():
    """Main function"""
    fasta_location = input("Please enter the name of the fasta file to parse: ")
    k_value = int(input("Please enter the value for k: "))
    sequence_dict = read_fasta(fasta_location)
    overlap_list = adjacency_list(sequence_dict, k_value)
    for v, w in overlap_list:
        print(v,w)

if __name__ == "__main__":
    main()
