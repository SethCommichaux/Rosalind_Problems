f = open('Rosalind.txt').read().splitlines()

for h,i in enumerate(f[1:]):
	i = (map(int,i.strip().split()))
	test = True
	for j in range(len(i)):
		for k in range(j+1,len(i)):
			if (i[j] + i[k]) == 0:
				print j+1,k+1
				test = False
				break
		if test == False:
			break
	else:
		print -1