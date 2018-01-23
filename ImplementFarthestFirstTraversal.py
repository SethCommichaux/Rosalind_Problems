f = open('Rosalind.txt')

points = []

for h,i in enumerate(f): ## collect data from file.
	i = i.strip().split()
	if h == 0:
		k = int(i[0]) ## k = number of centers
		m = int(i[1]) ## m = number of dimensions
	elif h == 1:
		firstpoint = [] ## first point will be first center
		for j in i:
			firstpoint.append(float(j))
	else:
		temp = []
		for j in i:
			temp.append(j)
		points.append(map(float,temp))

def EuclideanDistance(A,B): ## calculates the euclidean distance of any two points in n-dimensional space provided as lists
	result = 0
	for a in range(m):
		result += ((A[a]-B[a])**2)
	return (result**0.5)

def FarthestFirstTraversal(Data, k, firstpoint): ## from firstpoint center, finds furthest center away until it finds k centers
	Centers = [firstpoint]
	while len(Centers) < k:
		results = {}
		for i in Data:
			possibles = []
			for j in Centers:
				possibles.append(EuclideanDistance(i,j))
			results[min(possibles)] = i
		Centers.append(sorted(results.items())[-1][1])
		Data.remove(Data[possibles.index(max(possibles))])
	return Centers

n = FarthestFirstTraversal(points,k,firstpoint)

for x in n:
	print ' '.join(map(str,x))