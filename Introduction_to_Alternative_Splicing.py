import math
handle = open('Rosalind.txt').read().strip().split()

n = int(handle[0])
m = int(handle[1])
total_combinations = 0

for i in range(m,n+1):
	total_combinations += (math.factorial(float(n)))/(math.factorial(i)*math.factorial((n-i)))
print (total_combinations) % 1000000
