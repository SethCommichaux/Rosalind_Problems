f = open('Rosalind.txt')

for i,j in enumerate(f):
	if i == 1:
		j = j.strip().split()
		A = map(int,j)
	elif i == 3:
		j = j.strip().split()
		B = map(int,j)

a,b,result = 0,0,[]

while (A[a:] and B[b:]) != []:
	xa = False
	xb = False
	if A[a] < B[b]:
		result.append(A[a])
		a += 1
		xa = True
	else:
		result.append(B[b])
		b += 1
		xb = True

if xb == True:
	result = result+A[a:]
if xa == True:
	result = result+B[b:]

print ' '.join(map(str,result))