import math

handle = open('Rosalind.txt').read().split()
kth_generation = int(handle[0])
num_dom_offspring = int(handle[1])

num_offspring_generation_k = 2**kth_generation

def nCr(n,r):
	f = math.factorial
	return f(n) / f(r) / f(n-r)

possible_combinations = [(i,abs(num_offspring_generation_k - i)) for i in range(num_offspring_generation_k+1)]

prob_array = []

for i in possible_combinations:
	x = nCr(num_offspring_generation_k,i[0])
	if i[0] != 0:
		x *= (0.25**i[0])
	if i[1] != 0:
		x *= (0.75**i[1])
	prob_array.append(x)

print sum(prob_array[num_dom_offspring:])