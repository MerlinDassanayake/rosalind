"""
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa
Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.
"""


def expected_offspring(integer_list):
    """
    Determines the number of expected offspring in the next generation that display a dominant phenotype given each couple produces two offspring.
    """
    genotype_probability_list = [1,1,1,0.75,0.5,0]

    number_of_offspring = 0

    for num in range(len(integer_list)):
        if integer_list[num] > 0:
            temp_num = integer_list[num] * genotype_probability_list[num]
            number_of_offspring += temp_num
    return number_of_offspring * 2


def main():
    "main function"
    sample_list = [17490, 17707, 17782, 18957, 16732, 18158]
    print(expected_offspring(sample_list))


if __name__ == "__main__":
    main()
