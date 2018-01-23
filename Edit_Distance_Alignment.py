from Bio import SeqIO
import numpy as np

sequences = [i.seq for i in SeqIO.parse(open('Rosalind.txt'),'fasta')]

seq1 = sequences[0]
seq2 = sequences[1]
# print seq1,seq2

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
	print int(result_matrix[-1][-1])

	str1,str2 = '',''
	x,y = length2,length1
# 	print result_matrix

	while x != 0 or y != 0:
		if x == 0:
			str1 = seq1[:y] + str1
			str2 = '-'*y+str2
			y =0
		elif y == 0:
			str2 = seq2[:x] + str2
			str1 = '-'*y+str1
			y =0
		elif min(result_matrix[y-1][x], result_matrix[y][x-1], result_matrix[y-1][x-1]) == result_matrix[y-1][x-1]:
			str1 = seq1[y-1] + str1
			str2 = seq2[x-1] + str2
			x -=1
			y -=1
		elif min(result_matrix[y-1][x], result_matrix[y][x-1], result_matrix[y-1][x-1]) == result_matrix[y-1][x]:
			str1 = seq1[y-1] + str1
			str2 = '-' + str2
			y -=1
		elif min(result_matrix[y-1][x], result_matrix[y][x-1], result_matrix[y-1][x-1]) == result_matrix[y][x-1]:
			str2 = seq2[x-1] + str2
			str1 = '-' + str1
			x -=1
# 		print str1,str2,x,y
	print str1
	print str2

LongestIncreasingSubsequence(seq1,seq2)
