dna  = open('Rosalind.txt').read()

complements = {'A':'T','T':'A','C':'G','G':'C'}

compDNA = ''

for i in dna:
	compDNA = complements.get(i,'') + compDNA

print compDNA