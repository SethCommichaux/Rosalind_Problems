from math import log

handle = open('Rosalind.txt').readlines()

sequence = handle[0]
gc_content = map(float,handle[1].split())

AT,GC = sequence.count('A')+sequence.count('T'),sequence.count('G')+sequence.count('C')

for i in gc_content:
	print log((((1-i)/2.0)**AT),10) + log(((i/2.0)**GC),10)