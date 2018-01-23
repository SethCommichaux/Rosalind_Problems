import itertools

n = range(-6,7)
n.remove(0)

x = itertools.permutations(n,6)

results = []

for i in x:
	if len(set(map(abs,i))) == 6:
		results.append(' '.join(map(str,i)))

handle = open('Results.txt','w')
handle.write(str(len(results)))
handle.write('\n')
for i in results:
	handle.write(''.join(i))
	handle.write('\n')