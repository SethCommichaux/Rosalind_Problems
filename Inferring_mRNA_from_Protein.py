genetic_code = {"A":4,
"C":2,
"D":2,
"E":2,
"F":2,
"G":4,
"H":2,
"I":3,
"K":2,
"L":6,
"M":1,
"N":2,
"P":4,
"Q":2,
"R":6,
"S":6,
"T":4,
"V":4,
"W":1,
"Y":2
}

handle = open('Rosalind.txt').read().strip()

#start at 3 for 3 possible stop codons
total_combinations = 3

for i in handle:
	total_combinations *= genetic_code.get(i)

print total_combinations%1000000