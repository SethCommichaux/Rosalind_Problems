sequences = [i.strip() for i in open('Rosalind.txt').readlines()]

results = open('Results.txt','w')
trie = {1:{}}
count = 1

for seq in sequences:
	current_node = 1
	for nuc in seq:
		if nuc not in trie[current_node].keys():
			count += 1
			trie[current_node][nuc] = count
			trie[count] = {}
		current_node = trie[current_node][nuc]

for k,v in trie.items():
	for z,w in v.items():
		results.write(str(k))
		results.write(' ')
		results.write(str(w))
		results.write(' ')
		results.write(z)
		results.write('\n')

results.close()










# main_seq = max(sequences,key=len)
# sequences.remove(main_seq)
# 
# trie = {}
# temp = 0

# for i in range(0,len(main_seq)):
# 	trie[(i+1,i+2)] = main_seq[i]
# 	temp = i+2
# 
# for seq in sequences:
# 	if seq[0] not in trie.values():
# 		trie[1,temp+1] = seq[0]
# 		temp += 1
# 		for m in range(1,len(seq)):
# 			trie[(temp,temp+1)] = seq[m]
# 			temp += 1
# 	elif seq[0] in trie.values():
# 		for k,v in trie.items():
# 			if (seq[0] == v) and (k[0] == 1):
# 				r = k[1]
# 				for j in range(1,len(seq)):
# 					if trie.get((r,r+1),'') == seq[j]:
# 						if (j+2) > temp:
# 							temp = j+2
# 						r += 1
# 						continue
# 					elif trie.get((r,r+1),'') != seq[j]:
# 						trie[(r,temp+1)] = seq[j]
# 						temp += 1
# 						for w in range(j+1,len(seq)):
# 							trie[(temp,temp+1)] = seq[w]
# 							temp += 1
# 					break
# 				break
# 		else: 
# 			trie[1,temp+1] = seq[0]
# 			temp += 1
# 			for m in range(1,len(seq)):
# 				trie[(temp,temp+1)] = seq[m]
# 				temp += 1


# 		else:
# 			temp += 1
# 			trie[1,temp+1] = seq[0]
# 			temp += 1
# 			for m in range(1,len(seq)):
# 				trie[(temp,temp+1)] = seq[m]
# 				temp += 1

# 	elif seq[0] in trie.values():
# 		for k,v in trie.items():
# 			if v == seq[0]:
# 				for j in range(1,len(seq)):
# 					if trie.get((j+1,j+2),'') == seq[j]:
# 						if (j+2) > temp:
# 							temp = j+2
# 						continue
# 			elif trie.get((j+1,j+2),'') != seq[j]:
# 				trie[(j+1,temp+1)] = seq[j]
# 				temp += 1
# 				for k in range(j+1,len(seq)):
# 					trie[(temp,temp+1)] = seq[k]
# 					temp += 1
# 				break


# for (x,y),z in sorted(trie.items(),key=lambda (k,v):k[1]):
# 	results.write(str(x))
# 	results.write(' ')
# 	results.write(str(y))
# 	results.write(' ')
# 	results.write(z)
# 	results.write('\n')
# results.close()