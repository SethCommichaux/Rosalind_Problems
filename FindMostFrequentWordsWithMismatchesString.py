import itertools

in_file = open('Rosalind.txt').read().split()
seq = in_file[0]
kmer = int(in_file[1])
mismatches = int(in_file[2])

candidate_motifs = map(lambda x:''.join(x),itertools.product('ATCG',repeat=kmer))

results = {}
for j in candidate_motifs:
	for i in range(len(seq)-kmer +1):
		count = 0
		candidate = seq[i:i+kmer]
		for k in range(kmer):
			if candidate[k] != j[k]:
				count += 1
			if count > mismatches: break
		if count <= mismatches:
			if j in results:
				results[j] += 1
			else:
				results[j] = 1

maximum = max(results.values())
for k,v in results.items():
	if v == maximum:
		print k,

