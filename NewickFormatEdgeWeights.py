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
	print int(tree.distance(leaf1,leaf2)),

