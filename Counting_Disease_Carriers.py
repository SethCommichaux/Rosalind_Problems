handle = open('Rosalind.txt').read().strip().split()

handle = map(float,handle)

for i in handle:
	print round(1-((1.0-i**0.5)**2),3),