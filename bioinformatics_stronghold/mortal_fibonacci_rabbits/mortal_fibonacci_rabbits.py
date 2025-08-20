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

    ages = [0] * m
    ages[0] = 1

    for month in range(1, n):
        newborns = sum(ages[1:]) # number of newborns is sum of reproducing rabbits
        ages = [newborns] + ages[:-1] # adds newborns to position 0 and cuts last position.
    return sum(ages)


print(mortal_rabbits(89,20))
