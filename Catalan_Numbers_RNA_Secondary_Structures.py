from Bio import SeqIO
from math import factorial

### a matching is noncrossing as long as there are not edges (i,j) and (k,l) such that i<k<j<l

sequence = [str(i.seq) for i in SeqIO.parse('Rosalind.txt','fasta')][0]
matchings = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}

def perfectMatchings(seq):
	noncrossing_matchings = {}

	def subinterval_noncrossings(seq):
		if len(seq) <= 2:
			return 1
		elif seq in noncrossing_matchings:
			return noncrossing_matchings[seq]
		crosses = [i for i in range(1,len(seq),2) if (seq[0] == matchings[seq[i]] and samegc_at(seq[1:i]))]
		for j in crosses:
			if seq in noncrossing_matchings:
				noncrossing_matchings[seq] += subinterval_noncrossings(seq[1:j])*subinterval_noncrossings(seq[j+1:])
			else:
				noncrossing_matchings[seq] = subinterval_noncrossings(seq[1:j])*subinterval_noncrossings(seq[j+1:])
		try:
			return noncrossing_matchings[seq]%1000000
		except KeyError:
			return 0
	return subinterval_noncrossings(seq)

def samegc_at(seq):
	nucs = [seq.count(i) for i in 'AUCG']
	return nucs[0] == nucs[1] and nucs[2] == nucs[3]

print perfectMatchings(sequence)






# x = 0
# seq = sequence[0]
# 
# for i in range(1,len(sequence),2):
# 	if matchings.get(sequence[i]) == seq:
# 		if sequence[1:i].count('G') == sequence[1:i].count('C'):
# 			if sequence[1:i].count('U') == sequence[1:i].count('A'):
# 				if sequence[i+1:].count('G') == sequence[i+1:].count('C'):
# 					if sequence[i+1:].count('U') == sequence[i+1:].count('A'):
# # 						if sequence[:i].count('U') == sequence[:i].count('A'):
# # 							if sequence[:i].count('C') == sequence[:i].count('G'):
# 						x += 1
# 								
# 
# print x%1000000



# matchings = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
# orderings = []
# count = 0
# 
# for i in range(0,len(sequence),2):
# 	for j in range(i+1,len(sequence),2):
# 		if matchings.get(sequence[i]) == sequence[j]:
# 			if sequence[i+1:j].count('G') == sequence[i+1:j].count('C'):
# 				if sequence[i+1:j].count('U') == sequence[i+1:j].count('A'):
# 					if sequence[j+1:].count('G') == sequence[j+1:].count('C'):
# 						if sequence[j+1:].count('U') == sequence[j+1:].count('A'):
# 							if sequence[:i].count('U') == sequence[:i].count('A'):
# 								if sequence[:i].count('C') == sequence[:i].count('G'):
# 									x=sequence[i+1:j].count('G')
# 									y=sequence[j+1:].count('U')
# 									x = factorial(2*x)/(factorial(x+1)*factorial(x))
# 									y = factorial(2*y)/(factorial(y+1)*factorial(y))
# 									print count
# 									print (x+y)%1000000
# 									count += (x+y)%1000000
# 									orderings.append([i,sequence[i],j,sequence[j]])
# 
# print orderings
# results = {}
# 
# for n in orderings:
# 	if n[0] in results:
# 		results[n[0]] += 1
# 	else:
# 		results[n[0]] = 1
# 
# x = max(results.values())
# 
# print (factorial(2*x)/(factorial(x+1)*factorial(x)))%1000000

# for n in range(len(orderings)):
# 	for m in range(n+1,len(orderings)):
# # 		print orderings[n][0], orderings[m]
# # 		print orderings[n][0] in orderings[m]
# # 		print orderings[n][2], orderings[m]
# # 		print orderings[n][2] in orderings[m]
# # 		print count
# 		if (orderings[n][0] in orderings[m]) or (orderings[n][2] in orderings[m]):
# 			break
# else:
# 	count += 1
# print (count + 1)%1000000
# 
# print x%1000000

# print orderings

# for i in range(len(orderings)):
# 	count = 0
# 	for j in range(i,len(orderings)):
# 		print orderings[i][0],orderings[j][0],orderings[i][2],orderings[j][2]
# 		if not (orderings[i][0] < orderings[j][0] < orderings[i][2] < orderings[j][2]) and (orderings[i][0] == orderings[j][0]):
# 			count += 1
# 	print count