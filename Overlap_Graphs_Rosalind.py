# from Bio import SeqIO
# 
# handle = "Rosalind.txt"
# 
# seq_ls = {}
# for i in SeqIO.parse(handle,'fasta'):
# 	seq_ls[i.id] = i.seq
# 
# for i in range(len(seq_ls)):
# 	for j in range(len(seq_ls)):
# 		if (seq_ls.values()[i][-3:] == seq_ls.values()[j][:3]) and (seq_ls.values()[i] != seq_ls.values()[j]):
# 			print seq_ls.keys()[i],seq_ls.keys()[j]

# ___________________________________________________________________________________________

from Bio import SeqIO

handle = "Rosalind.txt"
o = open('output.txt','w')

seq_ls = {}
for i in SeqIO.parse(handle,'fasta'):
	seq_ls[str(i.id)] = str(i.seq)

suffix = 3

for k,v in seq_ls.items():
	for z,w in seq_ls.items():
		if v == w:
			continue
		else:
			if v[-3:] == w[:3]:
				o.write(k+' '+z+'\n')

o.close()










































