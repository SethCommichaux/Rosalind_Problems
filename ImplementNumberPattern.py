number2letter = {0:'A',1:'C',2:'G',3:'T'}

def Number2Pattern(codedpattern,kmer):
	if kmer == 1:
		return number2letter[codedpattern]
	prefix = codedpattern/4
	remainder = codedpattern%4
	symbol = number2letter[remainder]
	pattern = Number2Pattern(prefix,kmer-1)
	return pattern+symbol

print Number2Pattern(8132,9)