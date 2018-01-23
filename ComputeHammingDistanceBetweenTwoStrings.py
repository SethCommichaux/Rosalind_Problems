fh = open('Rosalind.txt').read().split()
seq1,seq2,count = fh[0],fh[1],0

for i in range(len(seq1)):
	if seq1[i] != seq2[i]:
		count += 1

print count