## key seems to be checking if sequence 'xyz' is in state A or B and then using corresponding 'xyz' probability sets

handle = open('Rosalind.txt').read().split()

seq = handle[0]
states = handle[6]
xa = float(handle[15])
ya = float(handle[16])
za = float(handle[17])
xb = float(handle[19])
yb = float(handle[20])
zb = float(handle[21])

prob_of_path = 1

for i in range(len(seq)):
	if states[i] == 'A':
		if seq[i] == 'x':
			prob_of_path *= xa
		elif seq[i] == 'y':
			prob_of_path *= ya
		elif seq[i] == 'z':
			prob_of_path *= za
	elif states[i] == 'B':
		if seq[i] == 'x':
			prob_of_path *= xb
		elif seq[i] == 'y':
			prob_of_path *= yb
		elif seq[i] == 'z':
			prob_of_path *= zb

print prob_of_path
