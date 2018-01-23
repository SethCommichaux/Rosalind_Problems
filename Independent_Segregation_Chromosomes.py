from math import log10
from scipy.misc import comb

results = []
n = int(raw_input('Enter a Number:'))
total_search_space = 2**(2*n)
diploid = 2*n

for i in range(diploid):
	total_search_space -= comb(diploid,i,exact=True)
	results.append(log10(total_search_space/float(2**(2*n))))

print ' '.join(map(str,results))