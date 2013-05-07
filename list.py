import sys
import os
items = []
def getCall():
	file = raw_input('dep.list Location--> ')
	if file == '':
		file = "dep.list"
	if os.path.exists(file):
		f = open(file, 'r')
		for line in f:
			if line.strip() != '':
				items.append(line.strip())
		print 
	else:
		print "Could not find the file needed"
	return items