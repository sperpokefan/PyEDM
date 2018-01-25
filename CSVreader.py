import csv
def read(name, col):
	with open(name, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		data=[]
		count=0
		for row in spamreader:
			count=count+1
			if count >1:
				data.append(float(row[col]))
	return data