# Given k,m, and n as positive integers
# representing population with k + m + n organisms.
# k individuals are homozygous dominant for a factor.
# m are heterozygous.
# n are homozygous recessive.

# Return: the probability that two randomly selected
# mating organisms will produce an individual possessing a dominant allele
# and thus displaying dominatnt phenotype
# assume any two organisms can mate.

# Derived equation from probability tree
k=19
m=19
n=29
pop=k+m+n
probability = (4*(k*(k-1)+2*(k*m)+2*(k*n)+m*n)+(3*m*(m-1)))/(4*(pop*(pop-1)))

# Print output with given population parameters
print(probability)
