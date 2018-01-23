handle = open('Rosalind.txt').read().split()

months = int(handle[0])
litter_size = int(handle[1])

a = 1
b = 1 + litter_size
temp = b

if months == 1 or months == 2:
	print 1
elif months >= 3:
	for i in range(3, months):
		temp = b
		b = a*litter_size + b
		a = temp
print b