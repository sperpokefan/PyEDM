def max(data, n):
	import numpy as np
	
	datasort = sorted(data)
	total=[]
	i=0
	length = len(data)
	values = []
	indexes = []
	

	while i!=n:
		curr = datasort[length-n+i] 
		values.append(curr)
		j=0
		while j!= length:
			if data[j] == curr:
				indexes.append(j)
				j = length-1
			j=j+1
		i=i+1
		total=np.vstack([values,indexes])
	indexes = np.vstack([indexes, indexes])
	return values, indexes


def min(data, n):
	import numpy as np
	
	datasort = sorted(data)
	total=[]
	i=0
	length = len(data)
	values = []
	indexes = []
	while i!=n:
		curr = datasort[i] 
		values.append(curr)
		
		j=0
		while j!= length:
			if data[j] == curr:
				indexes.append(j)
				j=length-1
			j=j+1
		i=i+1
		try:
			total=np.vstack([values,indexes])
		except:
			print 'error'
			print values
			print indexes
			print total
	return total
def val(data, val):
	length = len(data)
	i=0
	while i!= length:
		curr = data[i]
		if curr == val:
			index = i
		
		i = i+1
	return index



