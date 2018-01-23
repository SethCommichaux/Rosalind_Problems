import numpy as np
f = open('Rosalind.txt')

## dna is the superstring checked for combinations of interwoven sequences (strings)
sequences = []

for h,i in enumerate(f):
	i = i.strip()
	if h == 0:
		dna = i
	else:
		sequences.append(i)

def is_superstring(a, b, superstr):
	# Check if two strings can be interwoven into a superstring.
	if len(superstr) == 0:
		return True
	elif a[0] == b[0] == superstr[0]:
		return is_superstring(a[1:], b, superstr[1:]) or is_superstring(a, b[1:], superstr[1:])
	elif a[0] == superstr[0]:
		return is_superstring(a[1:], b, superstr[1:])
	elif b[0] == superstr[0]:
		return is_superstring(a, b[1:], superstr[1:])
	else:
		return False

## Make matrix to record results of comparing every sequence against every other sequence
## 1 means they can be found interwoven in dna.  0 means they cannot.
result_matrix = np.zeros((len(sequences),len(sequences)))

## check every sequence against every other sequence
for x in range(len(sequences)):
	for y in range(len(sequences)):
		for d in range(len(dna)-len(sequences[x])-len(sequences[y])+1):
			## to cut down on search space I only check substrings of dna for interwoven sequences
			## if the substring of dna begins and ends with one of the beginning or ending letters,
			## respectively, of one of the sequences
			if (dna[d] == sequences[x][0]) or (dna[d] == sequences[y][0]):
				if (dna[d+len(sequences[x])+len(sequences[y])-1] == sequences[x][-1]) or (dna[d+len(sequences[x])+len(sequences[y])-1] == sequences[y][-1]):
#					print dna[d],sequences[x][0], sequences[y][0]
					## the dollar signs ('$') are added so that you don't get index errors in the is_superstring function
					if is_superstring(sequences[x]+'$',sequences[y]+'$',dna[d:d+len(sequences[x])+len(sequences[y])]) == True:
# 						print repr(sequences[x]),repr(sequences[y]),repr(dna[d:d+len(sequences[x])+len(sequences[y])])
						result_matrix[y][x] = 1
						break
					else:
						result_matrix[y][x] = 0

## format printing of output
for j in result_matrix:
	print ' '.join(map(str,map(int,j)))

# print
# print
# print
# print
# print
# 

# from itertools import combinations_with_replacement as comb_r
# 
# def is_superstring(a, b, superstr):    
#     # Check if two strings can be interwoven into a superstring.
#     if len(superstr) == 0:
#         return True
#     elif a[0] == b[0] == superstr[0]:
#         return is_superstring(a[1:], b, superstr[1:]) or is_superstring(a, b[1:], superstr[1:])
#     elif a[0] == superstr[0]:
#         return is_superstring(a[1:], b, superstr[1:])
#     elif b[0] == superstr[0]:
#         return is_superstring(a, b[1:], superstr[1:])
#     else:
#         return False
#     
#     
# def find_disjoint_motifs(s, patterns):
#     # Initialize the matrix that will hold 1 at position i, j if pattern[i] and
#     # pattern[j] can be interwoven into a superstring in s, or 0 if they can't.
#     matrix = [[0 for j in range(len(patterns))] for i in range(len(patterns))]
#     
#     # For each unique combination of patterns...
#     for i in list(comb_r((i for i in range(len(patterns))), 2)):
#         a = patterns[i[0]]
#         b = patterns[i[1]]
#  
#         for j in range(len(s)-len(a)-len(b)+1):
#             superstr = s[j:j+len(a)+len(b)]
# 
#             # Add a character outside the alphabet to avoid out of range errors.
#             if is_superstring(a+'$', b+'$', superstr):
# 
#                 # If, for example, patterns 3 and 1 can form a superstring,
#                 # patterns 1 and 3 can as well.
#                 matrix[i[0]][i[1]] = 1
#                 matrix[i[1]][i[0]] = 1
#                 break
# 
#     return matrix
# 
# 
# def main():
#     # Read in string, s, and a list of patterns.
#     with open('Rosalind.txt') as infile:
#         s = infile.readline().strip()
#         patterns = infile.read().strip().split('\n')
# 
#     # Build and fill out the matrix.
#     matrix = find_disjoint_motifs(s, patterns)
# 
#     # Write answer.
#     with open('rosalind_itwv_out.txt', 'w') as outfile:
#         for i in matrix:
#             outfile.write(' '.join(map(str, i)) + '\n')
# 
#     for i in matrix:
#         print(' '.join(map(str, i)))
#         
# 
# if __name__ == '__main__':
#     main()
