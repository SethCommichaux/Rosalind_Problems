from Bio import ExPASy,SwissProt
import re

handle = open('Rosalind.txt').read().strip().split()

accessions = [i for i in handle]

for accession in accessions:
	x = ExPASy.get_sprot_raw(accession)
	record = SwissProt.read(x)
	results = [m.start()+1 for m in re.finditer(r'(?=N[^P][ST][^P])', record.sequence)]
	if len(results) > 0:
		print accession
		print ' '.join(map(str,results))