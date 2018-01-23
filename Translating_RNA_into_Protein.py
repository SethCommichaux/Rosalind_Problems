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

handle = open('Rosalind.txt').read()

protein = ''

for i in range(0,len(handle),3):
	protein += genetic_code.get(handle[i:i+3],'')
print protein