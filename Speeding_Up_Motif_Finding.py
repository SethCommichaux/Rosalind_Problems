from Bio import SeqIO

sequence = str([i.seq for i in SeqIO.parse(open('Rosalind.txt'),'fasta')][0].strip())

failure_array = [0]*len(sequence)

for x in range(1,len(sequence)):
	count = 0
	if sequence[x] == sequence[0]:
		count += 1
		temp = x+1
		if count > failure_array[x]:
			failure_array[x] = count
		while sequence.startswith(sequence[x:temp]):
			if count > failure_array[temp-1]:
				failure_array[temp-1] = count
			temp += 1
			count += 1

handle = open('Results.txt','w')

for i in failure_array:
	handle.write(str(i)+' ')

handle.close()