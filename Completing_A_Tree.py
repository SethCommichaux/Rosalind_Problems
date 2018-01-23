handle = open('Rosalind.txt').readlines()

number_of_nodes = int(handle[0])

number_unique_elements = []
branches = []

for index,j in enumerate(handle[1:]):
	x = map(int,j.split())
	branches.append(x)
	number_unique_elements.append(x[0])
	number_unique_elements.append(x[1])

number_unique_elements = int(len(set(number_unique_elements)))

var = True

while var == True:
	var = False
	for z in range(len(branches)-1):
		for w in range(z+1,len(branches)):
			if len(set(branches[z]) & set(branches[w])):
				branches.append(set(branches[z]) | set(branches[w]))
				var = True
				branches.remove(branches[z])
				branches.remove(branches[w-1])
				break

print (number_of_nodes - number_unique_elements) + len(branches) - 1