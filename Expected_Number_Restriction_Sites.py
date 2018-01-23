handle = open('Rosalind.txt').readlines()

seq_length = int(handle[0].strip())
motif = handle[1].strip()
gc_content = map(float,handle[2].strip().split())

motifGC = motif.count('G') + motif.count('C')
motifAT = motif.count('A') + motif.count('T')

for i in gc_content:
	print ((0.5*i)**motifGC)*((0.5*(1-i))**motifAT)*(seq_length-len(motif)+1),
