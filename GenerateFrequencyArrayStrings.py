import itertools

fh = open('Rosalind.txt').read().split()

seq,kmer = fh[0],int(fh[1])
candidate_motifs = sorted(map(lambda x:''.join(x),itertools.product('ATCG',repeat=kmer)))
results = []

for j in candidate_motifs:
	count = 0
	for i in range(len(seq)-kmer+1):
		candidate = seq[i:i+kmer]
		if j == candidate:
			count += 1
	results.append(count)
print ' '.join(map(str,results))