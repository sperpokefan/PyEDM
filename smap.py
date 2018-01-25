import matmul as mm

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

# E = int(raw_input("Embedding Dimension: "))
# Len = int(raw_input("Length of Library: "))
# predSet = int(raw_input("Point to Start Predictions From: "))
# nump = int(raw_input("Number of Predictions: "))
E = 3
Len = 100
predSet = 200
nump=1
i=0
theta = 0.5
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
k = len(matrix)-1

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
	while i!= len(matrix):
		d = pdist.pdist(matrix[i], LP)
		distances.append(d)
		i=i+1

	# find the k nearest neighbors, and their distances
	mins = fm.min(distances, len(distances))
	h=0
	indexes = mins[1]
	b=[]
	while h != len(indexes):
		index = indexes[h]
		v = matrix[index]
		number = RD[int(index)+1]
		b.append(number)

		

		if h!= 0 :
			matrix2 = np.vstack([matrix2, v])
		if h ==0:
			matrix2 = v
		h=h+1
	

	distances = mins[0]
	d = distances[0] #d is the distance of the closest point
	meanDist = np.mean(distances)

	weights = []

	h = 0
	while h != len(distances):
		weight = math.exp((-theta*distances[h])/meanDist)
		weights.append(weight)
		h=h+1
	W = np.diag(weights) #W is the diagonalized matrix of weights
	
	h=0
	A = W*matrix2
	A2=[]
	
	while h != len(A):
		array = A[h]
		v = np.append(weights[h], array)
		if h!= 0 :
			A2 = np.vstack([A2, v])
		if h ==0:
			A2 = v
		h=h+1
	b= W*b

	U, sigma, VT = la.svd(A2, full_matrices=False)	
	p = len(A2)
	q = len(A2[0])


	Sinv=np.zeros([q,p], dtype= float)
	print len(Sinv)
	print len(A2)

	i=0
	while i != len(sigma):
		if sigma[i] != 0:
			Sinv[i,i] = 1/sigma[i]
		i=i+1
	print Sinv
	c = mm.matmul(VT,Sinv)
	c = mm.matmul(c,np.transpose(U))
	c = mm.matmul(c, b)
	print len(c[0])
	print len(c)
	# c=  np.true_divide(c,la.norm(c))
	# print c
	# print len(c)
	# i=1
	# y=c[0]
	# while i != len(c):
	# 	y = y+c[i]*data[len(data)-1-i]
	# 	i=i+1
	# print c
	# print y





	g=g+1





