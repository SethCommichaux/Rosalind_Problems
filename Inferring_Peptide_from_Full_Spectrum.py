weights = map(float,[i.strip() for i in open('Rosalind.txt').readlines()])

parent_wgt = weights[0]
del weights[0]

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


B = []
Y = []
i = 0
j = 1
count = 0
var = True

while var == True:
	for k,v in amino_acid_masses.items():
		if abs((weights[j] - weights[i])-k) <= 0.001:
			B.append(v)
			i = j
			j += 1
			count += 1
			if len(B) == (len(weights)/2)-1:
				for x in weights[j:]:
					Y.append(x)
				var = False
			break
	else: 
		Y.append(weights[j])
		j += 1

aa_chain = ''

for i in range(len(Y)-1):
	for k,v in amino_acid_masses.items():
		if abs((Y[i+1]-Y[i]) - k) <= 0.001:
			aa_chain += v
			break

B = ''.join(B)
if B == aa_chain[::-1]:
	print B

