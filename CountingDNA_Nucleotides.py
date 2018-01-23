handle = open('Rosalind.txt').read().upper()

dna_cnt = {}

for i,j in enumerate(handle):
	if j in dna_cnt:
		dna_cnt[j] += 1
	else:
		dna_cnt[j] = 1

for i in "ACGT":
	try:
		print dna_cnt[i],
	except KeyError:
		continue
