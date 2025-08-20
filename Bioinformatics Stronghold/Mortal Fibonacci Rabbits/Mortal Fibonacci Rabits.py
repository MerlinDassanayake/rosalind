# Given: Positive integers n <= 100 and m <= 20.
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

def mortal_rabbits(n, m):
    previous1, previous2 = 1, 1
    for i in range(2, n):
        
