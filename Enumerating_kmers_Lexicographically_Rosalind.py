import itertools

handle = open('Rosalind.txt').readlines()

letter_ls = handle[0].split()
word_length = int(handle[1])

combinations_of_words = itertools.product(letter_ls,repeat=word_length)
for i in combinations_of_words:
	print ''.join(i)
