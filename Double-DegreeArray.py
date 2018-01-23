f = open('Rosalind.txt')

def DegreeArray(f):
	result = {}
	for h,i in enumerate(f):
		if h == 0:
			continue
		i = i.strip().split(' ')
		a,b = int(i[0]),int(i[1])
		if a in result:
			result[a] += 1
		else:
			result[a] = 1
		if b in result:
			result[b] += 1
		else:
			result[b] = 1

	return result

result = DegreeArray(f)
# print result

f = open('Rosalind.txt')

for h,i in enumerate(f):
	a,b = i.strip().split()
	if h == 0:
		vertices = int(a)
		edges = b
		DDArray = [0]*vertices
		continue
	DDArray[int(a)-1] += result[int(b)]
	DDArray[int(b)-1] += result[int(a)]

print ' '.join(map(str,DDArray))
