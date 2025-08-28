"""
Given: A collection of k(k<=100) DNA strings of length at most 1kbp each in FASTA format.
Return: A longest common  substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""


def read_FASTA(filePath):
    with open(filePath, 'r') as f:
        FASTAFile = [l.strip() for l in f.readlines()]

    FASTADict = {}
    FASTALabel = ""

    for line in FASTAFile:
        if '>' in line:
            FASTALabel = line
            FASTADict[FASTALabel] = ""
        else:
            FASTADict[FASTALabel] += line

    return FASTADict


