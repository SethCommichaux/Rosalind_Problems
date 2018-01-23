handle = open('Rosalind.txt').read().splitlines()

seq = handle[0]

x = handle[5].split()
y = handle[6].split()

## probabilities of going from one state to another
aa = float(x[1])
ab = float(x[2])
ba = float(y[1])
bb = float(y[2])

pr = 1

for i in range(1,len(seq)):
	if (seq[i-1] == 'A') and (seq[i] == 'A'):
		pr *= aa
	elif (seq[i-1] == 'A') and (seq[i] == 'B'):
		pr *= ab
	elif (seq[i-1] == 'B') and (seq[i] == 'A'):
		pr *= ba
	elif (seq[i-1] == 'B') and (seq[i] == 'B'):
		pr *= bb

## the 0.5 is included because there are 50/50 odds that the sequence will begin in state A or B
print pr * 0.5