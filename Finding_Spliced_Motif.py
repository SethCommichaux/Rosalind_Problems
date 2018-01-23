from Bio import SeqIO

sequences = [i.seq for i in SeqIO.parse('Rosalind.txt','fasta')]

seq1 = sequences[0]
seq2 = sequences[1]

index = 0

for i,k in enumerate(seq1):
	if index >= len(seq2):
		break
	if k == seq2[index]:
		index += 1
		print i+1,