handle = open('Rosalind.txt').read().strip().split()

sequence = handle[0]
k_mer_length = int(handle[1])

candidates = {}

for i in range(len(sequence)-k_mer_length+1):
	if sequence[i:i+k_mer_length] in candidates:
		candidates[sequence[i:i+k_mer_length]] += 1
	elif sequence[i:i+k_mer_length] not in candidates:
		candidates[sequence[i:i+k_mer_length]] = 1

x = max(candidates.values())

for k,v in sorted(candidates.items()):
	if v == x:
		print k,