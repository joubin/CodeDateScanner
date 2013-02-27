import sys
import os
items = []
def getCall():
	file = "/Users/joubin/Desktop/dep.list"
	if os.path.exists(file):
		f = open(file, 'r')
		for line in f:
			if line.strip() != '':
				items.append(line.strip())
		print 
	else:
		print "Could not find the file needed"
	return items