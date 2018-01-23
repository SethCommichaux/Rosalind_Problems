Pattern = 'TAACTTGCCAG'
d = 3

def Neighbors(Pattern,d):
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

x = Neighbors(Pattern,d)

for i in x:
	print i
