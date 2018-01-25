
import numpy as np
def pdist(a, b):
	i = 0
	tot = 0
	while i != len(b):
		av = np.ravel(a)
		bv = np.ravel(b)
		av = av[i]
		bv=bv[i]
		
		m = (av - bv)*(av-bv)
		tot = tot+m
		i=i+1
	return tot**0.5
