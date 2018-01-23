handle = open('Rosalind.txt').read().split()

num_of_strings = float(handle[0])
gc_content = float(handle[1])
dna = handle[2]

prob_of_motif = 1

for i in dna:
	if i in 'AT':
		prob_of_motif = prob_of_motif*0.5*(1.0-gc_content)
	elif i in 'GC':
		prob_of_motif = prob_of_motif*0.5*(gc_content)

print 1-(1-prob_of_motif)**num_of_strings
