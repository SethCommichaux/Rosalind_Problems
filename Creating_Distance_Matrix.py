from Bio import SeqIO

sequences = [i.seq for i in SeqIO.parse(open('Rosalind.txt'),'fasta')]
length = len(sequences)

matrix_zeroes = [[0 for j in range(length)] for i in range(length)]

for i,z in enumerate(sequences):
	for j,y in enumerate(sequences):
		count = 0
		for k in range(len(sequences[0])):
			if z[k] != y[k]:
				count += 1
		matrix_zeroes[i][j] = float(count)/len(sequences[0])

for i in matrix_zeroes:
	print ' '.join(map(str,i))