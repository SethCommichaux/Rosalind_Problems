from Bio import SeqIO

sequences = [i.seq for i in SeqIO.parse('Rosalind.txt','fasta')]

seq1 = sequences[0]
seq2 = sequences[1]

transition_conversions1 = 'AGCT'
transition_conversions2 = 'GATC'

Transitions = 0.0
Transversions = 0.0

for i in range(len(seq1)):
	if (seq1[i] != seq2[i]) and (transition_conversions2[transition_conversions1.find(seq1[i])] == seq2[i]):
		Transitions += 1
	elif seq1[i] != seq2[i]:
		Transversions += 1

print Transitions/Transversions