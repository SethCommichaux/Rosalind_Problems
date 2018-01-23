import itertools

in_file = open('Rosalind.txt').read().split()
sequence = in_file[0]
length = len(sequence)
kmer = int(in_file[1])
mismatches = int(in_file[2])
revcomp = (''.join([{'A':'T','T':'A','C':'G','G':'C'}.get(x) for x in sequence]))[::-1]
candidate_motifs = map(lambda x:''.join(x),itertools.product('ATCG',repeat=kmer))
results = {}

def FreqWordsWithMismatches(seq):
	for j in candidate_motifs:
		for i in range(length-kmer +1):
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

FreqWordsWithMismatches(sequence)
FreqWordsWithMismatches(revcomp)

maximum = max(results.values())

for k,v in results.items():
	if v == maximum:
		print k,
