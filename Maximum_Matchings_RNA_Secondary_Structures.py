from math import factorial

sequence = (open('Rosalind.txt').readlines())[1].strip()

def nPr(n, k):
	return factorial(n)/factorial(n-k)

GC,AT = [sequence.count('G'),sequence.count('C')],[sequence.count('U'),sequence.count('A')]

print nPr(max(GC),min(GC))*nPr(max(AT),min(AT))
