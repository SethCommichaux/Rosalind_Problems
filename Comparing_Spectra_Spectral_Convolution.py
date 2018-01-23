handle = open('Rosalind.txt').readlines()
seq1 = map(float,handle[0].strip().split())
seq2 = map(float,handle[1].strip().split())

spectralConvolution = {}

for j in seq2:
	for i in seq1:
		if round((i-j),3) in spectralConvolution:
			spectralConvolution[round((i-j),3)] += 1
		else:
			spectralConvolution[round((i-j),3)] = 1

x = sorted(spectralConvolution.items(),key = lambda x: x[1])[-1]
print x[1]
print x[0]