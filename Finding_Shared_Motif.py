from Bio import SeqIO
import sys

sequences = [str(i.seq) for i in SeqIO.parse(open(sys.argv[1]),'fasta')]
smallest = min(sequences,key=len)
sequences.remove(smallest)

subsequences = []
candidates = []

for i in range(len(smallest)):
	for j in range(i,len(smallest)+1):
		subsequences.append(smallest[i:j])

for l in subsequences:
	for k in sequences:
		if l not in k:
			break
	else:
		candidates.append(l)

print max(candidates,key=len)
