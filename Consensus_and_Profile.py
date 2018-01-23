from Bio import SeqIO

handle = open('Rosalind.txt')

sequences = [str(i.seq) for i in SeqIO.parse(handle,'fasta')]

combined_elementwise = zip(*(sequences))

letter_counter = {}

for i,m in enumerate(combined_elementwise):
	letter_counter[i] = [m.count('A'),m.count('C'),m.count('G'),m.count('T')]

A,C,G,T,sequence = [],[],[],[],''
for k,v in sorted(letter_counter.items()):
	sequence += 'ACGT'[v.index(max(v))]
	str(A.append(v[0]))
	str(C.append(v[1]))
	str(G.append(v[2]))
	str(T.append(v[3]))

print sequence
print 'A:',' '.join(map(str,A))
print 'C:',' '.join(map(str,C))
print 'G:',' '.join(map(str,G))
print 'T:',' '.join(map(str,T))