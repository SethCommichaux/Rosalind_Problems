from Bio import SeqIO

def RevComp(dna):
	complements = {'A':'T','T':'A','C':'G','G':'C'}
	compDNA = ''

	for i in dna:
		compDNA = complements.get(i,'') + compDNA
	return compDNA

sequence = [i.seq for i in SeqIO.parse('Rosalind.txt','fasta')]

for index,seq in enumerate(sequence[0]):
	for j in [4,6,8,10,12]:
		if sequence[0][index:index+j/2] == RevComp(sequence[0][(index+j/2):index+j]):
			print index+1,j