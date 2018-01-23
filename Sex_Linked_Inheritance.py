f = map(float,open('rosalind_sexl.txt').read().split())

for i in f:
	print 2*i*(1-i),