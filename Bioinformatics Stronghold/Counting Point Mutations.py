def hamming_distance(filename):
    data = open(filename, "r")
    dataset = data.read().splitlines()
    s = dataset[0]
    t = dataset[1]
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return count


filename = "/Users/merlindassanayake/Desktop/rosalind/test_data/rosalind_hamm.txt"
print(hamming_distance(filename))
