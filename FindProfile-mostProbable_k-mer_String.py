f = open('Rosalind.txt')

def ProfileProb(x):
	count = 1
	for i,h in enumerate(x):
		if h == 'A':
			count *= a[i]
		elif h == 'C':
			count *= c[i]
		elif h == 'G':
			count *= g[i]
		else:
			count *= t[i]
	return count

for i,j in enumerate(f):
	j = j.strip().split()
	if i == 0:
		dna = ''.join(j)
	elif i == 1:
		kmer = int(''.join(j))
	elif i == 2:
		a = [float(k.strip()) for k in j]
	elif i == 3:
		c = [float(k.strip()) for k in j]
	elif i == 4:
		g = [float(k.strip()) for k in j]
	elif i == 5:
		t = [float(k.strip()) for k in j]

result = {}

for n in range(0,len(dna)-kmer +1):
	result[dna[n:n+kmer]] = ProfileProb(dna[n:n+kmer])

print max(result.items(),key=(lambda x:x[1]))