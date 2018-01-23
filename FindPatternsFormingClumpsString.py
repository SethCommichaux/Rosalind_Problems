handle = open('Rosalind.txt').read().splitlines()

seq = handle[0]
kmer,frame,freq = map(int,handle[1].split(' '))
results = []

for i in range(0,len(seq)-frame + 1):
	x = seq[i:i+frame]
	candidates = {}
	for j in range(len(x)):
		if x[j:j+kmer] in candidates:
			candidates[x[j:j+kmer]] += 1
		elif x[j:j+kmer] not in candidates:
			candidates[x[j:j+kmer]] = 1
	for k,v in candidates.items():
		if v == freq:
			results.append(k)

for i in set(results):
	print i,