f = open('Rosalind.txt')
array = []
count = 0
result = []

for h,i in enumerate(f):
	i = i.strip().split(' ')
	if h == 0:
		n = i[0]
	else:
		for j in i:
			j = int(j)
			array.append(j)

for x in range(1,len(array)):
	k = x
	while (k >= 1) and (array[k] < array[k-1]):
		temp = array[k]
		array[k] = array[k - 1]
		array[k - 1] = temp
		count += 1
		k = k-1

# print array
print count