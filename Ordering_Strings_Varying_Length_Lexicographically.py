import itertools

handle = open('Rosalind.txt').readlines()

letter_ls = handle[0].split()
word_length = int(handle[1])

alphabet = 'abcdefghijklmnopqrstuvwxyz'
# letter_rating = map(str,range(len(letter_ls)))

letter_to_number = {}

for i in range(len(letter_ls)):
	letter_to_number[alphabet[i]] = letter_ls[i]

all_words = []

for i in range(1,word_length+1):
	for j in itertools.product(letter_to_number.keys(),repeat=i):
		all_words.append(j)

output_f = open('Rosalind_Output.txt','w')

for word in sorted(all_words):
	decoded_word = ''
	for index,num in enumerate(word):
		decoded_word += letter_to_number[num]
	output_f.write(decoded_word+'\n')

