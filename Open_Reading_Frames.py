from Bio import SeqIO
from Bio.Seq import Seq

genetic_code = {"GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
"UGC":"C", "UGU":"C",
"GAC":"D", "GAU":"D",
"GAA":"E", "GAG":"E",
"UUC":"F", "UUU":"F",
"GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G",
"CAC":"H", "CAU":"H",
"AUA":"I", "AUC":"I", "AUU":"I",
"AAA":"K", "AAG":"K",
"CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L", "UUA":"L", "UUG":"L",
"AUG":"M",
"AAC":"N", "AAU":"N",
"CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P",
"CAA":"Q", "CAG":"Q",
"AGA":"R", "AGG":"R", "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R",
"AGC":"S", "AGU":"S", "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S",
"ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T",
"GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V",
"UGG":"W",
"UAC":"Y", "UAU":"Y",
"UAA":"stop","UAG":'stop',"UGA":"stop"}

def Translate(starts,sequence): ## trick here is that valid results must end with stop codon
	results = []
	temp = sequence
	for i in starts:
		protein = ''
		sequence = temp[i:]
		for j in range(0,len(sequence),3):
			if genetic_code.get(sequence[j:j+3]) == 'stop':
				protein += genetic_code.get(sequence[j:j+3])
				break
			else:
				protein += genetic_code.get(sequence[j:j+3])
		if protein.endswith('stop'):
			results.append(protein[:-4])
	return results

def RevComp(dna):
	compDNA = ''
	for i in dna:
		compDNA = {'A':'U','U':'A','C':'G','G':'C'}.get(i,'') + compDNA
	return compDNA

def StartPositions(sequence):
	start_positions = [j for j in range(len(sequence)-3) if sequence[j:j+3] == 'AUG']
	return start_positions


handle = open('Rosalind.txt')

sequence = [(str(x.seq.transcribe())) for x in SeqIO.parse(handle,'fasta')]
for i in set(Translate(StartPositions(sequence[0]),sequence[0]))|set(Translate(StartPositions(RevComp(sequence[0])),RevComp(sequence[0]))):
	print i