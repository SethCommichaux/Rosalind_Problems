f = open('Rosalind.txt')

for h,i in enumerate(f):
	i = i.strip().split(' ')
	if h == 0:
		vertices = int(i[0])
		edges = int(i[1])
		result = [0]*vertices
	else:
		a,b = int(i[0]),int(i[1])
		result[a-1] += 1
		result[b-1] += 1

print ' '.join(map(str,result))