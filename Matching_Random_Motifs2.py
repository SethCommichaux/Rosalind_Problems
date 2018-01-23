import math

handle = open('Rosalind.txt').read().strip().split()

n = int(handle[0])
gc_content = float(handle[1])
seq = handle[2]

def Prob_of_motif_with_GC(sequence,gc_content):
	AT,GC = sequence.count('A')+sequence.count('T'),sequence.count('G')+sequence.count('C')
	return (((1-gc_content)/2.0)**AT)*(gc_content/2.0)**GC

prob = Prob_of_motif_with_GC(seq,gc_content)

print 1-(1-prob)**n
