handle = open('Rosalind.txt').readlines()
sequence = handle[0].strip()
motif = handle[1].strip()

for i in range(len(sequence)):
	if sequence[i:i+len(motif)] == motif:
		print i+1,