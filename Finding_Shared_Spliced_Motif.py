from Bio import SeqIO
import numpy as np

handle = open('Rosalind 2.txt')

sequences = [i.seq for i in SeqIO.parse(handle,'fasta')]

seq1 = sequences[0]
seq2 = sequences[1]

def LongestIncreasingSubsequence(seq1,seq2):
	length1 = len(seq1)
	length2 = len(seq2)
	result_matrix = np.zeros((length1 + 1,length2 + 1))
	results = []

	for i,j in enumerate(seq1):
		for m,n in enumerate(seq2):
			if j == n:
				result_matrix[i+1][m+1] = result_matrix[i][m] + 1
			else:
				result_matrix[i+1][m+1] = max(result_matrix[i+1][m], result_matrix[i][m+1])

	x, y = len(seq1), len(seq2)
	while x != 0 and y != 0:
		if result_matrix[x][y] == result_matrix[x-1][y]:
			x -= 1
		elif result_matrix[x][y] == result_matrix[x][y-1]:
			y -= 1
		else:
			assert seq1[x-1] == seq2[y-1]
			results.insert(0,seq1[x-1])
			x -= 1
			y -= 1
	return results



print ''.join(LongestIncreasingSubsequence(seq1,seq2))
