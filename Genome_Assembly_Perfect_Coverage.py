sequences = [i.strip() for i in open('Rosalind.txt').read().split()]

deBruijn = []

for x in (sequences):
	deBruijn.append([x[0:-1],x[1:]])

temp = deBruijn[0][1]

seq = deBruijn[0][0][-1]

while temp != deBruijn[0][0]:
	for i in deBruijn:
		if temp == i[0]:
			seq += temp[-1]
			temp = i[1]

print seq

