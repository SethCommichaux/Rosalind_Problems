import math

handle = open('Rosalind.txt').read().strip().split()

n_things = float(handle[0])
k_subset_of_n = float(handle[1])

print (math.factorial(n_things)/math.factorial(n_things-k_subset_of_n))%1000000