fh = open('Rosalind.txt').read().split()
seq,pattern,count = fh[0],fh[1],0

for i in range(len(seq)):
	if seq[i:i+len(pattern)] == pattern:
		count += 1

print count