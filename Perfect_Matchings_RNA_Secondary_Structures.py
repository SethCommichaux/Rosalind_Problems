import math

handle = open('Rosalind.txt').readlines()
sequence = handle[1]
print math.factorial(sequence.count('A'))*math.factorial(sequence.count('G'))