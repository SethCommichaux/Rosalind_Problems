seq = ''.join(open('Rosalind.txt').read().split())
skew = [0 for i in range(len(seq)+1)]

for i in range(len(seq)):
	if seq[i] == 'C':
		skew[i+1] = skew[i] -1
	elif seq[i] == 'G':
		skew[i+1] = skew[i] +1
	else:
		skew[i+1] = skew[i]

for i,j in enumerate(skew):
	if j == min(skew):
		print i