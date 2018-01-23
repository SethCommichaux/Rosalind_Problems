handle = open('Rosalind.txt').readlines()

num_of_seqs = int(handle[0].strip())
sequences = [handle[i].strip() for i in range(1,num_of_seqs+1)]
unknown_seq_spectrum = map(float,sorted([handle[i].strip() for i in range(num_of_seqs+1,len(handle))]))

amino_acid_masses = {"A":71.03711,
"C":103.00919,
"D":115.02694,
"E":129.04259,
"F":147.06841,
"G":57.02146,
"H":137.05891,
"I":113.08406,
"K":128.09496,
"L":113.08406,
"M":131.04049,
"N":114.04293,
"P":97.05276,
"Q":128.05858,
"R":156.10111,
"S":87.03203,
"T":101.04768,
"V":99.06841,
"W":186.07931,
"Y":163.06333}

def ProteinMass(seq):
	masses = []
	masses2 = []
	for i in seq:
		if masses == []:
			masses.append(amino_acid_masses.get(i,0))
		else:
			masses.append(round(amino_acid_masses.get(i,0)+masses[-1],5))
	for j in seq[::-1]:
		if masses2 == []:
			masses2.append(amino_acid_masses.get(j,0))
		else:
			masses2.append(round(amino_acid_masses.get(j,0)+masses2[-1],5))
	
	return masses + masses2

def SpectralConvolution(seq1,seq2):
	spectralConvolution = {}

	for j in seq2:
		for i in seq1:
			if round(abs(i-j),5) in spectralConvolution:
				spectralConvolution[round(abs(i-j),5)] += 1
			else:
				spectralConvolution[round(abs(i-j),5)] = 1

	x = sorted(spectralConvolution.items(),key = lambda x: x[1])[-1]
	return x[1]

results = []

for i in sequences:
	results.append([SpectralConvolution(ProteinMass(i),unknown_seq_spectrum),i])

x = max(results)

print x[0]
print ''.join(x[1])
