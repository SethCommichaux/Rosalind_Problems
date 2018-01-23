handle = open('Rosalind.txt').read().strip().split()

S = handle[0]
T = handle[1]

cur = [''] * (len(T) + 1) #dummy entries as per wiki
for s in S:
	last, cur = cur, [''] 
	for i, t in enumerate(T):
		cur.append(last[i] + s if s==t else max(last[i+1], cur[-1], key=len))
# print cur[-1]

superstring = ''

for i,j in enumerate(cur[-1]):
	posA = S.find(j)
	posB = T.find(j)
	superstring += S[:(posA)]
	S = S[(posA+1):]
	superstring += T[:(posB+1)]
	T = T[(posB+1):]

superstring += T+S

print superstring




# def superstring(seq1,seq2):
# 	superstring = ''
# 
# 	for i,j in enumerate(seq1):
# 		if j not in seq2[i:i + len(seq2)/2]:
# 			superstring += j
# 			continue
# 		elif len(seq2) == 0:
# 			superstring += seq1[i:]
# 			break
# 		superstring += seq2[:seq2.find(j)+1]
# 		seq2 = seq2[seq2.find(j)+1:]
# 	if seq2 >0:
# 		superstring += seq2
# 	return superstring
# 
# result1 = superstring(seq1,seq2)
# result2 = superstring(seq2,seq1)
# 
# if len(result1) > len(result2):
# 	print result2
# else:
# 	print result1










# var = True
# superstring = ''
# 
# while var == True:
# 	if (len(seq1) == 0) and (len(seq2) != 0):
# 		superstring += seq2
# 		var = False
# 		break
# 	elif (len(seq2) == 0) and (len(seq1) != 0):
# 		superstring += seq1
# 		var = False
# 		break
# 	elif (len(seq1) == 0) and (len(seq2) == 0):
# 		var = False
# 		break
# 	elif (seq2.find(seq1[0])) == (seq1.find(seq2[0])):
# 		superstring += seq1[0]
# 		seq1 = seq1[1:]
# 		seq2 = seq2[1:]
# 	elif (seq2.find(seq1[0])) > (seq1.find(seq2[0])):
# 		superstring += seq1[:seq1.find(seq2[0])+1]
# 		seq1 = seq1[seq1.find(seq2[0]):]
# 		seq2 = seq2[1:]
# 	else:
# 		superstring += seq2[:seq2.find(seq1[0])+1]
# 		seq2 = seq2[seq1.find(seq2[0]):]
# 		seq1 = seq1[1:]
# 
# print superstring