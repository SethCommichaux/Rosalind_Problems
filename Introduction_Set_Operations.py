handle = open('Rosalind.txt').readlines()

N = range(1,int(handle[0])+1)
subset1 = handle[1][1:-1].strip('}').split(',')
subset1 = set(map(int,subset1))
subset2 = handle[2][1:-1].strip('}').split(',')
subset2 = set(map(int,subset2))

AsubtractB = []
BsubtractA = []
AsubtractU = []
BsubtractU = []

for i in subset1:
	if i not in subset2:
		AsubtractB.append(i)

for k in N:
	if k not in subset1:
		AsubtractU.append(k)

for j in subset2:
	if j not in subset1:
		BsubtractA.append(j)

for m in N:
	if m not in subset2:
		BsubtractU.append(m)

print '{'+', '.join(map(str,list(subset1|subset2)))+'}'
print '{'+', '.join(map(str,list(subset1&subset2)))+'}'

print '{'+', '.join(map(str,AsubtractB))+'}'
print '{'+', '.join(map(str,BsubtractA))+'}'
print '{'+', '.join(map(str,AsubtractU))+'}'
print '{'+', '.join(map(str,BsubtractU))+'}'
