from Bio import SeqIO

substrings = [str(i.seq) for i in SeqIO.parse('Rosalind.txt','fasta')]

def For_Short_Strings1(substrings):
	contig = ''.join(substrings[0])
	substrings.remove(contig)

	while len(substrings) > 0:
		for i in substrings:
			if contig[:len(i)/2] in i:
				x = i.find(contig[:len(i)/2])
				contig = ''.join(i[:x]) + contig
				substrings.remove(i)
				break
			elif contig[-len(i)/2:] in i:
				x = contig.find(i[:len(i)/2])
				contig = contig[:x] + ''.join(i)
				substrings.remove(i)
				break
			else:
				continue
	print contig


For_Short_Strings1(substrings)
