f = open('Rosalind.txt')
seqs = []

for i,j in enumerate(f):
	j = j.strip()
	if i == 0:
		kmer = int(j)
	else:
		seqs.append(j)

library = {}

for x in seqs:
	for y in range(0,len(x)-kmer+1):
		library[x[y:y+kmer]] = 0

def HammingDist(A,B):
	count = 0
	for i in range(len(A)):
		if A[i] != B[i]:
			count += 1
	return count

for x in seqs:
	for k,v in library.items():
		result = []
		for y in range(0,len(x)-kmer+1):
			result.append(HammingDist(k,x[y:y+kmer]))
		library[k] += min(result)

minimum = min(library.values())

for k,v in library.items():
	if v == minimum:
		print k

