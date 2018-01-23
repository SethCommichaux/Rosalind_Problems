f = open('Rosalind.txt')
sequences = []

for i,j in enumerate(f): ## first we collect sequences from file into a list
	if i == 0:
		j = j.strip().split()
		kmer = int(j[0])
		mismatches = int(j[1])
	else:
		j = j.strip().split()
		sequences.append(j)

def Neighbors(Pattern,d): ## generates the d-neighborhood of the provided sequence
	if d == 0:
		return Pattern
	if len(Pattern) == 1:
		return ['A','C','G','T']
	Neighborhood = []
	SuffixNeighbors = Neighbors(Pattern[1:],d)
	for Text in SuffixNeighbors:
		count = 0
		for j in range(len(Text)):
			if Pattern[1:][j] != Text[j]:
				count += 1
		if count < d:
			for nuc in "ACGT":
				Neighborhood.append(nuc+Text)
		else:
			Neighborhood.append(Pattern[0]+Text)
	return set(Neighborhood)

def MOTIFENUMERATION(Dna, k, d): ## makes a set of all kmers with up to d mismatches found in sequence
	Dna = ''.join(Dna)
	Patterns = []
	for i in range(len(Dna)-k+1):
		w = Neighbors(Dna[i:i+k],mismatches)
		for z in w:
			Patterns.append(z)
	return set(Patterns)

for u,t in enumerate(sequences): ## finds the set of kmers with d mismatches held in common by all sequences
	if u == 0:
		results = MOTIFENUMERATION(t, kmer, mismatches)
	else:
		results = results & MOTIFENUMERATION(t, kmer, mismatches)

for k in results: ## prints results in format Rosalind requires
	print k,




