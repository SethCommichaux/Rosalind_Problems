handle = map(int,open('Rosalind.txt').read().strip().split())

probabilities = [1.0,1.0,1.0,0.75,0.5,0.0]

print sum([2*handle[i]*probabilities[i] for i in range(len(handle))])
