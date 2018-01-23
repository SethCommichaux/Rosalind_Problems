f = open('Rosalind.txt').read().splitlines()

def MergeSort(A,B):
	a,b,result = 0,0,[]

	while (A[a:] and B[b:]) != []:
		if A[a] < B[b]:
			result.append(A[a])
			a += 1
		elif A[a] == B[b]:
			result.append(A[a])
			result.append(B[b])
			a += 1
			b += 1
		else:
			result.append(B[b])
			b += 1

	if A[a:] == []:
		result = result+B[b:]
	if B[b:] == []:
		result = result+A[a:]
	return result

unsorted = [[i] for i in map(int,f[1].split())]
result = []
notmerged = []

while len(result) != 1:
	x = 0
	y = 1
	result = []
	while y < len(unsorted):
		result.append(MergeSort(unsorted[x],unsorted[y]))
		x += 2
		y += 2
	if len(unsorted)%2 != 0:
		result.append(unsorted[-1])
	unsorted = result

print ' '.join(map(str,unsorted[0]))
