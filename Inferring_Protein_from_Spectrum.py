amino_acid_masses = {71.03711:"A",
103.00919:"C",
115.02694:"D",
129.04259:"E",
147.06841:"F",
57.02146:"G",
137.05891:"H",
113.08406:"I",
128.09496:"K",
113.08406:"L",
131.04049:"M",
114.04293:"N",
97.05276:"P",
128.05858:"Q",
156.10111:"R",
87.03203:"S",
101.04768:"T",
99.06841:"V",
186.07931:"W",
163.06333:"Y"}

spectrum = sorted(map(float,open('Rosalind.txt').read().strip().split()))

aa_chain = ''

for i in range(len(spectrum)-1):
	for k,v in amino_acid_masses.items():
		if abs((spectrum[i+1]-spectrum[i]) - k) <= 0.001:
			aa_chain += v
			break

print aa_chain
