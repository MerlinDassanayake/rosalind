def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open (filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
    
def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round(seq.count('C')+seq.count('G')) /len(seq)*100

# === Calculate GC Content from the FASTA formatted text file:

# === Read data from the file (FASTA formatted file)
# Storing File contents in a list
FASTAFile = readFile("test_data/gc_content.txt")
#Dictionary for Labels + Data
FASTADict = {}
#String for holding the current label
FASTALabel = ""

# Converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

# === Clean/Prepare the data (Format for ease of you with our gc content function)
# === Format the data (Store the data in a convenient way)
# === Run needed operation on the data (pass the data to our gc_content functions)
# === Collect results (Rosalind Submission in our case)
