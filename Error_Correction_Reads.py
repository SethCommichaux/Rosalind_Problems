from Bio import SeqIO

def RevComp(dna):
	complements = {'A':'T','T':'A','C':'G','G':'C'}

	compDNA = ''

	for i in dna:
		compDNA = complements.get(i,'') + compDNA

	return compDNA

sequences= [(i.seq).tostring() for i in SeqIO.parse('Rosalind.txt','fasta')]
seq_copy = sequences

positions = []

for i,j in enumerate(sequences):
	for k in range(i+1,len(sequences)):
		if (j == (sequences[k])) or (j == RevComp(sequences[k])):
			positions.append(i),positions.append(k)

errors = []
results = []

for l in range(len(sequences)):
	if l not in positions:
		errors.append(sequences[l])

for i,j in enumerate(errors):
	for k in positions:
		count = 0
		for m in range(len(j)):
			if j[m] == sequences[k][m]:
				count += 1
		if count == len(j)-1:
			results.append((j,'->',sequences[k]))

for i,j in enumerate(errors):
	j = RevComp(j)
	for k in positions:
		count = 0
		for m in range(len(j)):
			if j[m] == sequences[k][m]:
				count += 1
		if count == len(j)-1:
			results.append((RevComp(j),'->',RevComp(sequences[k])))

handle = open('results.txt','w')

for x in set(results):
	print ''.join(x)
	handle.write(''.join(x))
	handle.write('\n')















