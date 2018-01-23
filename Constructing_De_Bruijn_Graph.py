sequences = [i.strip() for i in open('Rosalind.txt').read().split()]

def RevComp(dna):
	complements = {'A':'T','T':'A','C':'G','G':'C'}
	compDNA = ''

	for i in dna:
		compDNA = complements.get(i,'') + compDNA

	return compDNA



rev_comp_sequences = [RevComp(i) for i in sequences]

finalists = set(sequences)|set(rev_comp_sequences)

for x in sorted(finalists):
	print '('+''.join(x[0:-1])+',',''.join(x[1:])+')'