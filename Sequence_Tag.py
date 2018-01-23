amino_acid_masses = {"A":71.03711,
"C":103.00919,
"D":115.02694,
"E":129.04259,
"F":147.06841,
"G":57.02146,
"H":137.05891,
"M":131.04049,
"N":114.04293,
"P":97.05276,
"R":156.10111,
"S":87.03203,
"T":101.04768,
"V":99.06841,
"W":186.07931,
"Y":163.06333}

candidate_basePeaks = [347.42,475.46,612.45,669.47,768.51,778.17,879.53,967.5,1028.34,1096.49,1167.53,1238.46,1322.32,1339.45,1410.70,1449.40,1621.81]
print len(candidate_basePeaks)

candidate_aa = ['A','R','N','D','C','E','G','H','M','F','P','S','T','W','Y','V']

for i in range(len(candidate_basePeaks)):
	for j in range(i+1,len(candidate_basePeaks)):
		for k,v in amino_acid_masses.items():
			if abs((candidate_basePeaks[j]-candidate_basePeaks[i])-v) <= 0.5:
				print i+1,j+1,k

'''
2 3 H
3 4 G
3 5 R
4 5 V
6 7 T
8 10 E
10 11 A
11 12 A
12 14 T
14 15 A
'''
