seq = 'TGGAATCGGGGGTGGGAGCTGGTGTT'

symbol2number = {'A':0,'C':1,'G':2,'T':3}

def PatternToNumber(pattern):
	if len(pattern) == 0:
		return 0
	symbol = pattern[-1]
	prefix = pattern[:-1]
	return 4*PatternToNumber(prefix) + symbol2number[symbol]

print PatternToNumber(seq)




