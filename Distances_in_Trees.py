from Bio import Phylo
from cStringIO import StringIO

trees = open('Rosalind.txt').read().strip().split('\n')

for i,j in enumerate(trees):
	if j == '':
		del trees[i]

for i in range(0,len(trees),2):
	tree = trees[i]
	handle = StringIO(tree)
	tree = Phylo.read(handle, "newick")

# 	tree.ladderize()
# 	Phylo.draw(tree)

	leaf1 = trees[i+1].split()[0]
	leaf2 = trees[i+1].split()[1]

	leaf1path = tree.get_path(leaf1)
	leaf2path = tree.get_path(leaf2)

	depthMod = 0

	for i in range(min(len(leaf1path),len(leaf2path))):
		if(leaf1path[i] == leaf2path[i]):
			print leaf1path[i],leaf2path[i]
			depthMod += 1

	print((len(leaf1path) - depthMod) + (len(leaf2path) - depthMod)),















# 	x = [tree.find(leaf1),tree.find(leaf2)]
# 	print x # 	count = 0
# 	temp = 0
# 	for k,j in enumerate(tree[:max(x)]):
# 		if j == '(':
# 			count += 1
# 			temp = [k,j]
# 		elif j == ')':
# 			count -= 1
# 			temp = [k,j]
# 	if temp[1] == '(':
# 		print count,
# 		continue
# 	else:
# 		for x,y in enumerate(tree[temp[0]:max(x)]):
# 			if y == ',':
# 				count += 1
# 	print count + 1,