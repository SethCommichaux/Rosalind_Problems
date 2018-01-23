import itertools
from Bio import SeqIO

handle = open('/Users/sethcommichaux/Desktop/Rosalind.txt')

for i in SeqIO.parse(handle,'fasta'):
	query_seq = i.seq

letter_ls = ['A','C','G','T']
word_length = 4

combinations_of_words = {''.join(item):0 for item in itertools.product(letter_ls,repeat=word_length)}

for i in range(len(query_seq)-3):
	for k,v in combinations_of_words.items():
		if query_seq[i:i+4] == k:
			combinations_of_words[k] += 1 

for k,v in sorted(combinations_of_words.items()):
	print v,