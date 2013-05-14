import re
import os
import sys
import time
from list import getCall
from fabric.colors import *

files = []
d = {}

depricatedFunctions = []
s = ''
def CheckAndSetFolder(f):
	if os.path.exists(f):
		os.chdir(f)
		flag = 1
	else:
		print "Could not find the file you asked for."
		sys.exit
def GetFiles():
	CheckAndSetFolder(raw_input('FullPathtoTheFile--> ')) #give path to a file to test
	print "Checking folders in " + os.path.abspath(os.curdir)
	time.sleep(1)
	for dirname, dirnames, filenames in os.walk('.'):
		for filename in filenames:
			files.append( os.path.join(dirname, filename))
	print "Found these Files \n";

def CheckForDepricatedFiles():
	global xxyz
	for f in files:
		fileToCheck = f
		read = open(f, 'r').read();
		for test in deprecatedFunctions:
			if ernno:
				print (green("Testing " + test + " in " + fileToCheck))
			temp = re.split('\W+', read)
			if test in temp:
				xxyz = xxyz+1;
				print (red("found " + test + " in " + fileToCheck));
				if(test not in d):
					d[test] = 1;
				else:
					d[test] = d[test] + 1;


if __name__ == "__main__":
	try:
		try:
			if sys.argv[1] == '-v':
				ernno = True
			elif sys.argv[1] == '-':
				ernno = False
			else:
				print """
	You have the following options:
	- will print out only found deprecated fucntions
	-v will print out actual work being done
				"""
				exit(1)
		except Exception, e:
				print """
	You have the following options:
	- will print out only found deprecated fucntions
	-v will print out actual work being done
				"""
				exit(1)
		xxyz = 0
		deprecatedFunctions = getCall()
		GetFiles() #get all individual files

		print"""
		==========
		"""


		CheckForDepricatedFiles()
		print "Found " +str(xxyz) +" depricated Functions"

		for k, v in d.items():
			 print "%30s %3d" % (str(k), v)



	except KeyboardInterrupt, e:
		print 
		exit(1)
