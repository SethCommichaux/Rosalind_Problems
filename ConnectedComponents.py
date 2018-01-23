f = open('Rosalind.txt')
result = []
counter = []

for h,i in enumerate(f):
	i = i.strip().split()
	if h == 0:
		vertices = int(i[0])
		continue
	for n in i:
		counter.append(i[0])
		counter.append(i[1])
	if h == 1:
		result.append(set(i))
	for j in result:
		if len(set(i)|set(j)) < len(set(i)) + len(set(j)):
			result.remove(j)
			result.append(set(j)|set(i))
			break
	else:
		result.append(set(i))

counter = len(set(counter))
temp = 0

while temp != len(result):
	temp = len(result)
	test = True
	for i in range(len(result)):
		for j in range(i+1,len(result)):
			if len(set(result[i])|set(result[j])) < len(set(result[i])) + len(set(result[j])):
				a = (result[j])
				b = (result[i])
				result.append(set(result[j])|set(result[i]))
				result.remove(a)
				result.remove(b)
				test = False
				break
		if test == False:
			break

print len(result) + (vertices - counter)
