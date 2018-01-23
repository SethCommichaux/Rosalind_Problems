f = open('Rosalind.txt').read().splitlines()

number2indices = {}

for i in f[1:]:
	i = map(int,i.strip().split())
	for m,j in enumerate(i): #loop makes dictionary of each number in row and their index
		if j not in number2indices:
			number2indices[j] = m
	test = True
	for j in range(len(i)):
		for k in range(j+1,len(i)):
			if (-1*(i[j] + i[k])) in number2indices:
				print j+1,k+1,number2indices[(-1*(i[j] + i[k]))]+1
				test = False
				break
		if test == False:
			break
	else:
		print -1
	number2indices = {}
