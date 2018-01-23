handle = open('Rosalind.txt').read().split()

months = int(handle[0])
lifespan = int(handle[1])


lifearray_rabbits = [0 for i in range(lifespan)]
record_of_rabbits = []

if months <= 2:
	print 1
elif months >2:
	for i in range(months+1):
		if i == 0:
			lifearray_rabbits[0] = 1
		elif i > 1:
			lifearray_rabbits.insert(0,0)
			lifearray_rabbits[0] = sum(lifearray_rabbits[2:])
			del (lifearray_rabbits[-1])
			record_of_rabbits.append(sum(lifearray_rabbits))
print record_of_rabbits[-1]



































# if months == 1 or months == 2:
# 	print 1
# elif months >= 3:
# 	for i in range(0, months-2):
# 		b = num_of_rabbits[i]+num_of_rabbits[i+1]
# 		num_of_rabbits.append(b)
# print num_of_rabbits