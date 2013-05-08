import httplib2;
import sys
import urllib2
import os
from BeautifulSoup import BeautifulSoup, SoupStrainer;

allLinks = {};
visited = {};
functions = [];
counter = 0;

def getURls(url):
	#print len(visited)
	try:
		http = httplib2.Http();
		status, response = http.request(url);
	except Exception, e:
		return

	global allLinks;
	global visited;

	for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
	    if link.has_key('href'):
	    	#if "function" in link['href']:
	        allLinks["http://www.php.net/manual/en/"+link['href']] = 0; 

def findDepricated(url):
	try:
		response = urllib2.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html)
	
		outter = soup.find("div",{"class":"warning"})
		final = outter.find("p", {"class":"simpara"})
		final = final.find("em", {"class":"emphasis"})

		if "DEPRECATED" in final:
			allLinks[url] = 1;
			functions.append(url.split('.')[-2:][0]+"(")
			print functions
	except Exception, e:
		pass



def writeToFile(argv):
	fp = open('dep.list', "w+")
	for f in functions:
		fp.write(f+"\n");

if __name__ == '__main__':
	try:
		getURls('http://www.php.net/manual/en/indexes.functions.php')
	except Exception, e:
		pass
	for k, v in allLinks.items():
		counter+=1;
		if counter % 100 == 0:
			os.system('clear')
			print str(100*counter/len(allLinks))+"%"
		findDepricated(k);

	writeToFile();



