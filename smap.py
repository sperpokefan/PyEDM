import numpy as np
import csv
import pdist
import findmax as fm
import math
import numpy.linalg as la
import scipy.stats as stats
import CSVreader
data=CSVreader.read('filename.csv', 1)
RD=data #saves your raw-data time series

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
k = len(matrix)-1 #k is the number of nearest neighbors. In this case, we want all points in our attractor to be considered, so k=len(matrix)



g=0
total=0
rmse=0
perc=0
predictions=[]



while g!= nump: #this loop repeates for each prediction made
	

	# This creates LP: the last point in your matrix that you want to start predictions from
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
	indexes = mins[1] #this is an array of the indexes of the nearest neighbors within the attractor matrix, in order from closest to furthest. 
	b=[]


	while h != len(indexes):  #this loops creates a new matrix (matrix2) which contains the same points as matrix, but the points are ordered by their distance to LP
		index = indexes[h]
		v = matrix[index]
		number = RD[int(index)+1]
		b.append(number) #this creates an array, b, that is smiply the next value (assuming tp=1) associated with each of the nearest points.
		if h!= 0 :
			matrix2 = np.vstack([matrix2, v])
		if h ==0:
			matrix2 = v
		h=h+1
	

	distances = mins[0] #an array of all of the distances of each points from LP, ordered from closest to furthest
	d = distances[0] #d is the distance of the closest point
	meanDist = np.mean(distances) #the mean distance of all points from LP

	weights = np.exp(-theta*distances/meanDist) #creates an array of weights. They are ordered by the weight associated to the closest point first, and furthest point last.
	
	W = np.diag(weights) #W is the diagonalized matrix of weights
	
	h=0

	A = W*matrix2 #multiplies our ordered matrix of points by the diagonalized matrix W. Note that matrix 2 does not have a column of 1's on the far left (yet)
	A2=[]
	
	while h != len(A):#this loop essentially adds that column of 1's that was missing by creating a new matrix (A2) that has the assoiciated wait with each row in the left column
		array = A[h]
		v = np.append(weights[h], array)
		if h!= 0 :
			A2 = np.vstack([A2, v])
		if h ==0:
			A2 = v
		h=h+1

	b= W*b #mupltiplies b by the diagonalized matrix W

	U, sigma, VT = la.svd(A2, full_matrices=False) #computes the SVD of A2
	
	#p and q are the dimensions of the s-inverse matrix
	p = len(A2)
	q = len(A2[0])



	g=g+1





