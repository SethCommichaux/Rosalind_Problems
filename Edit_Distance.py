from Bio import SeqIO
import numpy as np

sequences = [i.seq for i in SeqIO.parse(open('Rosalind.txt'),'fasta')]

seq1 = sequences[0]
seq2 = sequences[1]

def LongestIncreasingSubsequence(seq1,seq2):
	length1 = len(seq1)
	length2 = len(seq2)
	result_matrix = np.zeros((length1+1,length2+1))

	for i in range(length1+1):
		result_matrix[i][0] = i
	for i in range(length2+1):
		result_matrix[0][i] = i

	for i in range(0,length1):
		for m in range(0,length2):
			if seq1[i] == seq2[m]:
				result_matrix[i+1][m+1] = result_matrix[i][m]
			else:
				result_matrix[i+1][m+1] = min(result_matrix[i+1][m], result_matrix[i][m+1], result_matrix[i][m]) + 1
	print result_matrix
	return int(result_matrix[-1][-1])


print LongestIncreasingSubsequence(seq1,seq2)
