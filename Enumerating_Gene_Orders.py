import itertools

permuts = [' '.join(i) for i in itertools.permutations('123456')]

x = open('results.txt','w')

x.write(str(len(permuts)))
x.write('\n')
for i in permuts:
	x.write(i)
	x.write('\n')

x.close()