from Bio import SeqIO

highest_gc = max([(100.00*float(i.seq.count('G')+i.seq.count('C'))/float(i.seq.count('A')+i.seq.count('T')+i.seq.count('G')+i.seq.count('C')),i.id) for i in SeqIO.parse(open('Rosalind.txt'),'fasta')])

print highest_gc[1]
print highest_gc[0]
