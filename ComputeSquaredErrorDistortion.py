## Distortion(Data,Centers) = (1/n) sum all points DataPoint in Data d(DataPoint, Centers)**2

centers = []
points = []
result = 0
count = 0

def EuclideanDistance(A,B): ## calculates the euclidean distance of any two points in n-dimensional space provided as lists
	result = 0
	for a in range(m):
		result += ((A[a]-B[a])**2)
	return (result**0.5)

f = open('Rosalind.txt')
for h,i in enumerate(f):
	i = i.strip().split()
	if h == 0:
		k = int(i[0])
		m = int(i[1])
	elif h <= k:
		centers.append(map(float,i))
	else:
		if not ''.join(i).startswith('-'):
			points.append(map(float,i))
			count += 1

for j in points:
	closer = []
	for l in centers:
		closer.append(EuclideanDistance(j,l))
	result += min(closer)**2

print result/count