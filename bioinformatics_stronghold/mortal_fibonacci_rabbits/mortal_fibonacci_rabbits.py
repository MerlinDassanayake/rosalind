"""Given: Positive integers n <= 100 and m <= 20.
Return: The total number of pairs of rabbits that will remain 
after the n-th month if all rabbits live for m months."""


def mortal_rabbits(n, m):
    """Function to return the total number of pairs of 
    rabbits that will remain after the n-th month if 
    all rabbits live for m months.
    
    Args:
        n (int): The n-th month we are interested in finding the number of rabbits.
        m (int): The number of months a rabbit will live for.
    
    Returns:
        int: The total number of pairs of rabbits that will remain after.
    """
    previous1, previous2 = 1, 1
    for i in range(2, n):
        current = previous1 + m * previous2
        previous2 = previous1
        previous1 = current
    return current

print(mortal_rabbits(6,3))

