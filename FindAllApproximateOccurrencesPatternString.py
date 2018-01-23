fh = open('Rosalind.txt').read().split()

pattern,seq,mismatches = fh[0],fh[1],int(fh[2])

length_pattern = len(pattern)

for i in range(len(seq)-length_pattern+1):
	count = 0
	candidate = seq[i:i+length_pattern]
	for j in range(length_pattern):
		if candidate[j] != pattern[j]:
			count += 1
	if count <= mismatches:
		print i,