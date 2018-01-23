from Bio import SeqIO

def Translate(sequence):
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
	"UAC":"Y", "UAU":"Y"}

	protein = ''

	for i in range(0,len(sequence),3):
		protein += genetic_code.get(sequence[i:i+3],'')

	print protein

sequences = [i.seq for i in SeqIO.parse('Rosalind.txt','fasta')]
pre_mRNA = sequences[0]

for i in sequences[1:]:
	if pre_mRNA.find(i) != 0:
		pre_mRNA = pre_mRNA[0:pre_mRNA.find(i)] + pre_mRNA[pre_mRNA.find(i)+len(i):]
	else:
		pre_mRNA = pre_mRNA[pre_mRNA.find(i)+len(i):]


Translate(str(pre_mRNA).replace('T','U'))