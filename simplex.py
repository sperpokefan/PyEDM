import numpy as np
#import matplotlib.pyplot as plt
import csv
import pdist
import findmax as fm
import math
import numpy.linalg as la
import scipy.stats as stats
import CSVreader
data=CSVreader.read('filename.csv', 1)
RD=data



E = int(raw_input("Embedding Dimension: "))
k = int(raw_input("k nearest neighbors: "))
Len = int(raw_input("Length of Library: "))
predSet = int(raw_input("Point to Start Predictions From: "))
nump = int(raw_input("Number of Predictions: "))
i=0
M=[]
data=data[0:Len]

i=0

# Turns dataset into E dimension manifold
while i != E: 
	array = data[0+i:len(data)-E+i+1]
	M.append(array)
	i=i+1
i=0
matrix= np.matrix(M)
matrix = np.transpose(matrix)


# This is the last point in your matrix that you want to start predictions from
g=0
total=0
rmse=0
perc=0
predictions=[]
while g!= nump:
	LP=[]
	o=predSet+1-E
	while o != predSet+1:
		LP.append(RD[o+g])
		o=o+1 
	
	#Finds the distances of all other points in matrix from LP
	i=0
	distances=[]
	while i!= len(matrix)-2:
		d = pdist.pdist(matrix[i], LP)
		distances.append(d)
		i=i+1

	# find the k nearest neighbors, and their distances
	mins = fm.min(distances, k)
	distances = mins[0]
	d = distances[0]
	A= mins[1]
	i=0
	weights=[]
	while i != k:
		w= math.exp(-distances[i]/d)
		weights.append(w)
		i=i+1
	sumOfWeights = np.sum(weights)
	i=0
	while i != k:
		curr = matrix[int(A[i])+1]
		val = curr*weights[i]
		if i ==0:
			y = val
		if i!=0:
			y=y+val	
		i=i+1
	y=y/sumOfWeights
	y=np.array(y)
	y=y[0]
	y=y[E-1]
	predictions.append(y)
	total = total+abs(RD[predSet+1+g]-y)
	rmse = rmse + math.pow(RD[predSet+1+g]-y, 2)
	if float(RD[predSet+1+g]/y) > 0:
		perc=perc+1
	g=g+1

perc=float(perc)/float(nump)
rmse = rmse/nump
print 'rmse: ', math.sqrt(rmse)
print 'mae: ', total/nump
spear= stats.spearmanr(predictions, RD[predSet+1:1+predSet+nump])
print 'rho: ', spear[0]
print 'p-value: ', spear[1]
print 'perc: ',  perc







