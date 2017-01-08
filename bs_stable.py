import sys
sys.setrecursionlimit(10000)

#http://stackoverflow.com/questions/31137552/unicodeencodeerror-ascii-codec-cant-encode-character-at-special-name
#import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2, sys
import csv
from bs4 import BeautifulSoup
#http://stackoverflow.com/questions/14911498/parsing-html-page-using-beautifulsoup




#site= "http://en.wikipedia.org/wiki/PLCB1"
site1= "https://en.wikipedia.org/wiki/Griffith,_Australian_Capital_Territory"
site2 ="https://en.wikipedia.org/wiki/Ferndale,_Western_Australia"
site3 = "https://en.wikipedia.org/wiki/Craigieburn,_Victoria"

sites = [site1 , site2, site3]

for site in sites:
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(site,headers=hdr)
	page = urllib2.urlopen(req)
	soup = BeautifulSoup(page, "html5lib")

#file = open("parseddata.txt", "wb")



	table = soup.find('table', {'class':'infobox'})
	#print table
	info = {}
	rows = table.findAll("th")
	for headercell in rows:
    		valuecell = headercell.findNextSibling('td')
    		if valuecell is None:
        		continue
    	header = ''.join([unicode(t).strip() for t in headercell.findAll(text=True)])
    	value = ''.join([unicode(t).strip() for t in valuecell.findAll(text=True)])
    	info[header] = value
   	 #file.write(info)
	#file.close()

	#http://stackoverflow.com/questions/8685809/python-writing-a-dictionary-to-a-csv-file-with-one-line-for-every-key-value

	print site
	print info

	if 'Established' in info: print info['Established']

