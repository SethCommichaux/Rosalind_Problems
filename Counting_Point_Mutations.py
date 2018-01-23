handle = open('Rosalind.txt').readlines()

dna1 = handle[0].strip()
dna2 = handle[1].strip()

assert len(dna1) == len(dna2), "Not same length!"

hamming_distance = 0

for i in range(len(dna1)):
	if dna1[i] != dna2[i]:
		hamming_distance += 1

print hamming_distance