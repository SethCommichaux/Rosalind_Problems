import itertools

numbers = int(open("Rosalind.txt").read().split()[0])
print (2**numbers)%1000000


# count = 0
# 
# for i in numbers:
# 	for j in itertools.combinations(numbers,i+1):
# 		count += 1
# print (count + 1 #for empty subset)%1000000

